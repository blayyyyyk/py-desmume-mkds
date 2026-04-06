import ctypes
from functools import reduce
import numpy as np
from typing import Union as Union_T, cast as t_cast, TypeVar, Callable, Any, TYPE_CHECKING


FX32_SCALE_FACTOR = 1 / (1 << 12)
RACER_PTR_ADDR = 0x0217ACF8
COURSE_ID_ADDR = 0x23CDCD8
OBJECTS_PTR_ADDR = 0x0217B588
CHECKPOINT_PTR_ADDR = 0x021755FC
CLOCK_DATA_PTR = 0x0217AA34
CAMERA_PTR_ADDR = 0x0217AA4C
RACE_STATUS_PTR_ADDR = 0x021755FC
MAP_DATA_PTR_ADDR = 0x02175600
COLLISION_DATA_ADDR = 0x0217B5F4
RACE_STATE_PTR_ADDR = 0x0217AA34
SCENE_STATE_PTR_ADDR = 0x021759AC
RACE_CONFIG_PTR_ADDR = 0x021759A0


class AsDictMixin:
    @classmethod
    def as_dict(cls, self):
        result = {}
        if not isinstance(self, AsDictMixin):
            # not a structure, assume it's already a python object
            return self
        if not hasattr(cls, "_fields_"):
            return result
        # sys.version_info >= (3, 5)
        # for (field, *_) in cls._fields_:  # noqa
        for field_tuple in cls._fields_:  # noqa
            field = field_tuple[0]
            if field.startswith('PADDING_'):
                continue
            value = getattr(self, field)
            type_ = type(value)
            if hasattr(value, "_length_") and hasattr(value, "_type_"):
                # array
                type_ = type_._type_
                if hasattr(type_, 'as_dict'):
                    value = [type_.as_dict(v) for v in value]
                else:
                    value = [i for i in value]
            elif hasattr(value, "contents") and hasattr(value, "_type_"):
                # pointer
                try:
                    if not hasattr(type_, "as_dict"):
                        value = value.contents
                    else:
                        type_ = type_._type_
                        value = type_.as_dict(value.contents)
                except ValueError:
                    # nullptr
                    value = None
            elif isinstance(value, AsDictMixin):
                # other structure
                value = type_.as_dict(value)
            result[field] = value
        return result


class Structure(ctypes.Structure, AsDictMixin):

    def __init__(self, *args, **kwds):
        # We don't want to use positional arguments fill PADDING_* fields.

        args = dict(zip(self.__class__._field_names_(), args))
        args.update(kwds)
        super(Structure, self).__init__(**args)

    @classmethod
    def _field_names_(cls):
        if hasattr(cls, '_fields_'):
            return (f[0] for f in cls._fields_ if not f[0].startswith('PADDING'))
        else:
            return ()

    @classmethod
    def get_type(cls, field):
        for f in cls._fields_:
            if f[0] == field:
                return f[1]
        return None

    @classmethod
    def bind(cls, bound_fields):
        fields = {}
        for name, type_ in cls._fields_:
            if hasattr(type_, "restype"):
                if name in bound_fields:
                    if bound_fields[name] is None:
                        fields[name] = type_()
                    else:
                        # use a closure to capture the callback from the loop scope
                        fields[name] = (
                            type_((lambda callback: lambda *args: callback(*args))(
                                bound_fields[name]))
                        )
                    del bound_fields[name]
                else:
                    # default callback implementation (does nothing)
                    try:
                        default_ = type_(0).restype().value
                    except TypeError:
                        default_ = None
                    fields[name] = type_((
                        lambda default_: lambda *args: default_)(default_))
            else:
                # not a callback function, use default initialization
                if name in bound_fields:
                    fields[name] = bound_fields[name]
                    del bound_fields[name]
                else:
                    fields[name] = type_()
        if len(bound_fields) != 0:
            raise ValueError(
                "Cannot bind the following unknown callback(s) {}.{}".format(
                    cls.__name__, bound_fields.keys()
            ))
        return cls(**fields)


class Union(ctypes.Union, AsDictMixin):
    pass



c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 8:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*8

class PointerConfig:
    reader = None

# if local wordsize is same as target, keep ctypes pointer function.
if ctypes.sizeof(ctypes.c_void_p) == 4:
    POINTER_T = ctypes.POINTER
else:
    
    class IncorrectWordSizeError(TypeError):
        pass
    # required to access _ctypes
    import _ctypes
    # Emulate a pointer class using the approriate c_int32/c_int64 type
    # The new class should have :
    # ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
    # but the class should be submitted to a unique instance for each base type
    # to that if A == B, POINTER_T(A) == POINTER_T(B)
    ctypes._pointer_t_type_cache = {}
    def POINTER_T(pointee):
        # a pointer should have the same length as LONG
        fake_ptr_base_type = ctypes.c_uint32
        # specific case for c_void_p
        if pointee is None: # VOID pointer type. c_void_p.
            pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
            clsname = 'c_void'
        else:
            clsname = pointee.__name__
        if clsname in ctypes._pointer_t_type_cache:
            return ctypes._pointer_t_type_cache[clsname]
        # make template
        class _T(_ctypes._SimpleCData,):
            _type_ = 'I'
            _subtype_ = pointee
            @property
            def contents(self):
                if PointerConfig.reader:
                    return PointerConfig.reader.read_struct(self._subtype_, self.value)
                raise RuntimeError("No reader registered for fake pointers")

            def __repr__(self):
                return 'LP_%s(0x%08X)' % (clsname, self.value)
        _class = type('LP_%d_%s'%(4, clsname), (_T,),{})
        ctypes._pointer_t_type_cache[clsname] = _class
        return _class

def string_cast(char_pointer, encoding='utf-8', errors='strict'):
    value = ctypes.cast(char_pointer, ctypes.c_char_p).value
    if value is not None and encoding is not None:
        value = value.decode(encoding, errors=errors)
    return value


def char_pointer_cast(string, encoding='utf-8'):
    if encoding is not None:
        try:
            string = string.encode(encoding)
        except AttributeError:
            # In Python3, bytes has no encode attribute
            pass
    string = ctypes.c_char_p(string)
    return ctypes.cast(string, POINTER_T(ctypes.c_char))



class fx(Structure):
    def __float__(self):
        return float(self.val) * FX32_SCALE_FACTOR

    def __int__(self):
        return int(self.val * FX32_SCALE_FACTOR)

    def __mul__(self, other):
        return float(self) * other

    def __rmul__(self, other):
        return float(self) * other
        
    def __imul__(self, other):
        self.val *= other * FX32_SCALE_FACTOR
        return self
        
    def __add__(self, other):
        return float(self) + float(other)
        
    def __radd__(self, other):
        return float(self) + float(other)
        
    def __iadd__(self, other):
        self.val += float(other) * FX32_SCALE_FACTOR
        return self
        
    def __sub__(self, other):
        return float(self) - float(other)
        
    def __rsub__(self, other):
        return float(self) - float(other)
        
    def __isub__(self, other):
        self.val -= float(other) * FX32_SCALE_FACTOR
        return self
        
    def __div__(self, other):
        return float(self) / float(other)
        
    def __idiv__(self, other):
        self.val /= float(other) * FX32_SCALE_FACTOR
        return self
        
    def __repr__(self):
        return f"{float(self):.4f}"

class struct_fx32(fx):
    pass
    
struct_fx32._pack_ = 1 # source:False
struct_fx32._fields_ = [
    # private/external_include/nitro/fx/fx.h 144
    ('val', ctypes.c_int32),
]

fx32 = struct_fx32
    
class union_MtxFx43(Union):
    pass
    
class union_MtxFx33(Union):
    pass
    
class union_MtxFx22(Union):
    pass
    
# private/external_include/nitro/fx/fx.h:251
# private/external_include/nitro/fx/fx.h:245
class struct_VecFx32(Structure):
    _pack_ = 1 # source:False
    _fields_ = [
    # private/external_include/nitro/fx/fx.h 245
    ('x', fx32),
    ('y', fx32),
    ('z', fx32),
     ]

VecFx32 = struct_VecFx32
class struct_VecFx16(Structure):
    pass

class struct_fx16(fx):
    pass

struct_fx16._pack_ = 1 # source:False
struct_fx16._fields_ = [
    ('val', ctypes.c_int16),
]

fx16 = struct_fx16
struct_VecFx16._pack_ = 1 # source:False
struct_VecFx16._fields_ = [
    ('x', fx16),
    ('y', fx16),
    ('z', fx16),
]

VecFx16 = struct_VecFx16

class struct_quaternion_t(Structure):
    _pack_ = 1 # source:False
    _fields_ = [
    # mkds_c/math/quaternion.h 3
    ('x', fx32),
    ('y', fx32),
    ('z', fx32),
    ('w', fx32),
     ]

quaternion_t = struct_quaternion_t