from ctypes import *
from ctypes import _Pointer, _SimpleCData, _CFunctionType
from typing import ClassVar, Any, List, Callable, TypeVar, Union as UnionT
from typing import TYPE_CHECKING
T = TypeVar('T', bound=UnionT[Structure, Union, _SimpleCData, _Pointer, _CFunctionType])
POINTER_T = _Pointer[T]

RACER_PTR_ADDR: int = 0x0217ACF8
COURSE_ID_ADDR: int = 0x23CDCD8
OBJECTS_PTR_ADDR: int = 0x0217B588
CHECKPOINT_PTR_ADDR: int = 0x021755FC
CLOCK_DATA_PTR: int = 0x0217AA34
CAMERA_PTR_ADDR: int = 0x0217AA4C
RACE_STATUS_PTR_ADDR: int = 0x021755FC
MAP_DATA_PTR_ADDR: int = 0x02175600
COLLISION_DATA_ADDR: int = 0x0217B5F4
RACE_STATE_PTR_ADDR: int = 0x0217AA34
SCENE_STATE_PTR_ADDR: int = 0x021759AC
RACE_CONFIG_PTR_ADDR: int = 0x021759A0
FX32_SCALE_FACTOR: float = 1 / (1 << 12)

# Forward declarations

class CARDRomRegion(Structure):
    """
    ```python
    offset: int (POINTER(I))
    length: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    offset: int
    length: int

class CPContext(Structure):
    """
    ```python
    div_numer: int (POINTER(L))
    div_denom: int (POINTER(L))
    sqrt: int (POINTER(L))
    div_mode: int (POINTER(H))
    sqrt_mode: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    div_numer: int
    div_denom: int
    sqrt: int
    div_mode: int
    sqrt_mode: int
    PADDING_0: list[int]

class FSArchive(Structure):
    """
    ```python
    name: union_FSArchive_name (union_FSArchive_name)
    next: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    prev: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    sync_q: struct__OSThreadQueue (struct__OSThreadQueue)
    stat_q: struct__OSThreadQueue (struct__OSThreadQueue)
    flag: int (POINTER(I))
    list: struct_FSFileLink (struct_FSFileLink)
    base: int (POINTER(I))
    fat: int (POINTER(I))
    fat_size: int (POINTER(I))
    fnt: int (POINTER(I))
    fnt_size: int (POINTER(I))
    fat_bak: int (POINTER(I))
    fnt_bak: int (POINTER(I))
    load_mem: c_void_p (c_void_p)
    read_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint] (CFunctionType)
    write_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint] (CFunctionType)
    table_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint] (CFunctionType)
    proc: Callable[[POINTER_T[struct_FSFile], int], c_uint] (CFunctionType)
    proc_flag: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    name: union_FSArchive_name
    next: POINTER_T[struct_FSArchive]
    prev: POINTER_T[struct_FSArchive]
    sync_q: struct__OSThreadQueue
    stat_q: struct__OSThreadQueue
    flag: int
    list: struct_FSFileLink
    base: int
    fat: int
    fat_size: int
    fnt: int
    fnt_size: int
    fat_bak: int
    fnt_bak: int
    load_mem: c_void_p
    read_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint]
    write_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint]
    table_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint]
    proc: Callable[[POINTER_T[struct_FSFile], int], c_uint]
    proc_flag: int

class FSFile(Structure):
    """
    ```python
    link: struct_FSFileLink (struct_FSFileLink)
    arc: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    stat: int (POINTER(I))
    command: int (POINTER(I))
    error: int (POINTER(I))
    queue: list[struct__OSThreadQueue] (struct__OSThreadQueue[1])
    prop: union_FSFile_prop (union_FSFile_prop)
    arg: union_FSFile_arg (union_FSFile_arg)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_FSFileLink
    arc: POINTER_T[struct_FSArchive]
    stat: int
    command: int
    error: int
    queue: list[struct__OSThreadQueue]
    prop: union_FSFile_prop
    arg: union_FSFile_arg

class FSFileLink(Structure):
    """
    ```python
    prev: POINTER_T[struct_FSFile] (POINTER(struct_FSFile))
    next: POINTER_T[struct_FSFile] (POINTER(struct_FSFile))
    ```
    """
    _pack_: ClassVar[int] = 1
    prev: POINTER_T[struct_FSFile]
    next: POINTER_T[struct_FSFile]

class FSOverlayInfo(Structure):
    """
    ```python
    header: struct_FSOverlayInfoHeader (struct_FSOverlayInfoHeader)
    target: int (POINTER(I))
    file_pos: struct_CARDRomRegion (struct_CARDRomRegion)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_FSOverlayInfoHeader
    target: int
    file_pos: struct_CARDRomRegion

class FSOverlayInfoHeader(Structure):
    """
    ```python
    id: int (POINTER(I))
    ram_address: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ram_size: int (POINTER(I))
    bss_size: int (POINTER(I))
    sinit_init: POINTER_T[_CFunctionType] (POINTER(CFunctionType))
    sinit_init_end: POINTER_T[_CFunctionType] (POINTER(CFunctionType))
    file_id: int (POINTER(I))
    compressed: int (POINTER(I))
    flag: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    ram_address: POINTER_T[c_ubyte]
    ram_size: int
    bss_size: int
    sinit_init: POINTER_T[_CFunctionType]
    sinit_init_end: POINTER_T[_CFunctionType]
    file_id: int
    compressed: int
    flag: int

class MATHRandContext32(Structure):
    """
    ```python
    x: int (POINTER(L))
    mul: int (POINTER(L))
    add: int (POINTER(L))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: int
    mul: int
    add: int

class MICAutoParam(Structure):
    """
    ```python
    type: int (POINTER(I))
    buffer: c_void_p (c_void_p)
    size: int (POINTER(I))
    rate: int (POINTER(I))
    loop_enable: int (POINTER(i))
    full_callback: Callable[[int, c_void_p], None] (CFunctionType)
    full_arg: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    type: int
    buffer: c_void_p
    size: int
    rate: int
    loop_enable: int
    full_callback: Callable[[int, c_void_p], None]
    full_arg: c_void_p

class MtxFx22(Union):
    """
    ```python
    _0: struct_MtxFx22_0 (struct_MtxFx22_0)
    m: list[fx32] (struct_fx32[2][2])
    a: list[fx32] (struct_fx32[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_MtxFx22_0
    m: list[fx32]
    a: list[fx32]

class MtxFx33(Union):
    """
    ```python
    _0: struct_MtxFx33_0 (struct_MtxFx33_0)
    m: list[fx32] (struct_fx32[3][3])
    a: list[fx32] (struct_fx32[9])
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_MtxFx33_0
    m: list[fx32]
    a: list[fx32]

class MtxFx43(Union):
    """
    ```python
    _0: struct_MtxFx43_0 (struct_MtxFx43_0)
    m: list[fx32] (struct_fx32[3][4])
    a: list[fx32] (struct_fx32[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_MtxFx43_0
    m: list[fx32]
    a: list[fx32]

class NNSFndArchive(Structure):
    """
    ```python
    fsArchive: struct_FSArchive (struct_FSArchive)
    arcBinary: POINTER_T[struct_NNSiFndArchiveHeader] (POINTER(struct_NNSiFndArchiveHeader))
    fatData: POINTER_T[struct_NNSiFndArchiveFatData] (POINTER(struct_NNSiFndArchiveFatData))
    fileImage: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    fsArchive: struct_FSArchive
    arcBinary: POINTER_T[struct_NNSiFndArchiveHeader]
    fatData: POINTER_T[struct_NNSiFndArchiveFatData]
    fileImage: int

class NNSFndLink(Structure):
    """
    ```python
    prevObject: c_void_p (c_void_p)
    nextObject: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    prevObject: c_void_p
    nextObject: c_void_p

class NNSFndList(Structure):
    """
    ```python
    headObject: c_void_p (c_void_p)
    tailObject: c_void_p (c_void_p)
    numObjects: int (POINTER(H))
    offset: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    headObject: c_void_p
    tailObject: c_void_p
    numObjects: int
    offset: int

class NNSG2dCellBoundingRectS16(Structure):
    """
    ```python
    maxX: int (POINTER(h))
    maxY: int (POINTER(h))
    minX: int (POINTER(h))
    minY: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    maxX: int
    maxY: int
    minX: int
    minY: int

class NNSG2dCellData(Structure):
    """
    ```python
    numOAMAttrs: int (POINTER(H))
    cellAttr: int (POINTER(H))
    pOamAttrArray: POINTER_T[struct_NNSG2dCellOAMAttrData] (POINTER(struct_NNSG2dCellOAMAttrData))
    ```
    """
    _pack_: ClassVar[int] = 1
    numOAMAttrs: int
    cellAttr: int
    pOamAttrArray: POINTER_T[struct_NNSG2dCellOAMAttrData]

class NNSG2dCharCanvas(Structure):
    """
    ```python
    charBase: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    areaWidth: int (POINTER(i))
    areaHeight: int (POINTER(i))
    dstBpp: int (POINTER(B))
    reserved: list[int] (POINTER(B)[3])
    param: int (POINTER(I))
    pDrawGlyph: Callable[[POINTER_T[struct_NNSG2dCharCanvas], POINTER_T[struct_NNSG2dFont], int, int, int, POINTER_T[struct_NNSG2dGlyph]], None] (CFunctionType)
    pClear: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int], None] (CFunctionType)
    pClearArea: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int, int, int, int, int], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    charBase: POINTER_T[c_ubyte]
    areaWidth: int
    areaHeight: int
    dstBpp: int
    reserved: list[int]
    param: int
    pDrawGlyph: Callable[[POINTER_T[struct_NNSG2dCharCanvas], POINTER_T[struct_NNSG2dFont], int, int, int, POINTER_T[struct_NNSG2dGlyph]], None]
    pClear: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int], None]
    pClearArea: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int, int, int, int, int], None]

class NNSG2dCharWidths(Structure):
    """
    ```python
    left: int (POINTER(b))
    glyphWidth: int (POINTER(B))
    charWidth: int (POINTER(b))
    ```
    """
    _pack_: ClassVar[int] = 1
    left: int
    glyphWidth: int
    charWidth: int

class NNSG2dTextCanvas(Structure):
    """
    ```python
    pCanvas: POINTER_T[struct_NNSG2dCharCanvas] (POINTER(struct_NNSG2dCharCanvas))
    pFont: POINTER_T[struct_NNSG2dFont] (POINTER(struct_NNSG2dFont))
    hSpace: int (POINTER(i))
    vSpace: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    pCanvas: POINTER_T[struct_NNSG2dCharCanvas]
    pFont: POINTER_T[struct_NNSG2dFont]
    hSpace: int
    vSpace: int

class NNSG3dJntAnmResult(Structure):
    """
    ```python
    flag: int (POINTER(I))
    scale: struct_VecFx32 (struct_VecFx32)
    scaleEx0: struct_VecFx32 (struct_VecFx32)
    scaleEx1: struct_VecFx32 (struct_VecFx32)
    rot: union_MtxFx33 (union_MtxFx33)
    trans: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    flag: int
    scale: struct_VecFx32
    scaleEx0: struct_VecFx32
    scaleEx1: struct_VecFx32
    rot: union_MtxFx33
    trans: struct_VecFx32

class NNSG3dMatAnmResult(Structure):
    """
    ```python
    flag: int (POINTER(I))
    prmMatColor0: int (POINTER(I))
    prmMatColor1: int (POINTER(I))
    prmPolygonAttr: int (POINTER(I))
    prmTexImage: int (POINTER(I))
    prmTexPltt: int (POINTER(I))
    scaleS: fx32 (struct_fx32)
    scaleT: fx32 (struct_fx32)
    sinR: fx16 (struct_fx16)
    cosR: fx16 (struct_fx16)
    transS: fx32 (struct_fx32)
    transT: fx32 (struct_fx32)
    origWidth: int (POINTER(H))
    origHeight: int (POINTER(H))
    magW: fx32 (struct_fx32)
    magH: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    flag: int
    prmMatColor0: int
    prmMatColor1: int
    prmPolygonAttr: int
    prmTexImage: int
    prmTexPltt: int
    scaleS: fx32
    scaleT: fx32
    sinR: fx16
    cosR: fx16
    transS: fx32
    transT: fx32
    origWidth: int
    origHeight: int
    magW: fx32
    magH: fx32

class NNSG3dRenderObj(Structure):
    """
    ```python
    flag: int (POINTER(I))
    resMdl: POINTER_T[struct_NNSG3dResMdl_] (POINTER(struct_NNSG3dResMdl_))
    anmMat: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    funcBlendMat: Callable[[POINTER_T[struct_NNSG3dMatAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int] (CFunctionType)
    anmJnt: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    funcBlendJnt: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int] (CFunctionType)
    anmVis: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    funcBlendVis: Callable[[POINTER_T[struct_NNSG3dVisAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int] (CFunctionType)
    cbFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None] (CFunctionType)
    cbCmd: int (POINTER(B))
    cbTiming: int (POINTER(B))
    dummy_: int (POINTER(H))
    cbInitFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None] (CFunctionType)
    ptrUser: c_void_p (c_void_p)
    ptrUserSbc: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    recJntAnm: POINTER_T[struct_NNSG3dJntAnmResult_] (POINTER(struct_NNSG3dJntAnmResult_))
    recMatAnm: POINTER_T[struct_NNSG3dMatAnmResult_] (POINTER(struct_NNSG3dMatAnmResult_))
    hintMatAnmExist: list[int] (POINTER(I)[2])
    hintJntAnmExist: list[int] (POINTER(I)[2])
    hintVisAnmExist: list[int] (POINTER(I)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    flag: int
    resMdl: POINTER_T[struct_NNSG3dResMdl_]
    anmMat: POINTER_T[struct_NNSG3dAnmObj_]
    funcBlendMat: Callable[[POINTER_T[struct_NNSG3dMatAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int]
    anmJnt: POINTER_T[struct_NNSG3dAnmObj_]
    funcBlendJnt: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int]
    anmVis: POINTER_T[struct_NNSG3dAnmObj_]
    funcBlendVis: Callable[[POINTER_T[struct_NNSG3dVisAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int]
    cbFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None]
    cbCmd: int
    cbTiming: int
    dummy_: int
    cbInitFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None]
    ptrUser: c_void_p
    ptrUserSbc: POINTER_T[c_ubyte]
    recJntAnm: POINTER_T[struct_NNSG3dJntAnmResult_]
    recMatAnm: POINTER_T[struct_NNSG3dMatAnmResult_]
    hintMatAnmExist: list[int]
    hintJntAnmExist: list[int]
    hintVisAnmExist: list[int]

class NNSG3dResDataBlockHeader(Structure):
    """
    ```python
    _0: union_NNSG3dResDataBlockHeader__0 (union_NNSG3dResDataBlockHeader__0)
    size: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: union_NNSG3dResDataBlockHeader__0
    size: int

class NNSG3dResDict(Structure):
    """
    ```python
    revision: int (POINTER(B))
    numEntry: int (POINTER(B))
    sizeDictBlk: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsEntry: int (POINTER(H))
    node: list[struct_NNSG3dResDictTreeNode_] (struct_NNSG3dResDictTreeNode_[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    revision: int
    numEntry: int
    sizeDictBlk: int
    dummy_: int
    ofsEntry: int
    node: list[struct_NNSG3dResDictTreeNode_]

class NNSG3dResMdlInfo(Structure):
    """
    ```python
    sbcType: int (POINTER(B))
    scalingRule: int (POINTER(B))
    texMtxMode: int (POINTER(B))
    numNode: int (POINTER(B))
    numMat: int (POINTER(B))
    numShp: int (POINTER(B))
    firstUnusedMtxStackID: int (POINTER(B))
    dummy_: int (POINTER(B))
    posScale: fx32 (struct_fx32)
    invPosScale: fx32 (struct_fx32)
    numVertex: int (POINTER(H))
    numPolygon: int (POINTER(H))
    numTriangle: int (POINTER(H))
    numQuad: int (POINTER(H))
    boxX: fx16 (struct_fx16)
    boxY: fx16 (struct_fx16)
    boxZ: fx16 (struct_fx16)
    boxW: fx16 (struct_fx16)
    boxH: fx16 (struct_fx16)
    boxD: fx16 (struct_fx16)
    boxPosScale: fx32 (struct_fx32)
    boxInvPosScale: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    sbcType: int
    scalingRule: int
    texMtxMode: int
    numNode: int
    numMat: int
    numShp: int
    firstUnusedMtxStackID: int
    dummy_: int
    posScale: fx32
    invPosScale: fx32
    numVertex: int
    numPolygon: int
    numTriangle: int
    numQuad: int
    boxX: fx16
    boxY: fx16
    boxZ: fx16
    boxW: fx16
    boxH: fx16
    boxD: fx16
    boxPosScale: fx32
    boxInvPosScale: fx32

class NNSG3dResNodeInfo(Structure):
    """
    ```python
    dict: struct_NNSG3dResDict_ (struct_NNSG3dResDict_)
    ```
    """
    _pack_: ClassVar[int] = 1
    dict: struct_NNSG3dResDict_

class NNSG3dResPlttInfo(Structure):
    """
    ```python
    vramKey: int (POINTER(I))
    sizePltt: int (POINTER(H))
    flag: int (POINTER(H))
    ofsDict: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsPlttData: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    vramKey: int
    sizePltt: int
    flag: int
    ofsDict: int
    dummy_: int
    ofsPlttData: int

class NNSG3dResTex4x4Info(Structure):
    """
    ```python
    vramKey: int (POINTER(I))
    sizeTex: int (POINTER(H))
    ofsDict: int (POINTER(H))
    flag: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsTex: int (POINTER(I))
    ofsTexPlttIdx: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    vramKey: int
    sizeTex: int
    ofsDict: int
    flag: int
    dummy_: int
    ofsTex: int
    ofsTexPlttIdx: int

class NNSG3dResTexInfo(Structure):
    """
    ```python
    vramKey: int (POINTER(I))
    sizeTex: int (POINTER(H))
    ofsDict: int (POINTER(H))
    flag: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsTex: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    vramKey: int
    sizeTex: int
    ofsDict: int
    flag: int
    dummy_: int
    ofsTex: int

class NNSG3dVisAnmResult(Structure):
    """
    ```python
    isVisible: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    isVisible: int

class NNSSndFader(Structure):
    """
    ```python
    origin: int (POINTER(i))
    target: int (POINTER(i))
    counter: int (POINTER(i))
    frame: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    origin: int
    target: int
    counter: int
    frame: int

class NNSSndHandle(Structure):
    """
    ```python
    player: POINTER_T[struct_NNSSndSeqPlayer] (POINTER(struct_NNSSndSeqPlayer))
    ```
    """
    _pack_: ClassVar[int] = 1
    player: POINTER_T[struct_NNSSndSeqPlayer]

class OSContext(Structure):
    """
    ```python
    cpsr: int (POINTER(I))
    r: list[int] (POINTER(I)[13])
    sp: int (POINTER(I))
    lr: int (POINTER(I))
    pc_plus4: int (POINTER(I))
    sp_svc: int (POINTER(I))
    cp_context: struct_CPContext (struct_CPContext)
    ```
    """
    _pack_: ClassVar[int] = 1
    cpsr: int
    r: list[int]
    sp: int
    lr: int
    pc_plus4: int
    sp_svc: int
    cp_context: struct_CPContext

class OSMutexLink(Structure):
    """
    ```python
    next: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    prev: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: POINTER_T[struct_OSMutex]
    prev: POINTER_T[struct_OSMutex]

class OSMutexQueue(Structure):
    """
    ```python
    head: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    tail: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    ```
    """
    _pack_: ClassVar[int] = 1
    head: POINTER_T[struct_OSMutex]
    tail: POINTER_T[struct_OSMutex]

class OSThread(Structure):
    """
    ```python
    context: struct_OSContext (struct_OSContext)
    state: int (POINTER(I))
    next: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    id: int (POINTER(I))
    priority: int (POINTER(I))
    profiler: c_void_p (c_void_p)
    queue: POINTER_T[struct__OSThreadQueue] (POINTER(struct__OSThreadQueue))
    link: struct__OSThreadLink (struct__OSThreadLink)
    mutex: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    mutexQueue: struct__OSMutexQueue (struct__OSMutexQueue)
    stackTop: int (POINTER(I))
    stackBottom: int (POINTER(I))
    stackWarningOffset: int (POINTER(I))
    joinQueue: struct__OSThreadQueue (struct__OSThreadQueue)
    specific: list[c_void_p] (c_void_p[3])
    alarmForSleep: POINTER_T[struct_OSiAlarm] (POINTER(struct_OSiAlarm))
    destructor: Callable[[c_void_p], None] (CFunctionType)
    userParameter: c_void_p (c_void_p)
    systemErrno: int (POINTER(i))
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    context: struct_OSContext
    state: int
    next: POINTER_T[struct__OSThread]
    id: int
    priority: int
    profiler: c_void_p
    queue: POINTER_T[struct__OSThreadQueue]
    link: struct__OSThreadLink
    mutex: POINTER_T[struct_OSMutex]
    mutexQueue: struct__OSMutexQueue
    stackTop: int
    stackBottom: int
    stackWarningOffset: int
    joinQueue: struct__OSThreadQueue
    specific: list[c_void_p]
    alarmForSleep: POINTER_T[struct_OSiAlarm]
    destructor: Callable[[c_void_p], None]
    userParameter: c_void_p
    systemErrno: int
    PADDING_0: list[int]

class OSThreadLink(Structure):
    """
    ```python
    prev: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    next: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    ```
    """
    _pack_: ClassVar[int] = 1
    prev: POINTER_T[struct__OSThread]
    next: POINTER_T[struct__OSThread]

class OSThreadQueue(Structure):
    """
    ```python
    head: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    tail: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    ```
    """
    _pack_: ClassVar[int] = 1
    head: POINTER_T[struct__OSThread]
    tail: POINTER_T[struct__OSThread]

class PMSleepCallbackInfo(Structure):
    """
    ```python
    callback: Callable[[c_void_p], None] (CFunctionType)
    arg: c_void_p (c_void_p)
    next: POINTER_T[struct_PMiSleepCallbackInfo] (POINTER(struct_PMiSleepCallbackInfo))
    ```
    """
    _pack_: ClassVar[int] = 1
    callback: Callable[[c_void_p], None]
    arg: c_void_p
    next: POINTER_T[struct_PMiSleepCallbackInfo]

class RTCRawDate(Structure):
    """
    ```python
    year: int (POINTER(I))
    month: int (POINTER(I))
    dummy0: int (POINTER(I))
    day: int (POINTER(I))
    dummy1: int (POINTER(I))
    week: int (POINTER(I))
    dummy2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    year: int
    month: int
    dummy0: int
    day: int
    dummy1: int
    week: int
    dummy2: int

class RTCRawTime(Structure):
    """
    ```python
    hour: int (POINTER(I))
    afternoon: int (POINTER(I))
    dummy0: int (POINTER(I))
    minute: int (POINTER(I))
    dummy1: int (POINTER(I))
    second: int (POINTER(I))
    dummy2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    hour: int
    afternoon: int
    dummy0: int
    minute: int
    dummy1: int
    second: int
    dummy2: int

class TPData(Structure):
    """
    ```python
    x: int (POINTER(H))
    y: int (POINTER(H))
    touch: int (POINTER(H))
    validity: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: int
    y: int
    touch: int
    validity: int

class VecFx16(Structure):
    """
    ```python
    x: fx16 (struct_fx16)
    y: fx16 (struct_fx16)
    z: fx16 (struct_fx16)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx16
    y: fx16
    z: fx16

class VecFx32(Structure):
    """
    ```python
    x: fx32 (struct_fx32)
    y: fx32 (struct_fx32)
    z: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx32
    y: fx32
    z: fx32

class _flock_t(Structure):
    """
    ```python
    lock: int (POINTER(i))
    thread_tag: int (POINTER(I))
    counter: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    lock: int
    thread_tag: int
    counter: int

class _mbstate_t(Structure):
    """
    ```python
    __count: int (POINTER(i))
    __value: union__mbstate_t___value (union__mbstate_t___value)
    ```
    """
    _pack_: ClassVar[int] = 1
    __count: int
    __value: union__mbstate_t___value

class airship_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    baseElevation: fx32 (struct_fx32)
    speed: fx32 (struct_fx32)
    fieldA8: struct_sinthing_t (struct_sinthing_t)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    baseElevation: fx32
    speed: fx32
    fieldA8: struct_sinthing_t
    pathwalker: struct_pw_pathwalker_t
    state: int

class anim_animator_t(Structure):
    """
    ```python
    loopMode: int (POINTER(H))
    hasEnded: int (POINTER(H))
    animLength: fx32 (struct_fx32)
    speed: fx32 (struct_fx32)
    progress: fx32 (struct_fx32)
    loopIteration: int (POINTER(H))
    loopCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    loopMode: int
    hasEnded: int
    animLength: fx32
    speed: fx32
    progress: fx32
    loopIteration: int
    loopCount: int

class anim_manager_t(Structure):
    """
    ```python
    animator: struct_anim_animator_t (struct_anim_animator_t)
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    animCount: int (POINTER(H))
    curAnimIdx: int (POINTER(H))
    anmObjs: POINTER_T[POINTER_T[struct_NNSG3dAnmObj_]] (POINTER(POINTER(struct_NNSG3dAnmObj_)))
    loopFlags: POINTER_T[c_int] (POINTER(POINTER(i)))
    field24: int (POINTER(I))
    animKind: int (POINTER(I))
    isBlending: int (POINTER(i))
    blendSpeed: fx32 (struct_fx32)
    blendAnmObj: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    ```
    """
    _pack_: ClassVar[int] = 1
    animator: struct_anim_animator_t
    model: POINTER_T[struct_model_t]
    animCount: int
    curAnimIdx: int
    anmObjs: POINTER_T[POINTER_T[struct_NNSG3dAnmObj_]]
    loopFlags: POINTER_T[c_int]
    field24: int
    animKind: int
    isBlending: int
    blendSpeed: fx32
    blendAnmObj: POINTER_T[struct_NNSG3dAnmObj_]

class arc_course_def_t(Structure):
    """
    ```python
    name: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    hasDVariant: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    name: POINTER_T[c_ubyte]
    hasDVariant: int
    PADDING_0: list[int]

class arc_data_t(Structure):
    """
    ```python
    arcs: list[struct_arc_t] (struct_arc_t[20])
    fsTableSize: int (POINTER(I))
    fsTable: c_void_p (c_void_p)
    arcLoader: struct_arc_loader_t (struct_arc_loader_t)
    file: struct_FSFile (struct_FSFile)
    something: list[struct_arc_something_t] (struct_arc_something_t[16])
    curLoadedCourse: int (POINTER(I))
    curLoadedRaceMode: int (POINTER(I))
    unk0xA78: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    unk0xA7C: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    unk0xA80: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    ```
    """
    _pack_: ClassVar[int] = 1
    arcs: list[struct_arc_t]
    fsTableSize: int
    fsTable: c_void_p
    arcLoader: struct_arc_loader_t
    file: struct_FSFile
    something: list[struct_arc_something_t]
    curLoadedCourse: int
    curLoadedRaceMode: int
    unk0xA78: POINTER_T[struct_NNSiFndHeapHead]
    unk0xA7C: POINTER_T[struct_NNSiFndHeapHead]
    unk0xA80: POINTER_T[struct_NNSiFndHeapHead]

class arc_def_t(Structure):
    """
    ```python
    path: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    next: int (POINTER(i))
    somethingId: int (POINTER(b))
    PADDING_0: list[int] (POINTER(B)[3])
    unk3: int (POINTER(I))
    allocFromTail: int (POINTER(i))
    unk5: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: POINTER_T[c_ubyte]
    next: int
    somethingId: int
    PADDING_0: list[int]
    unk3: int
    allocFromTail: int
    unk5: int

class arc_loader_t(Structure):
    """
    ```python
    path: list[int] (POINTER(B)[128])
    srcBuf: c_void_p (c_void_p)
    dstBuf: c_void_p (c_void_p)
    tmpBuf: c_void_p (c_void_p)
    arcId: int (POINTER(I))
    allocFromTail: int (POINTER(I))
    field94: int (POINTER(I))
    field98: int (POINTER(I))
    field9C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: list[int]
    srcBuf: c_void_p
    dstBuf: c_void_p
    tmpBuf: c_void_p
    arcId: int
    allocFromTail: int
    field94: int
    field98: int
    field9C: int

class arc_scene_def_t(Structure):
    """
    ```python
    name: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    unk: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    name: POINTER_T[c_ubyte]
    unk: int

class arc_something_t(Structure):
    """
    ```python
    heapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    b: c_void_p (c_void_p)
    flag0: int (POINTER(I))
    flag29: int (POINTER(I))
    flag30: int (POINTER(I))
    flag31: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    heapHandle: POINTER_T[struct_NNSiFndHeapHead]
    b: c_void_p
    flag0: int
    flag29: int
    flag30: int
    flag31: int

class arc_t(Structure):
    """
    ```python
    arc: struct_NNSFndArchive (struct_NNSFndArchive)
    loaded: int (POINTER(i))
    arcData: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    arc: struct_NNSFndArchive
    loaded: int
    arcData: c_void_p

class area_mission_rival_pass_area_status_t(Structure):
    """
    ```python
    entries: POINTER_T[struct_area_mission_rival_pass_area_t] (POINTER(struct_area_mission_rival_pass_area_t))
    count: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    entries: POINTER_T[struct_area_mission_rival_pass_area_t]
    count: int
    PADDING_0: list[int]

class area_mission_rival_pass_area_t(Structure):
    """
    ```python
    index: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    size: fx32 (struct_fx32)
    prevNrObjsInside: int (POINTER(B))
    passCount: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    index: int
    PADDING_0: list[int]
    size: fx32
    prevNrObjsInside: int
    passCount: int
    PADDING_1: list[int]

class bakubaku_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    waitCounter: int (POINTER(i))
    triggerPos: struct_VecFx32 (struct_VecFx32)
    state: int (POINTER(I))
    fieldB4: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    waitCounter: int
    triggerPos: struct_VecFx32
    state: int
    fieldB4: int

class balloon_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(i))
    driverId: int (POINTER(i))
    color: int (POINTER(i))
    gapAC: int (POINTER(I))
    fieldB0: struct_VecFx32 (struct_VecFx32)
    fieldBC: struct_VecFx32 (struct_VecFx32)
    fieldC8: int (POINTER(i))
    fieldCC: int (POINTER(i))
    inflationProgress: int (POINTER(i))
    inflationDelta: int (POINTER(i))
    scale3: int (POINTER(i))
    scale3Delta: int (POINTER(i))
    fieldE0: int (POINTER(i))
    scale: int (POINTER(i))
    fieldE8: struct_VecFx32 (struct_VecFx32)
    subBalloonCountPlusOne: int (POINTER(i))
    subBalloons: POINTER_T[POINTER_T[struct_balloon_t]] (POINTER(POINTER(struct_balloon_t)))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    driverId: int
    color: int
    gapAC: int
    fieldB0: struct_VecFx32
    fieldBC: struct_VecFx32
    fieldC8: int
    fieldCC: int
    inflationProgress: int
    inflationDelta: int
    scale3: int
    scale3Delta: int
    fieldE0: int
    scale: int
    fieldE8: struct_VecFx32
    subBalloonCountPlusOne: int
    subBalloons: POINTER_T[POINTER_T[struct_balloon_t]]
    state: int

class basabasa_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    velocity: struct_VecFx32 (struct_VecFx32)
    nsbtpFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    initialCounter: int (POINTER(i))
    state0Counter: int (POINTER(i))
    state2Counter: int (POINTER(i))
    emitSound: int (POINTER(i))
    mapIconType: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    rotZ: struct_idk_struct_t (struct_idk_struct_t)
    driverHitMask: int (POINTER(B))
    PADDING_2: list[int] (POINTER(B)[3])
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    velocity: struct_VecFx32
    nsbtpFrame: int
    PADDING_0: list[int]
    initialCounter: int
    state0Counter: int
    state2Counter: int
    emitSound: int
    mapIconType: int
    PADDING_1: list[int]
    rotZ: struct_idk_struct_t
    driverHitMask: int
    PADDING_2: list[int]
    state: int

class bbm_model_t(Structure):
    """
    ```python
    displayList: c_void_p (c_void_p)
    displayListLength: int (POINTER(I))
    posScale: fx32 (struct_fx32)
    diffAmb: int (POINTER(I))
    speEmi: int (POINTER(I))
    polygonAttr: int (POINTER(I))
    texIdx: int (POINTER(H))
    texCount: int (POINTER(H))
    texParamList: POINTER_T[c_uint] (POINTER(POINTER(I)))
    plttParamList: POINTER_T[c_uint] (POINTER(POINTER(I)))
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    nsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    displayList: c_void_p
    displayListLength: int
    posScale: fx32
    diffAmb: int
    speEmi: int
    polygonAttr: int
    texIdx: int
    texCount: int
    texParamList: POINTER_T[c_uint]
    plttParamList: POINTER_T[c_uint]
    model: POINTER_T[struct_model_t]
    nsbtpAnim: POINTER_T[struct_anim_manager_t]

class bbobj_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class bgwkr_queue_t(Structure):
    """
    ```python
    buffer: list[Callable[[], None]] (CFunctionType[10])
    writePtr: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    buffer: list[Callable[[], None]]
    writePtr: int
    PADDING_0: list[int]

class bgwkr_t(Structure):
    """
    ```python
    taskQueue: struct_bgwkr_queue_t (struct_bgwkr_queue_t)
    PADDING_0: list[int] (POINTER(B)[4])
    thread: struct__OSThread (struct__OSThread)
    unk: list[int] (POINTER(I)[2])
    threadStack: POINTER_T[c_uint] (POINTER(POINTER(I)))
    requestAvailable: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    taskQueue: struct_bgwkr_queue_t
    PADDING_0: list[int]
    thread: struct__OSThread
    unk: list[int]
    threadStack: POINTER_T[c_uint]
    requestAvailable: int

class bound_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbtpFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fieldA4: int (POINTER(I))
    fieldA8: int (POINTER(I))
    fieldAC: int (POINTER(I))
    fieldB0: int (POINTER(I))
    width: int (POINTER(I))
    scaleXZSinThing: struct_sinthing_t (struct_sinthing_t)
    scaleYSinThing: struct_sinthing_t (struct_sinthing_t)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    driverHitTimeouts: list[int] (POINTER(I)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbtpFrame: int
    PADDING_0: list[int]
    fieldA4: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    width: int
    scaleXZSinThing: struct_sinthing_t
    scaleYSinThing: struct_sinthing_t
    pathwalker: struct_pw_pathwalker_t
    state: int
    driverHitTimeouts: list[int]

class bridge_renderpart_t(Structure):
    """
    ```python
    renderPart: struct_mobj_render_part_t (struct_mobj_render_part_t)
    animLength: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    renderPart: struct_mobj_render_part_t
    animLength: fx32

class bridge_t(Structure):
    """
    ```python
    dcolMObj: struct_dcol_inst_t (struct_dcol_inst_t)
    field144: int (POINTER(H))
    rotSpeed: int (POINTER(H))
    angle: int (POINTER(H))
    field14A: int (POINTER(H))
    field14C: int (POINTER(H))
    field14E: int (POINTER(H))
    waitCounter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    animProgress: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    dcolMObj: struct_dcol_inst_t
    field144: int
    rotSpeed: int
    angle: int
    field14A: int
    field14C: int
    field14E: int
    waitCounter: int
    PADDING_0: list[int]
    animProgress: fx32

class bsfx_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    sfxAMaxVolume: int (POINTER(i))
    volume: int (POINTER(i))
    fieldA8: int (POINTER(i))
    position: struct_VecFx32 (struct_VecFx32)
    fieldB8: int (POINTER(i))
    sfxIdA: int (POINTER(H))
    sfxIdB: int (POINTER(H))
    stateUpdateCounter: int (POINTER(i))
    state: int (POINTER(i))
    sfxACounter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    sfxAMaxVolume: int
    volume: int
    fieldA8: int
    position: struct_VecFx32
    fieldB8: int
    sfxIdA: int
    sfxIdB: int
    stateUpdateCounter: int
    state: int
    sfxACounter: int

class cam_params_t(Structure):
    """
    ```python
    distance: fx32 (struct_fx32)
    elevation: fx32 (struct_fx32)
    maxTargetElevation: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    distance: fx32
    elevation: fx32
    maxTargetElevation: fx32

class came_routestat_t(Structure):
    """
    ```python
    pointCache: list[struct_VecFx32] (struct_VecFx32[4])
    progress: int (POINTER(i))
    index: int (POINTER(i))
    field38: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    pointCache: list[struct_VecFx32]
    progress: int
    index: int
    field38: int

class came_unknown_t(Structure):
    """
    ```python
    cameEntry: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    routestat1: struct_came_routestat_t (struct_came_routestat_t)
    routestat2: struct_came_routestat_t (struct_came_routestat_t)
    routeSpeed: int (POINTER(h))
    field7E: int (POINTER(H))
    field80: int (POINTER(I))
    field84: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    cameEntry: POINTER_T[struct_nkm_came_entry_t]
    routestat1: struct_came_routestat_t
    routestat2: struct_came_routestat_t
    routeSpeed: int
    field7E: int
    field80: int
    field84: int

class camera_t(Structure):
    """
    ```python
    up: struct_VecFx32 (struct_VecFx32)
    right: struct_VecFx32 (struct_VecFx32)
    target: struct_VecFx32 (struct_VecFx32)
    position: struct_VecFx32 (struct_VecFx32)
    mtx: union_MtxFx43 (union_MtxFx43)
    fov: int (POINTER(i))
    targetFov: int (POINTER(i))
    fovSin: fx16 (struct_fx16)
    fovCos: fx16 (struct_fx16)
    aspectRatio: fx32 (struct_fx32)
    frustumNear: fx32 (struct_fx32)
    frustumFar: fx32 (struct_fx32)
    frustumTop: fx32 (struct_fx32)
    frustumBottom: fx32 (struct_fx32)
    frustumLeft: fx32 (struct_fx32)
    frustumRight: fx32 (struct_fx32)
    field88: fx32 (struct_fx32)
    skyFrustumFar: fx32 (struct_fx32)
    lookAtTarget: struct_VecFx32 (struct_VecFx32)
    lookAtPosition: struct_VecFx32 (struct_VecFx32)
    fieldA8: struct_VecFx32 (struct_VecFx32)
    fieldB4: struct_VecFx32 (struct_VecFx32)
    upConst: struct_VecFx32 (struct_VecFx32)
    fieldCC: fx32 (struct_fx32)
    fieldD0: int (POINTER(i))
    targetElevation: fx32 (struct_fx32)
    fieldD8: int (POINTER(I))
    fieldDC: int (POINTER(I))
    fieldE0: int (POINTER(I))
    fieldE4: struct_VecFx32 (struct_VecFx32)
    playerOffsetDirection: fx32 (struct_fx32)
    fieldF4: struct_VecFx32 (struct_VecFx32)
    field100: struct_VecFx32 (struct_VecFx32)
    field10C: struct_VecFx32 (struct_VecFx32)
    field118: struct_VecFx32 (struct_VecFx32)
    field124: struct_VecFx32 (struct_VecFx32)
    field130: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    prevPosition: struct_VecFx32 (struct_VecFx32)
    isShaking: int (POINTER(i))
    field144: fx32 (struct_fx32)
    shakeAmount: fx32 (struct_fx32)
    field14C: int (POINTER(I))
    field150: int (POINTER(h))
    PADDING_1: list[int] (POINTER(B)[2])
    shakeDecay: fx32 (struct_fx32)
    field158: int (POINTER(I))
    targetDirection: struct_VecFx32 (struct_VecFx32)
    field168: fx32 (struct_fx32)
    field16C: int (POINTER(I))
    field170: int (POINTER(I))
    field174: int (POINTER(I))
    elevation: fx32 (struct_fx32)
    field17C: struct_VecFx32 (struct_VecFx32)
    field188: struct_VecFx32 (struct_VecFx32)
    routeStat: struct_came_routestat_t (struct_came_routestat_t)
    routeStat2: struct_came_routestat_t (struct_came_routestat_t)
    field20C: int (POINTER(H))
    field20E: int (POINTER(H))
    targetDriverId: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    currentCamId: int (POINTER(I))
    cameEntry: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    unknownMgCams: POINTER_T[struct_came_unknown_t] (POINTER(struct_came_unknown_t))
    unknownMgCamsCopy: POINTER_T[struct_came_unknown_t] (POINTER(struct_came_unknown_t))
    field224: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    field228: int (POINTER(I))
    field22C: int (POINTER(H))
    PADDING_4: list[int] (POINTER(B)[2])
    field230: int (POINTER(I))
    field234: int (POINTER(I))
    field238: int (POINTER(i))
    frameCounter: int (POINTER(H))
    PADDING_5: list[int] (POINTER(B)[2])
    fovProgress: fx32 (struct_fx32)
    targetProgress: fx32 (struct_fx32)
    field248: int (POINTER(I))
    mode: int (POINTER(I))
    field250: int (POINTER(I))
    field254: int (POINTER(I))
    field258: int (POINTER(i))
    field25C: int (POINTER(I))
    field260: struct_VecFx32 (struct_VecFx32)
    field26C: int (POINTER(h))
    field26E: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    up: struct_VecFx32
    right: struct_VecFx32
    target: struct_VecFx32
    position: struct_VecFx32
    mtx: union_MtxFx43
    fov: int
    targetFov: int
    fovSin: fx16
    fovCos: fx16
    aspectRatio: fx32
    frustumNear: fx32
    frustumFar: fx32
    frustumTop: fx32
    frustumBottom: fx32
    frustumLeft: fx32
    frustumRight: fx32
    field88: fx32
    skyFrustumFar: fx32
    lookAtTarget: struct_VecFx32
    lookAtPosition: struct_VecFx32
    fieldA8: struct_VecFx32
    fieldB4: struct_VecFx32
    upConst: struct_VecFx32
    fieldCC: fx32
    fieldD0: int
    targetElevation: fx32
    fieldD8: int
    fieldDC: int
    fieldE0: int
    fieldE4: struct_VecFx32
    playerOffsetDirection: fx32
    fieldF4: struct_VecFx32
    field100: struct_VecFx32
    field10C: struct_VecFx32
    field118: struct_VecFx32
    field124: struct_VecFx32
    field130: int
    PADDING_0: list[int]
    prevPosition: struct_VecFx32
    isShaking: int
    field144: fx32
    shakeAmount: fx32
    field14C: int
    field150: int
    PADDING_1: list[int]
    shakeDecay: fx32
    field158: int
    targetDirection: struct_VecFx32
    field168: fx32
    field16C: int
    field170: int
    field174: int
    elevation: fx32
    field17C: struct_VecFx32
    field188: struct_VecFx32
    routeStat: struct_came_routestat_t
    routeStat2: struct_came_routestat_t
    field20C: int
    field20E: int
    targetDriverId: int
    PADDING_2: list[int]
    currentCamId: int
    cameEntry: POINTER_T[struct_nkm_came_entry_t]
    unknownMgCams: POINTER_T[struct_came_unknown_t]
    unknownMgCamsCopy: POINTER_T[struct_came_unknown_t]
    field224: int
    PADDING_3: list[int]
    field228: int
    field22C: int
    PADDING_4: list[int]
    field230: int
    field234: int
    field238: int
    frameCounter: int
    PADDING_5: list[int]
    fovProgress: fx32
    targetProgress: fx32
    field248: int
    mode: int
    field250: int
    field254: int
    field258: int
    field25C: int
    field260: struct_VecFx32
    field26C: int
    field26E: int

class chandelier_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbcaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    counter: int (POINTER(i))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbcaFrame: int
    PADDING_0: list[int]
    counter: int
    state: int

class charkart_colors_t(Structure):
    """
    ```python
    diffuse: int (POINTER(H))
    emission: int (POINTER(H))
    ambient: int (POINTER(H))
    diffR: int (POINTER(H))
    diffG: int (POINTER(H))
    diffB: int (POINTER(H))
    diffRDelta: int (POINTER(h))
    diffGDelta: int (POINTER(h))
    diffBDelta: int (POINTER(h))
    emiR: int (POINTER(H))
    emiG: int (POINTER(H))
    emiB: int (POINTER(H))
    emiRDelta: int (POINTER(h))
    emiGDelta: int (POINTER(h))
    emiBDelta: int (POINTER(h))
    ambiR: int (POINTER(H))
    ambiG: int (POINTER(H))
    amibB: int (POINTER(H))
    amibRDelta: int (POINTER(h))
    ambiGDelta: int (POINTER(h))
    ambiBDelta: int (POINTER(h))
    progress: fx16 (struct_fx16)
    ```
    """
    _pack_: ClassVar[int] = 1
    diffuse: int
    emission: int
    ambient: int
    diffR: int
    diffG: int
    diffB: int
    diffRDelta: int
    diffGDelta: int
    diffBDelta: int
    emiR: int
    emiG: int
    emiB: int
    emiRDelta: int
    emiGDelta: int
    emiBDelta: int
    ambiR: int
    ambiG: int
    amibB: int
    amibRDelta: int
    ambiGDelta: int
    ambiBDelta: int
    progress: fx16

class charkart_field24_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    field10: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field14: int (POINTER(i))
    field18: int (POINTER(H))
    field1A: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    field10: int
    PADDING_0: list[int]
    field14: int
    field18: int
    field1A: int

class charkart_t(Structure):
    """
    ```python
    characterId: int (POINTER(I))
    kartId: int (POINTER(i))
    characterNsbcaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    characterNsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    characterModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartTireModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartShadowModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartOffsetData: POINTER_T[struct_kofs_entry_t] (POINTER(struct_kofs_entry_t))
    field24: struct_charkart_field24_t (struct_charkart_field24_t)
    light: struct_light_t (struct_light_t)
    PADDING_0: list[int] (POINTER(B)[2])
    field54: int (POINTER(I))
    isKartInvisible: int (POINTER(i))
    isCharacterInvisible: int (POINTER(i))
    useSeparateTires: int (POINTER(i))
    inStarToonMode: int (POINTER(i))
    kartABC: int (POINTER(H))
    colors: struct_charkart_colors_t (struct_charkart_colors_t)
    PADDING_1: list[int] (POINTER(B)[2])
    field98: struct_anim_animator_t (struct_anim_animator_t)
    nsbtpAnimDisabled: int (POINTER(i))
    fieldB0: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    characterId: int
    kartId: int
    characterNsbcaAnim: POINTER_T[struct_anim_manager_t]
    characterNsbtpAnim: POINTER_T[struct_anim_manager_t]
    characterModel: POINTER_T[struct_model_t]
    kartModel: POINTER_T[struct_model_t]
    kartTireModel: POINTER_T[struct_model_t]
    kartShadowModel: POINTER_T[struct_model_t]
    kartOffsetData: POINTER_T[struct_kofs_entry_t]
    field24: struct_charkart_field24_t
    light: struct_light_t
    PADDING_0: list[int]
    field54: int
    isKartInvisible: int
    isCharacterInvisible: int
    useSeparateTires: int
    inStarToonMode: int
    kartABC: int
    colors: struct_charkart_colors_t
    PADDING_1: list[int]
    field98: struct_anim_animator_t
    nsbtpAnimDisabled: int
    fieldB0: int

class choropu_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    setting1: int (POINTER(I))
    setting0: int (POINTER(I))
    fieldA8: int (POINTER(I))
    fieldAC: int (POINTER(i))
    fieldB0: int (POINTER(i))
    fieldB4: int (POINTER(i))
    rotZ: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    shadow: struct_objshadow_t (struct_objshadow_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    setting1: int
    setting0: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    fieldB4: int
    rotZ: int
    PADDING_0: list[int]
    shadow: struct_objshadow_t

class cklcr_char_def_t(Structure):
    """
    ```python
    playerModelName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    enemyModelName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    emblemName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ```
    """
    _pack_: ClassVar[int] = 1
    playerModelName: POINTER_T[c_ubyte]
    enemyModelName: POINTER_T[c_ubyte]
    emblemName: POINTER_T[c_ubyte]

class cklcr_kart_def_t(Structure):
    """
    ```python
    kartModelName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    kartShadowName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ```
    """
    _pack_: ClassVar[int] = 1
    kartModelName: POINTER_T[c_ubyte]
    kartShadowName: POINTER_T[c_ubyte]

class col_entry_t(Structure):
    """
    ```python
    segmentRightEndpoint: int (POINTER(h))
    segmentLeftEndpoint: int (POINTER(h))
    zMax: fx32 (struct_fx32)
    zMin: fx32 (struct_fx32)
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    boundingSphereRadius: fx32 (struct_fx32)
    flags: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    object: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    segmentRightEndpoint: int
    segmentLeftEndpoint: int
    zMax: fx32
    zMin: fx32
    position: POINTER_T[struct_VecFx32]
    boundingSphereRadius: fx32
    flags: int
    PADDING_0: list[int]
    object: c_void_p

class col_response_t(Structure):
    """
    ```python
    maxSomething: struct_VecFx32 (struct_VecFx32)
    minSomething: struct_VecFx32 (struct_VecFx32)
    distance: fx32 (struct_fx32)
    normal: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    maxSomething: struct_VecFx32
    minSomething: struct_VecFx32
    distance: fx32
    normal: struct_VecFx32

class col_segment_left_endpoint_t(Structure):
    """
    ```python
    rightEndpoint: int (POINTER(B))
    colEntryId: int (POINTER(B))
    xPos: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    rightEndpoint: int
    colEntryId: int
    xPos: int

class col_segment_right_endpoint_t(Structure):
    """
    ```python
    leftEndpoint: int (POINTER(B))
    minLeftEndpoint: int (POINTER(B))
    xPos: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    leftEndpoint: int
    minLeftEndpoint: int
    xPos: int

class cow_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class crab_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(H))
    rotZ: int (POINTER(H))
    counter: int (POINTER(i))
    bodyNsbtpFrame: fx32 (struct_fx32)
    handNsbtpFrame: fx32 (struct_fx32)
    fieldB0: struct_sinthing_t (struct_sinthing_t)
    fieldD0: struct_sinthing_t (struct_sinthing_t)
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    rotZ: int
    counter: int
    bodyNsbtpFrame: fx32
    handNsbtpFrame: fx32
    fieldB0: struct_sinthing_t
    fieldD0: struct_sinthing_t
    pathWalker: struct_pw_pathwalker_t
    state: int

class crsmdl_t(Structure):
    """
    ```python
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    modelV: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    nsbtpAnim: struct_anim_manager_t (struct_anim_manager_t)
    nsbtaAnim: struct_anim_manager_t (struct_anim_manager_t)
    nsbtaAnimV: struct_anim_manager_t (struct_anim_manager_t)
    mtx: union_MtxFx43 (union_MtxFx43)
    modelHasPartialFog: int (POINTER(i))
    PADDING_0: list[int] (POINTER(B)[4])
    modelFogFlags: int (POINTER(l))
    modelVHasPartialFog: int (POINTER(i))
    modelVFogFlags: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    model: POINTER_T[struct_model_t]
    modelV: POINTER_T[struct_model_t]
    nsbtpAnim: struct_anim_manager_t
    nsbtaAnim: struct_anim_manager_t
    nsbtaAnimV: struct_anim_manager_t
    mtx: union_MtxFx43
    modelHasPartialFog: int
    PADDING_0: list[int]
    modelFogFlags: int
    modelVHasPartialFog: int
    modelVFogFlags: int
    PADDING_1: list[int]

class dc_masterbright_t(Structure):
    """
    ```python
    state: int (POINTER(H))
    fadeType: int (POINTER(H))
    curFrame: int (POINTER(h))
    frameCount: int (POINTER(h))
    brightness: int (POINTER(h))
    fieldA: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    fadeType: int
    curFrame: int
    frameCount: int
    brightness: int
    fieldA: int

class dce_t(Structure):
    """
    ```python
    mode: int (POINTER(I))
    oamBuf: POINTER_T[struct_GXOamAttr] (POINTER(struct_GXOamAttr))
    flags: int (POINTER(H))
    blurAmount: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    blurProgress: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mode: int
    oamBuf: POINTER_T[struct_GXOamAttr]
    flags: int
    blurAmount: int
    PADDING_0: int
    blurProgress: fx32

class dcol_inst_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    lastMtx: union_MtxFx33 (union_MtxFx33)
    baseMtx: union_MtxFx33 (union_MtxFx33)
    lastPosition: struct_VecFx32 (struct_VecFx32)
    basePos: struct_VecFx32 (struct_VecFx32)
    size: struct_VecFx32 (struct_VecFx32)
    sizeZ2: fx32 (struct_fx32)
    isFloorYZ: int (POINTER(i))
    isFloorXZ: int (POINTER(i))
    isFloorXY: int (POINTER(i))
    isBoostPanel: int (POINTER(i))
    floorThreshold: fx32 (struct_fx32)
    field124: struct_VecFx32 (struct_VecFx32)
    field130: int (POINTER(I))
    shape: int (POINTER(I))
    field138: int (POINTER(I))
    field13C: int (POINTER(I))
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    lastMtx: union_MtxFx33
    baseMtx: union_MtxFx33
    lastPosition: struct_VecFx32
    basePos: struct_VecFx32
    size: struct_VecFx32
    sizeZ2: fx32
    isFloorYZ: int
    isFloorXZ: int
    isFloorXY: int
    isBoostPanel: int
    floorThreshold: fx32
    field124: struct_VecFx32
    field130: int
    shape: int
    field138: int
    field13C: int
    model: POINTER_T[struct_model_t]

class display_config_3d_t(Structure):
    """
    ```python
    clearColor: int (POINTER(H))
    sortMode: int (POINTER(B))
    bufferMode: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    clearColor: int
    sortMode: int
    bufferMode: int

class display_config_base_t(Structure):
    """
    ```python
    vblankWaitCount: int (POINTER(H))
    mainVisiblePlane: int (POINTER(H))
    subVisiblePlane: int (POINTER(H))
    mainDisplayMode: int (POINTER(H))
    mainBgMode: int (POINTER(H))
    mainBg03d: int (POINTER(H))
    subBgMode: int (POINTER(H))
    mainBgBank: int (POINTER(H))
    mainObjBank: int (POINTER(H))
    mainBgExtPlttBank: int (POINTER(H))
    mainObjExtPlttBank: int (POINTER(H))
    texBank: int (POINTER(H))
    texPlttBank: int (POINTER(H))
    clearImgBank: int (POINTER(H))
    subBgBank: int (POINTER(H))
    subObjBank: int (POINTER(H))
    subBgExtPlttBank: int (POINTER(H))
    subObjExtPlttBank: int (POINTER(H))
    arm7Bank: int (POINTER(H))
    lcdcBank: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    vblankWaitCount: int
    mainVisiblePlane: int
    subVisiblePlane: int
    mainDisplayMode: int
    mainBgMode: int
    mainBg03d: int
    subBgMode: int
    mainBgBank: int
    mainObjBank: int
    mainBgExtPlttBank: int
    mainObjExtPlttBank: int
    texBank: int
    texPlttBank: int
    clearImgBank: int
    subBgBank: int
    subObjBank: int
    subBgExtPlttBank: int
    subObjExtPlttBank: int
    arm7Bank: int
    lcdcBank: int

class display_config_bg01_t(Structure):
    """
    ```python
    common: struct_display_config_bgcommon_t (struct_display_config_bgcommon_t)
    extPlttSlot: int (POINTER(H))
    unk: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    common: struct_display_config_bgcommon_t
    extPlttSlot: int
    unk: int

class display_config_bg23_t(Structure):
    """
    ```python
    mode: int (POINTER(I))
    common: struct_display_config_bgcommon_t (struct_display_config_bgcommon_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mode: int
    common: struct_display_config_bgcommon_t

class display_config_bgcommon_t(Structure):
    """
    ```python
    priority: int (POINTER(H))
    mosaic: int (POINTER(H))
    screenSize: int (POINTER(H))
    colorMode: int (POINTER(H))
    screenBase: int (POINTER(H))
    characterBase: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    priority: int
    mosaic: int
    screenSize: int
    colorMode: int
    screenBase: int
    characterBase: int

class display_config_engine_t(Structure):
    """
    ```python
    bg0Config: struct_display_config_bg01_t (struct_display_config_bg01_t)
    bg1Config: struct_display_config_bg01_t (struct_display_config_bg01_t)
    bg2Config: struct_display_config_bg23_t (struct_display_config_bg23_t)
    bg3Config: struct_display_config_bg23_t (struct_display_config_bg23_t)
    objVRamModeChar: int (POINTER(H))
    objVRamModeBmp: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    bg0Config: struct_display_config_bg01_t
    bg1Config: struct_display_config_bg01_t
    bg2Config: struct_display_config_bg23_t
    bg3Config: struct_display_config_bg23_t
    objVRamModeChar: int
    objVRamModeBmp: int

class display_config_t(Structure):
    """
    ```python
    baseConfig: struct_display_config_base_t (struct_display_config_base_t)
    mainConfig: struct_display_config_engine_t (struct_display_config_engine_t)
    config3d: POINTER_T[struct_display_config_3d_t] (POINTER(struct_display_config_3d_t))
    subConfig: struct_display_config_engine_t (struct_display_config_engine_t)
    fieldB4: int (POINTER(I))
    vblankFunc: Callable[[], None] (CFunctionType)
    PADDING_0: list[int] (POINTER(B)[4])
    frameStartTime: int (POINTER(L))
    vblankTime: int (POINTER(L))
    renderDuration: int (POINTER(I))
    lastTotalDuration: int (POINTER(I))
    lastRenderDuration: int (POINTER(I))
    flags: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    baseConfig: struct_display_config_base_t
    mainConfig: struct_display_config_engine_t
    config3d: POINTER_T[struct_display_config_3d_t]
    subConfig: struct_display_config_engine_t
    fieldB4: int
    vblankFunc: Callable[[], None]
    PADDING_0: list[int]
    frameStartTime: int
    vblankTime: int
    renderDuration: int
    lastTotalDuration: int
    lastRenderDuration: int
    flags: int
    PADDING_1: list[int]

class dossun_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    state: int (POINTER(I))
    stateCounter: int (POINTER(i))
    someSpeed: fx32 (struct_fx32)
    floorY: fx32 (struct_fx32)
    isSmashing: int (POINTER(i))
    starHitAnimState: int (POINTER(I))
    rotYDelta: int (POINTER(h))
    rotY: int (POINTER(h))
    lastStarHitFrame: int (POINTER(I))
    noStarHitPlayerMask: int (POINTER(H))
    sinAng: int (POINTER(H))
    sinAmplitude: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    initialPathPoint: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    isHorizontalMoveType: int (POINTER(i))
    fieldF4: struct_VecFx32 (struct_VecFx32)
    field100: fx32 (struct_fx32)
    someAcceleration: fx32 (struct_fx32)
    anotherSpeed: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    state: int
    stateCounter: int
    someSpeed: fx32
    floorY: fx32
    isSmashing: int
    starHitAnimState: int
    rotYDelta: int
    rotY: int
    lastStarHitFrame: int
    noStarHitPlayerMask: int
    sinAng: int
    sinAmplitude: fx32
    pathwalker: struct_pw_pathwalker_t
    initialPathPoint: int
    PADDING_0: list[int]
    isHorizontalMoveType: int
    fieldF4: struct_VecFx32
    field100: fx32
    someAcceleration: fx32
    anotherSpeed: fx32

class dptc_t(Structure):
    """
    ```python
    whiteDustCloudEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    blueSparkEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    contRedSparkEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    contRedSparkSmallEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    redSparkEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    redSparksSmallEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    contRedSparksCounter: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    field34: int (POINTER(i))
    contRedSparksActive: int (POINTER(i))
    whiteDustCloudsActive: int (POINTER(i))
    redSparksActive: int (POINTER(i))
    blueSparksActive: int (POINTER(i))
    redSparksCounter: int (POINTER(h))
    blueSparkCounter: int (POINTER(h))
    whiteDustCloudParticleId: int (POINTER(i))
    contRedSparkParticleId: int (POINTER(i))
    contRedSparkSmallParticleId: int (POINTER(i))
    redSparkParticleId: int (POINTER(i))
    redSparksSmallParticleId: int (POINTER(i))
    driverId: int (POINTER(H))
    field62: int (POINTER(H))
    field64: int (POINTER(i))
    startContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    suspendContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    resumeContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    killContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    field78: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    hideAllFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    showAllFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    updateContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t], POINTER_T[struct_VecFx16], POINTER_T[struct_VecFx32]], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    whiteDustCloudEmitters: list[POINTER_T[struct_spa_emitter_t]]
    blueSparkEmitters: list[POINTER_T[struct_spa_emitter_t]]
    contRedSparkEmitters: list[POINTER_T[struct_spa_emitter_t]]
    contRedSparkSmallEmitters: list[POINTER_T[struct_spa_emitter_t]]
    redSparkEmitters: list[POINTER_T[struct_spa_emitter_t]]
    redSparksSmallEmitters: list[POINTER_T[struct_spa_emitter_t]]
    contRedSparksCounter: int
    PADDING_0: list[int]
    field34: int
    contRedSparksActive: int
    whiteDustCloudsActive: int
    redSparksActive: int
    blueSparksActive: int
    redSparksCounter: int
    blueSparkCounter: int
    whiteDustCloudParticleId: int
    contRedSparkParticleId: int
    contRedSparkSmallParticleId: int
    redSparkParticleId: int
    redSparksSmallParticleId: int
    driverId: int
    field62: int
    field64: int
    startContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    suspendContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    resumeContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    killContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    field78: Callable[[POINTER_T[struct_dptc_t]], None]
    hideAllFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    showAllFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    updateContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t], POINTER_T[struct_VecFx16], POINTER_T[struct_VecFx32]], None]

class dram_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    startStopFrameCount: int (POINTER(H))
    spinFrameCount: int (POINTER(H))
    waitFrameCount: int (POINTER(H))
    angle: int (POINTER(H))
    angularSpeed: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    currentSpeed: fx32 (struct_fx32)
    startStopSpeed: fx32 (struct_fx32)
    speeds: list[int] (POINTER(h)[3])
    PADDING_1: list[int] (POINTER(B)[2])
    alignRemainder: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    startStopFrameCount: int
    spinFrameCount: int
    waitFrameCount: int
    angle: int
    angularSpeed: int
    PADDING_0: list[int]
    currentSpeed: fx32
    startStopSpeed: fx32
    speeds: list[int]
    PADDING_1: list[int]
    alignRemainder: int

class driver_field450_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    field8: fx32 (struct_fx32)
    fieldC: int (POINTER(i))
    field10: int (POINTER(i))
    field14: int (POINTER(i))
    field18: fx32 (struct_fx32)
    field1C: fx32 (struct_fx32)
    field20: fx32 (struct_fx32)
    field24: fx32 (struct_fx32)
    prevLapProgress: int (POINTER(i))
    kaidanSfxAlternateCounter: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    field30: int (POINTER(i))
    field34: int (POINTER(i))
    sfxId: int (POINTER(i))
    computePitchOffsetFunc: Callable[[POINTER_T[struct_sfx_emitter_ex_params_t]], c_int] (CFunctionType)
    field40: struct_struc_334 (struct_struc_334)
    field68: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    PADDING_0: list[int]
    field8: fx32
    fieldC: int
    field10: int
    field14: int
    field18: fx32
    field1C: fx32
    field20: fx32
    field24: fx32
    prevLapProgress: int
    kaidanSfxAlternateCounter: int
    PADDING_1: list[int]
    field30: int
    field34: int
    sfxId: int
    computePitchOffsetFunc: Callable[[POINTER_T[struct_sfx_emitter_ex_params_t]], c_int]
    field40: struct_struc_334
    field68: int

class driver_field514_field8C_entry_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    field8: int (POINTER(h))
    gapA: list[int] (POINTER(B)[2])
    fieldC: struct_struc_351 (struct_struc_351)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    field8: int
    gapA: list[int]
    fieldC: struct_struc_351

class driver_net_state_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    fieldC: int (POINTER(H))
    fieldE: int (POINTER(H))
    field10: struct_VecFx32 (struct_VecFx32)
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: fx32 (struct_fx32)
    field28: int (POINTER(i))
    flags: int (POINTER(i))
    lastFlags: int (POINTER(i))
    field34: struct_VecFx32 (struct_VecFx32)
    driftRotY: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    field44: int (POINTER(i))
    field48: int (POINTER(I))
    field4C: quaternion_t (struct_quaternion_t)
    field5C: int (POINTER(h))
    PADDING_1: list[int] (POINTER(B)[2])
    field60: int (POINTER(i))
    field64: int (POINTER(i))
    gap68: list[int] (POINTER(B)[24])
    field80: struct_NNSFndList (struct_NNSFndList)
    field8C: struct_NNSFndList (struct_NNSFndList)
    field98: struct_VecFx32 (struct_VecFx32)
    fieldA4: int (POINTER(I))
    fieldA8: struct_VecFx32 (struct_VecFx32)
    fieldB4: int (POINTER(H))
    gapB6: list[int] (POINTER(B)[1])
    fieldB7: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    fieldC: int
    fieldE: int
    field10: struct_VecFx32
    field1C: int
    field20: int
    field24: fx32
    field28: int
    flags: int
    lastFlags: int
    field34: struct_VecFx32
    driftRotY: int
    PADDING_0: list[int]
    field44: int
    field48: int
    field4C: quaternion_t
    field5C: int
    PADDING_1: list[int]
    field60: int
    field64: int
    gap68: list[int]
    field80: struct_NNSFndList
    field8C: struct_NNSFndList
    field98: struct_VecFx32
    fieldA4: int
    fieldA8: struct_VecFx32
    fieldB4: int
    gapB6: list[int]
    fieldB7: int

class driver_statistics_t(Structure):
    """
    ```python
    gotStartBoost: int (POINTER(i))
    powerSlideCount: int (POINTER(I))
    itemHitCount: int (POINTER(i))
    offRoadTime: int (POINTER(I))
    wallHitCount: int (POINTER(i))
    damageCount: int (POINTER(i))
    respawnCount: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    gotStartBoost: int
    powerSlideCount: int
    itemHitCount: int
    offRoadTime: int
    wallHitCount: int
    damageCount: int
    respawnCount: int

class driver_t(Structure):
    """
    ```python
    soundEmitter: struct_sfx_emitter_t (struct_sfx_emitter_t)
    field44: int (POINTER(I))
    flags: int (POINTER(I))
    flags2: int (POINTER(I))
    direction: struct_VecFx32 (struct_VecFx32)
    drivingDirection: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    id: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    inputId: int (POINTER(I))
    field7C: int (POINTER(I))
    position: struct_VecFx32 (struct_VecFx32)
    lastPosition: struct_VecFx32 (struct_VecFx32)
    kartTiresPosition: struct_VecFx32 (struct_VecFx32)
    deltaPos: struct_VecFx32 (struct_VecFx32)
    deltaPosNormalized: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    fieldC8: fx32 (struct_fx32)
    targetMaxSpeed: fx32 (struct_fx32)
    maxSpeed: fx32 (struct_fx32)
    fieldD4: int (POINTER(I))
    slipstreamSpeedMultiplier: fx32 (struct_fx32)
    speedMultiplier: fx32 (struct_fx32)
    rotation: quaternion_t (struct_quaternion_t)
    fieldF0: quaternion_t (struct_quaternion_t)
    field100: quaternion_t (struct_quaternion_t)
    field110: quaternion_t (struct_quaternion_t)
    mainMtx: union_MtxFx43 (union_MtxFx43)
    field150: union_MtxFx43 (union_MtxFx43)
    colReaction: int (POINTER(I))
    field184: union_MtxFx43 (union_MtxFx43)
    charKartMtx: int (POINTER(I))
    colPos: struct_VecFx32 (struct_VecFx32)
    prevColPos: struct_VecFx32 (struct_VecFx32)
    colSphereSize: fx32 (struct_fx32)
    colSphereZOffset: fx32 (struct_fx32)
    netColPos: struct_VecFx32 (struct_VecFx32)
    lastNetColPos: struct_VecFx32 (struct_VecFx32)
    colPos2: struct_VecFx32 (struct_VecFx32)
    field1FC: struct_VecFx32 (struct_VecFx32)
    field208: POINTER_T[c_uint] (POINTER(POINTER(I)))
    field20C: list[c_void_p] (c_void_p[9])
    field230: Callable[[POINTER_T[struct_driver_t]], None] (CFunctionType)
    xRot: int (POINTER(h))
    yRot: int (POINTER(H))
    boostTimer: int (POINTER(h))
    field23A: int (POINTER(h))
    driftBoostCounter: int (POINTER(h))
    PADDING_1: list[int] (POINTER(B)[2])
    velocityMinusDirMultiplier: fx32 (struct_fx32)
    upDir: struct_VecFx32 (struct_VecFx32)
    field250: struct_VecFx32 (struct_VecFx32)
    velocityY: struct_VecFx32 (struct_VecFx32)
    fallsWaterForward: struct_VecFx32 (struct_VecFx32)
    fallsWaterStrength: fx32 (struct_fx32)
    forwardDir: struct_VecFx32 (struct_VecFx32)
    jumpDriftUp: struct_VecFx32 (struct_VecFx32)
    jumpDriftForward: struct_VecFx32 (struct_VecFx32)
    collisionMode: int (POINTER(I))
    maxSpeedFraction: fx32 (struct_fx32)
    deltaPosMag: fx32 (struct_fx32)
    speed: fx32 (struct_fx32)
    field2AC: fx32 (struct_fx32)
    driverHitCheckMask: int (POINTER(H))
    driverHitMask: int (POINTER(H))
    lastDriverHitMask: int (POINTER(H))
    gap2B6: list[int] (POINTER(B)[2])
    field2B8: int (POINTER(i))
    field2BC: int (POINTER(i))
    field2C0: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    leftRightDir: fx32 (struct_fx32)
    colEntryId1: int (POINTER(h))
    colEntryId2: int (POINTER(h))
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t] (POINTER(struct_physp_kart_params_t))
    charPhysicalParams: POINTER_T[struct_physp_char_params_t] (POINTER(struct_physp_char_params_t))
    turningAmount: fx32 (struct_fx32)
    field2D8: struct_VecFx32 (struct_VecFx32)
    field2E4: struct_VecFx32 (struct_VecFx32)
    field2F0: struct_VecFx32 (struct_VecFx32)
    driftLeftRightCount: int (POINTER(i))
    driftLeftCount: int (POINTER(H))
    driftRightCount: int (POINTER(H))
    driftDir1CountPtr: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    driftDir2CountPtr: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    driftLeftRightTimeout: int (POINTER(i))
    enemyState: POINTER_T[struct_enemy_t] (POINTER(struct_enemy_t))
    field314: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    field318: fx32 (struct_fx32)
    field31C: struct_VecFx32 (struct_VecFx32)
    field328: struct_VecFx32 (struct_VecFx32)
    field334: int (POINTER(I))
    field338: int (POINTER(H))
    PADDING_4: list[int] (POINTER(B)[2])
    field33C: int (POINTER(I))
    field340: fx32 (struct_fx32)
    field344: int (POINTER(I))
    field348: int (POINTER(I))
    field34C: quaternion_t (struct_quaternion_t)
    colReactionCounter: int (POINTER(h))
    PADDING_5: list[int] (POINTER(B)[2])
    field360: fx32 (struct_fx32)
    spinOutAngle: int (POINTER(H))
    spinOutSpinCount: int (POINTER(H))
    spinOutProgress: fx32 (struct_fx32)
    spinOutVelocity: int (POINTER(I))
    field370: int (POINTER(H))
    PADDING_6: list[int] (POINTER(B)[2])
    field374: struct_VecFx32 (struct_VecFx32)
    field380: int (POINTER(I))
    ghostFlickerPhase: int (POINTER(H))
    wallRotYSpeed: int (POINTER(h))
    driftRotY: int (POINTER(h))
    extraDrift: fx16 (struct_fx16)
    field38C: fx32 (struct_fx32)
    gap390: list[int] (POINTER(B)[4])
    field394: int (POINTER(I))
    field398: fx32 (struct_fx32)
    field39C: fx32 (struct_fx32)
    field3A0: fx32 (struct_fx32)
    tireRotX: int (POINTER(H))
    PADDING_7: list[int] (POINTER(B)[2])
    field3A8: int (POINTER(i))
    respawnCounter: int (POINTER(H))
    PADDING_8: list[int] (POINTER(B)[2])
    field3B0: struct_VecFx32 (struct_VecFx32)
    field3BC: int (POINTER(H))
    field3BE: int (POINTER(h))
    preRespawnCounter: int (POINTER(h))
    PADDING_9: list[int] (POINTER(B)[2])
    respawnId: int (POINTER(I))
    killTimer: int (POINTER(h))
    PADDING_10: list[int] (POINTER(B)[2])
    driverVoiceIdx: int (POINTER(I))
    kartABC: int (POINTER(h))
    field3D2: int (POINTER(h))
    field3D4: int (POINTER(h))
    PADDING_11: list[int] (POINTER(B)[2])
    place: int (POINTER(i))
    floorDriverColType: int (POINTER(I))
    floorColType: int (POINTER(I))
    floorColVariant: int (POINTER(i))
    field3E8: int (POINTER(h))
    PADDING_12: list[int] (POINTER(B)[2])
    yRotSpeedTarget: int (POINTER(I))
    yRotSpeed: int (POINTER(I))
    field3F4: fx32 (struct_fx32)
    field3F8: fx32 (struct_fx32)
    field3FC: int (POINTER(H))
    field3FE: int (POINTER(H))
    field400: int (POINTER(H))
    PADDING_13: list[int] (POINTER(B)[2])
    field404: fx32 (struct_fx32)
    field408: int (POINTER(I))
    respawnStartFrame: int (POINTER(I))
    respawnAPressFrame: int (POINTER(I))
    field414: fx32 (struct_fx32)
    field418: fx32 (struct_fx32)
    growBackScale: struct_VecFx32 (struct_VecFx32)
    thunderScale: struct_VecFx32 (struct_VecFx32)
    dossunYScale: fx32 (struct_fx32)
    mobjHitList: list[POINTER_T[struct_mobj_inst_t]] (POINTER(struct_mobj_inst_t)[2])
    mobjHitSfxTimeout: list[int] (POINTER(H)[2])
    mobjHitEmittedSfx: list[int] (POINTER(i)[2])
    smashDossun: POINTER_T[struct_mobj_inst_t] (POINTER(struct_mobj_inst_t))
    field450: struct_driver_field450_t (struct_driver_field450_t)
    field4BC: fx32 (struct_fx32)
    colFlagsMap2DShadow: int (POINTER(I))
    jumpPadSpeed: int (POINTER(I))
    field4C8: fx32 (struct_fx32)
    field4CC: int (POINTER(I))
    field4D0: int (POINTER(I))
    preStartEnginePower: fx32 (struct_fx32)
    fallsWaterDstId: int (POINTER(h))
    wallTouchTimeout: int (POINTER(h))
    floorTouchTimeout: int (POINTER(h))
    field4DE: int (POINTER(h))
    field4E0: int (POINTER(h))
    field4E2: int (POINTER(h))
    field4E4: int (POINTER(H))
    field4E6: int (POINTER(H))
    field4E8: fx32 (struct_fx32)
    field4EC: fx32 (struct_fx32)
    idkScale: struct_VecFx32 (struct_VecFx32)
    field4FC: int (POINTER(H))
    PADDING_14: list[int] (POINTER(B)[2])
    waterDepth: fx32 (struct_fx32)
    field504: int (POINTER(H))
    field506: int (POINTER(H))
    field508: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    field50C: POINTER_T[struct_quaternion_t] (POINTER(struct_quaternion_t))
    field510: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    netState: POINTER_T[struct_driver_net_state_t] (POINTER(struct_driver_net_state_t))
    field518: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    field534: c_void_p (c_void_p)
    timers: struct_driver_timers_t (struct_driver_timers_t)
    charKart: POINTER_T[struct_charkart_t] (POINTER(struct_charkart_t))
    field594: fx32 (struct_fx32)
    field598: int (POINTER(h))
    PADDING_15: list[int] (POINTER(B)[2])
    field59C: int (POINTER(I))
    field5A0: int (POINTER(H))
    gap5A2: list[int] (POINTER(B)[2])
    field5A4: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    soundEmitter: struct_sfx_emitter_t
    field44: int
    flags: int
    flags2: int
    direction: struct_VecFx32
    drivingDirection: struct_VecFx32
    velocity: struct_VecFx32
    id: int
    PADDING_0: list[int]
    inputId: int
    field7C: int
    position: struct_VecFx32
    lastPosition: struct_VecFx32
    kartTiresPosition: struct_VecFx32
    deltaPos: struct_VecFx32
    deltaPosNormalized: struct_VecFx32
    scale: struct_VecFx32
    fieldC8: fx32
    targetMaxSpeed: fx32
    maxSpeed: fx32
    fieldD4: int
    slipstreamSpeedMultiplier: fx32
    speedMultiplier: fx32
    rotation: quaternion_t
    fieldF0: quaternion_t
    field100: quaternion_t
    field110: quaternion_t
    mainMtx: union_MtxFx43
    field150: union_MtxFx43
    colReaction: int
    field184: union_MtxFx43
    charKartMtx: int
    colPos: struct_VecFx32
    prevColPos: struct_VecFx32
    colSphereSize: fx32
    colSphereZOffset: fx32
    netColPos: struct_VecFx32
    lastNetColPos: struct_VecFx32
    colPos2: struct_VecFx32
    field1FC: struct_VecFx32
    field208: POINTER_T[c_uint]
    field20C: list[c_void_p]
    field230: Callable[[POINTER_T[struct_driver_t]], None]
    xRot: int
    yRot: int
    boostTimer: int
    field23A: int
    driftBoostCounter: int
    PADDING_1: list[int]
    velocityMinusDirMultiplier: fx32
    upDir: struct_VecFx32
    field250: struct_VecFx32
    velocityY: struct_VecFx32
    fallsWaterForward: struct_VecFx32
    fallsWaterStrength: fx32
    forwardDir: struct_VecFx32
    jumpDriftUp: struct_VecFx32
    jumpDriftForward: struct_VecFx32
    collisionMode: int
    maxSpeedFraction: fx32
    deltaPosMag: fx32
    speed: fx32
    field2AC: fx32
    driverHitCheckMask: int
    driverHitMask: int
    lastDriverHitMask: int
    gap2B6: list[int]
    field2B8: int
    field2BC: int
    field2C0: int
    PADDING_2: list[int]
    leftRightDir: fx32
    colEntryId1: int
    colEntryId2: int
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t]
    charPhysicalParams: POINTER_T[struct_physp_char_params_t]
    turningAmount: fx32
    field2D8: struct_VecFx32
    field2E4: struct_VecFx32
    field2F0: struct_VecFx32
    driftLeftRightCount: int
    driftLeftCount: int
    driftRightCount: int
    driftDir1CountPtr: POINTER_T[c_ushort]
    driftDir2CountPtr: POINTER_T[c_ushort]
    driftLeftRightTimeout: int
    enemyState: POINTER_T[struct_enemy_t]
    field314: int
    PADDING_3: list[int]
    field318: fx32
    field31C: struct_VecFx32
    field328: struct_VecFx32
    field334: int
    field338: int
    PADDING_4: list[int]
    field33C: int
    field340: fx32
    field344: int
    field348: int
    field34C: quaternion_t
    colReactionCounter: int
    PADDING_5: list[int]
    field360: fx32
    spinOutAngle: int
    spinOutSpinCount: int
    spinOutProgress: fx32
    spinOutVelocity: int
    field370: int
    PADDING_6: list[int]
    field374: struct_VecFx32
    field380: int
    ghostFlickerPhase: int
    wallRotYSpeed: int
    driftRotY: int
    extraDrift: fx16
    field38C: fx32
    gap390: list[int]
    field394: int
    field398: fx32
    field39C: fx32
    field3A0: fx32
    tireRotX: int
    PADDING_7: list[int]
    field3A8: int
    respawnCounter: int
    PADDING_8: list[int]
    field3B0: struct_VecFx32
    field3BC: int
    field3BE: int
    preRespawnCounter: int
    PADDING_9: list[int]
    respawnId: int
    killTimer: int
    PADDING_10: list[int]
    driverVoiceIdx: int
    kartABC: int
    field3D2: int
    field3D4: int
    PADDING_11: list[int]
    place: int
    floorDriverColType: int
    floorColType: int
    floorColVariant: int
    field3E8: int
    PADDING_12: list[int]
    yRotSpeedTarget: int
    yRotSpeed: int
    field3F4: fx32
    field3F8: fx32
    field3FC: int
    field3FE: int
    field400: int
    PADDING_13: list[int]
    field404: fx32
    field408: int
    respawnStartFrame: int
    respawnAPressFrame: int
    field414: fx32
    field418: fx32
    growBackScale: struct_VecFx32
    thunderScale: struct_VecFx32
    dossunYScale: fx32
    mobjHitList: list[POINTER_T[struct_mobj_inst_t]]
    mobjHitSfxTimeout: list[int]
    mobjHitEmittedSfx: list[int]
    smashDossun: POINTER_T[struct_mobj_inst_t]
    field450: struct_driver_field450_t
    field4BC: fx32
    colFlagsMap2DShadow: int
    jumpPadSpeed: int
    field4C8: fx32
    field4CC: int
    field4D0: int
    preStartEnginePower: fx32
    fallsWaterDstId: int
    wallTouchTimeout: int
    floorTouchTimeout: int
    field4DE: int
    field4E0: int
    field4E2: int
    field4E4: int
    field4E6: int
    field4E8: fx32
    field4EC: fx32
    idkScale: struct_VecFx32
    field4FC: int
    PADDING_14: list[int]
    waterDepth: fx32
    field504: int
    field506: int
    field508: POINTER_T[struct_VecFx32]
    field50C: POINTER_T[struct_quaternion_t]
    field510: POINTER_T[struct_VecFx32]
    netState: POINTER_T[struct_driver_net_state_t]
    field518: struct_sfx_emitter_ex_params_t
    field534: c_void_p
    timers: struct_driver_timers_t
    charKart: POINTER_T[struct_charkart_t]
    field594: fx32
    field598: int
    PADDING_15: list[int]
    field59C: int
    field5A0: int
    gap5A2: list[int]
    field5A4: fx32

class driver_timers_t(Structure):
    """
    ```python
    shroomBoostTimer: int (POINTER(h))
    thunderShrinkTimer: int (POINTER(h))
    thunderGrowTimer: int (POINTER(h))
    starTimer: int (POINTER(h))
    slipstreamStartTimer: int (POINTER(h))
    slipstreamTimer: int (POINTER(h))
    dossunGrowTimer: int (POINTER(h))
    dossunFlatTimer: int (POINTER(h))
    teresaTimer: int (POINTER(h))
    teresaFlickerInterval: int (POINTER(h))
    teresaFlickerIntervalUpdateTimer: int (POINTER(h))
    teresaFlickerTimer: int (POINTER(h))
    teresaFlickerIntervalUpdateWaitTime: int (POINTER(h))
    teresaFlickerIntervalStep: int (POINTER(h))
    gessoInkTimer: int (POINTER(h))
    killerFrameCounter: int (POINTER(h))
    field20: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    isKillerFinishing: int (POINTER(i))
    killerTargetPlace: int (POINTER(h))
    gap2A: list[int] (POINTER(B)[2])
    killerState: list[int] (POINTER(B)[44])
    ```
    """
    _pack_: ClassVar[int] = 1
    shroomBoostTimer: int
    thunderShrinkTimer: int
    thunderGrowTimer: int
    starTimer: int
    slipstreamStartTimer: int
    slipstreamTimer: int
    dossunGrowTimer: int
    dossunFlatTimer: int
    teresaTimer: int
    teresaFlickerInterval: int
    teresaFlickerIntervalUpdateTimer: int
    teresaFlickerTimer: int
    teresaFlickerIntervalUpdateWaitTime: int
    teresaFlickerIntervalStep: int
    gessoInkTimer: int
    killerFrameCounter: int
    field20: int
    PADDING_0: list[int]
    isKillerFinishing: int
    killerTargetPlace: int
    gap2A: list[int]
    killerState: list[int]

class efbnr_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    counter: int (POINTER(i))
    nsbtaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    scale: fx32 (struct_fx32)
    state: int (POINTER(I))
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    driverHitTimeouts: list[int] (POINTER(i)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    counter: int
    nsbtaFrame: int
    PADDING_0: list[int]
    scale: fx32
    state: int
    pathwalker: struct_pw_pathwalker_t
    driverHitTimeouts: list[int]

class efbub_logic_part_t(Structure):
    """
    ```python
    logicPart: struct_mobj_logic_part_t (struct_mobj_logic_part_t)
    field28: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    logicPart: struct_mobj_logic_part_t
    field28: int

class efbub_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    waitTime: int (POINTER(i))
    lowYPos: fx32 (struct_fx32)
    rotation: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    highYPos: fx32 (struct_fx32)
    shadow: struct_objshadow_t (struct_objshadow_t)
    driverHitMask: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    emitter69: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    emitter70: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    emitterFail: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    waitTime: int
    lowYPos: fx32
    rotation: int
    PADDING_0: list[int]
    highYPos: fx32
    shadow: struct_objshadow_t
    driverHitMask: int
    PADDING_1: list[int]
    emitter69: POINTER_T[struct_spa_emitter_t]
    emitter70: POINTER_T[struct_spa_emitter_t]
    emitterFail: int

class enemy_field140_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    driverFieldCC: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    field10: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    driverFieldCC: int
    field8: int
    fieldC: int
    field10: int

class enemy_item_params_t(Structure):
    """
    ```python
    updateFunc: c_void_p (c_void_p)
    field4: int (POINTER(i))
    minTimeout: int (POINTER(H))
    timeoutRandomMax: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    updateFunc: c_void_p
    field4: int
    minTimeout: int
    timeoutRandomMax: int

class enemy_item_state_t(Structure):
    """
    ```python
    slotItemTimeout: int (POINTER(H))
    dragItemTimeout: int (POINTER(H))
    slotItemParams: POINTER_T[struct_enemy_item_params_t] (POINTER(struct_enemy_item_params_t))
    dragItemParams: POINTER_T[struct_enemy_item_params_t] (POINTER(struct_enemy_item_params_t))
    fieldC: int (POINTER(i))
    lxPressed: int (POINTER(i))
    dpadUpPressed: int (POINTER(i))
    dpadDownPressed: int (POINTER(i))
    dpadUpCounter: int (POINTER(H))
    dpadDownCounter: int (POINTER(H))
    field20: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    slotItemTimeout: int
    dragItemTimeout: int
    slotItemParams: POINTER_T[struct_enemy_item_params_t]
    dragItemParams: POINTER_T[struct_enemy_item_params_t]
    fieldC: int
    lxPressed: int
    dpadUpPressed: int
    dpadDownPressed: int
    dpadUpCounter: int
    dpadDownCounter: int
    field20: int

class enemy_rubberbanding_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    driverFieldCC: int (POINTER(i))
    rivalAggressiveness: int (POINTER(i))
    maxDriverFieldCC: int (POINTER(i))
    field10: int (POINTER(i))
    place: int (POINTER(i))
    field18: int (POINTER(i))
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    hasFailedStart: int (POINTER(i))
    hasStartBoost: int (POINTER(i))
    startBoostAmount: int (POINTER(H))
    field32: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    driverFieldCC: int
    rivalAggressiveness: int
    maxDriverFieldCC: int
    field10: int
    place: int
    field18: int
    field1C: int
    field20: int
    field24: int
    hasFailedStart: int
    hasStartBoost: int
    startBoostAmount: int
    field32: int

class enemy_t(Structure):
    """
    ```python
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    driverId: int (POINTER(H))
    field6: int (POINTER(H))
    epoi: struct_struc_316_epoi (struct_struc_316_epoi)
    mepo: struct_struc_313_mepo (struct_struc_313_mepo)
    targetPos: struct_VecFx32 (struct_VecFx32)
    field50: struct_VecFx32 (struct_VecFx32)
    field5C: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    driftOffset: struct_VecFx32 (struct_VecFx32)
    driftEpoiRadiusScaleUpdateCounter: int (POINTER(H))
    driftEpoiRadiusScaleUpdateFrames: int (POINTER(H))
    field70: int (POINTER(i))
    driftEpoiRadiusScale: fx32 (struct_fx32)
    field78: int (POINTER(H))
    field7A: int (POINTER(H))
    field7C: int (POINTER(i))
    field80: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field84: int (POINTER(i))
    field88: int (POINTER(i))
    field8C: int (POINTER(i))
    driftState: int (POINTER(i))
    driftDirection: int (POINTER(i))
    field98: int (POINTER(i))
    field9C: int (POINTER(i))
    fieldA0: int (POINTER(i))
    fieldA4: int (POINTER(i))
    fieldA8: int (POINTER(i))
    fieldAC: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    targetDriver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    fieldB4: int (POINTER(i))
    fieldB8: int (POINTER(i))
    fieldBC: int (POINTER(i))
    targetBalloonCount: int (POINTER(H))
    balloonInflateMicTimeout: int (POINTER(H))
    isInflatingBalloon: int (POINTER(i))
    fieldC8: int (POINTER(H))
    fieldCA: int (POINTER(H))
    fieldCC: int (POINTER(i))
    targetShine: c_void_p (c_void_p)
    shineIdx: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    fieldD8: int (POINTER(i))
    fieldDC: struct_VecFx32 (struct_VecFx32)
    rubberbanding: struct_enemy_rubberbanding_t (struct_enemy_rubberbanding_t)
    itemState: struct_enemy_item_state_t (struct_enemy_item_state_t)
    field140: struct_enemy_field140_t (struct_enemy_field140_t)
    field154: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    driver: POINTER_T[struct_driver_t]
    driverId: int
    field6: int
    epoi: struct_struc_316_epoi
    mepo: struct_struc_313_mepo
    targetPos: struct_VecFx32
    field50: struct_VecFx32
    field5C: POINTER_T[struct_VecFx32]
    driftOffset: struct_VecFx32
    driftEpoiRadiusScaleUpdateCounter: int
    driftEpoiRadiusScaleUpdateFrames: int
    field70: int
    driftEpoiRadiusScale: fx32
    field78: int
    field7A: int
    field7C: int
    field80: int
    PADDING_0: list[int]
    field84: int
    field88: int
    field8C: int
    driftState: int
    driftDirection: int
    field98: int
    field9C: int
    fieldA0: int
    fieldA4: int
    fieldA8: int
    fieldAC: int
    PADDING_1: list[int]
    targetDriver: POINTER_T[struct_driver_t]
    fieldB4: int
    fieldB8: int
    fieldBC: int
    targetBalloonCount: int
    balloonInflateMicTimeout: int
    isInflatingBalloon: int
    fieldC8: int
    fieldCA: int
    fieldCC: int
    targetShine: c_void_p
    shineIdx: int
    PADDING_2: list[int]
    fieldD8: int
    fieldDC: struct_VecFx32
    rubberbanding: struct_enemy_rubberbanding_t
    itemState: struct_enemy_item_state_t
    field140: struct_enemy_field140_t
    field154: int

class epipe_t(Structure):
    """
    ```python
    rotDieMObj: struct_rotdiemobj_t (struct_rotdiemobj_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    rotDieMObj: struct_rotdiemobj_t

class expl_def_t(Structure):
    """
    ```python
    instanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    hasNsbca: int (POINTER(i))
    hasNsbma: int (POINTER(i))
    hasNsbta: int (POINTER(i))
    initInstFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None] (CFunctionType)
    updateInstFunc: Callable[[POINTER_T[struct_expl_inst_t]], None] (CFunctionType)
    instanceSize: int (POINTER(I))
    modelRes: struct_model_res_t (struct_model_res_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    instanceCount: int
    PADDING_0: list[int]
    hasNsbca: int
    hasNsbma: int
    hasNsbta: int
    initInstFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None]
    updateInstFunc: Callable[[POINTER_T[struct_expl_inst_t]], None]
    instanceSize: int
    modelRes: struct_model_res_t

class expl_inst_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    model: struct_model_t (struct_model_t)
    position: struct_VecFx32 (struct_VecFx32)
    initFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None] (CFunctionType)
    updateFunc: Callable[[POINTER_T[struct_expl_inst_t]], None] (CFunctionType)
    state: int (POINTER(I))
    type: int (POINTER(I))
    nsbcaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbmaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    scale: struct_VecFx32 (struct_VecFx32)
    frameCounter: int (POINTER(I))
    lifeTime: int (POINTER(I))
    polygonId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    visible: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    model: struct_model_t
    position: struct_VecFx32
    initFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None]
    updateFunc: Callable[[POINTER_T[struct_expl_inst_t]], None]
    state: int
    type: int
    nsbcaAnim: POINTER_T[struct_anim_manager_t]
    nsbmaAnim: POINTER_T[struct_anim_manager_t]
    nsbtaAnim: POINTER_T[struct_anim_manager_t]
    scale: struct_VecFx32
    frameCounter: int
    lifeTime: int
    polygonId: int
    PADDING_0: list[int]
    visible: int

class expl_state_t(Structure):
    """
    ```python
    activeInstanceList: struct_NNSFndList (struct_NNSFndList)
    freeInstanceLists: list[struct_NNSFndList] (struct_NNSFndList[5])
    instances: list[POINTER_T[POINTER_T[struct_expl_inst_t]]] (POINTER(POINTER(struct_expl_inst_t))[5])
    curPolygonId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    activeInstanceList: struct_NNSFndList
    freeInstanceLists: list[struct_NNSFndList]
    instances: list[POINTER_T[POINTER_T[struct_expl_inst_t]]]
    curPolygonId: int
    PADDING_0: list[int]

class fireball2_fireball_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    armRotZ: int (POINTER(H))
    ballRotZ: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    armRotZ: int
    ballRotZ: int

class fireball2_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nrArms: int (POINTER(H))
    fireballsPerArm: int (POINTER(H))
    armAngleDistance: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fireballDistance: fx32 (struct_fx32)
    radius: fx32 (struct_fx32)
    rotSpeed: int (POINTER(H))
    rotation: int (POINTER(H))
    centerFireball: struct_fireball2_fireball_t (struct_fireball2_fireball_t)
    fireballs: list[struct_fireball2_fireball_t] (struct_fireball2_fireball_t[20][20])
    driverHitTimeouts: list[int] (POINTER(i)[8])
    playerDistanceFromRing: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nrArms: int
    fireballsPerArm: int
    armAngleDistance: int
    PADDING_0: list[int]
    fireballDistance: fx32
    radius: fx32
    rotSpeed: int
    rotation: int
    centerFireball: struct_fireball2_fireball_t
    fireballs: list[struct_fireball2_fireball_t]
    driverHitTimeouts: list[int]
    playerDistanceFromRing: fx32

class flipper_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(i))
    modelFlip: int (POINTER(i))
    baseMatrices: list[union_MtxFx43] (union_MtxFx43[30])
    extraColMatrices: list[union_MtxFx43] (union_MtxFx43[30])
    ptclEmitterPositions: list[struct_VecFx32] (struct_VecFx32[30])
    ptclEmitterTargets: list[struct_VecFx32] (struct_VecFx32[30])
    waitCounter: int (POINTER(i))
    ballHitFrameCounter: int (POINTER(i))
    animFrame: int (POINTER(i))
    nsbtpFrame: int (POINTER(H))
    nsbtaFrame: int (POINTER(H))
    electricityActive: int (POINTER(i))
    state: int (POINTER(I))
    ptclEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    driverHitTimeouts: list[int] (POINTER(i)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    modelFlip: int
    baseMatrices: list[union_MtxFx43]
    extraColMatrices: list[union_MtxFx43]
    ptclEmitterPositions: list[struct_VecFx32]
    ptclEmitterTargets: list[struct_VecFx32]
    waitCounter: int
    ballHitFrameCounter: int
    animFrame: int
    nsbtpFrame: int
    nsbtaFrame: int
    electricityActive: int
    state: int
    ptclEmitter: POINTER_T[struct_spa_emitter_t]
    driverHitTimeouts: list[int]

class fwdst_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    index: int (POINTER(H))
    ccDependentSetting: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    index: int
    ccDependentSetting: int

class fx16(Structure):
    """
    ```python
    val: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    val: int

class fx32(Structure):
    """
    ```python
    val: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    val: int

class gesso_t(Structure):
    """
    ```python
    item: struct_it_item_inst_t (struct_it_item_inst_t)
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    driverSplashCount: list[int] (POINTER(B)[8])
    field138: int (POINTER(i))
    field13C: struct_VecFx32 (struct_VecFx32)
    field148: struct_VecFx32 (struct_VecFx32)
    field154: struct_VecFx32 (struct_VecFx32)
    field160: int (POINTER(i))
    field164: int (POINTER(i))
    field168: int (POINTER(i))
    field16C: int (POINTER(i))
    field170: int (POINTER(i))
    field174: struct_VecFx32 (struct_VecFx32)
    field180: struct_VecFx32 (struct_VecFx32)
    field18C: int (POINTER(i))
    gap190: int (POINTER(I))
    field194: int (POINTER(i))
    visible: int (POINTER(i))
    field19C: fx32 (struct_fx32)
    gap1A0: list[int] (POINTER(B)[20])
    ```
    """
    _pack_: ClassVar[int] = 1
    item: struct_it_item_inst_t
    driver: POINTER_T[struct_driver_t]
    driverSplashCount: list[int]
    field138: int
    field13C: struct_VecFx32
    field148: struct_VecFx32
    field154: struct_VecFx32
    field160: int
    field164: int
    field168: int
    field16C: int
    field170: int
    field174: struct_VecFx32
    field180: struct_VecFx32
    field18C: int
    gap190: int
    field194: int
    visible: int
    field19C: fx32
    gap1A0: list[int]

class ghost_header_ex_t(Structure):
    """
    ```python
    header: struct_ghost_header_t (struct_ghost_header_t)
    emblem: list[int] (POINTER(B)[512])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_ghost_header_t
    emblem: list[int]

class ghost_header_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    character: int (POINTER(L))
    kart: int (POINTER(L))
    course: int (POINTER(L))
    _4: int (POINTER(L))
    isValid: int (POINTER(L))
    flagsBit1: int (POINTER(L))
    flagsBit2_3: int (POINTER(L))
    _8: int (POINTER(L))
    minutes: int (POINTER(L))
    seconds: int (POINTER(L))
    milliseconds: int (POINTER(L))
    nickname: list[int] (POINTER(H)[10])
    lapTimes: list[struct_ghost_time_t] (struct_ghost_time_t[5])
    field2F: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    character: int
    kart: int
    course: int
    _4: int
    isValid: int
    flagsBit1: int
    flagsBit2_3: int
    _8: int
    minutes: int
    seconds: int
    milliseconds: int
    nickname: list[int]
    lapTimes: list[struct_ghost_time_t]
    field2F: int
    PADDING_0: int

class ghost_time_t(Structure):
    """
    ```python
    field0: int (POINTER(B))
    field1: int (POINTER(B))
    field2: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field1: int
    field2: int

class gmenu_config_t(Structure):
    """
    ```python
    loadUnknown: int (POINTER(i))
    unkFont: POINTER_T[struct_NNSG2dFont] (POINTER(struct_NNSG2dFont))
    field8: int (POINTER(I))
    fieldC: int (POINTER(I))
    field10: int (POINTER(I))
    loadSelectChoises: int (POINTER(i))
    selectChoisesFont: POINTER_T[struct_NNSG2dFont] (POINTER(struct_NNSG2dFont))
    loadSelectReturn: int (POINTER(i))
    loadBackground: int (POINTER(i))
    field24: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    loadUnknown: int
    unkFont: POINTER_T[struct_NNSG2dFont]
    field8: int
    fieldC: int
    field10: int
    loadSelectChoises: int
    selectChoisesFont: POINTER_T[struct_NNSG2dFont]
    loadSelectReturn: int
    loadBackground: int
    field24: int

class gmenu_context_t(Structure):
    """
    ```python
    unknownLoaded: int (POINTER(i))
    selectChoisesLoaded: int (POINTER(i))
    selectReturnLoaded: int (POINTER(i))
    fieldC: int (POINTER(I))
    screenTmpBuf: list[int] (POINTER(H)[1024])
    charVramLeft: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    unknownLoaded: int
    selectChoisesLoaded: int
    selectReturnLoaded: int
    fieldC: int
    screenTmpBuf: list[int]
    charVramLeft: int

class gmenu_select_return_context_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    field8: int (POINTER(I))
    fieldC: int (POINTER(I))
    screenTmpBuf: list[int] (POINTER(H)[1024])
    field810: int (POINTER(I))
    field814: int (POINTER(I))
    field818: int (POINTER(I))
    field81C: int (POINTER(I))
    field820: int (POINTER(i))
    seqArcIndex: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    screenTmpBuf: list[int]
    field810: int
    field814: int
    field818: int
    field81C: int
    field820: int
    seqArcIndex: int

class grpconf_entry_t(Structure):
    """
    ```python
    objectId: int (POINTER(H))
    has3DModel: int (POINTER(H))
    nearClip: int (POINTER(H))
    farClip: int (POINTER(H))
    collisionType: int (POINTER(H))
    width: int (POINTER(H))
    height: int (POINTER(H))
    depth: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    objectId: int
    has3DModel: int
    nearClip: int
    farClip: int
    collisionType: int
    width: int
    height: int
    depth: int

class heap_info_t(Structure):
    """
    ```python
    unknown: int (POINTER(I))
    memoryRegionStart: c_void_p (c_void_p)
    heapStart: c_void_p (c_void_p)
    heapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    processName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ```
    """
    _pack_: ClassVar[int] = 1
    unknown: int
    memoryRegionStart: c_void_p
    heapStart: c_void_p
    heapHandle: POINTER_T[struct_NNSiFndHeapHead]
    processName: POINTER_T[c_ubyte]

class iball_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    rotZ: int (POINTER(i))
    fieldA4: int (POINTER(i))
    fieldA8: int (POINTER(i))
    fieldAC: int (POINTER(i))
    fieldB0: int (POINTER(i))
    fieldB4: int (POINTER(i))
    fieldB8: int (POINTER(i))
    elevation: int (POINTER(i))
    fieldC0: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    shadow: struct_objshadow_t (struct_objshadow_t)
    routePos: struct_VecFx32 (struct_VecFx32)
    clipAreaMask: int (POINTER(i))
    field12C: int (POINTER(i))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    rotZ: int
    fieldA4: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    fieldB4: int
    fieldB8: int
    elevation: int
    fieldC0: fx32
    pathwalker: struct_pw_pathwalker_t
    shadow: struct_objshadow_t
    routePos: struct_VecFx32
    clipAreaMask: int
    field12C: int
    state: int

class idk_struct2_t(Structure):
    """
    ```python
    value: fx32 (struct_fx32)
    velocity: fx32 (struct_fx32)
    min: fx32 (struct_fx32)
    max: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    value: fx32
    velocity: fx32
    min: fx32
    max: fx32

class idk_struct_t(Structure):
    """
    ```python
    value: fx32 (struct_fx32)
    velocity: fx32 (struct_fx32)
    reverse: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    value: fx32
    velocity: fx32
    reverse: int

class input_pad_data_t(Structure):
    """
    ```python
    field0: int (POINTER(H))
    pressedKeys: int (POINTER(H))
    flags: int (POINTER(H))
    field6: int (POINTER(H))
    field8: int (POINTER(I))
    fieldC: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    pressedKeys: int
    flags: int
    field6: int
    field8: int
    fieldC: int

class input_pad_t(Structure):
    """
    ```python
    triggeredKeys: int (POINTER(H))
    pressedKeys: int (POINTER(H))
    releasedKeys: int (POINTER(H))
    repeatedKeys: int (POINTER(H))
    repeatState: int (POINTER(H))
    repeatFrameCounter: int (POINTER(H))
    repeatMask: int (POINTER(H))
    repeatFirstFrame: int (POINTER(H))
    repeatNextFrame: int (POINTER(H))
    resetInvoked: int (POINTER(H))
    field14: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    resetStartTime: int (POINTER(L))
    field20: int (POINTER(I))
    field24: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    triggeredKeys: int
    pressedKeys: int
    releasedKeys: int
    repeatedKeys: int
    repeatState: int
    repeatFrameCounter: int
    repeatMask: int
    repeatFirstFrame: int
    repeatNextFrame: int
    resetInvoked: int
    field14: int
    PADDING_0: list[int]
    resetStartTime: int
    field20: int
    field24: int

class input_rec_recording_entry_t(Structure):
    """
    ```python
    keys: int (POINTER(B))
    duration: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    keys: int
    duration: int

class input_rec_recording_t(Structure):
    """
    ```python
    dataLength: int (POINTER(I))
    entries: list[struct_input_rec_recording_entry_t] (struct_input_rec_recording_entry_t[1764])
    ```
    """
    _pack_: ClassVar[int] = 1
    dataLength: int
    entries: list[struct_input_rec_recording_entry_t]

class input_rec_t(Structure):
    """
    ```python
    recording: POINTER_T[struct_input_rec_recording_t] (POINTER(struct_input_rec_recording_t))
    curEntry: int (POINTER(H))
    waitCounter: int (POINTER(H))
    state: int (POINTER(I))
    isBufferClear: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    recording: POINTER_T[struct_input_rec_recording_t]
    curEntry: int
    waitCounter: int
    state: int
    isBufferClear: int

class input_tpmic_t(Structure):
    """
    ```python
    curTp: struct_input_tpmic_tp_t (struct_input_tpmic_tp_t)
    prevTp: struct_input_tpmic_tp_t (struct_input_tpmic_tp_t)
    tpReleaseFrameCounter: int (POINTER(H))
    mic: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    curTp: struct_input_tpmic_tp_t
    prevTp: struct_input_tpmic_tp_t
    tpReleaseFrameCounter: int
    mic: int
    PADDING_0: int

class input_tpmic_tp_t(Structure):
    """
    ```python
    tpX: int (POINTER(H))
    tpY: int (POINTER(H))
    tpValid: int (POINTER(H))
    field6: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    tpX: int
    tpY: int
    tpValid: int
    field6: int

class input_unit_t(Structure):
    """
    ```python
    pad: struct_input_pad_t (struct_input_pad_t)
    inputRecorder: struct_input_rec_t (struct_input_rec_t)
    field38: int (POINTER(I))
    mode: int (POINTER(I))
    virtualPadKeys: int (POINTER(H))
    keyMask: int (POINTER(H))
    field44: int (POINTER(i))
    tpMic: struct_input_tpmic_t (struct_input_tpmic_t)
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    pad: struct_input_pad_t
    inputRecorder: struct_input_rec_t
    field38: int
    mode: int
    virtualPadKeys: int
    keyMask: int
    field44: int
    tpMic: struct_input_tpmic_t
    PADDING_0: list[int]

class it_driver_dragitem_t(Structure):
    """
    ```python
    itemType: int (POINTER(i))
    itemConfigId: int (POINTER(i))
    field8: int (POINTER(i))
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t] (POINTER(struct_it_driver_item_status_t))
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    items: list[POINTER_T[struct_it_item_inst_t]] (POINTER(struct_it_item_inst_t)[3])
    itemCount: int (POINTER(i))
    field24: int (POINTER(i))
    driverId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field2C: union_MtxFx43 (union_MtxFx43)
    field5C: struct_VecFx32 (struct_VecFx32)
    field68: int (POINTER(i))
    field6C: struct_VecFx32 (struct_VecFx32)
    field78: int (POINTER(i))
    field7C: int (POINTER(i))
    field80: int (POINTER(i))
    field84: struct_VecFx32 (struct_VecFx32)
    field90: struct_VecFx32 (struct_VecFx32)
    field9C: struct_VecFx32 (struct_VecFx32)
    fieldA8: struct_VecFx32 (struct_VecFx32)
    fieldB4: struct_VecFx32 (struct_VecFx32)
    gapC0: list[int] (POINTER(B)[12])
    fieldCC: list[int] (POINTER(i)[3])
    fieldD8: struct_VecFx32 (struct_VecFx32)
    fieldE4: int (POINTER(i))
    fieldE8: int (POINTER(i))
    fieldEC: list[int] (POINTER(i)[16])
    field12C: list[int] (POINTER(i)[16])
    field16C: int (POINTER(i))
    field170: int (POINTER(i))
    field174: int (POINTER(H))
    field176: int (POINTER(H))
    field178: int (POINTER(i))
    field17C: int (POINTER(i))
    field180: struct_VecFx32 (struct_VecFx32)
    field18C: list[int] (POINTER(H)[3])
    field192: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    itemType: int
    itemConfigId: int
    field8: int
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t]
    driver: POINTER_T[struct_driver_t]
    items: list[POINTER_T[struct_it_item_inst_t]]
    itemCount: int
    field24: int
    driverId: int
    PADDING_0: list[int]
    field2C: union_MtxFx43
    field5C: struct_VecFx32
    field68: int
    field6C: struct_VecFx32
    field78: int
    field7C: int
    field80: int
    field84: struct_VecFx32
    field90: struct_VecFx32
    field9C: struct_VecFx32
    fieldA8: struct_VecFx32
    fieldB4: struct_VecFx32
    gapC0: list[int]
    fieldCC: list[int]
    fieldD8: struct_VecFx32
    fieldE4: int
    fieldE8: int
    fieldEC: list[int]
    field12C: list[int]
    field16C: int
    field170: int
    field174: int
    field176: int
    field178: int
    field17C: int
    field180: struct_VecFx32
    field18C: list[int]
    field192: int

class it_driver_item_status_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    slotItemConfigId: int (POINTER(i))
    dragItemConfigId: int (POINTER(i))
    field18: POINTER_T[struct_it_driver_item_status_t] (POINTER(struct_it_driver_item_status_t))
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    field28: int (POINTER(i))
    field2C: int (POINTER(i))
    itemSlot: struct_it_driver_itemslot_t (struct_it_driver_itemslot_t)
    dragItem: struct_it_driver_dragitem_t (struct_it_driver_dragitem_t)
    field1EC: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ipoi: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    field1F4: int (POINTER(i))
    driverId: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    driverIndex: int (POINTER(i))
    isUsingShroom: int (POINTER(i))
    field208: int (POINTER(i))
    field20C: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    slotItemConfigId: int
    dragItemConfigId: int
    field18: POINTER_T[struct_it_driver_item_status_t]
    field1C: int
    field20: int
    field24: int
    field28: int
    field2C: int
    itemSlot: struct_it_driver_itemslot_t
    dragItem: struct_it_driver_dragitem_t
    field1EC: int
    PADDING_0: list[int]
    ipoi: POINTER_T[struct_mdat_itempoint_t]
    field1F4: int
    driverId: int
    PADDING_1: list[int]
    driver: POINTER_T[struct_driver_t]
    driverIndex: int
    isUsingShroom: int
    field208: int
    field20C: int

class it_driver_itemslot_t(Structure):
    """
    ```python
    itemConfigId: int (POINTER(i))
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t] (POINTER(struct_it_driver_item_status_t))
    itemCount: int (POINTER(i))
    fieldC: int (POINTER(i))
    timeout: int (POINTER(H))
    field12: int (POINTER(H))
    items: list[POINTER_T[struct_it_item_inst_t]] (POINTER(struct_it_item_inst_t)[3])
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    itemConfigId: int
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t]
    itemCount: int
    fieldC: int
    timeout: int
    field12: int
    items: list[POINTER_T[struct_it_item_inst_t]]
    field20: int
    field24: int

class it_item_def_t(Structure):
    """
    ```python
    instanceSize: int (POINTER(I))
    limit: int (POINTER(I))
    field8: int (POINTER(I))
    instanceCount: int (POINTER(i))
    field10: int (POINTER(i))
    loadFunc: c_void_p (c_void_p)
    initInstanceFunc: c_void_p (c_void_p)
    field1C: c_void_p (c_void_p)
    field20: c_void_p (c_void_p)
    field24: c_void_p (c_void_p)
    updateFunc: c_void_p (c_void_p)
    renderFunc: c_void_p (c_void_p)
    visibilityFlagCalcFunc: c_void_p (c_void_p)
    field34: c_void_p (c_void_p)
    field38: c_void_p (c_void_p)
    destroyInstFunc: c_void_p (c_void_p)
    field40: int (POINTER(i))
    field44: int (POINTER(i))
    field48: c_void_p (c_void_p)
    field4C: int (POINTER(i))
    field50: c_void_p (c_void_p)
    gap54: int (POINTER(I))
    field58: c_void_p (c_void_p)
    field5C: int (POINTER(i))
    field60: int (POINTER(i))
    colSphereRadius: int (POINTER(i))
    sphereRadius1: int (POINTER(i))
    sphereRadius2: int (POINTER(i))
    field70: int (POINTER(i))
    scale: int (POINTER(i))
    field78: int (POINTER(i))
    field7C: int (POINTER(i))
    field80: int (POINTER(i))
    field84: int (POINTER(i))
    field88: int (POINTER(i))
    gap8C: int (POINTER(I))
    field90: int (POINTER(i))
    field94: int (POINTER(i))
    field98: int (POINTER(i))
    field9C: int (POINTER(i))
    fieldA0: int (POINTER(i))
    fieldA4: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    instanceSize: int
    limit: int
    field8: int
    instanceCount: int
    field10: int
    loadFunc: c_void_p
    initInstanceFunc: c_void_p
    field1C: c_void_p
    field20: c_void_p
    field24: c_void_p
    updateFunc: c_void_p
    renderFunc: c_void_p
    visibilityFlagCalcFunc: c_void_p
    field34: c_void_p
    field38: c_void_p
    destroyInstFunc: c_void_p
    field40: int
    field44: int
    field48: c_void_p
    field4C: int
    field50: c_void_p
    gap54: int
    field58: c_void_p
    field5C: int
    field60: int
    colSphereRadius: int
    sphereRadius1: int
    sphereRadius2: int
    field70: int
    scale: int
    field78: int
    field7C: int
    field80: int
    field84: int
    field88: int
    gap8C: int
    field90: int
    field94: int
    field98: int
    field9C: int
    fieldA0: int
    fieldA4: int

class it_item_inst_t(Structure):
    """
    ```python
    sfxEmitter: struct_sfx_emitter_t (struct_sfx_emitter_t)
    type: int (POINTER(I))
    field48: int (POINTER(I))
    field4C: int (POINTER(H))
    field4E: int (POINTER(H))
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    flags: int (POINTER(I))
    field78: int (POINTER(H))
    field7A: int (POINTER(H))
    light: struct_light_t (struct_light_t)
    PADDING_0: list[int] (POINTER(B)[2])
    lightPtr: POINTER_T[struct_light_t] (POINTER(struct_light_t))
    mtx: union_MtxFx43 (union_MtxFx43)
    gapC4: list[int] (POINTER(B)[12])
    fieldD0: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    visibilityFlags: int (POINTER(I))
    alpha: int (POINTER(h))
    colEntryId: int (POINTER(H))
    fieldDC: int (POINTER(I))
    sphereSize: fx32 (struct_fx32)
    fieldE4: struct_VecFx32 (struct_VecFx32)
    fieldF0: struct_VecFx32 (struct_VecFx32)
    fieldFC: int (POINTER(I))
    field100: int (POINTER(I))
    field104: int (POINTER(I))
    field108: struct_VecFx32 (struct_VecFx32)
    field114: int (POINTER(H))
    field116: int (POINTER(H))
    field118: int (POINTER(H))
    field11A: int (POINTER(H))
    field11C: int (POINTER(I))
    field120: int (POINTER(I))
    field124: int (POINTER(I))
    field128DriverMask: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    sfxEmitter: struct_sfx_emitter_t
    type: int
    field48: int
    field4C: int
    field4E: int
    position: struct_VecFx32
    velocity: struct_VecFx32
    scale: struct_VecFx32
    flags: int
    field78: int
    field7A: int
    light: struct_light_t
    PADDING_0: list[int]
    lightPtr: POINTER_T[struct_light_t]
    mtx: union_MtxFx43
    gapC4: list[int]
    fieldD0: POINTER_T[struct_VecFx32]
    visibilityFlags: int
    alpha: int
    colEntryId: int
    fieldDC: int
    sphereSize: fx32
    fieldE4: struct_VecFx32
    fieldF0: struct_VecFx32
    fieldFC: int
    field100: int
    field104: int
    field108: struct_VecFx32
    field114: int
    field116: int
    field118: int
    field11A: int
    field11C: int
    field120: int
    field124: int
    field128DriverMask: int
    PADDING_1: list[int]

class it_itemconfig_t(Structure):
    """
    ```python
    enabled: int (POINTER(i))
    wifiEnabled: int (POINTER(i))
    type: int (POINTER(I))
    count: int (POINTER(I))
    field10: int (POINTER(I))
    field14: int (POINTER(I))
    activateFunc: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    enabled: int
    wifiEnabled: int
    type: int
    count: int
    field10: int
    field14: int
    activateFunc: c_void_p

class it_itemset_t(Structure):
    """
    ```python
    id: int (POINTER(I))
    instances: POINTER_T[struct_it_item_inst_t] (POINTER(struct_it_item_inst_t))
    totalInstanceCount: int (POINTER(I))
    itemParamsField10: int (POINTER(I))
    activeInstanceCount: int (POINTER(I))
    field14: int (POINTER(I))
    field18: int (POINTER(I))
    activeInstanceCount2: int (POINTER(I))
    limit: int (POINTER(I))
    renderFunc: c_void_p (c_void_p)
    visibilityFlagCalcFunc: c_void_p (c_void_p)
    itemParamsField70: int (POINTER(I))
    scale: fx32 (struct_fx32)
    itemParamsField78: int (POINTER(I))
    itemParamsField5C: int (POINTER(I))
    itemParamsFieldA4: int (POINTER(I))
    renderingDisabled: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    instances: POINTER_T[struct_it_item_inst_t]
    totalInstanceCount: int
    itemParamsField10: int
    activeInstanceCount: int
    field14: int
    field18: int
    activeInstanceCount2: int
    limit: int
    renderFunc: c_void_p
    visibilityFlagCalcFunc: c_void_p
    itemParamsField70: int
    scale: fx32
    itemParamsField78: int
    itemParamsField5C: int
    itemParamsFieldA4: int
    renderingDisabled: int

class itnet_action_t(Structure):
    """
    ```python
    data: list[int] (POINTER(B)[20])
    itemType: int (POINTER(I))
    action: int (POINTER(I))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    data: list[int]
    itemType: int
    action: int
    field1C: int

class jn_msg_bmg_dat1_t(Structure):
    """
    ```python
    sectionHeader: struct_jn_msg_bmg_section_header_t (struct_jn_msg_bmg_section_header_t)
    stringData: list[int] (POINTER(H)[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    sectionHeader: struct_jn_msg_bmg_section_header_t
    stringData: list[int]

class jn_msg_bmg_header_t(Structure):
    """
    ```python
    magic1: int (POINTER(I))
    magic2: int (POINTER(I))
    fileSize: int (POINTER(I))
    nrSections: int (POINTER(I))
    field10: int (POINTER(I))
    field14: int (POINTER(I))
    field18: int (POINTER(I))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic1: int
    magic2: int
    fileSize: int
    nrSections: int
    field10: int
    field14: int
    field18: int
    field1C: int

class jn_msg_bmg_inf1_t(Structure):
    """
    ```python
    sectionHeader: struct_jn_msg_bmg_section_header_t (struct_jn_msg_bmg_section_header_t)
    nrEntries: int (POINTER(H))
    fieldA: int (POINTER(H))
    fieldC: int (POINTER(I))
    offsets: list[int] (POINTER(I)[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    sectionHeader: struct_jn_msg_bmg_section_header_t
    nrEntries: int
    fieldA: int
    fieldC: int
    offsets: list[int]

class jn_msg_bmg_section_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    size: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    size: int

class jn_msg_bmg_t(Structure):
    """
    ```python
    header: struct_jn_msg_bmg_header_t (struct_jn_msg_bmg_header_t)
    inf1: struct_jn_msg_bmg_inf1_t (struct_jn_msg_bmg_inf1_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jn_msg_bmg_header_t
    inf1: struct_jn_msg_bmg_inf1_t

class jnui_bnbl_res_element_t(Structure):
    """
    ```python
    x: struct_jnui_coord_t (struct_jnui_coord_t)
    y: struct_jnui_coord_t (struct_jnui_coord_t)
    width: int (POINTER(B))
    height: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: struct_jnui_coord_t
    y: struct_jnui_coord_t
    width: int
    height: int

class jnui_bnbl_res_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    unknown: int (POINTER(H))
    nrElements: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    unknown: int
    nrElements: int

class jnui_bnbl_res_t(Structure):
    """
    ```python
    header: struct_jnui_bnbl_res_header_t (struct_jnui_bnbl_res_header_t)
    elements: list[struct_jnui_bnbl_res_element_t] (struct_jnui_bnbl_res_element_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jnui_bnbl_res_header_t
    elements: list[struct_jnui_bnbl_res_element_t]

class jnui_bncl_res_element_t(Structure):
    """
    ```python
    x: struct_jnui_coord_t (struct_jnui_coord_t)
    y: struct_jnui_coord_t (struct_jnui_coord_t)
    cellId: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: struct_jnui_coord_t
    y: struct_jnui_coord_t
    cellId: int

class jnui_bncl_res_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    unknown: int (POINTER(H))
    nrElements: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    unknown: int
    nrElements: int

class jnui_bncl_res_t(Structure):
    """
    ```python
    header: struct_jnui_bncl_res_header_t (struct_jnui_bncl_res_header_t)
    elements: list[struct_jnui_bncl_res_element_t] (struct_jnui_bncl_res_element_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jnui_bncl_res_header_t
    elements: list[struct_jnui_bncl_res_element_t]

class jnui_bnll_res_element_t(Structure):
    """
    ```python
    x: struct_jnui_coord_t (struct_jnui_coord_t)
    y: struct_jnui_coord_t (struct_jnui_coord_t)
    hSpace: int (POINTER(b))
    vSpace: int (POINTER(b))
    color: int (POINTER(H))
    palette: int (POINTER(H))
    font: int (POINTER(H))
    stringPtr: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: struct_jnui_coord_t
    y: struct_jnui_coord_t
    hSpace: int
    vSpace: int
    color: int
    palette: int
    font: int
    stringPtr: int

class jnui_bnll_res_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    unknown: int (POINTER(H))
    nrElements: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    unknown: int
    nrElements: int

class jnui_bnll_res_t(Structure):
    """
    ```python
    header: struct_jnui_bnll_res_header_t (struct_jnui_bnll_res_header_t)
    elements: list[struct_jnui_bnll_res_element_t] (struct_jnui_bnll_res_element_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jnui_bnll_res_header_t
    elements: list[struct_jnui_bnll_res_element_t]

class jnui_coord_t(Structure):
    """
    ```python
    coord: int (POINTER(h))
    origin: int (POINTER(h))
    unk: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    coord: int
    origin: int
    unk: int

class jnui_label_t(Structure):
    """
    ```python
    charCanvas: struct_NNSG2dCharCanvas (struct_NNSG2dCharCanvas)
    textCanvas: struct_NNSG2dTextCanvas (struct_NNSG2dTextCanvas)
    charData: c_void_p (c_void_p)
    charDataLength: int (POINTER(I))
    charDataTileOffset: int (POINTER(I))
    width: int (POINTER(I))
    height: int (POINTER(I))
    cellData: POINTER_T[struct_NNSG2dCellDataWithBR] (POINTER(struct_NNSG2dCellDataWithBR))
    ```
    """
    _pack_: ClassVar[int] = 1
    charCanvas: struct_NNSG2dCharCanvas
    textCanvas: struct_NNSG2dTextCanvas
    charData: c_void_p
    charDataLength: int
    charDataTileOffset: int
    width: int
    height: int
    cellData: POINTER_T[struct_NNSG2dCellDataWithBR]

class jnui_layout_element_t(Structure):
    """
    ```python
    visible: int (POINTER(i))
    offsetX: int (POINTER(h))
    offsetY: int (POINTER(h))
    usePosition: int (POINTER(i))
    positionX: int (POINTER(h))
    positionY: int (POINTER(h))
    useMtx: int (POINTER(i))
    baseMtx: union_MtxFx22 (union_MtxFx22)
    affineMtx: union_MtxFx22 (union_MtxFx22)
    useDoubleAffine: int (POINTER(i))
    subElement: int (POINTER(i))
    label: POINTER_T[struct_jnui_label_t] (POINTER(struct_jnui_label_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    visible: int
    offsetX: int
    offsetY: int
    usePosition: int
    positionX: int
    positionY: int
    useMtx: int
    baseMtx: union_MtxFx22
    affineMtx: union_MtxFx22
    useDoubleAffine: int
    subElement: int
    label: POINTER_T[struct_jnui_label_t]

class kcol_header_t(Structure):
    """
    ```python
    posDataOffset: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    nrmDataOffset: POINTER_T[struct_VecFx16] (POINTER(struct_VecFx16))
    prismDataOffset: POINTER_T[struct_kcol_prism_data_t] (POINTER(struct_kcol_prism_data_t))
    blockDataOffset: POINTER_T[c_uint] (POINTER(POINTER(I)))
    prismThickness: fx32 (struct_fx32)
    areaMinPos: struct_VecFx32 (struct_VecFx32)
    areaXWidthMask: int (POINTER(I))
    areaYWidthMask: int (POINTER(I))
    areaZWidthMask: int (POINTER(I))
    blockWidthShift: int (POINTER(I))
    areaXBlocksShift: int (POINTER(I))
    areaXYBlocksShift: int (POINTER(I))
    sphereRadius: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    posDataOffset: POINTER_T[struct_VecFx32]
    nrmDataOffset: POINTER_T[struct_VecFx16]
    prismDataOffset: POINTER_T[struct_kcol_prism_data_t]
    blockDataOffset: POINTER_T[c_uint]
    prismThickness: fx32
    areaMinPos: struct_VecFx32
    areaXWidthMask: int
    areaYWidthMask: int
    areaZWidthMask: int
    blockWidthShift: int
    areaXBlocksShift: int
    areaXYBlocksShift: int
    sphereRadius: fx32

class kcol_prism_data_t(Structure):
    """
    ```python
    height: fx32 (struct_fx32)
    posIdx: int (POINTER(H))
    fNrmIdx: int (POINTER(H))
    eNrm1Idx: int (POINTER(H))
    eNrm2Idx: int (POINTER(H))
    eNrm3Idx: int (POINTER(H))
    attribute: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    height: fx32
    posIdx: int
    fNrmIdx: int
    eNrm1Idx: int
    eNrm2Idx: int
    eNrm3Idx: int
    attribute: int

class kofs_entry_t(Structure):
    """
    ```python
    tireName: list[int] (POINTER(B)[16])
    frontTireScale: fx32 (struct_fx32)
    tirePositions: list[struct_VecFx32] (struct_VecFx32[4])
    characterPositions: list[struct_VecFx32] (struct_VecFx32[13])
    ```
    """
    _pack_: ClassVar[int] = 1
    tireName: list[int]
    frontTireScale: fx32
    tirePositions: list[struct_VecFx32]
    characterPositions: list[struct_VecFx32]

class kofs_t(Structure):
    """
    ```python
    entries: list[struct_kofs_entry_t] (struct_kofs_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    entries: list[struct_kofs_entry_t]

class koopablock_t(Structure):
    """
    ```python
    dcolMObj: struct_dcol_inst_t (struct_dcol_inst_t)
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    speed: fx32 (struct_fx32)
    waitCounter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    dcolMObj: struct_dcol_inst_t
    pathWalker: struct_pw_pathwalker_t
    speed: fx32
    waitCounter: int
    PADDING_0: list[int]

class kouragreen_t(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[364])
    sfxExParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    sfxExParams: struct_sfx_emitter_ex_params_t

class kourared_t(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[600])
    sfxExParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    sfxExParams: struct_sfx_emitter_ex_params_t

class kourawing_t(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[768])
    sfxExParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    sfxExParams: struct_sfx_emitter_ex_params_t

class kuribo_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: fx32 (struct_fx32)
    direction: quaternion_t (struct_quaternion_t)
    targetDir: quaternion_t (struct_quaternion_t)
    squashRatio: fx32 (struct_fx32)
    squashVelocity: fx32 (struct_fx32)
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    frame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fieldF4: int (POINTER(i))
    dirInterpRatio: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    reappearAfterHit: int (POINTER(i))
    alpha: int (POINTER(H))
    field102: int (POINTER(h))
    field104: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: fx32
    direction: quaternion_t
    targetDir: quaternion_t
    squashRatio: fx32
    squashVelocity: fx32
    pathWalker: struct_pw_pathwalker_t
    frame: int
    PADDING_0: list[int]
    fieldF4: int
    dirInterpRatio: int
    PADDING_1: list[int]
    reappearAfterHit: int
    alpha: int
    field102: int
    field104: int

class light_t(Structure):
    """
    ```python
    color: int (POINTER(H))
    r: int (POINTER(h))
    g: int (POINTER(h))
    b: int (POINTER(h))
    rDelta: int (POINTER(h))
    gDelta: int (POINTER(h))
    bDelta: int (POINTER(h))
    lightMask: int (POINTER(H))
    progress: fx16 (struct_fx16)
    ```
    """
    _pack_: ClassVar[int] = 1
    color: int
    r: int
    g: int
    b: int
    rDelta: int
    gDelta: int
    bDelta: int
    lightMask: int
    progress: fx16

class list_link_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    list: POINTER_T[struct_NNSFndList] (POINTER(struct_NNSFndList))
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    list: POINTER_T[struct_NNSFndList]

class max_align_t(Structure):
    """
    ```python
    __clang_max_align_nonce1: int (POINTER(l))
    __clang_max_align_nonce2: float (POINTER(d))
    ```
    """
    _pack_: ClassVar[int] = 1
    __clang_max_align_nonce1: int
    __clang_max_align_nonce2: float

class mdat_clip_area_list_entry_t(Structure):
    """
    ```python
    entry: POINTER_T[struct_nkm_area_entry_t] (POINTER(struct_nkm_area_entry_t))
    next: POINTER_T[struct_mdat_clip_area_list_entry_t] (POINTER(struct_mdat_clip_area_list_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    entry: POINTER_T[struct_nkm_area_entry_t]
    next: POINTER_T[struct_mdat_clip_area_list_entry_t]

class mdat_enemypath_data_t(Structure):
    """
    ```python
    points: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    firstPoint: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    lastPoint: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    points: POINTER_T[struct_mdat_enemypoint_t]
    firstPoint: POINTER_T[struct_mdat_enemypoint_t]
    lastPoint: POINTER_T[struct_mdat_enemypoint_t]

class mdat_enemypoint_t(Structure):
    """
    ```python
    next: list[POINTER_T[struct_mdat_enemypoint_t]] (POINTER(struct_mdat_enemypoint_t)[3])
    previous: list[POINTER_T[struct_mdat_enemypoint_t]] (POINTER(struct_mdat_enemypoint_t)[3])
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    radius: fx32 (struct_fx32)
    settings: POINTER_T[struct_nkm_epoi_entry_settings_t] (POINTER(struct_nkm_epoi_entry_settings_t))
    nextCount: int (POINTER(H))
    previousCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: list[POINTER_T[struct_mdat_enemypoint_t]]
    previous: list[POINTER_T[struct_mdat_enemypoint_t]]
    position: POINTER_T[struct_VecFx32]
    radius: fx32
    settings: POINTER_T[struct_nkm_epoi_entry_settings_t]
    nextCount: int
    previousCount: int

class mdat_itempath_data_t(Structure):
    """
    ```python
    points: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    firstPoint: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    lastPoint: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    points: POINTER_T[struct_mdat_itempoint_t]
    firstPoint: POINTER_T[struct_mdat_itempoint_t]
    lastPoint: POINTER_T[struct_mdat_itempoint_t]

class mdat_itempoint_t(Structure):
    """
    ```python
    next: list[POINTER_T[struct_mdat_itempoint_t]] (POINTER(struct_mdat_itempoint_t)[3])
    previous: list[POINTER_T[struct_mdat_itempoint_t]] (POINTER(struct_mdat_itempoint_t)[3])
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    radius: fx32 (struct_fx32)
    recalcIdx: int (POINTER(B))
    dirX: int (POINTER(b))
    dirY: int (POINTER(b))
    dirZ: int (POINTER(b))
    nextCount: int (POINTER(H))
    previousCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: list[POINTER_T[struct_mdat_itempoint_t]]
    previous: list[POINTER_T[struct_mdat_itempoint_t]]
    position: POINTER_T[struct_VecFx32]
    radius: fx32
    recalcIdx: int
    dirX: int
    dirY: int
    dirZ: int
    nextCount: int
    previousCount: int

class mdat_mapdata_t(Structure):
    """
    ```python
    obji: POINTER_T[struct_nkm_obji_entry_t] (POINTER(struct_nkm_obji_entry_t))
    objiCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    path: POINTER_T[struct_nkm_path_entry_t] (POINTER(struct_nkm_path_entry_t))
    pathCount: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    poit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    poitCount: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    stag: POINTER_T[struct_nkm_stag_data_t] (POINTER(struct_nkm_stag_data_t))
    ktps: POINTER_T[struct_nkm_ktps_entry_t] (POINTER(struct_nkm_ktps_entry_t))
    ktpsCount: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    ktpj: POINTER_T[struct_nkm_ktpj_entry_t] (POINTER(struct_nkm_ktpj_entry_t))
    ktpjCount: int (POINTER(H))
    PADDING_4: list[int] (POINTER(B)[2])
    ktp2: POINTER_T[struct_nkm_ktp2_entry_t] (POINTER(struct_nkm_ktp2_entry_t))
    ktp2Count: int (POINTER(H))
    PADDING_5: list[int] (POINTER(B)[2])
    ktpc: POINTER_T[struct_nkm_ktpc_entry_t] (POINTER(struct_nkm_ktpc_entry_t))
    ktpcCount: int (POINTER(H))
    PADDING_6: list[int] (POINTER(B)[2])
    ktpm: POINTER_T[struct_nkm_ktpm_entry_t] (POINTER(struct_nkm_ktpm_entry_t))
    ktpmCount: int (POINTER(H))
    PADDING_7: list[int] (POINTER(B)[2])
    cpoi: POINTER_T[struct_nkm_cpoi_entry_t] (POINTER(struct_nkm_cpoi_entry_t))
    cpoiCount: int (POINTER(H))
    PADDING_8: list[int] (POINTER(B)[2])
    cpat: POINTER_T[struct_nkm_cpat_entry_t] (POINTER(struct_nkm_cpat_entry_t))
    cpatCount: int (POINTER(H))
    PADDING_9: list[int] (POINTER(B)[2])
    ipoi: union_nkm_ipoi_entry_pointer_t (union_nkm_ipoi_entry_pointer_t)
    ipoiCount: int (POINTER(H))
    PADDING_10: list[int] (POINTER(B)[2])
    ipat: POINTER_T[struct_nkm_ipat_entry_t] (POINTER(struct_nkm_ipat_entry_t))
    ipatCount: int (POINTER(H))
    PADDING_11: list[int] (POINTER(B)[2])
    epoi: POINTER_T[struct_nkm_epoi_entry_t] (POINTER(struct_nkm_epoi_entry_t))
    epoiCount: int (POINTER(H))
    PADDING_12: list[int] (POINTER(B)[2])
    epat: POINTER_T[struct_nkm_epat_entry_t] (POINTER(struct_nkm_epat_entry_t))
    epatCount: int (POINTER(H))
    PADDING_13: list[int] (POINTER(B)[2])
    area: POINTER_T[struct_nkm_area_entry_t] (POINTER(struct_nkm_area_entry_t))
    areaCount: int (POINTER(H))
    PADDING_14: list[int] (POINTER(B)[2])
    came: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameCount: int (POINTER(H))
    PADDING_15: list[int] (POINTER(B)[2])
    mepo: POINTER_T[struct_nkm_mepo_entry_t] (POINTER(struct_nkm_mepo_entry_t))
    mepoCount: int (POINTER(H))
    PADDING_16: list[int] (POINTER(B)[2])
    mepa: POINTER_T[struct_nkm_mepa_entry_t] (POINTER(struct_nkm_mepa_entry_t))
    mepaCount: int (POINTER(H))
    PADDING_17: list[int] (POINTER(B)[2])
    paths: POINTER_T[struct_mdat_path_t] (POINTER(struct_mdat_path_t))
    cpoiKeyCount: int (POINTER(H))
    cpatLastCpoiIndex: int (POINTER(H))
    cpatMaxSectionOrder: int (POINTER(H))
    unknown49: int (POINTER(B))
    unknown50: int (POINTER(B))
    enemyPathData: struct_mdat_enemypath_data_t (struct_mdat_enemypath_data_t)
    itemPathData: struct_mdat_itempath_data_t (struct_mdat_itempath_data_t)
    mgEnemyPathData: struct_mdat_mgenemypath_data_t (struct_mdat_mgenemypath_data_t)
    cameIntroFirstTopCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameIntroFirstBottomCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameType6: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameBattleIntroCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameMissionFinishCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    clipAreaLists: list[POINTER_T[struct_mdat_clip_area_list_entry_t]] (POINTER(struct_mdat_clip_area_list_entry_t)[8])
    ktpjIndexTable: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    ktpcIndexTable: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    curMgRespawnId: int (POINTER(H))
    enemyRespawnRouteAreaCount: int (POINTER(H))
    trackLength: fx32 (struct_fx32)
    trackLengthDiv15000: int (POINTER(I))
    nkmVersion: int (POINTER(H))
    unknown141: int (POINTER(B))
    missionEndAreaCount: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    obji: POINTER_T[struct_nkm_obji_entry_t]
    objiCount: int
    PADDING_0: list[int]
    path: POINTER_T[struct_nkm_path_entry_t]
    pathCount: int
    PADDING_1: list[int]
    poit: POINTER_T[struct_nkm_poit_entry_t]
    poitCount: int
    PADDING_2: list[int]
    stag: POINTER_T[struct_nkm_stag_data_t]
    ktps: POINTER_T[struct_nkm_ktps_entry_t]
    ktpsCount: int
    PADDING_3: list[int]
    ktpj: POINTER_T[struct_nkm_ktpj_entry_t]
    ktpjCount: int
    PADDING_4: list[int]
    ktp2: POINTER_T[struct_nkm_ktp2_entry_t]
    ktp2Count: int
    PADDING_5: list[int]
    ktpc: POINTER_T[struct_nkm_ktpc_entry_t]
    ktpcCount: int
    PADDING_6: list[int]
    ktpm: POINTER_T[struct_nkm_ktpm_entry_t]
    ktpmCount: int
    PADDING_7: list[int]
    cpoi: POINTER_T[struct_nkm_cpoi_entry_t]
    cpoiCount: int
    PADDING_8: list[int]
    cpat: POINTER_T[struct_nkm_cpat_entry_t]
    cpatCount: int
    PADDING_9: list[int]
    ipoi: union_nkm_ipoi_entry_pointer_t
    ipoiCount: int
    PADDING_10: list[int]
    ipat: POINTER_T[struct_nkm_ipat_entry_t]
    ipatCount: int
    PADDING_11: list[int]
    epoi: POINTER_T[struct_nkm_epoi_entry_t]
    epoiCount: int
    PADDING_12: list[int]
    epat: POINTER_T[struct_nkm_epat_entry_t]
    epatCount: int
    PADDING_13: list[int]
    area: POINTER_T[struct_nkm_area_entry_t]
    areaCount: int
    PADDING_14: list[int]
    came: POINTER_T[struct_nkm_came_entry_t]
    cameCount: int
    PADDING_15: list[int]
    mepo: POINTER_T[struct_nkm_mepo_entry_t]
    mepoCount: int
    PADDING_16: list[int]
    mepa: POINTER_T[struct_nkm_mepa_entry_t]
    mepaCount: int
    PADDING_17: list[int]
    paths: POINTER_T[struct_mdat_path_t]
    cpoiKeyCount: int
    cpatLastCpoiIndex: int
    cpatMaxSectionOrder: int
    unknown49: int
    unknown50: int
    enemyPathData: struct_mdat_enemypath_data_t
    itemPathData: struct_mdat_itempath_data_t
    mgEnemyPathData: struct_mdat_mgenemypath_data_t
    cameIntroFirstTopCam: POINTER_T[struct_nkm_came_entry_t]
    cameIntroFirstBottomCam: POINTER_T[struct_nkm_came_entry_t]
    cameType6: POINTER_T[struct_nkm_came_entry_t]
    cameBattleIntroCam: POINTER_T[struct_nkm_came_entry_t]
    cameMissionFinishCam: POINTER_T[struct_nkm_came_entry_t]
    clipAreaLists: list[POINTER_T[struct_mdat_clip_area_list_entry_t]]
    ktpjIndexTable: POINTER_T[c_ushort]
    ktpcIndexTable: POINTER_T[c_ushort]
    curMgRespawnId: int
    enemyRespawnRouteAreaCount: int
    trackLength: fx32
    trackLengthDiv15000: int
    nkmVersion: int
    unknown141: int
    missionEndAreaCount: int

class mdat_mgenemypath_data_t(Structure):
    """
    ```python
    points: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    firstPoint: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    lastPoint: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    points: POINTER_T[struct_mdat_mgenemypoint_t]
    firstPoint: POINTER_T[struct_mdat_mgenemypoint_t]
    lastPoint: POINTER_T[struct_mdat_mgenemypoint_t]

class mdat_mgenemypoint_t(Structure):
    """
    ```python
    next: list[POINTER_T[struct_mdat_mgenemypoint_t]] (POINTER(struct_mdat_mgenemypoint_t)[8])
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    radius: fx32 (struct_fx32)
    settings: POINTER_T[struct_nkm_mepo_entry_settings_t] (POINTER(struct_nkm_mepo_entry_settings_t))
    nextCount: int (POINTER(H))
    nextIsNewPathMask: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: list[POINTER_T[struct_mdat_mgenemypoint_t]]
    position: POINTER_T[struct_VecFx32]
    radius: fx32
    settings: POINTER_T[struct_nkm_mepo_entry_settings_t]
    nextCount: int
    nextIsNewPathMask: int
    PADDING_0: int

class mdat_path_t(Structure):
    """
    ```python
    path: POINTER_T[struct_nkm_path_entry_t] (POINTER(struct_nkm_path_entry_t))
    poit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: POINTER_T[struct_nkm_path_entry_t]
    poit: POINTER_T[struct_nkm_poit_entry_t]

class mgcnt_driver_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    state: int (POINTER(I))
    position: struct_VecFx32 (struct_VecFx32)
    field18: int (POINTER(i))
    field1C: int (POINTER(i))
    field20: int (POINTER(I))
    field24: list[int] (POINTER(I)[8])
    field44: int (POINTER(H))
    mgDriverTeamId: int (POINTER(H))
    place: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    balloonShineCount: int (POINTER(i))
    balloonShineInventoryCount: int (POINTER(H))
    gap52: list[int] (POINTER(B)[18])
    micInflatingCounter: int (POINTER(i))
    keyInflating: int (POINTER(i))
    isInflating: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    state: int
    position: struct_VecFx32
    field18: int
    field1C: int
    field20: int
    field24: list[int]
    field44: int
    mgDriverTeamId: int
    place: int
    PADDING_0: list[int]
    balloonShineCount: int
    balloonShineInventoryCount: int
    gap52: list[int]
    micInflatingCounter: int
    keyInflating: int
    isInflating: int

class mgcnt_t(Structure):
    """
    ```python
    drivers: list[struct_mgcnt_driver_t] (struct_mgcnt_driver_t[8])
    tryStealBalloonFunc: Callable[[int, int], c_int] (CFunctionType)
    field384: Callable[[int, int], None] (CFunctionType)
    onDamageFunc: Callable[[int, int], c_int] (CFunctionType)
    onKillFunc: Callable[[int], None] (CFunctionType)
    onEndFunc: Callable[[], None] (CFunctionType)
    gap394: list[int] (POINTER(B)[8])
    applyForceToDriverBalloonsFunc: Callable[[int, POINTER_T[struct_VecFx32]], None] (CFunctionType)
    collectableShineCount: int (POINTER(H))
    timeLimit: int (POINTER(H))
    shineRunnersRound: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    mgEndDelayCounter: int (POINTER(i))
    maxOwnedShineCount: int (POINTER(i))
    minOwnedShineCount: int (POINTER(i))
    winDriverTeamId: int (POINTER(i))
    lastShineMepoIdx: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    blncntDriverEntries: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    drivers: list[struct_mgcnt_driver_t]
    tryStealBalloonFunc: Callable[[int, int], c_int]
    field384: Callable[[int, int], None]
    onDamageFunc: Callable[[int, int], c_int]
    onKillFunc: Callable[[int], None]
    onEndFunc: Callable[[], None]
    gap394: list[int]
    applyForceToDriverBalloonsFunc: Callable[[int, POINTER_T[struct_VecFx32]], None]
    collectableShineCount: int
    timeLimit: int
    shineRunnersRound: int
    PADDING_0: list[int]
    mgEndDelayCounter: int
    maxOwnedShineCount: int
    minOwnedShineCount: int
    winDriverTeamId: int
    lastShineMepoIdx: int
    PADDING_1: list[int]
    blncntDriverEntries: c_void_p

class mic_t(Structure):
    """
    ```python
    sampleBuffer: list[int] (POINTER(b)[1024])
    autoParam: struct_MICAutoParam (struct_MICAutoParam)
    frameCounter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    sampleBuffer: list[int]
    autoParam: struct_MICAutoParam
    frameCounter: int

class mission_config_t(Structure):
    """
    ```python
    timeLimit: int (POINTER(H))
    rankTime: int (POINTER(H))
    timeTolerance: int (POINTER(h))
    id: int (POINTER(B))
    task: int (POINTER(B))
    course: int (POINTER(B))
    ccMode: int (POINTER(B))
    character: int (POINTER(B))
    kart: int (POINTER(B))
    menuId: int (POINTER(B))
    fieldD: int (POINTER(B))
    camParamsIdx: int (POINTER(B))
    targetValue: int (POINTER(B))
    winDelay: int (POINTER(H))
    gap12: int (POINTER(H))
    objectIds: list[int] (POINTER(H)[4])
    flags: int (POINTER(H))
    enemyCharacter: int (POINTER(B))
    enemyKart: int (POINTER(B))
    name: list[int] (POINTER(B)[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    timeLimit: int
    rankTime: int
    timeTolerance: int
    id: int
    task: int
    course: int
    ccMode: int
    character: int
    kart: int
    menuId: int
    fieldD: int
    camParamsIdx: int
    targetValue: int
    winDelay: int
    gap12: int
    objectIds: list[int]
    flags: int
    enemyCharacter: int
    enemyKart: int
    name: list[int]

class mission_mr_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    nrMissions: int (POINTER(I))
    missions: list[struct_mission_config_t] (struct_mission_config_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    nrMissions: int
    missions: list[struct_mission_config_t]

class mobj_config_t(Structure):
    """
    ```python
    driverCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_driver_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint] (CFunctionType)
    itemCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint] (CFunctionType)
    colType: int (POINTER(I))
    size: struct_VecFx32 (struct_VecFx32)
    sphereCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_VecFx32], fx32, POINTER_T[struct_VecFx32]], c_int] (CFunctionType)
    providesPushback: int (POINTER(i))
    logicType: int (POINTER(I))
    driverHitSfxId: int (POINTER(i))
    itemHitSfxId: int (POINTER(I))
    nearClip: fx32 (struct_fx32)
    farClip: fx32 (struct_fx32)
    has3DModel: int (POINTER(i))
    sfxAudibleMaxCamYDiff: fx32 (struct_fx32)
    sfxAudibleMinCamYDiff: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    driverCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_driver_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint]
    itemCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint]
    colType: int
    size: struct_VecFx32
    sphereCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_VecFx32], fx32, POINTER_T[struct_VecFx32]], c_int]
    providesPushback: int
    logicType: int
    driverHitSfxId: int
    itemHitSfxId: int
    nearClip: fx32
    farClip: fx32
    has3DModel: int
    sfxAudibleMaxCamYDiff: fx32
    sfxAudibleMinCamYDiff: fx32

class mobj_def_t(Structure):
    """
    ```python
    instanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    instanceSize: int (POINTER(I))
    instInitFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_nkm_obji_entry_t], c_void_p], None] (CFunctionType)
    configSetupFunc: Callable[[], POINTER_T[struct_mobj_config_t]] (CFunctionType)
    renderPartSetupFuncs: list[Callable[[], POINTER_T[struct_mobj_render_part_t]]] (CFunctionType[3])
    logicPartSetupFunc: Callable[[], POINTER_T[struct_mobj_logic_part_t]] (CFunctionType)
    config: POINTER_T[struct_mobj_config_t] (POINTER(struct_mobj_config_t))
    renderParts: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[3])
    logicPart: POINTER_T[struct_mobj_logic_part_t] (POINTER(struct_mobj_logic_part_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    instanceCount: int
    PADDING_0: list[int]
    instanceSize: int
    instInitFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_nkm_obji_entry_t], c_void_p], None]
    configSetupFunc: Callable[[], POINTER_T[struct_mobj_config_t]]
    renderPartSetupFuncs: list[Callable[[], POINTER_T[struct_mobj_render_part_t]]]
    logicPartSetupFunc: Callable[[], POINTER_T[struct_mobj_logic_part_t]]
    config: POINTER_T[struct_mobj_config_t]
    renderParts: list[POINTER_T[struct_mobj_render_part_t]]
    logicPart: POINTER_T[struct_mobj_logic_part_t]

class mobj_inst_t(Structure):
    """
    ```python
    objectId: int (POINTER(H))
    flags: int (POINTER(H))
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    mtx: union_MtxFx43 (union_MtxFx43)
    size: struct_VecFx32 (struct_VecFx32)
    colEntryId: int (POINTER(h))
    alpha: int (POINTER(H))
    nearClip: fx32 (struct_fx32)
    farClip: fx32 (struct_fx32)
    sfxMaxDistanceSquare: int (POINTER(i))
    clipAreaMask: int (POINTER(I))
    visibilityFlags: int (POINTER(I))
    has3DModel: int (POINTER(H))
    rotY: int (POINTER(H))
    stateMachine: struct_state_machine_t (struct_state_machine_t)
    soundEmitter: POINTER_T[struct_sfx_emitter_t] (POINTER(struct_sfx_emitter_t))
    config: POINTER_T[struct_mobj_config_t] (POINTER(struct_mobj_config_t))
    objiEntry: POINTER_T[struct_nkm_obji_entry_t] (POINTER(struct_nkm_obji_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    objectId: int
    flags: int
    position: struct_VecFx32
    velocity: struct_VecFx32
    scale: struct_VecFx32
    mtx: union_MtxFx43
    size: struct_VecFx32
    colEntryId: int
    alpha: int
    nearClip: fx32
    farClip: fx32
    sfxMaxDistanceSquare: int
    clipAreaMask: int
    visibilityFlags: int
    has3DModel: int
    rotY: int
    stateMachine: struct_state_machine_t
    soundEmitter: POINTER_T[struct_sfx_emitter_t]
    config: POINTER_T[struct_mobj_config_t]
    objiEntry: POINTER_T[struct_nkm_obji_entry_t]

class mobj_logic_part_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    mobjInstanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    globalInitFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None] (CFunctionType)
    globalPreUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None] (CFunctionType)
    instanceUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t], POINTER_T[struct_mobj_inst_t]], None] (CFunctionType)
    globalPostUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None] (CFunctionType)
    type: int (POINTER(I))
    thunderFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint] (CFunctionType)
    thunderObjResp: int (POINTER(I))
    thisPointer: POINTER_T[POINTER_T[struct_mobj_logic_part_t]] (POINTER(POINTER(struct_mobj_logic_part_t)))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    mobjInstanceCount: int
    PADDING_0: list[int]
    globalInitFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None]
    globalPreUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None]
    instanceUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t], POINTER_T[struct_mobj_inst_t]], None]
    globalPostUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None]
    type: int
    thunderFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint]
    thunderObjResp: int
    thisPointer: POINTER_T[POINTER_T[struct_mobj_logic_part_t]]

class mobj_model_t(Structure):
    """
    ```python
    scale: struct_VecFx32 (struct_VecFx32)
    bbModel: POINTER_T[struct_bbm_model_t] (POINTER(struct_bbm_model_t))
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    shadowModel: POINTER_T[struct_shadowmodel_t] (POINTER(struct_shadowmodel_t))
    nsbmd: c_void_p (c_void_p)
    nsbcaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbmaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    scale: struct_VecFx32
    bbModel: POINTER_T[struct_bbm_model_t]
    model: POINTER_T[struct_model_t]
    shadowModel: POINTER_T[struct_shadowmodel_t]
    nsbmd: c_void_p
    nsbcaAnim: POINTER_T[struct_anim_manager_t]
    nsbtpAnim: POINTER_T[struct_anim_manager_t]
    nsbmaAnim: POINTER_T[struct_anim_manager_t]
    nsbtaAnim: POINTER_T[struct_anim_manager_t]

class mobj_render_part_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    mobjInstanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    globalInitFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None] (CFunctionType)
    globalPreRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None] (CFunctionType)
    instanceRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t], POINTER_T[struct_mobj_inst_t], POINTER_T[union_MtxFx43], int], None] (CFunctionType)
    globalPostRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None] (CFunctionType)
    type: int (POINTER(I))
    isTranslucent: int (POINTER(i))
    isShadow: int (POINTER(i))
    alphaSortList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    thisPointer: POINTER_T[POINTER_T[struct_mobj_render_part_t]] (POINTER(POINTER(struct_mobj_render_part_t)))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    mobjInstanceCount: int
    PADDING_0: list[int]
    globalInitFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None]
    globalPreRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None]
    instanceRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t], POINTER_T[struct_mobj_inst_t], POINTER_T[union_MtxFx43], int], None]
    globalPostRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None]
    type: int
    isTranslucent: int
    isShadow: int
    alphaSortList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    thisPointer: POINTER_T[POINTER_T[struct_mobj_render_part_t]]

class mobj_state_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    mobjInstanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    renderPartList: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[24])
    renderPart3dList: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[24])
    renderPart2dList: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[24])
    renderPartCount: int (POINTER(H))
    renderPart3dCount: int (POINTER(H))
    renderPart2dCount: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    field130: int (POINTER(I))
    logicPartList: list[POINTER_T[struct_mobj_logic_part_t]] (POINTER(struct_mobj_logic_part_t)[16])
    logicPartCount: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    field178: int (POINTER(I))
    hasKoopaBlock: int (POINTER(i))
    hasRotatingCylinder: int (POINTER(i))
    hasBridge: int (POINTER(i))
    hasWall: int (POINTER(i))
    pseudoItem: struct_it_item_inst_t (struct_it_item_inst_t)
    logicUpdateEnabled: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    mobjInstanceCount: int
    PADDING_0: list[int]
    renderPartList: list[POINTER_T[struct_mobj_render_part_t]]
    renderPart3dList: list[POINTER_T[struct_mobj_render_part_t]]
    renderPart2dList: list[POINTER_T[struct_mobj_render_part_t]]
    renderPartCount: int
    renderPart3dCount: int
    renderPart2dCount: int
    PADDING_1: list[int]
    field130: int
    logicPartList: list[POINTER_T[struct_mobj_logic_part_t]]
    logicPartCount: int
    PADDING_2: list[int]
    field178: int
    hasKoopaBlock: int
    hasRotatingCylinder: int
    hasBridge: int
    hasWall: int
    pseudoItem: struct_it_item_inst_t
    logicUpdateEnabled: int

class mobj_table_entry_t(Structure):
    """
    ```python
    id: int (POINTER(I))
    def_: POINTER_T[struct_mobj_def_t] (POINTER(struct_mobj_def_t))
    arg: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    def_: POINTER_T[struct_mobj_def_t]
    arg: c_void_p

class model_res_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    nsbmd: c_void_p (c_void_p)
    texRes: POINTER_T[struct_NNSG3dResTex_] (POINTER(struct_NNSG3dResTex_))
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    nsbmd: c_void_p
    texRes: POINTER_T[struct_NNSG3dResTex_]

class model_t(Structure):
    """
    ```python
    renderObj: struct_NNSG3dRenderObj_ (struct_NNSG3dRenderObj_)
    cullReversed: int (POINTER(I))
    render1Mat1Shp: int (POINTER(i))
    res: struct_model_res_t (struct_model_res_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    renderObj: struct_NNSG3dRenderObj_
    cullReversed: int
    render1Mat1Shp: int
    res: struct_model_res_t

class movetree_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    pointDuration: int (POINTER(i))
    counter: int (POINTER(i))
    speed: fx32 (struct_fx32)
    nsbcaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    nsbcaFrameDelta: int (POINTER(i))
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    shadow: struct_objshadow_t (struct_objshadow_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    pointDuration: int
    counter: int
    speed: fx32
    nsbcaFrame: int
    PADDING_0: list[int]
    nsbcaFrameDelta: int
    pathwalker: struct_pw_pathwalker_t
    state: int
    shadow: struct_objshadow_t

class mpicn_def_t(Structure):
    """
    ```python
    createFunc: Callable[[], c_int] (CFunctionType)
    destroyFunc: Callable[[], None] (CFunctionType)
    updateFunc: Callable[[], None] (CFunctionType)
    renderFunc: Callable[[POINTER_T[struct_oam_buf_t]], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    createFunc: Callable[[], c_int]
    destroyFunc: Callable[[], None]
    updateFunc: Callable[[], None]
    renderFunc: Callable[[POINTER_T[struct_oam_buf_t]], None]

class mpicn_icon_data_t(Structure):
    """
    ```python
    minPriority: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field4: int (POINTER(I))
    field8: int (POINTER(I))
    groupCount: int (POINTER(I))
    destroyFuncs: list[Callable[[], None]] (CFunctionType[49])
    updateFuncs: list[Callable[[], None]] (CFunctionType[49])
    renderFuncs: list[Callable[[POINTER_T[struct_oam_buf_t]], None]] (CFunctionType[49])
    ```
    """
    _pack_: ClassVar[int] = 1
    minPriority: int
    PADDING_0: list[int]
    field4: int
    field8: int
    groupCount: int
    destroyFuncs: list[Callable[[], None]]
    updateFuncs: list[Callable[[], None]]
    renderFuncs: list[Callable[[POINTER_T[struct_oam_buf_t]], None]]

class mpicn_mobj_icon_cell_t(Structure):
    """
    ```python
    position: struct_vec2i_t (struct_vec2i_t)
    cell: POINTER_T[struct_NNSG2dCellData] (POINTER(struct_NNSG2dCellData))
    priority: int (POINTER(H))
    flipX: int (POINTER(H))
    rotation: int (POINTER(H))
    field12: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_vec2i_t
    cell: POINTER_T[struct_NNSG2dCellData]
    priority: int
    flipX: int
    rotation: int
    field12: int

class mpicn_mobj_icon_group_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    cellCount: int (POINTER(I))
    mobjInstanceCount: int (POINTER(i))
    points: POINTER_T[struct_vec2i_t] (POINTER(struct_vec2i_t))
    cells: POINTER_T[struct_mpicn_mobj_icon_cell_t] (POINTER(struct_mpicn_mobj_icon_cell_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    cellCount: int
    mobjInstanceCount: int
    points: POINTER_T[struct_vec2i_t]
    cells: POINTER_T[struct_mpicn_mobj_icon_cell_t]

class mrbarrier_t(Structure):
    """
    ```python
    dcolMObj: struct_dcol_inst_t (struct_dcol_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    dcolMObj: struct_dcol_inst_t

class net_field_12F0_t(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[12])
    inetStatus: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    inetStatus: int

class net_match_property_t(Structure):
    """
    ```python
    value: int (POINTER(I))
    key: list[int] (POINTER(B)[16])
    field14: int (POINTER(B))
    gap15: list[int] (POINTER(B)[2])
    field16: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    value: int
    key: list[int]
    field14: int
    gap15: list[int]
    field16: int

class net_match_status_t(Structure):
    """
    ```python
    state: int (POINTER(I))
    PADDING_0: list[int] (POINTER(B)[4])
    rand: struct_MATHRandContext32 (struct_MATHRandContext32)
    gap1C: list[int] (POINTER(B)[20])
    field30: int (POINTER(I))
    field34: list[int] (POINTER(I)[4])
    gap44: list[int] (POINTER(B)[5])
    emblemNotSentAidMax: int (POINTER(B))
    gap4A: list[int] (POINTER(B)[16])
    receivedHellosBitmap: int (POINTER(B))
    receivedBitmap: int (POINTER(B))
    field5C: int (POINTER(B))
    field5D: int (POINTER(B))
    field5E: int (POINTER(B))
    field5F: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    PADDING_0: list[int]
    rand: struct_MATHRandContext32
    gap1C: list[int]
    field30: int
    field34: list[int]
    gap44: list[int]
    emblemNotSentAidMax: int
    gap4A: list[int]
    receivedHellosBitmap: int
    receivedBitmap: int
    field5C: int
    field5D: int
    field5E: int
    field5F: int
    PADDING_1: list[int]

class net_menu_config_t(Structure):
    """
    ```python
    field0: list[int] (POINTER(I)[4])
    field10: list[int] (POINTER(I)[4])
    selectedCourse: int (POINTER(I))
    field24: int (POINTER(I))
    field28: int (POINTER(I))
    vote: int (POINTER(I))
    gap30: list[int] (POINTER(B)[4])
    field34: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: list[int]
    field10: list[int]
    selectedCourse: int
    field24: int
    field28: int
    vote: int
    gap30: list[int]
    field34: int

class net_menu_dgram_header_t(Structure):
    """
    ```python
    opcode: int (POINTER(I))
    size: int (POINTER(I))
    aidSrc: int (POINTER(B))
    aidDest: int (POINTER(B))
    connectedAids: int (POINTER(B))
    fieldB: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    opcode: int
    size: int
    aidSrc: int
    aidDest: int
    connectedAids: int
    fieldB: int

class net_menu_dgram_t(Structure):
    """
    ```python
    header: struct_net_menu_dgram_header_t_ (struct_net_menu_dgram_header_t_)
    data: struct_net_menu_config_t_ (struct_net_menu_config_t_)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_net_menu_dgram_header_t_
    data: struct_net_menu_config_t_

class net_menu_profile_dgram_t(Structure):
    """
    ```python
    header: struct_net_menu_dgram_header_t_ (struct_net_menu_dgram_header_t_)
    profile: struct_struct_217AA00_field45C_t (struct_struct_217AA00_field45C_t)
    field238: int (POINTER(I))
    field23C: int (POINTER(I))
    field240: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_net_menu_dgram_header_t_
    profile: struct_struct_217AA00_field45C_t
    field238: int
    field23C: int
    field240: int

class net_race_state_t(Structure):
    """
    ```python
    stateMachine: struct_state_machine_t (struct_state_machine_t)
    PADDING_0: list[int] (POINTER(B)[4])
    pingStatuses: list[struct_rnet_ping_t_] (struct_rnet_ping_t_[4])
    fieldF4: int (POINTER(I))
    lastSentAid: int (POINTER(H))
    heardFromBitmap: int (POINTER(B))
    fieldFB: int (POINTER(B))
    initialAidsBitmap: int (POINTER(B))
    fieldFD: int (POINTER(B))
    gapFE: list[int] (POINTER(B)[6])
    drivers: list[struct_struc_222] (struct_struc_222[4])
    itemActionSlots: list[struct_rnet_item_action_entry_t_] (struct_rnet_item_action_entry_t_[16])
    incomingItemActions: list[struct_rnet_item_action_entry_t_] (struct_rnet_item_action_entry_t_[4][16])
    itemActionProcessed: list[int] (POINTER(B)[4][16])
    bufferAvailable: int (POINTER(h))
    gap726: list[int] (POINTER(B)[2])
    frameCounter: int (POINTER(i))
    field72C: int (POINTER(i))
    gap730: list[int] (POINTER(B)[4])
    lastAidSent: int (POINTER(H))
    field_736: int (POINTER(H))
    idleTime: int (POINTER(H))
    nextAid: int (POINTER(B))
    gap73B: list[int] (POINTER(B)[3])
    field73E: int (POINTER(B))
    gap73F: int (POINTER(B))
    field740: list[int] (POINTER(H)[4])
    sendBufferHeader2: int (POINTER(B))
    connectedAidsBitmap: int (POINTER(B))
    field74A: list[int] (POINTER(B)[4])
    field74E: list[int] (POINTER(B)[4])
    gap752: list[int] (POINTER(B)[2])
    dwcSendBuffer: POINTER_T[struct_rnet_dgram_t_] (POINTER(struct_rnet_dgram_t_))
    packetNextState: int (POINTER(I))
    flags: int (POINTER(H))
    gap75E: list[int] (POINTER(B)[1])
    field75F: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    stateMachine: struct_state_machine_t
    PADDING_0: list[int]
    pingStatuses: list[struct_rnet_ping_t_]
    fieldF4: int
    lastSentAid: int
    heardFromBitmap: int
    fieldFB: int
    initialAidsBitmap: int
    fieldFD: int
    gapFE: list[int]
    drivers: list[struct_struc_222]
    itemActionSlots: list[struct_rnet_item_action_entry_t_]
    incomingItemActions: list[struct_rnet_item_action_entry_t_]
    itemActionProcessed: list[int]
    bufferAvailable: int
    gap726: list[int]
    frameCounter: int
    field72C: int
    gap730: list[int]
    lastAidSent: int
    field_736: int
    idleTime: int
    nextAid: int
    gap73B: list[int]
    field73E: int
    gap73F: int
    field740: list[int]
    sendBufferHeader2: int
    connectedAidsBitmap: int
    field74A: list[int]
    field74E: list[int]
    gap752: list[int]
    dwcSendBuffer: POINTER_T[struct_rnet_dgram_t_]
    packetNextState: int
    flags: int
    gap75E: list[int]
    field75F: int
    PADDING_1: list[int]

class net_state_field_B2C_t(Structure):
    """
    ```python
    control: list[int] (POINTER(B)[3508])
    fieldDB4: int (POINTER(B))
    fieldDB5: int (POINTER(B))
    gapDB6: list[int] (POINTER(B)[2])
    fieldDB8: int (POINTER(I))
    state: int (POINTER(I))
    region: struct_net_match_property_t_ (struct_net_match_property_t_)
    matchType: struct_net_match_property_t_ (struct_net_match_property_t_)
    fieldDF0: struct_net_match_property_t_ (struct_net_match_property_t_)
    elo: struct_net_match_property_t_ (struct_net_match_property_t_)
    numPlayersMatch: int (POINTER(B))
    nFriendsInMatchmaker: int (POINTER(B))
    fieldE22: int (POINTER(B))
    fieldE23: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    control: list[int]
    fieldDB4: int
    fieldDB5: int
    gapDB6: list[int]
    fieldDB8: int
    state: int
    region: struct_net_match_property_t_
    matchType: struct_net_match_property_t_
    fieldDF0: struct_net_match_property_t_
    elo: struct_net_match_property_t_
    numPlayersMatch: int
    nFriendsInMatchmaker: int
    fieldE22: int
    fieldE23: int

class net_state_t(Structure):
    """
    ```python
    heap: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    heapMem: c_void_p (c_void_p)
    stateMachine: int (POINTER(I))
    raceRecvBuffers: list[int] (POINTER(B)[128][4])
    profileDatagramBuffers: list[struct_net_menu_profile_dgram_t_] (struct_net_menu_profile_dgram_t_[4])
    fieldB2C: struct_net_state_field_B2C_t_ (struct_net_state_field_B2C_t_)
    matchStatus: struct_net_match_status_t_ (struct_net_match_status_t_)
    userData: c_void_p (c_void_p)
    friends: list[c_void_p] (c_void_p[60])
    friendStatuses: list[int] (POINTER(B)[60])
    friendListChanged: int (POINTER(i))
    menuRecvBuffers: list[struct_net_menu_dgram_t_] (struct_net_menu_dgram_t_[4])
    menuSendBuffers: list[struct_net_menu_dgram_t_] (struct_net_menu_dgram_t_[4])
    field1F20: struct_net_field_12F0_t_ (struct_net_field_12F0_t_)
    heapInitialized: int (POINTER(i))
    field1F34: int (POINTER(i))
    field1F38: int (POINTER(i))
    frameCount: int (POINTER(I))
    field1F40: int (POINTER(i))
    lastError: int (POINTER(i))
    field1F48: int (POINTER(i))
    field1F4C: int (POINTER(B))
    field1F4D: int (POINTER(B))
    field1F4E: list[int] (POINTER(B)[4])
    numConnections: int (POINTER(B))
    aidMax: int (POINTER(B))
    field1F54: int (POINTER(B))
    connectedAids: int (POINTER(B))
    newlyDisconnectedAidsBitmap: int (POINTER(B))
    lastFriendStatusFetched: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    heap: POINTER_T[struct_NNSiFndHeapHead]
    heapMem: c_void_p
    stateMachine: int
    raceRecvBuffers: list[int]
    profileDatagramBuffers: list[struct_net_menu_profile_dgram_t_]
    fieldB2C: struct_net_state_field_B2C_t_
    matchStatus: struct_net_match_status_t_
    userData: c_void_p
    friends: list[c_void_p]
    friendStatuses: list[int]
    friendListChanged: int
    menuRecvBuffers: list[struct_net_menu_dgram_t_]
    menuSendBuffers: list[struct_net_menu_dgram_t_]
    field1F20: struct_net_field_12F0_t_
    heapInitialized: int
    field1F34: int
    field1F38: int
    frameCount: int
    field1F40: int
    lastError: int
    field1F48: int
    field1F4C: int
    field1F4D: int
    field1F4E: list[int]
    numConnections: int
    aidMax: int
    field1F54: int
    connectedAids: int
    newlyDisconnectedAidsBitmap: int
    lastFriendStatusFetched: int
    PADDING_0: list[int]

class nkdg_t(Structure):
    """
    ```python
    header: struct_ghost_header_t (struct_ghost_header_t)
    emblem: list[int] (POINTER(B)[512])
    inputData: struct_input_rec_recording_t (struct_input_rec_recording_t)
    padding: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_ghost_header_t
    emblem: list[int]
    inputData: struct_input_rec_recording_t
    padding: int

class nkm_area_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    length: struct_VecFx32 (struct_VecFx32)
    xVector: struct_VecFx32 (struct_VecFx32)
    yVector: struct_VecFx32 (struct_VecFx32)
    zVector: struct_VecFx32 (struct_VecFx32)
    param0: int (POINTER(h))
    param1: int (POINTER(h))
    enemyPointId: int (POINTER(h))
    shape: int (POINTER(B))
    cameraId: int (POINTER(B))
    type: int (POINTER(B))
    field45: int (POINTER(B))
    field46: int (POINTER(B))
    field47: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    length: struct_VecFx32
    xVector: struct_VecFx32
    yVector: struct_VecFx32
    zVector: struct_VecFx32
    param0: int
    param1: int
    enemyPointId: int
    shape: int
    cameraId: int
    type: int
    field45: int
    field46: int
    field47: int

class nkm_area_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_area_entry_t] (struct_nkm_area_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_area_entry_t]

class nkm_came_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    target1: struct_VecFx32 (struct_VecFx32)
    target2: struct_VecFx32 (struct_VecFx32)
    fovBegin: int (POINTER(H))
    fovBeginSin: fx16 (struct_fx16)
    fovBeginCos: fx16 (struct_fx16)
    fovEnd: int (POINTER(H))
    fovEndSin: fx16 (struct_fx16)
    fovEndCos: fx16 (struct_fx16)
    fovSpeed: int (POINTER(h))
    type: int (POINTER(H))
    pathId: int (POINTER(h))
    routeSpeed: int (POINTER(h))
    targetSpeed: int (POINTER(H))
    duration: int (POINTER(H))
    next: int (POINTER(h))
    introFirst: int (POINTER(B))
    unknown: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    target1: struct_VecFx32
    target2: struct_VecFx32
    fovBegin: int
    fovBeginSin: fx16
    fovBeginCos: fx16
    fovEnd: int
    fovEndSin: fx16
    fovEndCos: fx16
    fovSpeed: int
    type: int
    pathId: int
    routeSpeed: int
    targetSpeed: int
    duration: int
    next: int
    introFirst: int
    unknown: int

class nkm_came_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_came_entry_t] (struct_nkm_came_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_came_entry_t]

class nkm_cpat_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[3])
    previous: list[int] (POINTER(B)[3])
    sectionOrder: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]
    sectionOrder: int
    PADDING_0: int

class nkm_cpat_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_cpat_entry_t] (struct_nkm_cpat_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_cpat_entry_t]

class nkm_cpoi_entry_t(Structure):
    """
    ```python
    x1: fx32 (struct_fx32)
    z1: fx32 (struct_fx32)
    x2: fx32 (struct_fx32)
    z2: fx32 (struct_fx32)
    sin: fx32 (struct_fx32)
    cos: fx32 (struct_fx32)
    distance: fx32 (struct_fx32)
    gotoSection: int (POINTER(h))
    startSection: int (POINTER(h))
    keyId: int (POINTER(h))
    respawnId: int (POINTER(B))
    flags: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    x1: fx32
    z1: fx32
    x2: fx32
    z2: fx32
    sin: fx32
    cos: fx32
    distance: fx32
    gotoSection: int
    startSection: int
    keyId: int
    respawnId: int
    flags: int

class nkm_cpoi_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_cpoi_entry_t] (struct_nkm_cpoi_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_cpoi_entry_t]

class nkm_epat_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[3])
    previous: list[int] (POINTER(B)[3])
    sectionOrder: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]
    sectionOrder: int

class nkm_epat_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_epat_entry_t] (struct_nkm_epat_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_epat_entry_t]

class nkm_epoi_entry_settings_t(Structure):
    """
    ```python
    drifting: int (POINTER(H))
    unknown1: int (POINTER(H))
    unknown2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    drifting: int
    unknown1: int
    unknown2: int

class nkm_epoi_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    settings: struct_nkm_epoi_entry_settings_t (struct_nkm_epoi_entry_settings_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32
    settings: struct_nkm_epoi_entry_settings_t

class nkm_epoi_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_epoi_entry_t] (struct_nkm_epoi_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_epoi_entry_t]

class nkm_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    version: int (POINTER(H))
    headerLength: int (POINTER(H))
    offsets: list[int] (POINTER(I)[17])
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    version: int
    headerLength: int
    offsets: list[int]

class nkm_ipat_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[3])
    previous: list[int] (POINTER(B)[3])
    sectionOrder: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]
    sectionOrder: int

class nkm_ipat_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ipat_entry_t] (struct_nkm_ipat_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ipat_entry_t]

class nkm_ipoi_entry_beta_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32

class nkm_ipoi_entry_pointer_t(Union):
    """
    ```python
    final: POINTER_T[struct_nkm_ipoi_entry_t] (POINTER(struct_nkm_ipoi_entry_t))
    beta: POINTER_T[struct_nkm_ipoi_entry_beta_t] (POINTER(struct_nkm_ipoi_entry_beta_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    final: POINTER_T[struct_nkm_ipoi_entry_t]
    beta: POINTER_T[struct_nkm_ipoi_entry_beta_t]

class nkm_ipoi_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    recalcIdx: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32
    recalcIdx: int
    PADDING_0: list[int]

class nkm_ipoi_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ipoi_entry_t] (struct_nkm_ipoi_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ipoi_entry_t]

class nkm_ktp2_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    padding: int (POINTER(H))
    id: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    padding: int
    id: int

class nkm_ktp2_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktp2_entry_t] (struct_nkm_ktp2_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktp2_entry_t]

class nkm_ktpc_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    nextMepo: int (POINTER(h))
    id: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    nextMepo: int
    id: int

class nkm_ktpc_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktpc_entry_t] (struct_nkm_ktpc_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktpc_entry_t]

class nkm_ktpj_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    enemyPointId: int (POINTER(H))
    itemPointId: int (POINTER(H))
    id: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    enemyPointId: int
    itemPointId: int
    id: int
    PADDING_0: list[int]

class nkm_ktpj_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktpj_entry_t] (struct_nkm_ktpj_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktpj_entry_t]

class nkm_ktpm_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    padding: int (POINTER(H))
    id: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    padding: int
    id: int

class nkm_ktpm_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktpm_entry_t] (struct_nkm_ktpm_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktpm_entry_t]

class nkm_ktps_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    padding: int (POINTER(H))
    index: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    padding: int
    index: int

class nkm_ktps_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktps_entry_t] (struct_nkm_ktps_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktps_entry_t]

class nkm_mepa_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[8])
    previous: list[int] (POINTER(B)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]

class nkm_mepa_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_mepa_entry_t] (struct_nkm_mepa_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_mepa_entry_t]

class nkm_mepo_entry_settings_t(Structure):
    """
    ```python
    drifting: int (POINTER(I))
    unknown1: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    drifting: int
    unknown1: int

class nkm_mepo_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    settings: struct_nkm_mepo_entry_settings_t (struct_nkm_mepo_entry_settings_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32
    settings: struct_nkm_mepo_entry_settings_t

class nkm_mepo_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_mepo_entry_t] (struct_nkm_mepo_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_mepo_entry_t]

class nkm_obji_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    objectId: int (POINTER(H))
    pathId: int (POINTER(h))
    settings: list[int] (POINTER(h)[7])
    flags: int (POINTER(h))
    showsInTT: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    scale: struct_VecFx32
    objectId: int
    pathId: int
    settings: list[int]
    flags: int
    showsInTT: int
    PADDING_0: list[int]

class nkm_obji_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_obji_entry_t] (struct_nkm_obji_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_obji_entry_t]

class nkm_path_entry_t(Structure):
    """
    ```python
    id: int (POINTER(B))
    loop: int (POINTER(B))
    pointCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    loop: int
    pointCount: int

class nkm_path_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_path_entry_t] (struct_nkm_path_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_path_entry_t]

class nkm_poit_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    pointIndex: int (POINTER(B))
    unknown1: int (POINTER(B))
    duration: int (POINTER(h))
    _0: union_nkm_poit_entry_t_0 (union_nkm_poit_entry_t_0)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    pointIndex: int
    unknown1: int
    duration: int
    _0: union_nkm_poit_entry_t_0

class nkm_poit_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_poit_entry_t] (struct_nkm_poit_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_poit_entry_t]

class nkm_section_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    count: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    count: int

class nkm_stag_data_t(Structure):
    """
    ```python
    courseId: int (POINTER(H))
    nrLaps: int (POINTER(H))
    polePosition: int (POINTER(B))
    fogEnabled: int (POINTER(B))
    fogTableGenMode: int (POINTER(B))
    fogSlope: int (POINTER(B))
    unknown2: list[int] (POINTER(B)[8])
    fogDensity: fx32 (struct_fx32)
    fogColor: int (POINTER(I))
    kclColors: list[int] (POINTER(H)[4])
    mobjFarClip: fx32 (struct_fx32)
    frustumFar: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    courseId: int
    nrLaps: int
    polePosition: int
    fogEnabled: int
    fogTableGenMode: int
    fogSlope: int
    unknown2: list[int]
    fogDensity: fx32
    fogColor: int
    kclColors: list[int]
    mobjFarClip: fx32
    frustumFar: fx32

class nkm_stag_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    data: struct_nkm_stag_data_t (struct_nkm_stag_data_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    data: struct_nkm_stag_data_t

class nkm_t(Structure):
    """
    ```python
    header: struct_nkm_header_t (struct_nkm_header_t)
    obji: struct_nkm_obji_t (struct_nkm_obji_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_header_t
    obji: struct_nkm_obji_t

class nkpg_t(Structure):
    """
    ```python
    header: struct_ghost_header_t (struct_ghost_header_t)
    inputData: list[int] (POINTER(B)[3532])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_ghost_header_t
    inputData: list[int]

class nksy_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    gap4: list[int] (POINTER(B)[8])
    nickname: list[int] (POINTER(H)[10])
    unlockBits: list[int] (POINTER(B)[4])
    field24: int (POINTER(H))
    personalGhostBits: list[int] (POINTER(B)[4])
    downloadGhostBits: list[int] (POINTER(B)[4])
    nkfeBits: list[int] (POINTER(B)[2])
    gap30: int (POINTER(B))
    field31: int (POINTER(B))
    gap32: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    field34: int (POINTER(I))
    field38: int (POINTER(I))
    field3C: int (POINTER(I))
    field40: int (POINTER(I))
    field44: int (POINTER(I))
    field48: int (POINTER(I))
    dwcUserData: c_void_p (c_void_p)
    gap8C: list[int] (POINTER(B)[116])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    gap4: list[int]
    nickname: list[int]
    unlockBits: list[int]
    field24: int
    personalGhostBits: list[int]
    downloadGhostBits: list[int]
    nkfeBits: list[int]
    gap30: int
    field31: int
    gap32: int
    PADDING_0: int
    field34: int
    field38: int
    field3C: int
    field40: int
    field44: int
    field48: int
    dwcUserData: c_void_p
    gap8C: list[int]

class nsk1_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    counter: int (POINTER(i))
    unkA4: list[int] (POINTER(B)[4])
    state: int (POINTER(I))
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    counter: int
    unkA4: list[int]
    state: int
    pathwalker: struct_pw_pathwalker_t

class nsk2_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    counter: int (POINTER(i))
    state: int (POINTER(I))
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t] (POINTER(struct_sfx_emitter_ex_params_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    counter: int
    state: int
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t]

class oam_buf_t(Structure):
    """
    ```python
    oam: list[struct_GXOamAttr] (struct_GXOamAttr[128])
    objCount: int (POINTER(H))
    affineCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    oam: list[struct_GXOamAttr]
    objCount: int
    affineCount: int

class oam_buffers_t(Structure):
    """
    ```python
    mainOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    subOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mainOamBuf: struct_oam_buf_t
    subOamBuf: struct_oam_buf_t

class objshadow_t(Structure):
    """
    ```python
    mtx: union_MtxFx43 (union_MtxFx43)
    alpha: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    mtx: union_MtxFx43
    alpha: int
    PADDING_0: list[int]

class obpakkunsf_t(Structure):
    """
    ```python
    rotDieMObj: struct_rotdiemobj_t (struct_rotdiemobj_t)
    counter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    rotDieMObj: struct_rotdiemobj_t
    counter: int
    PADDING_0: list[int]

class overlay_data_overlayinfo_t(Structure):
    """
    ```python
    id: int (POINTER(I))
    start: int (POINTER(I))
    end: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    start: int
    end: int

class overlay_data_t(Structure):
    """
    ```python
    curOverlay: int (POINTER(I))
    state: int (POINTER(I))
    overlays: list[struct_overlay_data_overlayinfo_t] (struct_overlay_data_overlayinfo_t[3])
    overlayInfo: struct_FSOverlayInfo (struct_FSOverlayInfo)
    overlayFile: struct_FSFile (struct_FSFile)
    overlayFrmHeap: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    overlayExpHeap: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    overlayRegionStart: int (POINTER(I))
    overlayRegionEnd: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    curOverlay: int
    state: int
    overlays: list[struct_overlay_data_overlayinfo_t]
    overlayInfo: struct_FSOverlayInfo
    overlayFile: struct_FSFile
    overlayFrmHeap: POINTER_T[struct_NNSiFndHeapHead]
    overlayExpHeap: POINTER_T[struct_NNSiFndHeapHead]
    overlayRegionStart: int
    overlayRegionEnd: int

class pakkun_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    polygonId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    nsbcaFrame: int (POINTER(i))
    fieldA8: int (POINTER(i))
    fieldAC: int (POINTER(i))
    fieldB0: int (POINTER(i))
    state: int (POINTER(I))
    pathwalkers: list[struct_pw_pathwalker_t] (struct_pw_pathwalker_t[7])
    counter: int (POINTER(i))
    curPath: int (POINTER(H))
    pathCount: int (POINTER(H))
    field1BC: list[int] (POINTER(i)[7])
    field1D8: int (POINTER(i))
    mouthRotY: int (POINTER(i))
    mouthRotX: int (POINTER(i))
    field1E4: int (POINTER(i))
    field1E8: int (POINTER(i))
    field1EC: int (POINTER(i))
    scale: int (POINTER(i))
    scaleVelocity: int (POINTER(i))
    headElevation: int (POINTER(i))
    fireballElevation: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    polygonId: int
    PADDING_0: list[int]
    nsbcaFrame: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    state: int
    pathwalkers: list[struct_pw_pathwalker_t]
    counter: int
    curPath: int
    pathCount: int
    field1BC: list[int]
    field1D8: int
    mouthRotY: int
    mouthRotX: int
    field1E4: int
    field1E8: int
    field1EC: int
    scale: int
    scaleVelocity: int
    headElevation: int
    fireballElevation: int

class pakkunfire_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    elevation: fx32 (struct_fx32)
    elevationVelocity: fx32 (struct_fx32)
    state: int (POINTER(I))
    emitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    pathwalker: struct_pw_pathwalker_t
    elevation: fx32
    elevationVelocity: fx32
    state: int
    emitter: POINTER_T[struct_spa_emitter_t]

class pendulum_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    rotation: quaternion_t (struct_quaternion_t)
    prevPosition: struct_VecFx32 (struct_VecFx32)
    renderPos: struct_VecFx32 (struct_VecFx32)
    shadowMtx: union_MtxFx43 (union_MtxFx43)
    offsetY: fx32 (struct_fx32)
    swingRange: int (POINTER(H))
    swingVelocity: int (POINTER(H))
    angle: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    size: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    rotation: quaternion_t
    prevPosition: struct_VecFx32
    renderPos: struct_VecFx32
    shadowMtx: union_MtxFx43
    offsetY: fx32
    swingRange: int
    swingVelocity: int
    angle: int
    PADDING_0: list[int]
    size: struct_VecFx32

class physp_char_params_t(Structure):
    """
    ```python
    field0: fx32 (struct_fx32)
    weight: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: fx32
    weight: fx32

class physp_kart_params_t(Structure):
    """
    ```python
    colSphereSize: fx32 (struct_fx32)
    colSphereZOffset: fx32 (struct_fx32)
    gap8: list[int] (POINTER(B)[4])
    weight: fx16 (struct_fx16)
    driftBoostTime: int (POINTER(h))
    maxSpeed: fx32 (struct_fx32)
    baseAcceleration: fx32 (struct_fx32)
    field18: fx32 (struct_fx32)
    field1C: fx32 (struct_fx32)
    driftBaseAcceleration: fx32 (struct_fx32)
    field24: fx32 (struct_fx32)
    field28: fx32 (struct_fx32)
    deceleration: fx32 (struct_fx32)
    handling: fx16 (struct_fx16)
    drift: fx16 (struct_fx16)
    driftTurningCompensation: fx32 (struct_fx32)
    collisionVelocityMinusDirMultipliers: list[fx32] (struct_fx32[12])
    collisionSpeedMultipliers: list[fx32] (struct_fx32[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    colSphereSize: fx32
    colSphereZOffset: fx32
    gap8: list[int]
    weight: fx16
    driftBoostTime: int
    maxSpeed: fx32
    baseAcceleration: fx32
    field18: fx32
    field1C: fx32
    driftBaseAcceleration: fx32
    field24: fx32
    field28: fx32
    deceleration: fx32
    handling: fx16
    drift: fx16
    driftTurningCompensation: fx32
    collisionVelocityMinusDirMultipliers: list[fx32]
    collisionSpeedMultipliers: list[fx32]

class physp_t(Structure):
    """
    ```python
    driverKartPhysicalParams: POINTER_T[struct_physp_kart_params_t] (POINTER(struct_physp_kart_params_t))
    driverCharPhysicalParams: POINTER_T[struct_physp_char_params_t] (POINTER(struct_physp_char_params_t))
    field8: int (POINTER(I))
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t] (POINTER(struct_physp_kart_params_t))
    charPhysicalParams: POINTER_T[struct_physp_char_params_t] (POINTER(struct_physp_char_params_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    driverKartPhysicalParams: POINTER_T[struct_physp_kart_params_t]
    driverCharPhysicalParams: POINTER_T[struct_physp_char_params_t]
    field8: int
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t]
    charPhysicalParams: POINTER_T[struct_physp_char_params_t]

class picture_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbcaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    pictureType: int (POINTER(I))
    counter: int (POINTER(i))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbcaFrame: int
    PADDING_0: list[int]
    pictureType: int
    counter: int
    state: int

class pole_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class process_t(Structure):
    """
    ```python
    name: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    mainFunc: Callable[[c_void_p], c_int] (CFunctionType)
    exitFunc: Callable[[int], None] (CFunctionType)
    heapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    prevProcess: POINTER_T[struct_process_t] (POINTER(struct_process_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    name: POINTER_T[c_ubyte]
    mainFunc: Callable[[c_void_p], c_int]
    exitFunc: Callable[[int], None]
    heapHandle: POINTER_T[struct_NNSiFndHeapHead]
    prevProcess: POINTER_T[struct_process_t]

class ptcm_camflashes_t(Structure):
    """
    ```python
    directions: list[struct_VecFx32] (struct_VecFx32[6])
    emitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[6])
    waitCounter: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    directions: list[struct_VecFx32]
    emitters: list[POINTER_T[struct_spa_emitter_t]]
    waitCounter: int
    PADDING_0: list[int]

class puddle_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class pukupuku_t(Structure):
    """
    ```python
    rdmobj: struct_rotdiemobj_t (struct_rotdiemobj_t)
    fieldB8: struct_VecFx32 (struct_VecFx32)
    fieldC4: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    shadow: struct_objshadow_t (struct_objshadow_t)
    fieldFC: int (POINTER(I))
    field100: fx32 (struct_fx32)
    field104: fx32 (struct_fx32)
    field108: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    rdmobj: struct_rotdiemobj_t
    fieldB8: struct_VecFx32
    fieldC4: int
    PADDING_0: list[int]
    shadow: struct_objshadow_t
    fieldFC: int
    field100: fx32
    field104: fx32
    field108: fx32

class pw_path_part_t(Structure):
    """
    ```python
    p0: struct_VecFx32 (struct_VecFx32)
    p1: struct_VecFx32 (struct_VecFx32)
    p2: struct_VecFx32 (struct_VecFx32)
    p3: struct_VecFx32 (struct_VecFx32)
    length: fx32 (struct_fx32)
    oneDivLength: int (POINTER(i))
    hermLength: fx32 (struct_fx32)
    oneDivHermLength: int (POINTER(i))
    linLength: fx32 (struct_fx32)
    oneDivLinLength: int (POINTER(i))
    field48: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    p0: struct_VecFx32
    p1: struct_VecFx32
    p2: struct_VecFx32
    p3: struct_VecFx32
    length: fx32
    oneDivLength: int
    hermLength: fx32
    oneDivHermLength: int
    linLength: fx32
    oneDivLinLength: int
    field48: struct_VecFx32

class pw_path_t(Structure):
    """
    ```python
    parts: POINTER_T[struct_pw_path_part_t] (POINTER(struct_pw_path_part_t))
    partCount: int (POINTER(I))
    loop: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    parts: POINTER_T[struct_pw_path_part_t]
    partCount: int
    loop: int

class pw_pathwalker_t(Structure):
    """
    ```python
    path: POINTER_T[struct_pw_path_t] (POINTER(struct_pw_path_t))
    speed: fx32 (struct_fx32)
    pathId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    partIdx: int (POINTER(I))
    partSpeed: int (POINTER(i))
    partProgress: int (POINTER(i))
    isForwards: int (POINTER(i))
    prevPoit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    curPoit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: POINTER_T[struct_pw_path_t]
    speed: fx32
    pathId: int
    PADDING_0: list[int]
    partIdx: int
    partSpeed: int
    partProgress: int
    isForwards: int
    prevPoit: POINTER_T[struct_nkm_poit_entry_t]
    curPoit: POINTER_T[struct_nkm_poit_entry_t]

class pw_simple_pathwalker_t(Structure):
    """
    ```python
    pathPart: struct_pw_path_part_t (struct_pw_path_part_t)
    speed: fx32 (struct_fx32)
    partSpeed: int (POINTER(i))
    progress: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    pathPart: struct_pw_path_part_t
    speed: fx32
    partSpeed: int
    progress: int

class quaternion_t(Structure):
    """
    ```python
    x: fx32 (struct_fx32)
    y: fx32 (struct_fx32)
    z: fx32 (struct_fx32)
    w: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx32
    y: fx32
    z: fx32
    w: fx32

class r2d_race_mode_top_hud_state_t(Structure):
    """
    ```python
    _0: union_r2d_race_mode_top_hud_state_t_0 (union_r2d_race_mode_top_hud_state_t_0)
    mrTargetValue: int (POINTER(i))
    ghostAvailable: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: union_r2d_race_mode_top_hud_state_t_0
    mrTargetValue: int
    ghostAvailable: int

class race_config_driver_t(Structure):
    """
    ```python
    character: int (POINTER(I))
    kart: int (POINTER(I))
    type: int (POINTER(I))
    team: int (POINTER(i))
    field10: int (POINTER(I))
    driverIndex: int (POINTER(I))
    ghostType: int (POINTER(I))
    field1C: int (POINTER(H))
    field1E: int (POINTER(b))
    field1F: int (POINTER(B))
    nickname: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    emblemTex: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    field28: int (POINTER(I))
    useCustomEmblem: int (POINTER(B))
    field2D: int (POINTER(B))
    field2E: int (POINTER(B))
    field2F: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    character: int
    kart: int
    type: int
    team: int
    field10: int
    driverIndex: int
    ghostType: int
    field1C: int
    field1E: int
    field1F: int
    nickname: POINTER_T[c_ushort]
    emblemTex: POINTER_T[c_ubyte]
    field28: int
    useCustomEmblem: int
    field2D: int
    field2E: int
    field2F: int

class race_config_t(Structure):
    """
    ```python
    course: int (POINTER(I))
    cup: int (POINTER(I))
    raceMode: int (POINTER(I))
    displayMode: int (POINTER(I))
    ccMode: int (POINTER(I))
    cpuMode: int (POINTER(I))
    mgMode: int (POINTER(I))
    rules: int (POINTER(I))
    courseMode: int (POINTER(I))
    taGhost: int (POINTER(I))
    mrConfig: struct_mission_config_t (struct_mission_config_t)
    mrLevel: int (POINTER(b))
    mrIndex: int (POINTER(b))
    field56: int (POINTER(B))
    isMirror: int (POINTER(b))
    teams: int (POINTER(b))
    field59: int (POINTER(B))
    field5A: int (POINTER(B))
    field5B: int (POINTER(B))
    rngSeed: int (POINTER(I))
    raceNr: int (POINTER(H))
    playerDriverId: int (POINTER(b))
    cpuDriverId: int (POINTER(B))
    lapCountOverride: int (POINTER(b))
    field65: int (POINTER(B))
    gap66: list[int] (POINTER(B)[2])
    drivers: list[struct_race_config_driver_t] (struct_race_config_driver_t[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    course: int
    cup: int
    raceMode: int
    displayMode: int
    ccMode: int
    cpuMode: int
    mgMode: int
    rules: int
    courseMode: int
    taGhost: int
    mrConfig: struct_mission_config_t
    mrLevel: int
    mrIndex: int
    field56: int
    isMirror: int
    teams: int
    field59: int
    field5A: int
    field5B: int
    rngSeed: int
    raceNr: int
    playerDriverId: int
    cpuDriverId: int
    lapCountOverride: int
    field65: int
    gap66: list[int]
    drivers: list[struct_race_config_driver_t]

class race_driver_result_t(Structure):
    """
    ```python
    totalRankPoints: int (POINTER(H))
    globalPlace: int (POINTER(B))
    place: int (POINTER(B))
    rankPoints: int (POINTER(B))
    winCount: int (POINTER(B))
    raceTime: struct_race_time_t (struct_race_time_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    totalRankPoints: int
    globalPlace: int
    place: int
    rankPoints: int
    winCount: int
    raceTime: struct_race_time_t

class race_driver_status_t(Structure):
    """
    ```python
    state: int (POINTER(I))
    lapFrameCounter: int (POINTER(I))
    field8: int (POINTER(I))
    lapTimes: list[struct_race_time_t] (struct_race_time_t[5])
    totalTime: struct_race_time_t (struct_race_time_t)
    curLap: int (POINTER(i))
    firstPlaceTime: int (POINTER(I))
    totalMilliseconds: int (POINTER(I))
    flags: int (POINTER(H))
    curCpoi: int (POINTER(H))
    lastCorrectKeyPoint: int (POINTER(h))
    curKeyPoint: int (POINTER(h))
    curCpat: int (POINTER(H))
    highestReachedLap: int (POINTER(H))
    place: int (POINTER(H))
    driverId: int (POINTER(H))
    field3CBit89: int (POINTER(H))
    PADDING_0: int (POINTER(B))
    skillRankPoints: int (POINTER(h))
    cpoiProgress: fx32 (struct_fx32)
    raceProgress: fx32 (struct_fx32)
    lapProgress: fx32 (struct_fx32)
    cpoiMask: list[int] (POINTER(I)[16])
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    lapFrameCounter: int
    field8: int
    lapTimes: list[struct_race_time_t]
    totalTime: struct_race_time_t
    curLap: int
    firstPlaceTime: int
    totalMilliseconds: int
    flags: int
    curCpoi: int
    lastCorrectKeyPoint: int
    curKeyPoint: int
    curCpat: int
    highestReachedLap: int
    place: int
    driverId: int
    field3CBit89: int
    PADDING_0: int
    skillRankPoints: int
    cpoiProgress: fx32
    raceProgress: fx32
    lapProgress: fx32
    cpoiMask: list[int]

class race_multi_config_t(Structure):
    """
    ```python
    current: struct_race_config_t (struct_race_config_t)
    next: struct_race_config_t (struct_race_config_t)
    driverCount: int (POINTER(B))
    field3D1: int (POINTER(B))
    teamDriverCount: list[int] (POINTER(B)[2])
    field3D4: int (POINTER(B))
    field3D5: list[int] (POINTER(b)[2])
    field3D7: int (POINTER(B))
    nrRacesNrWins: int (POINTER(H))
    gap3DA: list[int] (POINTER(B)[2])
    courseQueue: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    courseQueueIdx: int (POINTER(B))
    field3E1: int (POINTER(B))
    personalGhostTime: struct_race_time_t (struct_race_time_t)
    personalGhostAvailable: int (POINTER(B))
    gap3E7: int (POINTER(B))
    ghostTime: struct_race_time_t (struct_race_time_t)
    ghostLapTimes: list[struct_race_time_t] (struct_race_time_t[5])
    ```
    """
    _pack_: ClassVar[int] = 1
    current: struct_race_config_t
    next: struct_race_config_t
    driverCount: int
    field3D1: int
    teamDriverCount: list[int]
    field3D4: int
    field3D5: list[int]
    field3D7: int
    nrRacesNrWins: int
    gap3DA: list[int]
    courseQueue: POINTER_T[c_ubyte]
    courseQueueIdx: int
    field3E1: int
    personalGhostTime: struct_race_time_t
    personalGhostAvailable: int
    gap3E7: int
    ghostTime: struct_race_time_t
    ghostLapTimes: list[struct_race_time_t]

class race_results_t(Structure):
    """
    ```python
    driverResults: list[struct_race_driver_result_t] (struct_race_driver_result_t[8][4])
    totalSkillRankPoints: int (POINTER(I))
    teamResults: list[struct_race_team_result_t] (struct_race_team_result_t[2][4])
    field164: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    driverResults: list[struct_race_driver_result_t]
    totalSkillRankPoints: int
    teamResults: list[struct_race_team_result_t]
    field164: int

class race_skill_rankpoints_t(Structure):
    """
    ```python
    rankTimeDeltaPoints: int (POINTER(i))
    firstPlacePercentagePoints: int (POINTER(i))
    startBoostPoints: int (POINTER(i))
    powerSlidePoints: int (POINTER(i))
    itemHitPoints: int (POINTER(i))
    offRoadTimePoints: int (POINTER(i))
    wallHitPoints: int (POINTER(i))
    damagePoints: int (POINTER(i))
    respawnPoints: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    rankTimeDeltaPoints: int
    firstPlacePercentagePoints: int
    startBoostPoints: int
    powerSlidePoints: int
    itemHitPoints: int
    offRoadTimePoints: int
    wallHitPoints: int
    damagePoints: int
    respawnPoints: int

class race_state_t(Structure):
    """
    ```python
    state: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    frameCounter: int (POINTER(I))
    frameCounter2: int (POINTER(i))
    frameCounterModulo8: int (POINTER(i))
    isOddFrame: int (POINTER(i))
    frameCounterModuloDriverCount: int (POINTER(i))
    toonTableOffset: int (POINTER(I))
    toonTableUpdateCounter: int (POINTER(I))
    darkeningFogState: int (POINTER(I))
    prevDarkeningFogState: int (POINTER(I))
    isCamAnimMode: int (POINTER(i))
    isCamAnimSingleScreen: int (POINTER(i))
    field30: int (POINTER(I))
    field34: int (POINTER(I))
    isAwardStaffRoll: int (POINTER(i))
    field3C: int (POINTER(I))
    light0Dir: struct_VecFx16 (struct_VecFx16)
    PADDING_1: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    PADDING_0: list[int]
    frameCounter: int
    frameCounter2: int
    frameCounterModulo8: int
    isOddFrame: int
    frameCounterModuloDriverCount: int
    toonTableOffset: int
    toonTableUpdateCounter: int
    darkeningFogState: int
    prevDarkeningFogState: int
    isCamAnimMode: int
    isCamAnimSingleScreen: int
    field30: int
    field34: int
    isAwardStaffRoll: int
    field3C: int
    light0Dir: struct_VecFx16
    PADDING_1: list[int]

class race_status_t(Structure):
    """
    ```python
    time: struct_race_status_time_t (struct_race_status_time_t)
    rankTimeGp: int (POINTER(H))
    finishedDriverCount: int (POINTER(H))
    field10: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    driverStatus: list[struct_race_driver_status_t] (struct_race_driver_status_t[8])
    placeDriverIds: list[int] (POINTER(b)[8])
    PADDING_1: list[int] (POINTER(B)[4])
    safeRng: struct_MATHRandContext32 (struct_MATHRandContext32)
    rngSeed: int (POINTER(I))
    PADDING_2: list[int] (POINTER(B)[4])
    randomRng: struct_MATHRandContext32 (struct_MATHRandContext32)
    stableRng: struct_MATHRandContext32 (struct_MATHRandContext32)
    rankTimeGpRtt: POINTER_T[struct_ranktime_gp_t] (POINTER(struct_ranktime_gp_t))
    resultsStored: int (POINTER(i))
    camAnimComplete: int (POINTER(i))
    cpoiKeyPointProgress: POINTER_T[fx32] (POINTER(struct_fx32))
    gap4D8: list[int] (POINTER(B)[4])
    rankPointRpt: POINTER_T[struct_rankpoint_t] (POINTER(struct_rankpoint_t))
    missionResult: int (POINTER(I))
    oneDivCpatSegmentCount: fx32 (struct_fx32)
    oneDivNrLaps: fx32 (struct_fx32)
    useTimeLimit: int (POINTER(i))
    uncontrollable: int (POINTER(i))
    timeLimit: int (POINTER(I))
    field4F8: int (POINTER(B))
    field4F9: int (POINTER(B))
    mrWinDelayCounter: int (POINTER(H))
    mrLoseDelayCounter: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    skillRankPoints: struct_race_skill_rankpoints_t (struct_race_skill_rankpoints_t)
    PADDING_4: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    time: struct_race_status_time_t
    rankTimeGp: int
    finishedDriverCount: int
    field10: int
    PADDING_0: list[int]
    driverStatus: list[struct_race_driver_status_t]
    placeDriverIds: list[int]
    PADDING_1: list[int]
    safeRng: struct_MATHRandContext32
    rngSeed: int
    PADDING_2: list[int]
    randomRng: struct_MATHRandContext32
    stableRng: struct_MATHRandContext32
    rankTimeGpRtt: POINTER_T[struct_ranktime_gp_t]
    resultsStored: int
    camAnimComplete: int
    cpoiKeyPointProgress: POINTER_T[fx32]
    gap4D8: list[int]
    rankPointRpt: POINTER_T[struct_rankpoint_t]
    missionResult: int
    oneDivCpatSegmentCount: fx32
    oneDivNrLaps: fx32
    useTimeLimit: int
    uncontrollable: int
    timeLimit: int
    field4F8: int
    field4F9: int
    mrWinDelayCounter: int
    mrLoseDelayCounter: int
    PADDING_3: list[int]
    skillRankPoints: struct_race_skill_rankpoints_t
    PADDING_4: list[int]

class race_status_time_t(Structure):
    """
    ```python
    frameCounter: int (POINTER(I))
    timeRunning: int (POINTER(i))
    lapTime: struct_race_time_t (struct_race_time_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    frameCounter: int
    timeRunning: int
    lapTime: struct_race_time_t

class race_team_result_t(Structure):
    """
    ```python
    totalRankPoints: int (POINTER(H))
    winCount: int (POINTER(B))
    flags: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    totalRankPoints: int
    winCount: int
    flags: int

class race_time_t(Structure):
    """
    ```python
    milliseconds: int (POINTER(H))
    minutes: int (POINTER(B))
    seconds: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    milliseconds: int
    minutes: int
    seconds: int

class rainstar_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbtaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbtaFrame: int
    PADDING_0: list[int]

class rankpoint_entry_t(Structure):
    """
    ```python
    points: list[int] (POINTER(B)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    points: list[int]

class rankpoint_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    fileSize: int (POINTER(I))
    entries: list[struct_rankpoint_entry_t] (struct_rankpoint_entry_t[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    fileSize: int
    entries: list[struct_rankpoint_entry_t]

class ranktime_gp_entry_t(Structure):
    """
    ```python
    courseId: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    rankTime50cc: int (POINTER(H))
    rankTime100cc: int (POINTER(H))
    rankTime150cc: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    courseId: int
    PADDING_0: int
    rankTime50cc: int
    rankTime100cc: int
    rankTime150cc: int

class ranktime_gp_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    fileSize: int (POINTER(I))
    courseCount: int (POINTER(H))
    rankTimeDeltaFactor: int (POINTER(H))
    firstPlacePercentageFactor: int (POINTER(H))
    startBoostFactor: int (POINTER(H))
    powerSlideFactor: int (POINTER(H))
    itemHitFactor: int (POINTER(H))
    offRoadTimeFactor: int (POINTER(H))
    wallHitFactor: int (POINTER(H))
    damageFactor: int (POINTER(H))
    respawnFactor: int (POINTER(H))
    courseRankTimes: list[struct_ranktime_gp_entry_t] (struct_ranktime_gp_entry_t[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    fileSize: int
    courseCount: int
    rankTimeDeltaFactor: int
    firstPlacePercentageFactor: int
    startBoostFactor: int
    powerSlideFactor: int
    itemHitFactor: int
    offRoadTimeFactor: int
    wallHitFactor: int
    damageFactor: int
    respawnFactor: int
    courseRankTimes: list[struct_ranktime_gp_entry_t]

class result_t(Structure):
    """
    ```python
    mainOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    subOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    raceMode: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mainOamBuf: struct_oam_buf_t
    subOamBuf: struct_oam_buf_t
    raceMode: int

class rnet_aid_map_t(Structure):
    """
    ```python
    driverToAid: list[int] (POINTER(b)[4])
    initialAids: int (POINTER(B))
    initialized: int (POINTER(B))
    aidToDriver: list[int] (POINTER(b)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    driverToAid: list[int]
    initialAids: int
    initialized: int
    aidToDriver: list[int]

class rnet_dgram_t(Structure):
    """
    ```python
    src: int (POINTER(B))
    dst: int (POINTER(B))
    op: int (POINTER(B))
    field1: int (POINTER(B))
    field2: int (POINTER(B))
    field3: int (POINTER(B))
    data: list[int] (POINTER(B)[104])
    ```
    """
    _pack_: ClassVar[int] = 1
    src: int
    dst: int
    op: int
    field1: int
    field2: int
    field3: int
    data: list[int]

class rnet_driver_item_action_buffer_t(Structure):
    """
    ```python
    itemActions: list[int] (POINTER(B)[16])
    itemEventData: list[int] (POINTER(B)[48])
    ```
    """
    _pack_: ClassVar[int] = 1
    itemActions: list[int]
    itemEventData: list[int]

class rnet_driver_state_field20_t(Structure):
    """
    ```python
    field1: int (POINTER(H))
    field2: int (POINTER(H))
    field3: int (POINTER(H))
    field4: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    field1: int
    field2: int
    field3: int
    field4: int

class rnet_driver_state_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    raceProgress: int (POINTER(I))
    state: struct_struc_351 (struct_struc_351)
    field20: list[struct_rnet_driver_state_field20_t_] (struct_rnet_driver_state_field20_t_[4])
    itemActionsBuffer: struct_rnet_driver_item_action_buffer_t_ (struct_rnet_driver_item_action_buffer_t_)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    raceProgress: int
    state: struct_struc_351
    field20: list[struct_rnet_driver_state_field20_t_]
    itemActionsBuffer: struct_rnet_driver_item_action_buffer_t_

class rnet_item_action_entry_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    buffer: c_void_p (c_void_p)
    filled: int (POINTER(B))
    item: int (POINTER(B))
    action: int (POINTER(B))
    size: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    buffer: c_void_p
    filled: int
    item: int
    action: int
    size: int

class rnet_packet_sync_t(Structure):
    """
    ```python
    srcAid: int (POINTER(H))
    gap2: list[int] (POINTER(B)[2])
    PADDING_0: list[int] (POINTER(B)[4])
    field4: int (POINTER(L))
    fieldC: int (POINTER(L))
    field14: int (POINTER(L))
    field1C: int (POINTER(I))
    field20: int (POINTER(I))
    field24: int (POINTER(I))
    PADDING_1: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    srcAid: int
    gap2: list[int]
    PADDING_0: list[int]
    field4: int
    fieldC: int
    field14: int
    field1C: int
    field20: int
    field24: int
    PADDING_1: list[int]

class rnet_ping_t(Structure):
    """
    ```python
    data: struct_rnet_packet_sync_t_ (struct_rnet_packet_sync_t_)
    field28: list[int] (POINTER(I)[2])
    field30: int (POINTER(I))
    field34: int (POINTER(B))
    field35: int (POINTER(B))
    field36: int (POINTER(B))
    field37: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    data: struct_rnet_packet_sync_t_
    field28: list[int]
    field30: int
    field34: int
    field35: int
    field36: int
    field37: int

class rotcyl_params_t(Structure):
    """
    ```python
    isXZFloor: int (POINTER(i))
    sizeX: fx32 (struct_fx32)
    sizeY: fx32 (struct_fx32)
    type: int (POINTER(I))
    dcolFloorThreshold: int (POINTER(I))
    dcolField138: int (POINTER(I))
    sfxId: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    isXZFloor: int
    sizeX: fx32
    sizeY: fx32
    type: int
    dcolFloorThreshold: int
    dcolField138: int
    sfxId: int

class rotcyl_t(Structure):
    """
    ```python
    dcol: struct_dcol_inst_t (struct_dcol_inst_t)
    startStopDuration: int (POINTER(H))
    rotateDuration: int (POINTER(H))
    idleDuration: int (POINTER(H))
    rotYVelocity: int (POINTER(h))
    velocityProgress: fx32 (struct_fx32)
    startStopSpeed: fx32 (struct_fx32)
    field154: int (POINTER(I))
    type: int (POINTER(I))
    sfxId: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    dcol: struct_dcol_inst_t
    startStopDuration: int
    rotateDuration: int
    idleDuration: int
    rotYVelocity: int
    velocityProgress: fx32
    startStopSpeed: fx32
    field154: int
    type: int
    sfxId: int

class rotdiemobj_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    dieMinY: fx32 (struct_fx32)
    dieYAccel: fx32 (struct_fx32)
    dieRotZDir: int (POINTER(i))
    dieRotZ: int (POINTER(H))
    dieRotZSpeed: int (POINTER(H))
    dieInitialYVelo: fx32 (struct_fx32)
    fieldB4: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    dieMinY: fx32
    dieYAccel: fx32
    dieRotZDir: int
    dieRotZ: int
    dieRotZSpeed: int
    dieInitialYVelo: fx32
    fieldB4: fx32

class rptc_col_effect_t(Structure):
    """
    ```python
    variants: list[struct_rptc_col_effect_variant_t] (struct_rptc_col_effect_variant_t[2])
    func: Callable[[POINTER_T[struct_rptc_col_effect_variant_t], int, POINTER_T[struct_driver_t]], c_int] (CFunctionType)
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    variants: list[struct_rptc_col_effect_variant_t]
    func: Callable[[POINTER_T[struct_rptc_col_effect_variant_t], int, POINTER_T[struct_driver_t]], c_int]
    field1C: int

class rptc_col_effect_variant_t(Structure):
    """
    ```python
    emitterCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    emitterIds: list[int] (POINTER(I)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    emitterCount: int
    PADDING_0: list[int]
    emitterIds: list[int]

class rptc_driver_effect_controller_t(Structure):
    """
    ```python
    emitterId: int (POINTER(i))
    tireEmitterIds: list[int] (POINTER(i)[2])
    emitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    tireEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2][2])
    field20: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    wallLeafEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    bulletBillEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    electricEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    tireEmitterPositions: list[struct_VecFx32] (struct_VecFx32[2])
    tireEmitterAxes: list[struct_VecFx16] (struct_VecFx16[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    emitterId: int
    tireEmitterIds: list[int]
    emitter: POINTER_T[struct_spa_emitter_t]
    tireEmitters: list[POINTER_T[struct_spa_emitter_t]]
    field20: list[POINTER_T[struct_spa_emitter_t]]
    wallLeafEmitter: POINTER_T[struct_spa_emitter_t]
    bulletBillEmitter: POINTER_T[struct_spa_emitter_t]
    electricEmitter: POINTER_T[struct_spa_emitter_t]
    tireEmitterPositions: list[struct_VecFx32]
    tireEmitterAxes: list[struct_VecFx16]

class rptc_rainbow_effect_t(Structure):
    """
    ```python
    emitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    emitters: list[POINTER_T[struct_spa_emitter_t]]

class sanbo_part_t(Structure):
    """
    ```python
    dieingPosition: struct_VecFx32 (struct_VecFx32)
    dieingVelocity: struct_VecFx32 (struct_VecFx32)
    scaleXY: fx32 (struct_fx32)
    rotZSinThing: struct_sinthing_t (struct_sinthing_t)
    rotZ: int (POINTER(i))
    rotZSpeed: int (POINTER(i))
    wiggleWaitCounter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    dieingPosition: struct_VecFx32
    dieingVelocity: struct_VecFx32
    scaleXY: fx32
    rotZSinThing: struct_sinthing_t
    rotZ: int
    rotZSpeed: int
    wiggleWaitCounter: int

class sanbo_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    pwWaitCounter: int (POINTER(i))
    hitTimeout: int (POINTER(i))
    resurrectionWaitCounter: int (POINTER(i))
    sfxTimeout: int (POINTER(i))
    bodyParts: list[struct_sanbo_part_t] (struct_sanbo_part_t[4])
    bodyPartCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    pwSpeed: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    pwWaitCounter: int
    hitTimeout: int
    resurrectionWaitCounter: int
    sfxTimeout: int
    bodyParts: list[struct_sanbo_part_t]
    bodyPartCount: int
    PADDING_0: list[int]
    pwSpeed: fx32
    pathwalker: struct_pw_pathwalker_t
    state: int

class save_core_t(Structure):
    """
    ```python
    status: int (POINTER(I))
    error: int (POINTER(I))
    backupLock: int (POINTER(I))
    isEnabled: int (POINTER(i))
    isBusy: int (POINTER(i))
    transferType: int (POINTER(I))
    backupSrcDst: int (POINTER(I))
    originalError: int (POINTER(I))
    originalSrcDst: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    originalTimestamp: int (POINTER(H))
    field26: int (POINTER(H))
    readDst: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    readSrc: int (POINTER(I))
    readLen: int (POINTER(I))
    readBlockSignature: int (POINTER(I))
    readBlockIsHeader: int (POINTER(i))
    field3C: int (POINTER(I))
    writeSrc: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    writeDst: int (POINTER(I))
    writeLength: int (POINTER(I))
    field4C: int (POINTER(I))
    writeBlockIsHeader: int (POINTER(i))
    callbackArg: c_void_p (c_void_p)
    field58: int (POINTER(I))
    field5C: int (POINTER(I))
    tmpBuf: c_void_p (c_void_p)
    testByte: c_void_p (c_void_p)
    realDst: int (POINTER(I))
    field6C: int (POINTER(B))
    field6D: int (POINTER(B))
    field6E: int (POINTER(B))
    field6F: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    status: int
    error: int
    backupLock: int
    isEnabled: int
    isBusy: int
    transferType: int
    backupSrcDst: int
    originalError: int
    originalSrcDst: POINTER_T[c_ubyte]
    originalTimestamp: int
    field26: int
    readDst: POINTER_T[c_ubyte]
    readSrc: int
    readLen: int
    readBlockSignature: int
    readBlockIsHeader: int
    field3C: int
    writeSrc: POINTER_T[c_ubyte]
    writeDst: int
    writeLength: int
    field4C: int
    writeBlockIsHeader: int
    callbackArg: c_void_p
    field58: int
    field5C: int
    tmpBuf: c_void_p
    testByte: c_void_p
    realDst: int
    field6C: int
    field6D: int
    field6E: int
    field6F: int

class save_data_t(Structure):
    """
    ```python
    nksy: POINTER_T[struct_nksy_t] (POINTER(struct_nksy_t))
    nkem: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    nkgp: int (POINTER(I))
    nkta: int (POINTER(I))
    nkmr: int (POINTER(I))
    nkpg: POINTER_T[struct_nkpg_t] (POINTER(struct_nkpg_t))
    nkdg: POINTER_T[struct_nkdg_t] (POINTER(struct_nkdg_t))
    staffGhost: POINTER_T[struct_nkdg_t] (POINTER(struct_nkdg_t))
    nkfl: int (POINTER(I))
    nkfe: int (POINTER(I))
    isBusy: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    blockErrorFlags: int (POINTER(H))
    error: int (POINTER(I))
    field30: list[int] (POINTER(B)[4])
    field34: list[int] (POINTER(B)[4])
    field38: int (POINTER(B))
    field39: int (POINTER(B))
    unk3A: list[int] (POINTER(B)[2])
    field3C: int (POINTER(B))
    unk3D: list[int] (POINTER(B)[3])
    field40: int (POINTER(I))
    field44: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    nksy: POINTER_T[struct_nksy_t]
    nkem: POINTER_T[c_ubyte]
    nkgp: int
    nkta: int
    nkmr: int
    nkpg: POINTER_T[struct_nkpg_t]
    nkdg: POINTER_T[struct_nkdg_t]
    staffGhost: POINTER_T[struct_nkdg_t]
    nkfl: int
    nkfe: int
    isBusy: int
    PADDING_0: int
    blockErrorFlags: int
    error: int
    field30: list[int]
    field34: list[int]
    field38: int
    field39: int
    unk3A: list[int]
    field3C: int
    unk3D: list[int]
    field40: int
    field44: int

class sblln_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    scale: fx32 (struct_fx32)
    scaleDelta: fx32 (struct_fx32)
    counter: int (POINTER(i))
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    scale: fx32
    scaleDelta: fx32
    counter: int
    driver: POINTER_T[struct_driver_t]
    state: int

class scene_def_t(Structure):
    """
    ```python
    initFunc: Callable[[POINTER_T[struct_scene_manager_t]], None] (CFunctionType)
    updateFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None] (CFunctionType)
    finalizeFunc: Callable[[POINTER_T[struct_scene_manager_t]], None] (CFunctionType)
    vblankFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None] (CFunctionType)
    preSleepFunc: Callable[[], None] (CFunctionType)
    postSleepFunc: Callable[[], None] (CFunctionType)
    fadeInLength: int (POINTER(h))
    fadeOutLength: int (POINTER(h))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    initFunc: Callable[[POINTER_T[struct_scene_manager_t]], None]
    updateFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None]
    finalizeFunc: Callable[[POINTER_T[struct_scene_manager_t]], None]
    vblankFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None]
    preSleepFunc: Callable[[], None]
    postSleepFunc: Callable[[], None]
    fadeInLength: int
    fadeOutLength: int
    field1C: int

class scene_manager_t(Structure):
    """
    ```python
    previousScene: int (POINTER(h))
    currentScene: int (POINTER(h))
    nextScene: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    previousScene: int
    currentScene: int
    nextScene: int

class scene_proc_t(Structure):
    """
    ```python
    overlayId: int (POINTER(I))
    nextOverlayId: int (POINTER(I))
    sceneId: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    soundHeap: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    overlayId: int
    nextOverlayId: int
    sceneId: int
    PADDING_0: list[int]
    soundHeap: c_void_p

class scene_state_t(Structure):
    """
    ```python
    threadStack: POINTER_T[c_uint] (POINTER(POINTER(I)))
    PADDING_0: list[int] (POINTER(B)[4])
    thread: struct__OSThread (struct__OSThread)
    threadQueue: struct__OSThreadQueue (struct__OSThreadQueue)
    preSleepCallback: struct_PMiSleepCallbackInfo (struct_PMiSleepCallbackInfo)
    postSleepCallback: struct_PMiSleepCallbackInfo (struct_PMiSleepCallbackInfo)
    sceneFrameCounter: int (POINTER(i))
    totalFrameCounter: int (POINTER(i))
    curSceneDef: struct_scene_def_t (struct_scene_def_t)
    state: int (POINTER(I))
    isLcdOff: int (POINTER(i))
    gap114: list[int] (POINTER(B)[4])
    field118: int (POINTER(I))
    field11C: int (POINTER(I))
    field120: int (POINTER(b))
    gap121: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    threadStack: POINTER_T[c_uint]
    PADDING_0: list[int]
    thread: struct__OSThread
    threadQueue: struct__OSThreadQueue
    preSleepCallback: struct_PMiSleepCallbackInfo
    postSleepCallback: struct_PMiSleepCallbackInfo
    sceneFrameCounter: int
    totalFrameCounter: int
    curSceneDef: struct_scene_def_t
    state: int
    isLcdOff: int
    gap114: list[int]
    field118: int
    field11C: int
    field120: int
    gap121: list[int]

class secondhand_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    curRotation: quaternion_t (struct_quaternion_t)
    baseRotation: quaternion_t (struct_quaternion_t)
    startStopFrameCount: int (POINTER(H))
    oneDirFrameCount: int (POINTER(H))
    waitFrameCount: int (POINTER(H))
    baseVelocity: int (POINTER(h))
    velocity: fx32 (struct_fx32)
    acceleration: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    curRotation: quaternion_t
    baseRotation: quaternion_t
    startStopFrameCount: int
    oneDirFrameCount: int
    waitFrameCount: int
    baseVelocity: int
    velocity: fx32
    acceleration: fx32

class seq_handle_t(Structure):
    """
    ```python
    seqLoadInfo: struct_seq_load_info_t (struct_seq_load_info_t)
    handle: struct_NNSSndHandle (struct_NNSSndHandle)
    heapState: POINTER_T[struct_seq_heap_state_t] (POINTER(struct_seq_heap_state_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    seqLoadInfo: struct_seq_load_info_t
    handle: struct_NNSSndHandle
    heapState: POINTER_T[struct_seq_heap_state_t]

class seq_heap_state_t(Structure):
    """
    ```python
    seqLoadInfo: struct_seq_load_info_t (struct_seq_load_info_t)
    heapLevel: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    seqLoadInfo: struct_seq_load_info_t
    heapLevel: int

class seq_load_info_t(Structure):
    """
    ```python
    seqId: int (POINTER(I))
    bank1: int (POINTER(I))
    bank2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    seqId: int
    bank1: int
    bank2: int

class sfsn_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    state1Counter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    state0Counter: int (POINTER(i))
    spawnPos: struct_VecFx32 (struct_VecFx32)
    angle: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    state: int (POINTER(I))
    ptclEmitterA: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ptclEmitterB: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    state1Counter: int
    PADDING_0: list[int]
    state0Counter: int
    spawnPos: struct_VecFx32
    angle: int
    PADDING_1: list[int]
    state: int
    ptclEmitterA: POINTER_T[struct_spa_emitter_t]
    ptclEmitterB: POINTER_T[struct_spa_emitter_t]

class sfx_base_params_t(Structure):
    """
    ```python
    maxDistance: int (POINTER(I))
    fadePart1EndDistance: int (POINTER(I))
    fadePart1EndVolume: int (POINTER(I))
    fadeStartDistance: int (POINTER(I))
    maxVolume: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    maxDistance: int
    fadePart1EndDistance: int
    fadePart1EndVolume: int
    fadeStartDistance: int
    maxVolume: int

class sfx_emitter_ex_params_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    pitchOffset: int (POINTER(I))
    fieldC: int (POINTER(I))
    unk10: list[int] (POINTER(B)[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    pitchOffset: int
    fieldC: int
    unk10: list[int]

class sfx_emitter_ex_t(Structure):
    """
    ```python
    emitter: struct_sfx_emitter_t (struct_sfx_emitter_t)
    exParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    emitter: struct_sfx_emitter_t
    exParams: struct_sfx_emitter_ex_params_t

class sfx_emitter_t(Structure):
    """
    ```python
    listLink: struct_list_link_t (struct_list_link_t)
    soundList: struct_NNSFndList (struct_NNSFndList)
    field18: int (POINTER(I))
    field1C: struct_list_link_t (struct_list_link_t)
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    startFunc: c_void_p (c_void_p)
    updateFunc: c_void_p (c_void_p)
    field34: int (POINTER(H))
    field36: int (POINTER(H))
    field38: int (POINTER(I))
    sfxParamIdx: int (POINTER(B))
    field3D: list[int] (POINTER(B)[3])
    squareDistance: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    listLink: struct_list_link_t
    soundList: struct_NNSFndList
    field18: int
    field1C: struct_list_link_t
    position: POINTER_T[struct_VecFx32]
    startFunc: c_void_p
    updateFunc: c_void_p
    field34: int
    field36: int
    field38: int
    sfxParamIdx: int
    field3D: list[int]
    squareDistance: int

class sfx_params_t(Structure):
    """
    ```python
    maxDistance: int (POINTER(i))
    fadePart1EndDistance: int (POINTER(i))
    fadePart1EndVolume: int (POINTER(I))
    fadeStartDistance: int (POINTER(i))
    maxVolume: int (POINTER(i))
    fadePart1Factor: fx32 (struct_fx32)
    fadePart2Factor: fx32 (struct_fx32)
    field1C: int (POINTER(I))
    maxDistanceSquare: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    maxDistance: int
    fadePart1EndDistance: int
    fadePart1EndVolume: int
    fadeStartDistance: int
    maxVolume: int
    fadePart1Factor: fx32
    fadePart2Factor: fx32
    field1C: int
    maxDistanceSquare: int

class sfx_sound_t(Structure):
    """
    ```python
    poolHandle: struct_sp_handle_t (struct_sp_handle_t)
    listLink: struct_list_link_t (struct_list_link_t)
    pitch: int (POINTER(h))
    sfxId: int (POINTER(H))
    seqArcId: int (POINTER(B))
    field19: int (POINTER(B))
    volume: int (POINTER(B))
    field1B: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    poolHandle: struct_sp_handle_t
    listLink: struct_list_link_t
    pitch: int
    sfxId: int
    seqArcId: int
    field19: int
    volume: int
    field1B: int

class shadowmodel_t(Structure):
    """
    ```python
    model: struct_model_t (struct_model_t)
    polygonId: int (POINTER(H))
    alpha: int (POINTER(H))
    flags: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    model: struct_model_t
    polygonId: int
    alpha: int
    flags: int
    PADDING_0: list[int]

class shinc_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    hasSpawned: int (POINTER(i))
    fieldA4: int (POINTER(I))
    counter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    hasSpawned: int
    fieldA4: int
    counter: int

class sinthing_t(Structure):
    """
    ```python
    phase: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    value: fx32 (struct_fx32)
    velocity: fx32 (struct_fx32)
    baseOffset: fx32 (struct_fx32)
    amplitude: fx32 (struct_fx32)
    amplitudeVelocity: fx32 (struct_fx32)
    phaseVelocity: int (POINTER(i))
    phaseAcceleration: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    phase: int
    PADDING_0: list[int]
    value: fx32
    velocity: fx32
    baseOffset: fx32
    amplitude: fx32
    amplitudeVelocity: fx32
    phaseVelocity: int
    phaseAcceleration: int

class snd_unkstruct_field0_t(Structure):
    """
    ```python
    sfxId: int (POINTER(I))
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    sfxParamsId: int (POINTER(I))
    squareDistance: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    sfxId: int
    position: POINTER_T[struct_VecFx32]
    sfxParamsId: int
    squareDistance: int

class snd_unkstruct_t(Structure):
    """
    ```python
    field0: struct_snd_unkstruct_field0_t (struct_snd_unkstruct_field0_t)
    position: struct_VecFx32 (struct_VecFx32)
    soundHandle: struct_NNSSndHandle (struct_NNSSndHandle)
    field20: int (POINTER(I))
    field24: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: struct_snd_unkstruct_field0_t
    position: struct_VecFx32
    soundHandle: struct_NNSSndHandle
    field20: int
    field24: int

class snowman_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    headRotEnabled: int (POINTER(i))
    headRotZ: int (POINTER(i))
    headRotZVelocity: int (POINTER(i))
    counter: int (POINTER(i))
    headElevationProgress: fx32 (struct_fx32)
    bottomScale: fx32 (struct_fx32)
    headElevation: fx32 (struct_fx32)
    headElevationVelocity: fx32 (struct_fx32)
    headMaxElevation: fx32 (struct_fx32)
    headMinElevation: fx32 (struct_fx32)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    headRotEnabled: int
    headRotZ: int
    headRotZVelocity: int
    counter: int
    headElevationProgress: fx32
    bottomScale: fx32
    headElevation: fx32
    headElevationVelocity: fx32
    headMaxElevation: fx32
    headMinElevation: fx32
    state: int

class sound_pool_t(Structure):
    """
    ```python
    nrElements: int (POINTER(i))
    elements1Idx: int (POINTER(I))
    elements1: c_void_p (c_void_p)
    elements: c_void_p (c_void_p)
    elementSize: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    nrElements: int
    elements1Idx: int
    elements1: c_void_p
    elements: c_void_p
    elementSize: int

class sound_var_t(Structure):
    """
    ```python
    value: int (POINTER(h))
    field2: int (POINTER(h))
    field4: int (POINTER(i))
    id: int (POINTER(b))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    value: int
    field2: int
    field4: int
    id: int
    PADDING_0: list[int]

class sp_handle_t(Structure):
    """
    ```python
    handle: struct_NNSSndHandle (struct_NNSSndHandle)
    age: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    handle: struct_NNSSndHandle
    age: int

class spa_emitter_data_t(Structure):
    """
    ```python
    resource: POINTER_T[struct_spa_res_emitter_t] (POINTER(struct_spa_res_emitter_t))
    scaleAnim: POINTER_T[struct_spa_res_emitter_scaleanim_t] (POINTER(struct_spa_res_emitter_scaleanim_t))
    colorAnim: POINTER_T[struct_spa_res_emitter_coloranim_t] (POINTER(struct_spa_res_emitter_coloranim_t))
    alphaAnim: POINTER_T[struct_spa_res_emitter_alphaanim_t] (POINTER(struct_spa_res_emitter_alphaanim_t))
    texAnim: POINTER_T[struct_spa_res_emitter_texanim_t] (POINTER(struct_spa_res_emitter_texanim_t))
    childData: POINTER_T[struct_spa_res_emitter_child_t] (POINTER(struct_spa_res_emitter_child_t))
    fieldFuncs: POINTER_T[struct_spa_transform_func_arg_pair_t] (POINTER(struct_spa_transform_func_arg_pair_t))
    fieldFuncCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    resource: POINTER_T[struct_spa_res_emitter_t]
    scaleAnim: POINTER_T[struct_spa_res_emitter_scaleanim_t]
    colorAnim: POINTER_T[struct_spa_res_emitter_coloranim_t]
    alphaAnim: POINTER_T[struct_spa_res_emitter_alphaanim_t]
    texAnim: POINTER_T[struct_spa_res_emitter_texanim_t]
    childData: POINTER_T[struct_spa_res_emitter_child_t]
    fieldFuncs: POINTER_T[struct_spa_transform_func_arg_pair_t]
    fieldFuncCount: int
    PADDING_0: list[int]

class spa_emitter_t(Structure):
    """
    ```python
    listLink: struct_spa_list_link_t (struct_spa_list_link_t)
    mainParticleList: struct_spa_list_t (struct_spa_list_t)
    childParticleList: struct_spa_list_t (struct_spa_list_t)
    emitterData: POINTER_T[struct_spa_emitter_data_t] (POINTER(struct_spa_emitter_data_t))
    _0: union_spa_emitter_t_0 (union_spa_emitter_t_0)
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    particleVelocity: struct_VecFx32 (struct_VecFx32)
    age: int (POINTER(H))
    lastEmissionFraction: fx16 (struct_fx16)
    axis: struct_VecFx16 (struct_VecFx16)
    particleRotation: int (POINTER(H))
    emissionCount: fx32 (struct_fx32)
    radius: fx32 (struct_fx32)
    length: fx32 (struct_fx32)
    particlePosVeloMag: fx32 (struct_fx32)
    particleAxisVeloMag: fx32 (struct_fx32)
    particleScale: fx32 (struct_fx32)
    particleLifetime: int (POINTER(H))
    color: int (POINTER(H))
    collisionPlaneYOverride: fx32 (struct_fx32)
    texS: fx16 (struct_fx16)
    texT: fx16 (struct_fx16)
    childTexS: fx16 (struct_fx16)
    childTexT: fx16 (struct_fx16)
    emissionInterval: int (POINTER(I))
    particleAlpha: int (POINTER(I))
    updateMoment: int (POINTER(I))
    field80Unk2: int (POINTER(I))
    axisRight: struct_VecFx16 (struct_VecFx16)
    axisUp: struct_VecFx16 (struct_VecFx16)
    callbackFunc: Callable[[POINTER_T[struct_spa_emitter_t], int], None] (CFunctionType)
    userData: int (POINTER(I))
    _1: union_spa_emitter_t_1 (union_spa_emitter_t_1)
    ```
    """
    _pack_: ClassVar[int] = 1
    listLink: struct_spa_list_link_t
    mainParticleList: struct_spa_list_t
    childParticleList: struct_spa_list_t
    emitterData: POINTER_T[struct_spa_emitter_data_t]
    _0: union_spa_emitter_t_0
    position: struct_VecFx32
    velocity: struct_VecFx32
    particleVelocity: struct_VecFx32
    age: int
    lastEmissionFraction: fx16
    axis: struct_VecFx16
    particleRotation: int
    emissionCount: fx32
    radius: fx32
    length: fx32
    particlePosVeloMag: fx32
    particleAxisVeloMag: fx32
    particleScale: fx32
    particleLifetime: int
    color: int
    collisionPlaneYOverride: fx32
    texS: fx16
    texT: fx16
    childTexS: fx16
    childTexT: fx16
    emissionInterval: int
    particleAlpha: int
    updateMoment: int
    field80Unk2: int
    axisRight: struct_VecFx16
    axisUp: struct_VecFx16
    callbackFunc: Callable[[POINTER_T[struct_spa_emitter_t], int], None]
    userData: int
    _1: union_spa_emitter_t_1

class spa_list_link_t(Structure):
    """
    ```python
    next: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    prev: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: POINTER_T[struct_spa_list_link_t]
    prev: POINTER_T[struct_spa_list_link_t]

class spa_list_t(Structure):
    """
    ```python
    head: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    count: int (POINTER(I))
    tail: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    head: POINTER_T[struct_spa_list_link_t]
    count: int
    tail: POINTER_T[struct_spa_list_link_t]

class spa_particle_t(Structure):
    """
    ```python
    listLink: struct_spa_list_link_t (struct_spa_list_link_t)
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    rotation: int (POINTER(H))
    rotationVelocity: int (POINTER(h))
    maxAge: int (POINTER(H))
    age: int (POINTER(H))
    progressSpeedLoop: int (POINTER(H))
    progressSpeedNoLoop: int (POINTER(H))
    textureId: int (POINTER(B))
    progressOffset: int (POINTER(B))
    baseAlpha: int (POINTER(H))
    alpha: int (POINTER(H))
    polygonId: int (POINTER(H))
    baseScale: fx32 (struct_fx32)
    scale: fx16 (struct_fx16)
    color: int (POINTER(H))
    basePosition: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    listLink: struct_spa_list_link_t
    position: struct_VecFx32
    velocity: struct_VecFx32
    rotation: int
    rotationVelocity: int
    maxAge: int
    age: int
    progressSpeedLoop: int
    progressSpeedNoLoop: int
    textureId: int
    progressOffset: int
    baseAlpha: int
    alpha: int
    polygonId: int
    baseScale: fx32
    scale: fx16
    color: int
    basePosition: struct_VecFx32

class spa_particleset_t(Structure):
    """
    ```python
    allocFunc: Callable[[int], c_void_p] (CFunctionType)
    activeEmitterList: struct_spa_list_t (struct_spa_list_t)
    freeEmitterList: struct_spa_list_t (struct_spa_list_t)
    freeParticleList: struct_spa_list_t (struct_spa_list_t)
    emitterData: POINTER_T[struct_spa_emitter_data_t] (POINTER(struct_spa_emitter_data_t))
    textureData: POINTER_T[struct_spa_texture_data_t] (POINTER(struct_spa_texture_data_t))
    resEmitterCount: int (POINTER(H))
    resTexCount: int (POINTER(H))
    maxEmitterCount: int (POINTER(H))
    maxParticleCount: int (POINTER(H))
    firstPolygonId: int (POINTER(I))
    lastPolygonId: int (POINTER(I))
    curPolygonId: int (POINTER(I))
    constPolygonId: int (POINTER(I))
    reverseRenderOrder: int (POINTER(I))
    unknown: int (POINTER(I))
    polygonAttr: int (POINTER(I))
    curEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    cameraMtx: POINTER_T[union_MtxFx43] (POINTER(union_MtxFx43))
    frameIndex: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    allocFunc: Callable[[int], c_void_p]
    activeEmitterList: struct_spa_list_t
    freeEmitterList: struct_spa_list_t
    freeParticleList: struct_spa_list_t
    emitterData: POINTER_T[struct_spa_emitter_data_t]
    textureData: POINTER_T[struct_spa_texture_data_t]
    resEmitterCount: int
    resTexCount: int
    maxEmitterCount: int
    maxParticleCount: int
    firstPolygonId: int
    lastPolygonId: int
    curPolygonId: int
    constPolygonId: int
    reverseRenderOrder: int
    unknown: int
    polygonAttr: int
    curEmitter: POINTER_T[struct_spa_emitter_t]
    cameraMtx: POINTER_T[union_MtxFx43]
    frameIndex: int
    PADDING_0: list[int]

class spa_res_emitter_alphaanim_t(Structure):
    """
    ```python
    initialAlpha: int (POINTER(H))
    peakAlpha: int (POINTER(H))
    endingAlpha: int (POINTER(H))
    _3: int (POINTER(H))
    randomness: int (POINTER(H))
    loop: int (POINTER(H))
    _6: int (POINTER(H))
    inCompletedTiming: int (POINTER(H))
    outStartTiming: int (POINTER(B))
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    initialAlpha: int
    peakAlpha: int
    endingAlpha: int
    _3: int
    randomness: int
    loop: int
    _6: int
    inCompletedTiming: int
    outStartTiming: int
    padding: int

class spa_res_emitter_child_t(Structure):
    """
    ```python
    applyEmitterField: int (POINTER(H))
    useScaleAnim: int (POINTER(H))
    hasAlphaFade: int (POINTER(H))
    rotInheritMode: int (POINTER(H))
    followEmitter: int (POINTER(H))
    useChildColor: int (POINTER(H))
    particleType: int (POINTER(H))
    rotMtxMode: int (POINTER(H))
    quadDirection: int (POINTER(H))
    _9: int (POINTER(H))
    initVelocityRandomness: int (POINTER(h))
    targetScale: fx16 (struct_fx16)
    lifeTime: int (POINTER(H))
    velocityInheritRatio: int (POINTER(B))
    scale: int (POINTER(B))
    color: int (POINTER(H))
    emissionVolume: int (POINTER(B))
    emissionTime: int (POINTER(B))
    emissionInterval: int (POINTER(B))
    textureId: int (POINTER(B))
    texRepeatShiftS: int (POINTER(I))
    texRepeatShiftT: int (POINTER(I))
    texFlipS: int (POINTER(I))
    texFlipT: int (POINTER(I))
    centerDirPolygon: int (POINTER(I))
    _25: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    applyEmitterField: int
    useScaleAnim: int
    hasAlphaFade: int
    rotInheritMode: int
    followEmitter: int
    useChildColor: int
    particleType: int
    rotMtxMode: int
    quadDirection: int
    _9: int
    initVelocityRandomness: int
    targetScale: fx16
    lifeTime: int
    velocityInheritRatio: int
    scale: int
    color: int
    emissionVolume: int
    emissionTime: int
    emissionInterval: int
    textureId: int
    texRepeatShiftS: int
    texRepeatShiftT: int
    texFlipS: int
    texFlipT: int
    centerDirPolygon: int
    _25: int

class spa_res_emitter_coloranim_t(Structure):
    """
    ```python
    initialColor: int (POINTER(H))
    endingColor: int (POINTER(H))
    inCompletedTiming: int (POINTER(B))
    peakTiming: int (POINTER(B))
    outStartTiming: int (POINTER(B))
    field7: int (POINTER(B))
    isRandom: int (POINTER(H))
    loop: int (POINTER(H))
    interpolate: int (POINTER(H))
    _9: int (POINTER(H))
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    initialColor: int
    endingColor: int
    inCompletedTiming: int
    peakTiming: int
    outStartTiming: int
    field7: int
    isRandom: int
    loop: int
    interpolate: int
    _9: int
    padding: int

class spa_res_emitter_field_collision_t(Structure):
    """
    ```python
    collisionPlaneY: fx32 (struct_fx32)
    bounceCoef: fx16 (struct_fx16)
    behavior: int (POINTER(H))
    _3: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    collisionPlaneY: fx32
    bounceCoef: fx16
    behavior: int
    _3: int

class spa_res_emitter_field_convergence_t(Structure):
    """
    ```python
    convergencePos: struct_VecFx32 (struct_VecFx32)
    convergenceRatio: fx16 (struct_fx16)
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    convergencePos: struct_VecFx32
    convergenceRatio: fx16
    padding: int

class spa_res_emitter_field_gravity_t(Structure):
    """
    ```python
    gravity: struct_VecFx16 (struct_VecFx16)
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    gravity: struct_VecFx16
    padding: int

class spa_res_emitter_field_magnet_t(Structure):
    """
    ```python
    magnetPos: struct_VecFx32 (struct_VecFx32)
    magnetPower: fx16 (struct_fx16)
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magnetPos: struct_VecFx32
    magnetPower: fx16
    padding: int

class spa_res_emitter_field_random_t(Structure):
    """
    ```python
    strength: struct_VecFx16 (struct_VecFx16)
    interval: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    strength: struct_VecFx16
    interval: int

class spa_res_emitter_field_spin_t(Structure):
    """
    ```python
    rotation: int (POINTER(H))
    type: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    rotation: int
    type: int

class spa_res_emitter_flags_t(Structure):
    """
    ```python
    emitterShape: int (POINTER(I))
    particleType: int (POINTER(I))
    axisDirType: int (POINTER(I))
    hasScaleAnim: int (POINTER(I))
    hasColorAnim: int (POINTER(I))
    hasAlphaAnim: int (POINTER(I))
    hasTexAnim: int (POINTER(I))
    hasRandomParticleDeltaRotation: int (POINTER(I))
    hasRandomParticleRotation: int (POINTER(I))
    emitterIsOneTime: int (POINTER(I))
    particlesFollowEmitter: int (POINTER(I))
    hasChildParticles: int (POINTER(I))
    rotMtxMode: int (POINTER(I))
    quadDirection: int (POINTER(I))
    randomizeParticleProgressOffset: int (POINTER(I))
    renderChildParticlesFirst: int (POINTER(I))
    dontRenderMainParticles: int (POINTER(I))
    relativePosAsRotOrigin: int (POINTER(I))
    hasFieldGravity: int (POINTER(I))
    hasFieldRandom: int (POINTER(I))
    hasFieldMagnetic: int (POINTER(I))
    hasFieldSpin: int (POINTER(I))
    hasFieldCollision: int (POINTER(I))
    hasFieldConvergence: int (POINTER(I))
    useConstPolygonIdForMainParticles: int (POINTER(I))
    useConstPolygonIdForChildParticles: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    emitterShape: int
    particleType: int
    axisDirType: int
    hasScaleAnim: int
    hasColorAnim: int
    hasAlphaAnim: int
    hasTexAnim: int
    hasRandomParticleDeltaRotation: int
    hasRandomParticleRotation: int
    emitterIsOneTime: int
    particlesFollowEmitter: int
    hasChildParticles: int
    rotMtxMode: int
    quadDirection: int
    randomizeParticleProgressOffset: int
    renderChildParticlesFirst: int
    dontRenderMainParticles: int
    relativePosAsRotOrigin: int
    hasFieldGravity: int
    hasFieldRandom: int
    hasFieldMagnetic: int
    hasFieldSpin: int
    hasFieldCollision: int
    hasFieldConvergence: int
    useConstPolygonIdForMainParticles: int
    useConstPolygonIdForChildParticles: int

class spa_res_emitter_scaleanim_t(Structure):
    """
    ```python
    initialScale: fx16 (struct_fx16)
    intermediateScale: fx16 (struct_fx16)
    endingScale: fx16 (struct_fx16)
    inCompletedTiming: int (POINTER(B))
    scaleOutStartTime: int (POINTER(B))
    loop: int (POINTER(H))
    _6: int (POINTER(H))
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    initialScale: fx16
    intermediateScale: fx16
    endingScale: fx16
    inCompletedTiming: int
    scaleOutStartTime: int
    loop: int
    _6: int
    padding: int

class spa_res_emitter_t(Structure):
    """
    ```python
    flags: struct_spa_res_emitter_flags_t (struct_spa_res_emitter_flags_t)
    position: struct_VecFx32 (struct_VecFx32)
    emissionCount: fx32 (struct_fx32)
    emitterRadius: fx32 (struct_fx32)
    emitterLength: fx32 (struct_fx32)
    emitterAxis: struct_VecFx16 (struct_VecFx16)
    color: int (POINTER(H))
    particlePosVeloMag: fx32 (struct_fx32)
    particleAxisVeloMag: fx32 (struct_fx32)
    particleBaseScale: fx32 (struct_fx32)
    aspectRatio: fx16 (struct_fx16)
    emissionStartTime: int (POINTER(H))
    minRotVelocity: int (POINTER(h))
    maxRotVelocity: int (POINTER(h))
    particleRotation: int (POINTER(H))
    padding1: int (POINTER(H))
    emissionTime: int (POINTER(H))
    particleLifetime: int (POINTER(H))
    particleScaleRandomness: int (POINTER(B))
    particleLifetimeRandomness: int (POINTER(B))
    particleVeloMagRandomness: int (POINTER(B))
    padding2: int (POINTER(B))
    emissionInterval: int (POINTER(B))
    particleAlpha: int (POINTER(B))
    airResistance: int (POINTER(B))
    textureId: int (POINTER(B))
    loopFrame: int (POINTER(L))
    dirBillboardScale: int (POINTER(L))
    texRepeatShiftS: int (POINTER(L))
    texRepeatShiftT: int (POINTER(L))
    scaleMode: int (POINTER(L))
    centerDirPolygon: int (POINTER(L))
    texFlipS: int (POINTER(L))
    texFlipT: int (POINTER(L))
    _34: int (POINTER(L))
    quadXOffset: fx16 (struct_fx16)
    quadYZOffset: fx16 (struct_fx16)
    _0: union_spa_res_emitter_t_0 (union_spa_res_emitter_t_0)
    ```
    """
    _pack_: ClassVar[int] = 1
    flags: struct_spa_res_emitter_flags_t
    position: struct_VecFx32
    emissionCount: fx32
    emitterRadius: fx32
    emitterLength: fx32
    emitterAxis: struct_VecFx16
    color: int
    particlePosVeloMag: fx32
    particleAxisVeloMag: fx32
    particleBaseScale: fx32
    aspectRatio: fx16
    emissionStartTime: int
    minRotVelocity: int
    maxRotVelocity: int
    particleRotation: int
    padding1: int
    emissionTime: int
    particleLifetime: int
    particleScaleRandomness: int
    particleLifetimeRandomness: int
    particleVeloMagRandomness: int
    padding2: int
    emissionInterval: int
    particleAlpha: int
    airResistance: int
    textureId: int
    loopFrame: int
    dirBillboardScale: int
    texRepeatShiftS: int
    texRepeatShiftT: int
    scaleMode: int
    centerDirPolygon: int
    texFlipS: int
    texFlipT: int
    _34: int
    quadXOffset: fx16
    quadYZOffset: fx16
    _0: union_spa_res_emitter_t_0

class spa_res_emitter_texanim_t(Structure):
    """
    ```python
    frames: list[int] (POINTER(B)[8])
    frameCount: int (POINTER(I))
    frameDuration: int (POINTER(I))
    isRandom: int (POINTER(I))
    loop: int (POINTER(I))
    _5: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    frames: list[int]
    frameCount: int
    frameDuration: int
    isRandom: int
    loop: int
    _5: int

class spa_res_header_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    version: int (POINTER(I))
    emitterCount: int (POINTER(H))
    textureCount: int (POINTER(H))
    fieldC: int (POINTER(I))
    emitterBlockLength: int (POINTER(I))
    textureBlockLength: int (POINTER(I))
    textureBlockOffset: int (POINTER(I))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    version: int
    emitterCount: int
    textureCount: int
    fieldC: int
    emitterBlockLength: int
    textureBlockLength: int
    textureBlockOffset: int
    field1C: int

class spa_res_texture_params_t(Structure):
    """
    ```python
    format: int (POINTER(I))
    width: int (POINTER(I))
    height: int (POINTER(I))
    repeat: int (POINTER(I))
    flip: int (POINTER(I))
    pltt0Transparent: int (POINTER(I))
    refTexData: int (POINTER(I))
    refTexId: int (POINTER(I))
    _8: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    format: int
    width: int
    height: int
    repeat: int
    flip: int
    pltt0Transparent: int
    refTexData: int
    refTexId: int
    _8: int

class spa_res_texture_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    texParams: struct_spa_res_texture_params_t (struct_spa_res_texture_params_t)
    texSize: int (POINTER(I))
    plttOffset: int (POINTER(I))
    plttSize: int (POINTER(I))
    plttIdxOffset: int (POINTER(I))
    plttIdxSize: int (POINTER(I))
    blockSize: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    texParams: struct_spa_res_texture_params_t
    texSize: int
    plttOffset: int
    plttSize: int
    plttIdxOffset: int
    plttIdxSize: int
    blockSize: int

class spa_texture_data_t(Structure):
    """
    ```python
    resource: POINTER_T[struct_spa_res_texture_t] (POINTER(struct_spa_res_texture_t))
    texVramAddr: int (POINTER(I))
    plttVramAddr: int (POINTER(I))
    texParams: struct_spa_res_texture_params_t (struct_spa_res_texture_params_t)
    width: int (POINTER(H))
    height: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    resource: POINTER_T[struct_spa_res_texture_t]
    texVramAddr: int
    plttVramAddr: int
    texParams: struct_spa_res_texture_params_t
    width: int
    height: int

class spa_transform_func_arg_pair_t(Structure):
    """
    ```python
    func: Callable[[c_void_p, POINTER_T[struct_spa_particle_t], POINTER_T[struct_VecFx32], POINTER_T[struct_spa_emitter_t]], None] (CFunctionType)
    resData: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    func: Callable[[c_void_p, POINTER_T[struct_spa_particle_t], POINTER_T[struct_VecFx32], POINTER_T[struct_spa_emitter_t]], None]
    resData: c_void_p

class spi_t(Structure):
    """
    ```python
    tpSampleBuf: list[struct_TPData] (struct_TPData[5])
    curTp: struct_TPData (struct_TPData)
    tpAutoSamplingEnabled: int (POINTER(i))
    micAutoSamplingEnabled: int (POINTER(i))
    micAutoSamplingPaused: int (POINTER(i))
    micInputDetected: int (POINTER(i))
    PADDING_0: int (POINTER(B))
    gap34: list[int] (POINTER(B)[8])
    PADDING_1: list[int] (POINTER(B)[3])
    micData: POINTER_T[struct_mic_t] (POINTER(struct_mic_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    tpSampleBuf: list[struct_TPData]
    curTp: struct_TPData
    tpAutoSamplingEnabled: int
    micAutoSamplingEnabled: int
    micAutoSamplingPaused: int
    micInputDetected: int
    PADDING_0: int
    gap34: list[int]
    PADDING_1: list[int]
    micData: POINTER_T[struct_mic_t]

class ssm_state_t(Structure):
    """
    ```python
    vblankFunc: Callable[[], None] (CFunctionType)
    renderFunc: Callable[[POINTER_T[struct_scene_manager_t]], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    vblankFunc: Callable[[], None]
    renderFunc: Callable[[POINTER_T[struct_scene_manager_t]], None]

class ssm_t(Structure):
    """
    ```python
    frameCounter: int (POINTER(i))
    changingState: int (POINTER(i))
    prevState: int (POINTER(I))
    curState: int (POINTER(I))
    nextState: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    frameCounter: int
    changingState: int
    prevState: int
    curState: int
    nextState: int

class state_machine_state_t(Structure):
    """
    ```python
    initFunc: Callable[[c_void_p], None] (CFunctionType)
    stateFunc: Callable[[c_void_p], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    initFunc: Callable[[c_void_p], None]
    stateFunc: Callable[[c_void_p], None]

class state_machine_t(Structure):
    """
    ```python
    states: POINTER_T[struct_state_machine_state_t] (POINTER(struct_state_machine_state_t))
    counter: int (POINTER(I))
    userData: c_void_p (c_void_p)
    nrStates: int (POINTER(H))
    curState: int (POINTER(H))
    nextState: int (POINTER(H))
    gotoNextState: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    states: POINTER_T[struct_state_machine_state_t]
    counter: int
    userData: c_void_p
    nrStates: int
    curState: int
    nextState: int
    gotoNextState: int

class struc_222_field_68_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    frameCounter: int (POINTER(I))
    fieldC: int (POINTER(H))
    fieldE: int (POINTER(H))
    field10: int (POINTER(I))
    field14: int (POINTER(H))
    gap16: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    frameCounter: int
    fieldC: int
    fieldE: int
    field10: int
    field14: int
    gap16: list[int]

class struc_313_mepo(Structure):
    """
    ```python
    nextMepo: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    curMepo: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    direction: struct_VecFx32 (struct_VecFx32)
    areaMepo: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    areaMepoValid: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    nextMepo: POINTER_T[struct_mdat_mgenemypoint_t]
    curMepo: POINTER_T[struct_mdat_mgenemypoint_t]
    direction: struct_VecFx32
    areaMepo: POINTER_T[struct_mdat_mgenemypoint_t]
    areaMepoValid: int

class struc_316_epoi(Structure):
    """
    ```python
    nextEpoi: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    curEpoi: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    direction: struct_VecFx32 (struct_VecFx32)
    areaEpoi: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    areaEpoiValid: int (POINTER(i))
    driverId: int (POINTER(H))
    field1E: int (POINTER(B))
    field1F: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    nextEpoi: POINTER_T[struct_mdat_enemypoint_t]
    curEpoi: POINTER_T[struct_mdat_enemypoint_t]
    direction: struct_VecFx32
    areaEpoi: POINTER_T[struct_mdat_enemypoint_t]
    areaEpoiValid: int
    driverId: int
    field1E: int
    field1F: int

class struc_334(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    field10: int (POINTER(i))
    field14: int (POINTER(i))
    field18: int (POINTER(i))
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    field10: int
    field14: int
    field18: int
    field1C: int
    field20: int
    field24: int

class struc_351(Structure):
    """
    ```python
    posX: int (POINTER(h))
    posY: int (POINTER(h))
    posZ: int (POINTER(h))
    speed: int (POINTER(h))
    driftRotY: int (POINTER(h))
    yRot: int (POINTER(H))
    flags: int (POINTER(I))
    field514field48: int (POINTER(i))
    field514field44: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    posX: int
    posY: int
    posZ: int
    speed: int
    driftRotY: int
    yRot: int
    flags: int
    field514field48: int
    field514field44: int

class struct_217AA00_field1E4C_entry_t(Structure):
    """
    ```python
    unk0: list[int] (POINTER(B)[6])
    field6: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    unk0: list[int]
    field6: int

class struct_217AA00_field45C_t(Structure):
    """
    ```python
    nickName: list[int] (POINTER(H)[10])
    emblem: list[int] (POINTER(B)[512])
    hasEmblem: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    field216: int (POINTER(H))
    exchangeToken: c_void_p (c_void_p)
    unlockBits: list[int] (POINTER(B)[4])
    field228: int (POINTER(B))
    _7: int (POINTER(B))
    field229: int (POINTER(B))
    field22A: int (POINTER(B))
    field22B: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    nickName: list[int]
    emblem: list[int]
    hasEmblem: int
    PADDING_0: int
    field216: int
    exchangeToken: c_void_p
    unlockBits: list[int]
    field228: int
    _7: int
    field229: int
    field22A: int
    field22B: int

class struct_217AA00_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    field8: int (POINTER(I))
    unkC: list[int] (POINTER(B)[1062])
    field432: int (POINTER(H))
    field434: int (POINTER(H))
    field436: int (POINTER(H))
    field438: int (POINTER(B))
    field439: int (POINTER(B))
    field43A: int (POINTER(B))
    field43B: int (POINTER(B))
    field43C: int (POINTER(B))
    unk43D: list[int] (POINTER(B)[23])
    field454: int (POINTER(H))
    field456: int (POINTER(B))
    field457: int (POINTER(B))
    field458: int (POINTER(B))
    unk459: list[int] (POINTER(B)[3])
    field45C: list[struct_struct_217AA00_field45C_t] (struct_struct_217AA00_field45C_t[8])
    unk15BC: list[int] (POINTER(B)[12])
    field15C8: POINTER_T[struct_struc_252] (POINTER(struct_struc_252))
    unk15CC: list[int] (POINTER(B)[42])
    field15F6: int (POINTER(B))
    unk15F7: list[int] (POINTER(B)[2133])
    field1E4C: list[struct_struct_217AA00_field1E4C_entry_t] (struct_struct_217AA00_field1E4C_entry_t[8])
    field1E8C: list[int] (POINTER(H)[8])
    unk1E9C: list[int] (POINTER(B)[20])
    field1EB0: int (POINTER(I))
    unk1EB4: list[int] (POINTER(B)[52])
    field1EE8: struct_MATHRandContext32 (struct_MATHRandContext32)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    unkC: list[int]
    field432: int
    field434: int
    field436: int
    field438: int
    field439: int
    field43A: int
    field43B: int
    field43C: int
    unk43D: list[int]
    field454: int
    field456: int
    field457: int
    field458: int
    unk459: list[int]
    field45C: list[struct_struct_217AA00_field45C_t]
    unk15BC: list[int]
    field15C8: POINTER_T[struct_struc_252]
    unk15CC: list[int]
    field15F6: int
    unk15F7: list[int]
    field1E4C: list[struct_struct_217AA00_field1E4C_entry_t]
    field1E8C: list[int]
    unk1E9C: list[int]
    field1EB0: int
    unk1EB4: list[int]
    field1EE8: struct_MATHRandContext32

class struct_217B488_driver_config_t(Structure):
    """
    ```python
    characterId: int (POINTER(I))
    kartId: int (POINTER(I))
    field8: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    characterId: int
    kartId: int
    field8: int

class struct_217B488_t(Structure):
    """
    ```python
    titleMenuSkipIntro: int (POINTER(I))
    field4: int (POINTER(I))
    singlePlayerMenuTarget: int (POINTER(I))
    ghostReceive: int (POINTER(i))
    field10: int (POINTER(I))
    field14: int (POINTER(I))
    unk18: int (POINTER(I))
    field1C: int (POINTER(I))
    driverConfigs: list[struct_struct_217B488_driver_config_t] (struct_struct_217B488_driver_config_t[4])
    unk50: int (POINTER(I))
    field54: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    field58: int (POINTER(I))
    playedCourses: list[int] (POINTER(I)[5])
    field70: int (POINTER(I))
    field74: int (POINTER(I))
    useDLResult: int (POINTER(i))
    playerGlobalRank: int (POINTER(i))
    gpRank: int (POINTER(I))
    cup: int (POINTER(I))
    ccMode: int (POINTER(I))
    mirrorMode: int (POINTER(I))
    playerCharacter: int (POINTER(I))
    playerKart: int (POINTER(I))
    courseTimes: list[struct_race_time_t] (struct_race_time_t[4])
    playerTotalRankPoints: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    driverCharacters: list[int] (POINTER(I)[8])
    driverKarts: list[int] (POINTER(I)[8])
    unkEC: list[int] (POINTER(B)[32])
    heyhoPaletteRows: list[int] (POINTER(I)[8])
    field12C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    titleMenuSkipIntro: int
    field4: int
    singlePlayerMenuTarget: int
    ghostReceive: int
    field10: int
    field14: int
    unk18: int
    field1C: int
    driverConfigs: list[struct_struct_217B488_driver_config_t]
    unk50: int
    field54: int
    PADDING_0: list[int]
    field58: int
    playedCourses: list[int]
    field70: int
    field74: int
    useDLResult: int
    playerGlobalRank: int
    gpRank: int
    cup: int
    ccMode: int
    mirrorMode: int
    playerCharacter: int
    playerKart: int
    courseTimes: list[struct_race_time_t]
    playerTotalRankPoints: int
    PADDING_1: list[int]
    driverCharacters: list[int]
    driverKarts: list[int]
    unkEC: list[int]
    heyhoPaletteRows: list[int]
    field12C: int

class struct_CARDRomRegion(Structure):
    """
    ```python
    offset: int (POINTER(I))
    length: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    offset: int
    length: int

class struct_CPContext(Structure):
    """
    ```python
    div_numer: int (POINTER(L))
    div_denom: int (POINTER(L))
    sqrt: int (POINTER(L))
    div_mode: int (POINTER(H))
    sqrt_mode: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    div_numer: int
    div_denom: int
    sqrt: int
    div_mode: int
    sqrt_mode: int
    PADDING_0: list[int]

class struct_FSArchive(Structure):
    """
    ```python
    name: union_FSArchive_name (union_FSArchive_name)
    next: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    prev: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    sync_q: struct__OSThreadQueue (struct__OSThreadQueue)
    stat_q: struct__OSThreadQueue (struct__OSThreadQueue)
    flag: int (POINTER(I))
    list: struct_FSFileLink (struct_FSFileLink)
    base: int (POINTER(I))
    fat: int (POINTER(I))
    fat_size: int (POINTER(I))
    fnt: int (POINTER(I))
    fnt_size: int (POINTER(I))
    fat_bak: int (POINTER(I))
    fnt_bak: int (POINTER(I))
    load_mem: c_void_p (c_void_p)
    read_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint] (CFunctionType)
    write_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint] (CFunctionType)
    table_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint] (CFunctionType)
    proc: Callable[[POINTER_T[struct_FSFile], int], c_uint] (CFunctionType)
    proc_flag: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    name: union_FSArchive_name
    next: POINTER_T[struct_FSArchive]
    prev: POINTER_T[struct_FSArchive]
    sync_q: struct__OSThreadQueue
    stat_q: struct__OSThreadQueue
    flag: int
    list: struct_FSFileLink
    base: int
    fat: int
    fat_size: int
    fnt: int
    fnt_size: int
    fat_bak: int
    fnt_bak: int
    load_mem: c_void_p
    read_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint]
    write_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint]
    table_func: Callable[[POINTER_T[struct_FSArchive], c_void_p, int, int], c_uint]
    proc: Callable[[POINTER_T[struct_FSFile], int], c_uint]
    proc_flag: int

class struct_FSCloseFileInfo(Structure):
    """
    ```python
    reserved: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    reserved: int

class struct_FSDirEntry(Structure):
    """
    ```python
    _0: union_FSDirEntry_0 (union_FSDirEntry_0)
    is_directory: int (POINTER(I))
    name_len: int (POINTER(I))
    name: list[int] (POINTER(B)[128])
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: union_FSDirEntry_0
    is_directory: int
    name_len: int
    name: list[int]

class struct_FSDirPos(Structure):
    """
    ```python
    arc: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    own_id: int (POINTER(H))
    index: int (POINTER(H))
    pos: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    arc: POINTER_T[struct_FSArchive]
    own_id: int
    index: int
    pos: int

class struct_FSFile(Structure):
    """
    ```python
    link: struct_FSFileLink (struct_FSFileLink)
    arc: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    stat: int (POINTER(I))
    command: int (POINTER(I))
    error: int (POINTER(I))
    queue: list[struct__OSThreadQueue] (struct__OSThreadQueue[1])
    prop: union_FSFile_prop (union_FSFile_prop)
    arg: union_FSFile_arg (union_FSFile_arg)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_FSFileLink
    arc: POINTER_T[struct_FSArchive]
    stat: int
    command: int
    error: int
    queue: list[struct__OSThreadQueue]
    prop: union_FSFile_prop
    arg: union_FSFile_arg

class struct_FSFileID(Structure):
    """
    ```python
    arc: POINTER_T[struct_FSArchive] (POINTER(struct_FSArchive))
    file_id: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    arc: POINTER_T[struct_FSArchive]
    file_id: int

class struct_FSFileLink(Structure):
    """
    ```python
    prev: POINTER_T[struct_FSFile] (POINTER(struct_FSFile))
    next: POINTER_T[struct_FSFile] (POINTER(struct_FSFile))
    ```
    """
    _pack_: ClassVar[int] = 1
    prev: POINTER_T[struct_FSFile]
    next: POINTER_T[struct_FSFile]

class struct_FSFile_0_dir(Structure):
    """
    ```python
    pos: struct_FSDirPos (struct_FSDirPos)
    parent: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    pos: struct_FSDirPos
    parent: int

class struct_FSFile_0_file(Structure):
    """
    ```python
    own_id: int (POINTER(I))
    top: int (POINTER(I))
    bottom: int (POINTER(I))
    pos: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    own_id: int
    top: int
    bottom: int
    pos: int

class struct_FSFindPathInfo(Structure):
    """
    ```python
    pos: struct_FSDirPos (struct_FSDirPos)
    path: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    find_directory: int (POINTER(i))
    result: union_FSFindPathInfo_result (union_FSFindPathInfo_result)
    ```
    """
    _pack_: ClassVar[int] = 1
    pos: struct_FSDirPos
    path: POINTER_T[c_ubyte]
    find_directory: int
    result: union_FSFindPathInfo_result

class struct_FSGetPathInfo(Structure):
    """
    ```python
    buf: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    buf_len: int (POINTER(I))
    total_len: int (POINTER(H))
    dir_id: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    buf: POINTER_T[c_ubyte]
    buf_len: int
    total_len: int
    dir_id: int

class struct_FSOpenFileDirectInfo(Structure):
    """
    ```python
    top: int (POINTER(I))
    bottom: int (POINTER(I))
    index: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    top: int
    bottom: int
    index: int

class struct_FSOpenFileFastInfo(Structure):
    """
    ```python
    id: struct_FSFileID (struct_FSFileID)
    ```
    """
    _pack_: ClassVar[int] = 1
    id: struct_FSFileID

class struct_FSOverlayInfo(Structure):
    """
    ```python
    header: struct_FSOverlayInfoHeader (struct_FSOverlayInfoHeader)
    target: int (POINTER(I))
    file_pos: struct_CARDRomRegion (struct_CARDRomRegion)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_FSOverlayInfoHeader
    target: int
    file_pos: struct_CARDRomRegion

class struct_FSOverlayInfoHeader(Structure):
    """
    ```python
    id: int (POINTER(I))
    ram_address: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ram_size: int (POINTER(I))
    bss_size: int (POINTER(I))
    sinit_init: POINTER_T[_CFunctionType] (POINTER(CFunctionType))
    sinit_init_end: POINTER_T[_CFunctionType] (POINTER(CFunctionType))
    file_id: int (POINTER(I))
    compressed: int (POINTER(I))
    flag: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    ram_address: POINTER_T[c_ubyte]
    ram_size: int
    bss_size: int
    sinit_init: POINTER_T[_CFunctionType]
    sinit_init_end: POINTER_T[_CFunctionType]
    file_id: int
    compressed: int
    flag: int

class struct_FSReadDirInfo(Structure):
    """
    ```python
    p_entry: POINTER_T[struct_FSDirEntry] (POINTER(struct_FSDirEntry))
    skip_string: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    p_entry: POINTER_T[struct_FSDirEntry]
    skip_string: int

class struct_FSReadFileInfo(Structure):
    """
    ```python
    dst: c_void_p (c_void_p)
    len_org: int (POINTER(I))
    len: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    dst: c_void_p
    len_org: int
    len: int

class struct_FSSeekDirInfo(Structure):
    """
    ```python
    pos: struct_FSDirPos (struct_FSDirPos)
    ```
    """
    _pack_: ClassVar[int] = 1
    pos: struct_FSDirPos

class struct_FSWriteFileInfo(Structure):
    """
    ```python
    src: c_void_p (c_void_p)
    len_org: int (POINTER(I))
    len: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    src: c_void_p
    len_org: int
    len: int

class struct_GXOamAttr(Structure):
    """
    ```python
    _0: union_GXOamAttr_0 (union_GXOamAttr_0)
    _1: union_GXOamAttr_1 (union_GXOamAttr_1)
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: union_GXOamAttr_0
    _1: union_GXOamAttr_1

class struct_GXOamAttr_0_0(Structure):
    """
    ```python
    attr0: int (POINTER(H))
    attr1: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    attr0: int
    attr1: int

class struct_GXOamAttr_0_1(Structure):
    """
    ```python
    y: int (POINTER(I))
    rsMode: int (POINTER(I))
    objMode: int (POINTER(I))
    mosaic: int (POINTER(I))
    colorMode: int (POINTER(I))
    shape: int (POINTER(I))
    x: int (POINTER(I))
    rsParam: int (POINTER(I))
    size: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    y: int
    rsMode: int
    objMode: int
    mosaic: int
    colorMode: int
    shape: int
    x: int
    rsParam: int
    size: int

class struct_GXOamAttr_0_2(Structure):
    """
    ```python
    pad0: int (POINTER(I))
    flipH: int (POINTER(I))
    flipV: int (POINTER(I))
    pad1: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    pad0: int
    flipH: int
    flipV: int
    pad1: int

class struct_GXOamAttr_1_0(Structure):
    """
    ```python
    attr2: int (POINTER(H))
    _3: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    attr2: int
    _3: int

class struct_GXOamAttr_1_1(Structure):
    """
    ```python
    charNo: int (POINTER(I))
    priority: int (POINTER(I))
    cParam: int (POINTER(I))
    _2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    charNo: int
    priority: int
    cParam: int
    _2: int

class struct_MATHRandContext32(Structure):
    """
    ```python
    x: int (POINTER(L))
    mul: int (POINTER(L))
    add: int (POINTER(L))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: int
    mul: int
    add: int

class struct_MICAutoParam(Structure):
    """
    ```python
    type: int (POINTER(I))
    buffer: c_void_p (c_void_p)
    size: int (POINTER(I))
    rate: int (POINTER(I))
    loop_enable: int (POINTER(i))
    full_callback: Callable[[int, c_void_p], None] (CFunctionType)
    full_arg: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    type: int
    buffer: c_void_p
    size: int
    rate: int
    loop_enable: int
    full_callback: Callable[[int, c_void_p], None]
    full_arg: c_void_p

class struct_MtxFx22_0(Structure):
    """
    ```python
    _00: fx32 (struct_fx32)
    _01: fx32 (struct_fx32)
    _10: fx32 (struct_fx32)
    _11: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    _00: fx32
    _01: fx32
    _10: fx32
    _11: fx32

class struct_MtxFx33_0(Structure):
    """
    ```python
    _00: fx32 (struct_fx32)
    _01: fx32 (struct_fx32)
    _02: fx32 (struct_fx32)
    _10: fx32 (struct_fx32)
    _11: fx32 (struct_fx32)
    _12: fx32 (struct_fx32)
    _20: fx32 (struct_fx32)
    _21: fx32 (struct_fx32)
    _22: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    _00: fx32
    _01: fx32
    _02: fx32
    _10: fx32
    _11: fx32
    _12: fx32
    _20: fx32
    _21: fx32
    _22: fx32

class struct_MtxFx43_0(Structure):
    """
    ```python
    _00: fx32 (struct_fx32)
    _01: fx32 (struct_fx32)
    _02: fx32 (struct_fx32)
    _10: fx32 (struct_fx32)
    _11: fx32 (struct_fx32)
    _12: fx32 (struct_fx32)
    _20: fx32 (struct_fx32)
    _21: fx32 (struct_fx32)
    _22: fx32 (struct_fx32)
    _30: fx32 (struct_fx32)
    _31: fx32 (struct_fx32)
    _32: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    _00: fx32
    _01: fx32
    _02: fx32
    _10: fx32
    _11: fx32
    _12: fx32
    _20: fx32
    _21: fx32
    _22: fx32
    _30: fx32
    _31: fx32
    _32: fx32

class struct_NNSFndArchive(Structure):
    """
    ```python
    fsArchive: struct_FSArchive (struct_FSArchive)
    arcBinary: POINTER_T[struct_NNSiFndArchiveHeader] (POINTER(struct_NNSiFndArchiveHeader))
    fatData: POINTER_T[struct_NNSiFndArchiveFatData] (POINTER(struct_NNSiFndArchiveFatData))
    fileImage: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    fsArchive: struct_FSArchive
    arcBinary: POINTER_T[struct_NNSiFndArchiveHeader]
    fatData: POINTER_T[struct_NNSiFndArchiveFatData]
    fileImage: int

class struct_NNSFndLink(Structure):
    """
    ```python
    prevObject: c_void_p (c_void_p)
    nextObject: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    prevObject: c_void_p
    nextObject: c_void_p

class struct_NNSFndList(Structure):
    """
    ```python
    headObject: c_void_p (c_void_p)
    tailObject: c_void_p (c_void_p)
    numObjects: int (POINTER(H))
    offset: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    headObject: c_void_p
    tailObject: c_void_p
    numObjects: int
    offset: int

class struct_NNSG2dCellBoundingRectS16(Structure):
    """
    ```python
    maxX: int (POINTER(h))
    maxY: int (POINTER(h))
    minX: int (POINTER(h))
    minY: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    maxX: int
    maxY: int
    minX: int
    minY: int

class struct_NNSG2dCellData(Structure):
    """
    ```python
    numOAMAttrs: int (POINTER(H))
    cellAttr: int (POINTER(H))
    pOamAttrArray: POINTER_T[struct_NNSG2dCellOAMAttrData] (POINTER(struct_NNSG2dCellOAMAttrData))
    ```
    """
    _pack_: ClassVar[int] = 1
    numOAMAttrs: int
    cellAttr: int
    pOamAttrArray: POINTER_T[struct_NNSG2dCellOAMAttrData]

class struct_NNSG2dCellDataBank(Structure):
    """
    ```python
    numCells: int (POINTER(H))
    cellBankAttr: int (POINTER(H))
    pCellDataArrayHead: POINTER_T[struct_NNSG2dCellData] (POINTER(struct_NNSG2dCellData))
    mappingMode: int (POINTER(I))
    pVramTransferData: POINTER_T[struct_NNSG2dVramTransferData] (POINTER(struct_NNSG2dVramTransferData))
    pStringBank: c_void_p (c_void_p)
    pExtendedData: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    numCells: int
    cellBankAttr: int
    pCellDataArrayHead: POINTER_T[struct_NNSG2dCellData]
    mappingMode: int
    pVramTransferData: POINTER_T[struct_NNSG2dVramTransferData]
    pStringBank: c_void_p
    pExtendedData: c_void_p

class struct_NNSG2dCellDataWithBR(Structure):
    """
    ```python
    cellData: struct_NNSG2dCellData (struct_NNSG2dCellData)
    boundingRect: struct_NNSG2dCellBoundingRectS16 (struct_NNSG2dCellBoundingRectS16)
    ```
    """
    _pack_: ClassVar[int] = 1
    cellData: struct_NNSG2dCellData
    boundingRect: struct_NNSG2dCellBoundingRectS16

class struct_NNSG2dCellOAMAttrData(Structure):
    """
    ```python
    attr0: int (POINTER(H))
    attr1: int (POINTER(H))
    attr2: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    attr0: int
    attr1: int
    attr2: int

class struct_NNSG2dCellVramTransferData(Structure):
    """
    ```python
    srcDataOffset: int (POINTER(I))
    szByte: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    srcDataOffset: int
    szByte: int

class struct_NNSG2dCharCanvas(Structure):
    """
    ```python
    charBase: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    areaWidth: int (POINTER(i))
    areaHeight: int (POINTER(i))
    dstBpp: int (POINTER(B))
    reserved: list[int] (POINTER(B)[3])
    param: int (POINTER(I))
    pDrawGlyph: Callable[[POINTER_T[struct_NNSG2dCharCanvas], POINTER_T[struct_NNSG2dFont], int, int, int, POINTER_T[struct_NNSG2dGlyph]], None] (CFunctionType)
    pClear: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int], None] (CFunctionType)
    pClearArea: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int, int, int, int, int], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    charBase: POINTER_T[c_ubyte]
    areaWidth: int
    areaHeight: int
    dstBpp: int
    reserved: list[int]
    param: int
    pDrawGlyph: Callable[[POINTER_T[struct_NNSG2dCharCanvas], POINTER_T[struct_NNSG2dFont], int, int, int, POINTER_T[struct_NNSG2dGlyph]], None]
    pClear: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int], None]
    pClearArea: Callable[[POINTER_T[struct_NNSG2dCharCanvas], int, int, int, int, int], None]

class struct_NNSG2dCharWidths(Structure):
    """
    ```python
    left: int (POINTER(b))
    glyphWidth: int (POINTER(B))
    charWidth: int (POINTER(b))
    ```
    """
    _pack_: ClassVar[int] = 1
    left: int
    glyphWidth: int
    charWidth: int

class struct_NNSG2dCharacterData(Structure):
    """
    ```python
    H: int (POINTER(H))
    W: int (POINTER(H))
    pixelFmt: int (POINTER(I))
    mapingType: int (POINTER(I))
    characterFmt: int (POINTER(I))
    szByte: int (POINTER(I))
    pRawData: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    H: int
    W: int
    pixelFmt: int
    mapingType: int
    characterFmt: int
    szByte: int
    pRawData: c_void_p

class struct_NNSG2dFont(Structure):
    """
    ```python
    pRes: POINTER_T[struct_NNSG2dFontInformation] (POINTER(struct_NNSG2dFontInformation))
    cbCharSpliter: Callable[[POINTER_T[c_void_p]], c_ushort] (CFunctionType)
    isOldVer: int (POINTER(H))
    widthsSize: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    pRes: POINTER_T[struct_NNSG2dFontInformation]
    cbCharSpliter: Callable[[POINTER_T[c_void_p]], c_ushort]
    isOldVer: int
    widthsSize: int

class struct_NNSG2dFontCodeMap(Structure):
    """
    ```python
    ccodeBegin: int (POINTER(H))
    ccodeEnd: int (POINTER(H))
    mappingMethod: int (POINTER(H))
    reserved: int (POINTER(H))
    pNext: POINTER_T[struct_NNSG2dFontCodeMap] (POINTER(struct_NNSG2dFontCodeMap))
    mapInfo: list[int] (POINTER(H)[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    ccodeBegin: int
    ccodeEnd: int
    mappingMethod: int
    reserved: int
    pNext: POINTER_T[struct_NNSG2dFontCodeMap]
    mapInfo: list[int]

class struct_NNSG2dFontGlyph(Structure):
    """
    ```python
    cellWidth: int (POINTER(B))
    cellHeight: int (POINTER(B))
    cellSize: int (POINTER(H))
    baselinePos: int (POINTER(b))
    maxCharWidth: int (POINTER(B))
    bpp: int (POINTER(B))
    reserved: int (POINTER(B))
    glyphTable: list[int] (POINTER(B)[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    cellWidth: int
    cellHeight: int
    cellSize: int
    baselinePos: int
    maxCharWidth: int
    bpp: int
    reserved: int
    glyphTable: list[int]

class struct_NNSG2dFontInformation(Structure):
    """
    ```python
    fontType: int (POINTER(B))
    linefeed: int (POINTER(b))
    alterCharIndex: int (POINTER(H))
    defaultWidth: struct_NNSG2dCharWidths (struct_NNSG2dCharWidths)
    encoding: int (POINTER(B))
    pGlyph: POINTER_T[struct_NNSG2dFontGlyph] (POINTER(struct_NNSG2dFontGlyph))
    pWidth: POINTER_T[struct_NNSG2dFontWidth] (POINTER(struct_NNSG2dFontWidth))
    pMap: POINTER_T[struct_NNSG2dFontCodeMap] (POINTER(struct_NNSG2dFontCodeMap))
    ```
    """
    _pack_: ClassVar[int] = 1
    fontType: int
    linefeed: int
    alterCharIndex: int
    defaultWidth: struct_NNSG2dCharWidths
    encoding: int
    pGlyph: POINTER_T[struct_NNSG2dFontGlyph]
    pWidth: POINTER_T[struct_NNSG2dFontWidth]
    pMap: POINTER_T[struct_NNSG2dFontCodeMap]

class struct_NNSG2dFontWidth(Structure):
    """
    ```python
    indexBegin: int (POINTER(H))
    indexEnd: int (POINTER(H))
    pNext: POINTER_T[struct_NNSG2dFontWidth] (POINTER(struct_NNSG2dFontWidth))
    widthTable: list[struct_NNSG2dCharWidths] (struct_NNSG2dCharWidths[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    indexBegin: int
    indexEnd: int
    pNext: POINTER_T[struct_NNSG2dFontWidth]
    widthTable: list[struct_NNSG2dCharWidths]

class struct_NNSG2dGlyph(Structure):
    """
    ```python
    pWidths: POINTER_T[struct_NNSG2dCharWidths] (POINTER(struct_NNSG2dCharWidths))
    image: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ```
    """
    _pack_: ClassVar[int] = 1
    pWidths: POINTER_T[struct_NNSG2dCharWidths]
    image: POINTER_T[c_ubyte]

class struct_NNSG2dPaletteData(Structure):
    """
    ```python
    fmt: int (POINTER(I))
    bExtendedPlt: int (POINTER(i))
    szByte: int (POINTER(I))
    pRawData: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    fmt: int
    bExtendedPlt: int
    szByte: int
    pRawData: c_void_p

class struct_NNSG2dScreenData(Structure):
    """
    ```python
    screenWidth: int (POINTER(H))
    screenHeight: int (POINTER(H))
    colorMode: int (POINTER(H))
    screenFormat: int (POINTER(H))
    szByte: int (POINTER(I))
    rawData: list[int] (POINTER(I)[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    screenWidth: int
    screenHeight: int
    colorMode: int
    screenFormat: int
    szByte: int
    rawData: list[int]

class struct_NNSG2dTextCanvas(Structure):
    """
    ```python
    pCanvas: POINTER_T[struct_NNSG2dCharCanvas] (POINTER(struct_NNSG2dCharCanvas))
    pFont: POINTER_T[struct_NNSG2dFont] (POINTER(struct_NNSG2dFont))
    hSpace: int (POINTER(i))
    vSpace: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    pCanvas: POINTER_T[struct_NNSG2dCharCanvas]
    pFont: POINTER_T[struct_NNSG2dFont]
    hSpace: int
    vSpace: int

class struct_NNSG2dVramTransferData(Structure):
    """
    ```python
    szByteMax: int (POINTER(I))
    pCellTransferDataArray: POINTER_T[struct_NNSG2dCellVramTransferData] (POINTER(struct_NNSG2dCellVramTransferData))
    ```
    """
    _pack_: ClassVar[int] = 1
    szByteMax: int
    pCellTransferDataArray: POINTER_T[struct_NNSG2dCellVramTransferData]

class struct_NNSG3dAnmObj_(Structure):
    """
    ```python
    frame: fx32 (struct_fx32)
    ratio: fx32 (struct_fx32)
    resAnm: c_void_p (c_void_p)
    funcAnm: c_void_p (c_void_p)
    next: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    resTex: POINTER_T[struct_NNSG3dResTex_] (POINTER(struct_NNSG3dResTex_))
    priority: int (POINTER(B))
    numMapData: int (POINTER(B))
    mapData: list[int] (POINTER(H)[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    frame: fx32
    ratio: fx32
    resAnm: c_void_p
    funcAnm: c_void_p
    next: POINTER_T[struct_NNSG3dAnmObj_]
    resTex: POINTER_T[struct_NNSG3dResTex_]
    priority: int
    numMapData: int
    mapData: list[int]

class struct_NNSG3dJntAnmResult_(Structure):
    """
    ```python
    flag: int (POINTER(I))
    scale: struct_VecFx32 (struct_VecFx32)
    scaleEx0: struct_VecFx32 (struct_VecFx32)
    scaleEx1: struct_VecFx32 (struct_VecFx32)
    rot: union_MtxFx33 (union_MtxFx33)
    trans: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    flag: int
    scale: struct_VecFx32
    scaleEx0: struct_VecFx32
    scaleEx1: struct_VecFx32
    rot: union_MtxFx33
    trans: struct_VecFx32

class struct_NNSG3dMatAnmResult_(Structure):
    """
    ```python
    flag: int (POINTER(I))
    prmMatColor0: int (POINTER(I))
    prmMatColor1: int (POINTER(I))
    prmPolygonAttr: int (POINTER(I))
    prmTexImage: int (POINTER(I))
    prmTexPltt: int (POINTER(I))
    scaleS: fx32 (struct_fx32)
    scaleT: fx32 (struct_fx32)
    sinR: fx16 (struct_fx16)
    cosR: fx16 (struct_fx16)
    transS: fx32 (struct_fx32)
    transT: fx32 (struct_fx32)
    origWidth: int (POINTER(H))
    origHeight: int (POINTER(H))
    magW: fx32 (struct_fx32)
    magH: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    flag: int
    prmMatColor0: int
    prmMatColor1: int
    prmPolygonAttr: int
    prmTexImage: int
    prmTexPltt: int
    scaleS: fx32
    scaleT: fx32
    sinR: fx16
    cosR: fx16
    transS: fx32
    transT: fx32
    origWidth: int
    origHeight: int
    magW: fx32
    magH: fx32

class struct_NNSG3dRS_(Structure):
    """
    ```python
    c: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    pRenderObj: POINTER_T[struct_NNSG3dRenderObj_] (POINTER(struct_NNSG3dRenderObj_))
    flag: int (POINTER(I))
    cbVecFunc: list[Callable[[POINTER_T[struct_NNSG3dRS_]], None]] (CFunctionType[32])
    cbVecTiming: list[int] (POINTER(B)[32])
    currentNode: int (POINTER(B))
    currentMat: int (POINTER(B))
    currentNodeDesc: int (POINTER(B))
    dummy_: int (POINTER(B))
    pMatAnmResult: POINTER_T[struct_NNSG3dMatAnmResult_] (POINTER(struct_NNSG3dMatAnmResult_))
    pJntAnmResult: POINTER_T[struct_NNSG3dJntAnmResult_] (POINTER(struct_NNSG3dJntAnmResult_))
    pVisAnmResult: POINTER_T[struct_NNSG3dVisAnmResult_] (POINTER(struct_NNSG3dVisAnmResult_))
    isMatCached: list[int] (POINTER(I)[2])
    isScaleCacheOne: list[int] (POINTER(I)[2])
    isEvpCached: list[int] (POINTER(I)[2])
    pResNodeInfo: POINTER_T[struct_NNSG3dResNodeInfo_] (POINTER(struct_NNSG3dResNodeInfo_))
    pResMat: POINTER_T[struct_NNSG3dResMat_] (POINTER(struct_NNSG3dResMat_))
    pResShp: POINTER_T[struct_NNSG3dResShp_] (POINTER(struct_NNSG3dResShp_))
    posScale: fx32 (struct_fx32)
    invPosScale: fx32 (struct_fx32)
    funcJntScale: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_], POINTER_T[fx32], POINTER_T[c_ubyte], int], None] (CFunctionType)
    funcJntMtx: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_]], None] (CFunctionType)
    funcTexMtx: Callable[[POINTER_T[struct_NNSG3dMatAnmResult_]], None] (CFunctionType)
    tmpMatAnmResult: struct_NNSG3dMatAnmResult_ (struct_NNSG3dMatAnmResult_)
    tmpJntAnmResult: struct_NNSG3dJntAnmResult_ (struct_NNSG3dJntAnmResult_)
    tmpVisAnmResult: struct_NNSG3dVisAnmResult_ (struct_NNSG3dVisAnmResult_)
    ```
    """
    _pack_: ClassVar[int] = 1
    c: POINTER_T[c_ubyte]
    pRenderObj: POINTER_T[struct_NNSG3dRenderObj_]
    flag: int
    cbVecFunc: list[Callable[[POINTER_T[struct_NNSG3dRS_]], None]]
    cbVecTiming: list[int]
    currentNode: int
    currentMat: int
    currentNodeDesc: int
    dummy_: int
    pMatAnmResult: POINTER_T[struct_NNSG3dMatAnmResult_]
    pJntAnmResult: POINTER_T[struct_NNSG3dJntAnmResult_]
    pVisAnmResult: POINTER_T[struct_NNSG3dVisAnmResult_]
    isMatCached: list[int]
    isScaleCacheOne: list[int]
    isEvpCached: list[int]
    pResNodeInfo: POINTER_T[struct_NNSG3dResNodeInfo_]
    pResMat: POINTER_T[struct_NNSG3dResMat_]
    pResShp: POINTER_T[struct_NNSG3dResShp_]
    posScale: fx32
    invPosScale: fx32
    funcJntScale: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_], POINTER_T[fx32], POINTER_T[c_ubyte], int], None]
    funcJntMtx: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_]], None]
    funcTexMtx: Callable[[POINTER_T[struct_NNSG3dMatAnmResult_]], None]
    tmpMatAnmResult: struct_NNSG3dMatAnmResult_
    tmpJntAnmResult: struct_NNSG3dJntAnmResult_
    tmpVisAnmResult: struct_NNSG3dVisAnmResult_

class struct_NNSG3dRenderObj_(Structure):
    """
    ```python
    flag: int (POINTER(I))
    resMdl: POINTER_T[struct_NNSG3dResMdl_] (POINTER(struct_NNSG3dResMdl_))
    anmMat: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    funcBlendMat: Callable[[POINTER_T[struct_NNSG3dMatAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int] (CFunctionType)
    anmJnt: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    funcBlendJnt: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int] (CFunctionType)
    anmVis: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    funcBlendVis: Callable[[POINTER_T[struct_NNSG3dVisAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int] (CFunctionType)
    cbFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None] (CFunctionType)
    cbCmd: int (POINTER(B))
    cbTiming: int (POINTER(B))
    dummy_: int (POINTER(H))
    cbInitFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None] (CFunctionType)
    ptrUser: c_void_p (c_void_p)
    ptrUserSbc: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    recJntAnm: POINTER_T[struct_NNSG3dJntAnmResult_] (POINTER(struct_NNSG3dJntAnmResult_))
    recMatAnm: POINTER_T[struct_NNSG3dMatAnmResult_] (POINTER(struct_NNSG3dMatAnmResult_))
    hintMatAnmExist: list[int] (POINTER(I)[2])
    hintJntAnmExist: list[int] (POINTER(I)[2])
    hintVisAnmExist: list[int] (POINTER(I)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    flag: int
    resMdl: POINTER_T[struct_NNSG3dResMdl_]
    anmMat: POINTER_T[struct_NNSG3dAnmObj_]
    funcBlendMat: Callable[[POINTER_T[struct_NNSG3dMatAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int]
    anmJnt: POINTER_T[struct_NNSG3dAnmObj_]
    funcBlendJnt: Callable[[POINTER_T[struct_NNSG3dJntAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int]
    anmVis: POINTER_T[struct_NNSG3dAnmObj_]
    funcBlendVis: Callable[[POINTER_T[struct_NNSG3dVisAnmResult_], POINTER_T[struct_NNSG3dAnmObj_], int], c_int]
    cbFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None]
    cbCmd: int
    cbTiming: int
    dummy_: int
    cbInitFunc: Callable[[POINTER_T[struct_NNSG3dRS_]], None]
    ptrUser: c_void_p
    ptrUserSbc: POINTER_T[c_ubyte]
    recJntAnm: POINTER_T[struct_NNSG3dJntAnmResult_]
    recMatAnm: POINTER_T[struct_NNSG3dMatAnmResult_]
    hintMatAnmExist: list[int]
    hintJntAnmExist: list[int]
    hintVisAnmExist: list[int]

class struct_NNSG3dResDataBlockHeader_(Structure):
    """
    ```python
    _0: union_NNSG3dResDataBlockHeader__0 (union_NNSG3dResDataBlockHeader__0)
    size: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: union_NNSG3dResDataBlockHeader__0
    size: int

class struct_NNSG3dResDictTreeNode_(Structure):
    """
    ```python
    refBit: int (POINTER(B))
    idxLeft: int (POINTER(B))
    idxRight: int (POINTER(B))
    idxEntry: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    refBit: int
    idxLeft: int
    idxRight: int
    idxEntry: int

class struct_NNSG3dResDict_(Structure):
    """
    ```python
    revision: int (POINTER(B))
    numEntry: int (POINTER(B))
    sizeDictBlk: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsEntry: int (POINTER(H))
    node: list[struct_NNSG3dResDictTreeNode_] (struct_NNSG3dResDictTreeNode_[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    revision: int
    numEntry: int
    sizeDictBlk: int
    dummy_: int
    ofsEntry: int
    node: list[struct_NNSG3dResDictTreeNode_]

class struct_NNSG3dResMat_(Structure):
    """
    ```python
    ofsDictTexToMatList: int (POINTER(H))
    ofsDictPlttToMatList: int (POINTER(H))
    dict: struct_NNSG3dResDict_ (struct_NNSG3dResDict_)
    ```
    """
    _pack_: ClassVar[int] = 1
    ofsDictTexToMatList: int
    ofsDictPlttToMatList: int
    dict: struct_NNSG3dResDict_

class struct_NNSG3dResMdlInfo_(Structure):
    """
    ```python
    sbcType: int (POINTER(B))
    scalingRule: int (POINTER(B))
    texMtxMode: int (POINTER(B))
    numNode: int (POINTER(B))
    numMat: int (POINTER(B))
    numShp: int (POINTER(B))
    firstUnusedMtxStackID: int (POINTER(B))
    dummy_: int (POINTER(B))
    posScale: fx32 (struct_fx32)
    invPosScale: fx32 (struct_fx32)
    numVertex: int (POINTER(H))
    numPolygon: int (POINTER(H))
    numTriangle: int (POINTER(H))
    numQuad: int (POINTER(H))
    boxX: fx16 (struct_fx16)
    boxY: fx16 (struct_fx16)
    boxZ: fx16 (struct_fx16)
    boxW: fx16 (struct_fx16)
    boxH: fx16 (struct_fx16)
    boxD: fx16 (struct_fx16)
    boxPosScale: fx32 (struct_fx32)
    boxInvPosScale: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    sbcType: int
    scalingRule: int
    texMtxMode: int
    numNode: int
    numMat: int
    numShp: int
    firstUnusedMtxStackID: int
    dummy_: int
    posScale: fx32
    invPosScale: fx32
    numVertex: int
    numPolygon: int
    numTriangle: int
    numQuad: int
    boxX: fx16
    boxY: fx16
    boxZ: fx16
    boxW: fx16
    boxH: fx16
    boxD: fx16
    boxPosScale: fx32
    boxInvPosScale: fx32

class struct_NNSG3dResMdl_(Structure):
    """
    ```python
    size: int (POINTER(I))
    ofsSbc: int (POINTER(I))
    ofsMat: int (POINTER(I))
    ofsShp: int (POINTER(I))
    ofsEvpMtx: int (POINTER(I))
    info: struct_NNSG3dResMdlInfo_ (struct_NNSG3dResMdlInfo_)
    nodeInfo: struct_NNSG3dResNodeInfo_ (struct_NNSG3dResNodeInfo_)
    ```
    """
    _pack_: ClassVar[int] = 1
    size: int
    ofsSbc: int
    ofsMat: int
    ofsShp: int
    ofsEvpMtx: int
    info: struct_NNSG3dResMdlInfo_
    nodeInfo: struct_NNSG3dResNodeInfo_

class struct_NNSG3dResNodeInfo_(Structure):
    """
    ```python
    dict: struct_NNSG3dResDict_ (struct_NNSG3dResDict_)
    ```
    """
    _pack_: ClassVar[int] = 1
    dict: struct_NNSG3dResDict_

class struct_NNSG3dResPlttInfo_(Structure):
    """
    ```python
    vramKey: int (POINTER(I))
    sizePltt: int (POINTER(H))
    flag: int (POINTER(H))
    ofsDict: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsPlttData: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    vramKey: int
    sizePltt: int
    flag: int
    ofsDict: int
    dummy_: int
    ofsPlttData: int

class struct_NNSG3dResShp_(Structure):
    """
    ```python
    dict: struct_NNSG3dResDict_ (struct_NNSG3dResDict_)
    ```
    """
    _pack_: ClassVar[int] = 1
    dict: struct_NNSG3dResDict_

class struct_NNSG3dResTex4x4Info_(Structure):
    """
    ```python
    vramKey: int (POINTER(I))
    sizeTex: int (POINTER(H))
    ofsDict: int (POINTER(H))
    flag: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsTex: int (POINTER(I))
    ofsTexPlttIdx: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    vramKey: int
    sizeTex: int
    ofsDict: int
    flag: int
    dummy_: int
    ofsTex: int
    ofsTexPlttIdx: int

class struct_NNSG3dResTexInfo_(Structure):
    """
    ```python
    vramKey: int (POINTER(I))
    sizeTex: int (POINTER(H))
    ofsDict: int (POINTER(H))
    flag: int (POINTER(H))
    dummy_: int (POINTER(H))
    ofsTex: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    vramKey: int
    sizeTex: int
    ofsDict: int
    flag: int
    dummy_: int
    ofsTex: int

class struct_NNSG3dResTex_(Structure):
    """
    ```python
    header: struct_NNSG3dResDataBlockHeader_ (struct_NNSG3dResDataBlockHeader_)
    texInfo: struct_NNSG3dResTexInfo_ (struct_NNSG3dResTexInfo_)
    tex4x4Info: struct_NNSG3dResTex4x4Info_ (struct_NNSG3dResTex4x4Info_)
    plttInfo: struct_NNSG3dResPlttInfo_ (struct_NNSG3dResPlttInfo_)
    dict: struct_NNSG3dResDict_ (struct_NNSG3dResDict_)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_NNSG3dResDataBlockHeader_
    texInfo: struct_NNSG3dResTexInfo_
    tex4x4Info: struct_NNSG3dResTex4x4Info_
    plttInfo: struct_NNSG3dResPlttInfo_
    dict: struct_NNSG3dResDict_

class struct_NNSG3dVisAnmResult_(Structure):
    """
    ```python
    isVisible: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    isVisible: int

class struct_NNSSndFader(Structure):
    """
    ```python
    origin: int (POINTER(i))
    target: int (POINTER(i))
    counter: int (POINTER(i))
    frame: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    origin: int
    target: int
    counter: int
    frame: int

class struct_NNSSndHandle(Structure):
    """
    ```python
    player: POINTER_T[struct_NNSSndSeqPlayer] (POINTER(struct_NNSSndSeqPlayer))
    ```
    """
    _pack_: ClassVar[int] = 1
    player: POINTER_T[struct_NNSSndSeqPlayer]

class struct_NNSSndPlayer(Structure):
    """
    ```python
    playerList: struct_NNSFndList (struct_NNSFndList)
    heapList: struct_NNSFndList (struct_NNSFndList)
    playableSeqCount: int (POINTER(I))
    allocChBitFlag: int (POINTER(I))
    volume: int (POINTER(B))
    pad_: int (POINTER(B))
    pad2_: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    playerList: struct_NNSFndList
    heapList: struct_NNSFndList
    playableSeqCount: int
    allocChBitFlag: int
    volume: int
    pad_: int
    pad2_: int

class struct_NNSSndPlayerHeap(Structure):
    pass

class struct_NNSSndSeqPlayer(Structure):
    """
    ```python
    handle: POINTER_T[struct_NNSSndHandle] (POINTER(struct_NNSSndHandle))
    player: POINTER_T[struct_NNSSndPlayer] (POINTER(struct_NNSSndPlayer))
    heap: POINTER_T[struct_NNSSndPlayerHeap] (POINTER(struct_NNSSndPlayerHeap))
    playerLink: struct_NNSFndLink (struct_NNSFndLink)
    prioLink: struct_NNSFndLink (struct_NNSFndLink)
    fader: struct_NNSSndFader (struct_NNSSndFader)
    status: int (POINTER(B))
    startFlag: int (POINTER(B))
    pauseFlag: int (POINTER(B))
    prepareFlag: int (POINTER(B))
    commandTag: int (POINTER(I))
    seqType: int (POINTER(H))
    pad2: int (POINTER(H))
    seqNo: int (POINTER(H))
    seqArcIndex: int (POINTER(H))
    playerNo: int (POINTER(B))
    prio: int (POINTER(B))
    volume: int (POINTER(h))
    initVolume: int (POINTER(B))
    extVolume: int (POINTER(B))
    pad3_: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    handle: POINTER_T[struct_NNSSndHandle]
    player: POINTER_T[struct_NNSSndPlayer]
    heap: POINTER_T[struct_NNSSndPlayerHeap]
    playerLink: struct_NNSFndLink
    prioLink: struct_NNSFndLink
    fader: struct_NNSSndFader
    status: int
    startFlag: int
    pauseFlag: int
    prepareFlag: int
    commandTag: int
    seqType: int
    pad2: int
    seqNo: int
    seqArcIndex: int
    playerNo: int
    prio: int
    volume: int
    initVolume: int
    extVolume: int
    pad3_: int

class struct_NNSiFndArchiveFatData(Structure):
    """
    ```python
    blockType: int (POINTER(I))
    blockSize: int (POINTER(I))
    numFiles: int (POINTER(H))
    reserved: int (POINTER(H))
    fatEntries: list[struct_NNSiFndArchiveFatEntry] (struct_NNSiFndArchiveFatEntry[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    blockType: int
    blockSize: int
    numFiles: int
    reserved: int
    fatEntries: list[struct_NNSiFndArchiveFatEntry]

class struct_NNSiFndArchiveFatEntry(Structure):
    """
    ```python
    fileTop: int (POINTER(I))
    fileBottom: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    fileTop: int
    fileBottom: int

class struct_NNSiFndArchiveHeader(Structure):
    """
    ```python
    signature: int (POINTER(I))
    byteOrder: int (POINTER(H))
    version: int (POINTER(H))
    fileSize: int (POINTER(I))
    headerSize: int (POINTER(H))
    dataBlocks: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    byteOrder: int
    version: int
    fileSize: int
    headerSize: int
    dataBlocks: int

class struct_NNSiFndHeapHead(Structure):
    """
    ```python
    signature: int (POINTER(I))
    link: struct_NNSFndLink (struct_NNSFndLink)
    childList: struct_NNSFndList (struct_NNSFndList)
    heapStart: c_void_p (c_void_p)
    heapEnd: c_void_p (c_void_p)
    attribute: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    link: struct_NNSFndLink
    childList: struct_NNSFndList
    heapStart: c_void_p
    heapEnd: c_void_p
    attribute: int

class struct_OSContext(Structure):
    """
    ```python
    cpsr: int (POINTER(I))
    r: list[int] (POINTER(I)[13])
    sp: int (POINTER(I))
    lr: int (POINTER(I))
    pc_plus4: int (POINTER(I))
    sp_svc: int (POINTER(I))
    cp_context: struct_CPContext (struct_CPContext)
    ```
    """
    _pack_: ClassVar[int] = 1
    cpsr: int
    r: list[int]
    sp: int
    lr: int
    pc_plus4: int
    sp_svc: int
    cp_context: struct_CPContext

class struct_OSMutex(Structure):
    """
    ```python
    queue: struct__OSThreadQueue (struct__OSThreadQueue)
    thread: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    count: int (POINTER(i))
    link: struct__OSMutexLink (struct__OSMutexLink)
    ```
    """
    _pack_: ClassVar[int] = 1
    queue: struct__OSThreadQueue
    thread: POINTER_T[struct__OSThread]
    count: int
    link: struct__OSMutexLink

class struct_OSiAlarm(Structure):
    """
    ```python
    handler: Callable[[c_void_p], None] (CFunctionType)
    arg: c_void_p (c_void_p)
    tag: int (POINTER(I))
    PADDING_0: list[int] (POINTER(B)[4])
    fire: int (POINTER(L))
    prev: POINTER_T[struct_OSiAlarm] (POINTER(struct_OSiAlarm))
    next: POINTER_T[struct_OSiAlarm] (POINTER(struct_OSiAlarm))
    period: int (POINTER(L))
    start: int (POINTER(L))
    ```
    """
    _pack_: ClassVar[int] = 1
    handler: Callable[[c_void_p], None]
    arg: c_void_p
    tag: int
    PADDING_0: list[int]
    fire: int
    prev: POINTER_T[struct_OSiAlarm]
    next: POINTER_T[struct_OSiAlarm]
    period: int
    start: int

class struct_PMiSleepCallbackInfo(Structure):
    """
    ```python
    callback: Callable[[c_void_p], None] (CFunctionType)
    arg: c_void_p (c_void_p)
    next: POINTER_T[struct_PMiSleepCallbackInfo] (POINTER(struct_PMiSleepCallbackInfo))
    ```
    """
    _pack_: ClassVar[int] = 1
    callback: Callable[[c_void_p], None]
    arg: c_void_p
    next: POINTER_T[struct_PMiSleepCallbackInfo]

class struct_RTCRawData_t(Structure):
    """
    ```python
    date: struct_RTCRawDate (struct_RTCRawDate)
    time: struct_RTCRawTime (struct_RTCRawTime)
    ```
    """
    _pack_: ClassVar[int] = 1
    date: struct_RTCRawDate
    time: struct_RTCRawTime

class struct_RTCRawDate(Structure):
    """
    ```python
    year: int (POINTER(I))
    month: int (POINTER(I))
    dummy0: int (POINTER(I))
    day: int (POINTER(I))
    dummy1: int (POINTER(I))
    week: int (POINTER(I))
    dummy2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    year: int
    month: int
    dummy0: int
    day: int
    dummy1: int
    week: int
    dummy2: int

class struct_RTCRawTime(Structure):
    """
    ```python
    hour: int (POINTER(I))
    afternoon: int (POINTER(I))
    dummy0: int (POINTER(I))
    minute: int (POINTER(I))
    dummy1: int (POINTER(I))
    second: int (POINTER(I))
    dummy2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    hour: int
    afternoon: int
    dummy0: int
    minute: int
    dummy1: int
    second: int
    dummy2: int

class struct_TPData(Structure):
    """
    ```python
    x: int (POINTER(H))
    y: int (POINTER(H))
    touch: int (POINTER(H))
    validity: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: int
    y: int
    touch: int
    validity: int

class struct_VecFx16(Structure):
    """
    ```python
    x: fx16 (struct_fx16)
    y: fx16 (struct_fx16)
    z: fx16 (struct_fx16)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx16
    y: fx16
    z: fx16

class struct_VecFx32(Structure):
    """
    ```python
    x: fx32 (struct_fx32)
    y: fx32 (struct_fx32)
    z: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx32
    y: fx32
    z: fx32

class struct__OSMutexLink(Structure):
    """
    ```python
    next: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    prev: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: POINTER_T[struct_OSMutex]
    prev: POINTER_T[struct_OSMutex]

class struct__OSMutexQueue(Structure):
    """
    ```python
    head: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    tail: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    ```
    """
    _pack_: ClassVar[int] = 1
    head: POINTER_T[struct_OSMutex]
    tail: POINTER_T[struct_OSMutex]

class struct__OSThread(Structure):
    """
    ```python
    context: struct_OSContext (struct_OSContext)
    state: int (POINTER(I))
    next: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    id: int (POINTER(I))
    priority: int (POINTER(I))
    profiler: c_void_p (c_void_p)
    queue: POINTER_T[struct__OSThreadQueue] (POINTER(struct__OSThreadQueue))
    link: struct__OSThreadLink (struct__OSThreadLink)
    mutex: POINTER_T[struct_OSMutex] (POINTER(struct_OSMutex))
    mutexQueue: struct__OSMutexQueue (struct__OSMutexQueue)
    stackTop: int (POINTER(I))
    stackBottom: int (POINTER(I))
    stackWarningOffset: int (POINTER(I))
    joinQueue: struct__OSThreadQueue (struct__OSThreadQueue)
    specific: list[c_void_p] (c_void_p[3])
    alarmForSleep: POINTER_T[struct_OSiAlarm] (POINTER(struct_OSiAlarm))
    destructor: Callable[[c_void_p], None] (CFunctionType)
    userParameter: c_void_p (c_void_p)
    systemErrno: int (POINTER(i))
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    context: struct_OSContext
    state: int
    next: POINTER_T[struct__OSThread]
    id: int
    priority: int
    profiler: c_void_p
    queue: POINTER_T[struct__OSThreadQueue]
    link: struct__OSThreadLink
    mutex: POINTER_T[struct_OSMutex]
    mutexQueue: struct__OSMutexQueue
    stackTop: int
    stackBottom: int
    stackWarningOffset: int
    joinQueue: struct__OSThreadQueue
    specific: list[c_void_p]
    alarmForSleep: POINTER_T[struct_OSiAlarm]
    destructor: Callable[[c_void_p], None]
    userParameter: c_void_p
    systemErrno: int
    PADDING_0: list[int]

class struct__OSThreadLink(Structure):
    """
    ```python
    prev: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    next: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    ```
    """
    _pack_: ClassVar[int] = 1
    prev: POINTER_T[struct__OSThread]
    next: POINTER_T[struct__OSThread]

class struct__OSThreadQueue(Structure):
    """
    ```python
    head: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    tail: POINTER_T[struct__OSThread] (POINTER(struct__OSThread))
    ```
    """
    _pack_: ClassVar[int] = 1
    head: POINTER_T[struct__OSThread]
    tail: POINTER_T[struct__OSThread]

class struct___locale_t(Structure):
    pass

class struct___lock_t(Structure):
    """
    ```python
    lock: int (POINTER(i))
    thread_tag: int (POINTER(I))
    counter: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    lock: int
    thread_tag: int
    counter: int

class struct__mbstate_t(Structure):
    """
    ```python
    __count: int (POINTER(i))
    __value: union__mbstate_t___value (union__mbstate_t___value)
    ```
    """
    _pack_: ClassVar[int] = 1
    __count: int
    __value: union__mbstate_t___value

class struct_airship_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    baseElevation: fx32 (struct_fx32)
    speed: fx32 (struct_fx32)
    fieldA8: struct_sinthing_t (struct_sinthing_t)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    baseElevation: fx32
    speed: fx32
    fieldA8: struct_sinthing_t
    pathwalker: struct_pw_pathwalker_t
    state: int

class struct_anim_animator_t(Structure):
    """
    ```python
    loopMode: int (POINTER(H))
    hasEnded: int (POINTER(H))
    animLength: fx32 (struct_fx32)
    speed: fx32 (struct_fx32)
    progress: fx32 (struct_fx32)
    loopIteration: int (POINTER(H))
    loopCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    loopMode: int
    hasEnded: int
    animLength: fx32
    speed: fx32
    progress: fx32
    loopIteration: int
    loopCount: int

class struct_anim_manager_t(Structure):
    """
    ```python
    animator: struct_anim_animator_t (struct_anim_animator_t)
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    animCount: int (POINTER(H))
    curAnimIdx: int (POINTER(H))
    anmObjs: POINTER_T[POINTER_T[struct_NNSG3dAnmObj_]] (POINTER(POINTER(struct_NNSG3dAnmObj_)))
    loopFlags: POINTER_T[c_int] (POINTER(POINTER(i)))
    field24: int (POINTER(I))
    animKind: int (POINTER(I))
    isBlending: int (POINTER(i))
    blendSpeed: fx32 (struct_fx32)
    blendAnmObj: POINTER_T[struct_NNSG3dAnmObj_] (POINTER(struct_NNSG3dAnmObj_))
    ```
    """
    _pack_: ClassVar[int] = 1
    animator: struct_anim_animator_t
    model: POINTER_T[struct_model_t]
    animCount: int
    curAnimIdx: int
    anmObjs: POINTER_T[POINTER_T[struct_NNSG3dAnmObj_]]
    loopFlags: POINTER_T[c_int]
    field24: int
    animKind: int
    isBlending: int
    blendSpeed: fx32
    blendAnmObj: POINTER_T[struct_NNSG3dAnmObj_]

class struct_arc_course_def_t(Structure):
    """
    ```python
    name: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    hasDVariant: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    name: POINTER_T[c_ubyte]
    hasDVariant: int
    PADDING_0: list[int]

class struct_arc_data_t(Structure):
    """
    ```python
    arcs: list[struct_arc_t] (struct_arc_t[20])
    fsTableSize: int (POINTER(I))
    fsTable: c_void_p (c_void_p)
    arcLoader: struct_arc_loader_t (struct_arc_loader_t)
    file: struct_FSFile (struct_FSFile)
    something: list[struct_arc_something_t] (struct_arc_something_t[16])
    curLoadedCourse: int (POINTER(I))
    curLoadedRaceMode: int (POINTER(I))
    unk0xA78: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    unk0xA7C: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    unk0xA80: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    ```
    """
    _pack_: ClassVar[int] = 1
    arcs: list[struct_arc_t]
    fsTableSize: int
    fsTable: c_void_p
    arcLoader: struct_arc_loader_t
    file: struct_FSFile
    something: list[struct_arc_something_t]
    curLoadedCourse: int
    curLoadedRaceMode: int
    unk0xA78: POINTER_T[struct_NNSiFndHeapHead]
    unk0xA7C: POINTER_T[struct_NNSiFndHeapHead]
    unk0xA80: POINTER_T[struct_NNSiFndHeapHead]

class struct_arc_def_t(Structure):
    """
    ```python
    path: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    next: int (POINTER(i))
    somethingId: int (POINTER(b))
    PADDING_0: list[int] (POINTER(B)[3])
    unk3: int (POINTER(I))
    allocFromTail: int (POINTER(i))
    unk5: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: POINTER_T[c_ubyte]
    next: int
    somethingId: int
    PADDING_0: list[int]
    unk3: int
    allocFromTail: int
    unk5: int

class struct_arc_loader_t(Structure):
    """
    ```python
    path: list[int] (POINTER(B)[128])
    srcBuf: c_void_p (c_void_p)
    dstBuf: c_void_p (c_void_p)
    tmpBuf: c_void_p (c_void_p)
    arcId: int (POINTER(I))
    allocFromTail: int (POINTER(I))
    field94: int (POINTER(I))
    field98: int (POINTER(I))
    field9C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: list[int]
    srcBuf: c_void_p
    dstBuf: c_void_p
    tmpBuf: c_void_p
    arcId: int
    allocFromTail: int
    field94: int
    field98: int
    field9C: int

class struct_arc_scene_def_t(Structure):
    """
    ```python
    name: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    unk: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    name: POINTER_T[c_ubyte]
    unk: int

class struct_arc_something_t(Structure):
    """
    ```python
    heapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    b: c_void_p (c_void_p)
    flag0: int (POINTER(I))
    flag29: int (POINTER(I))
    flag30: int (POINTER(I))
    flag31: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    heapHandle: POINTER_T[struct_NNSiFndHeapHead]
    b: c_void_p
    flag0: int
    flag29: int
    flag30: int
    flag31: int

class struct_arc_t(Structure):
    """
    ```python
    arc: struct_NNSFndArchive (struct_NNSFndArchive)
    loaded: int (POINTER(i))
    arcData: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    arc: struct_NNSFndArchive
    loaded: int
    arcData: c_void_p

class struct_area_mission_rival_pass_area_status_t(Structure):
    """
    ```python
    entries: POINTER_T[struct_area_mission_rival_pass_area_t] (POINTER(struct_area_mission_rival_pass_area_t))
    count: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    entries: POINTER_T[struct_area_mission_rival_pass_area_t]
    count: int
    PADDING_0: list[int]

class struct_area_mission_rival_pass_area_t(Structure):
    """
    ```python
    index: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    size: fx32 (struct_fx32)
    prevNrObjsInside: int (POINTER(B))
    passCount: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    index: int
    PADDING_0: list[int]
    size: fx32
    prevNrObjsInside: int
    passCount: int
    PADDING_1: list[int]

class struct_bakubaku_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    waitCounter: int (POINTER(i))
    triggerPos: struct_VecFx32 (struct_VecFx32)
    state: int (POINTER(I))
    fieldB4: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    waitCounter: int
    triggerPos: struct_VecFx32
    state: int
    fieldB4: int

class struct_balloon_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(i))
    driverId: int (POINTER(i))
    color: int (POINTER(i))
    gapAC: int (POINTER(I))
    fieldB0: struct_VecFx32 (struct_VecFx32)
    fieldBC: struct_VecFx32 (struct_VecFx32)
    fieldC8: int (POINTER(i))
    fieldCC: int (POINTER(i))
    inflationProgress: int (POINTER(i))
    inflationDelta: int (POINTER(i))
    scale3: int (POINTER(i))
    scale3Delta: int (POINTER(i))
    fieldE0: int (POINTER(i))
    scale: int (POINTER(i))
    fieldE8: struct_VecFx32 (struct_VecFx32)
    subBalloonCountPlusOne: int (POINTER(i))
    subBalloons: POINTER_T[POINTER_T[struct_balloon_t]] (POINTER(POINTER(struct_balloon_t)))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    driverId: int
    color: int
    gapAC: int
    fieldB0: struct_VecFx32
    fieldBC: struct_VecFx32
    fieldC8: int
    fieldCC: int
    inflationProgress: int
    inflationDelta: int
    scale3: int
    scale3Delta: int
    fieldE0: int
    scale: int
    fieldE8: struct_VecFx32
    subBalloonCountPlusOne: int
    subBalloons: POINTER_T[POINTER_T[struct_balloon_t]]
    state: int

class struct_basabasa_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    velocity: struct_VecFx32 (struct_VecFx32)
    nsbtpFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    initialCounter: int (POINTER(i))
    state0Counter: int (POINTER(i))
    state2Counter: int (POINTER(i))
    emitSound: int (POINTER(i))
    mapIconType: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    rotZ: struct_idk_struct_t (struct_idk_struct_t)
    driverHitMask: int (POINTER(B))
    PADDING_2: list[int] (POINTER(B)[3])
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    velocity: struct_VecFx32
    nsbtpFrame: int
    PADDING_0: list[int]
    initialCounter: int
    state0Counter: int
    state2Counter: int
    emitSound: int
    mapIconType: int
    PADDING_1: list[int]
    rotZ: struct_idk_struct_t
    driverHitMask: int
    PADDING_2: list[int]
    state: int

class struct_bbm_model_t(Structure):
    """
    ```python
    displayList: c_void_p (c_void_p)
    displayListLength: int (POINTER(I))
    posScale: fx32 (struct_fx32)
    diffAmb: int (POINTER(I))
    speEmi: int (POINTER(I))
    polygonAttr: int (POINTER(I))
    texIdx: int (POINTER(H))
    texCount: int (POINTER(H))
    texParamList: POINTER_T[c_uint] (POINTER(POINTER(I)))
    plttParamList: POINTER_T[c_uint] (POINTER(POINTER(I)))
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    nsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    displayList: c_void_p
    displayListLength: int
    posScale: fx32
    diffAmb: int
    speEmi: int
    polygonAttr: int
    texIdx: int
    texCount: int
    texParamList: POINTER_T[c_uint]
    plttParamList: POINTER_T[c_uint]
    model: POINTER_T[struct_model_t]
    nsbtpAnim: POINTER_T[struct_anim_manager_t]

class struct_bbobj_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class struct_bgwkr_queue_t(Structure):
    """
    ```python
    buffer: list[Callable[[], None]] (CFunctionType[10])
    writePtr: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    buffer: list[Callable[[], None]]
    writePtr: int
    PADDING_0: list[int]

class struct_bgwkr_t(Structure):
    """
    ```python
    taskQueue: struct_bgwkr_queue_t (struct_bgwkr_queue_t)
    PADDING_0: list[int] (POINTER(B)[4])
    thread: struct__OSThread (struct__OSThread)
    unk: list[int] (POINTER(I)[2])
    threadStack: POINTER_T[c_uint] (POINTER(POINTER(I)))
    requestAvailable: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    taskQueue: struct_bgwkr_queue_t
    PADDING_0: list[int]
    thread: struct__OSThread
    unk: list[int]
    threadStack: POINTER_T[c_uint]
    requestAvailable: int

class struct_bound_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbtpFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fieldA4: int (POINTER(I))
    fieldA8: int (POINTER(I))
    fieldAC: int (POINTER(I))
    fieldB0: int (POINTER(I))
    width: int (POINTER(I))
    scaleXZSinThing: struct_sinthing_t (struct_sinthing_t)
    scaleYSinThing: struct_sinthing_t (struct_sinthing_t)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    driverHitTimeouts: list[int] (POINTER(I)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbtpFrame: int
    PADDING_0: list[int]
    fieldA4: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    width: int
    scaleXZSinThing: struct_sinthing_t
    scaleYSinThing: struct_sinthing_t
    pathwalker: struct_pw_pathwalker_t
    state: int
    driverHitTimeouts: list[int]

class struct_bridge_renderpart_t(Structure):
    """
    ```python
    renderPart: struct_mobj_render_part_t (struct_mobj_render_part_t)
    animLength: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    renderPart: struct_mobj_render_part_t
    animLength: fx32

class struct_bridge_t(Structure):
    """
    ```python
    dcolMObj: struct_dcol_inst_t (struct_dcol_inst_t)
    field144: int (POINTER(H))
    rotSpeed: int (POINTER(H))
    angle: int (POINTER(H))
    field14A: int (POINTER(H))
    field14C: int (POINTER(H))
    field14E: int (POINTER(H))
    waitCounter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    animProgress: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    dcolMObj: struct_dcol_inst_t
    field144: int
    rotSpeed: int
    angle: int
    field14A: int
    field14C: int
    field14E: int
    waitCounter: int
    PADDING_0: list[int]
    animProgress: fx32

class struct_bsfx_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    sfxAMaxVolume: int (POINTER(i))
    volume: int (POINTER(i))
    fieldA8: int (POINTER(i))
    position: struct_VecFx32 (struct_VecFx32)
    fieldB8: int (POINTER(i))
    sfxIdA: int (POINTER(H))
    sfxIdB: int (POINTER(H))
    stateUpdateCounter: int (POINTER(i))
    state: int (POINTER(i))
    sfxACounter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    sfxAMaxVolume: int
    volume: int
    fieldA8: int
    position: struct_VecFx32
    fieldB8: int
    sfxIdA: int
    sfxIdB: int
    stateUpdateCounter: int
    state: int
    sfxACounter: int

class struct_cam_params_t(Structure):
    """
    ```python
    distance: fx32 (struct_fx32)
    elevation: fx32 (struct_fx32)
    maxTargetElevation: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    distance: fx32
    elevation: fx32
    maxTargetElevation: fx32

class struct_came_routestat_t(Structure):
    """
    ```python
    pointCache: list[struct_VecFx32] (struct_VecFx32[4])
    progress: int (POINTER(i))
    index: int (POINTER(i))
    field38: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    pointCache: list[struct_VecFx32]
    progress: int
    index: int
    field38: int

class struct_came_unknown_t(Structure):
    """
    ```python
    cameEntry: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    routestat1: struct_came_routestat_t (struct_came_routestat_t)
    routestat2: struct_came_routestat_t (struct_came_routestat_t)
    routeSpeed: int (POINTER(h))
    field7E: int (POINTER(H))
    field80: int (POINTER(I))
    field84: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    cameEntry: POINTER_T[struct_nkm_came_entry_t]
    routestat1: struct_came_routestat_t
    routestat2: struct_came_routestat_t
    routeSpeed: int
    field7E: int
    field80: int
    field84: int

class struct_camera_t(Structure):
    """
    ```python
    up: struct_VecFx32 (struct_VecFx32)
    right: struct_VecFx32 (struct_VecFx32)
    target: struct_VecFx32 (struct_VecFx32)
    position: struct_VecFx32 (struct_VecFx32)
    mtx: union_MtxFx43 (union_MtxFx43)
    fov: int (POINTER(i))
    targetFov: int (POINTER(i))
    fovSin: fx16 (struct_fx16)
    fovCos: fx16 (struct_fx16)
    aspectRatio: fx32 (struct_fx32)
    frustumNear: fx32 (struct_fx32)
    frustumFar: fx32 (struct_fx32)
    frustumTop: fx32 (struct_fx32)
    frustumBottom: fx32 (struct_fx32)
    frustumLeft: fx32 (struct_fx32)
    frustumRight: fx32 (struct_fx32)
    field88: fx32 (struct_fx32)
    skyFrustumFar: fx32 (struct_fx32)
    lookAtTarget: struct_VecFx32 (struct_VecFx32)
    lookAtPosition: struct_VecFx32 (struct_VecFx32)
    fieldA8: struct_VecFx32 (struct_VecFx32)
    fieldB4: struct_VecFx32 (struct_VecFx32)
    upConst: struct_VecFx32 (struct_VecFx32)
    fieldCC: fx32 (struct_fx32)
    fieldD0: int (POINTER(i))
    targetElevation: fx32 (struct_fx32)
    fieldD8: int (POINTER(I))
    fieldDC: int (POINTER(I))
    fieldE0: int (POINTER(I))
    fieldE4: struct_VecFx32 (struct_VecFx32)
    playerOffsetDirection: fx32 (struct_fx32)
    fieldF4: struct_VecFx32 (struct_VecFx32)
    field100: struct_VecFx32 (struct_VecFx32)
    field10C: struct_VecFx32 (struct_VecFx32)
    field118: struct_VecFx32 (struct_VecFx32)
    field124: struct_VecFx32 (struct_VecFx32)
    field130: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    prevPosition: struct_VecFx32 (struct_VecFx32)
    isShaking: int (POINTER(i))
    field144: fx32 (struct_fx32)
    shakeAmount: fx32 (struct_fx32)
    field14C: int (POINTER(I))
    field150: int (POINTER(h))
    PADDING_1: list[int] (POINTER(B)[2])
    shakeDecay: fx32 (struct_fx32)
    field158: int (POINTER(I))
    targetDirection: struct_VecFx32 (struct_VecFx32)
    field168: fx32 (struct_fx32)
    field16C: int (POINTER(I))
    field170: int (POINTER(I))
    field174: int (POINTER(I))
    elevation: fx32 (struct_fx32)
    field17C: struct_VecFx32 (struct_VecFx32)
    field188: struct_VecFx32 (struct_VecFx32)
    routeStat: struct_came_routestat_t (struct_came_routestat_t)
    routeStat2: struct_came_routestat_t (struct_came_routestat_t)
    field20C: int (POINTER(H))
    field20E: int (POINTER(H))
    targetDriverId: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    currentCamId: int (POINTER(I))
    cameEntry: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    unknownMgCams: POINTER_T[struct_came_unknown_t] (POINTER(struct_came_unknown_t))
    unknownMgCamsCopy: POINTER_T[struct_came_unknown_t] (POINTER(struct_came_unknown_t))
    field224: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    field228: int (POINTER(I))
    field22C: int (POINTER(H))
    PADDING_4: list[int] (POINTER(B)[2])
    field230: int (POINTER(I))
    field234: int (POINTER(I))
    field238: int (POINTER(i))
    frameCounter: int (POINTER(H))
    PADDING_5: list[int] (POINTER(B)[2])
    fovProgress: fx32 (struct_fx32)
    targetProgress: fx32 (struct_fx32)
    field248: int (POINTER(I))
    mode: int (POINTER(I))
    field250: int (POINTER(I))
    field254: int (POINTER(I))
    field258: int (POINTER(i))
    field25C: int (POINTER(I))
    field260: struct_VecFx32 (struct_VecFx32)
    field26C: int (POINTER(h))
    field26E: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    up: struct_VecFx32
    right: struct_VecFx32
    target: struct_VecFx32
    position: struct_VecFx32
    mtx: union_MtxFx43
    fov: int
    targetFov: int
    fovSin: fx16
    fovCos: fx16
    aspectRatio: fx32
    frustumNear: fx32
    frustumFar: fx32
    frustumTop: fx32
    frustumBottom: fx32
    frustumLeft: fx32
    frustumRight: fx32
    field88: fx32
    skyFrustumFar: fx32
    lookAtTarget: struct_VecFx32
    lookAtPosition: struct_VecFx32
    fieldA8: struct_VecFx32
    fieldB4: struct_VecFx32
    upConst: struct_VecFx32
    fieldCC: fx32
    fieldD0: int
    targetElevation: fx32
    fieldD8: int
    fieldDC: int
    fieldE0: int
    fieldE4: struct_VecFx32
    playerOffsetDirection: fx32
    fieldF4: struct_VecFx32
    field100: struct_VecFx32
    field10C: struct_VecFx32
    field118: struct_VecFx32
    field124: struct_VecFx32
    field130: int
    PADDING_0: list[int]
    prevPosition: struct_VecFx32
    isShaking: int
    field144: fx32
    shakeAmount: fx32
    field14C: int
    field150: int
    PADDING_1: list[int]
    shakeDecay: fx32
    field158: int
    targetDirection: struct_VecFx32
    field168: fx32
    field16C: int
    field170: int
    field174: int
    elevation: fx32
    field17C: struct_VecFx32
    field188: struct_VecFx32
    routeStat: struct_came_routestat_t
    routeStat2: struct_came_routestat_t
    field20C: int
    field20E: int
    targetDriverId: int
    PADDING_2: list[int]
    currentCamId: int
    cameEntry: POINTER_T[struct_nkm_came_entry_t]
    unknownMgCams: POINTER_T[struct_came_unknown_t]
    unknownMgCamsCopy: POINTER_T[struct_came_unknown_t]
    field224: int
    PADDING_3: list[int]
    field228: int
    field22C: int
    PADDING_4: list[int]
    field230: int
    field234: int
    field238: int
    frameCounter: int
    PADDING_5: list[int]
    fovProgress: fx32
    targetProgress: fx32
    field248: int
    mode: int
    field250: int
    field254: int
    field258: int
    field25C: int
    field260: struct_VecFx32
    field26C: int
    field26E: int

class struct_chandelier_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbcaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    counter: int (POINTER(i))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbcaFrame: int
    PADDING_0: list[int]
    counter: int
    state: int

class struct_charkart_colors_t(Structure):
    """
    ```python
    diffuse: int (POINTER(H))
    emission: int (POINTER(H))
    ambient: int (POINTER(H))
    diffR: int (POINTER(H))
    diffG: int (POINTER(H))
    diffB: int (POINTER(H))
    diffRDelta: int (POINTER(h))
    diffGDelta: int (POINTER(h))
    diffBDelta: int (POINTER(h))
    emiR: int (POINTER(H))
    emiG: int (POINTER(H))
    emiB: int (POINTER(H))
    emiRDelta: int (POINTER(h))
    emiGDelta: int (POINTER(h))
    emiBDelta: int (POINTER(h))
    ambiR: int (POINTER(H))
    ambiG: int (POINTER(H))
    amibB: int (POINTER(H))
    amibRDelta: int (POINTER(h))
    ambiGDelta: int (POINTER(h))
    ambiBDelta: int (POINTER(h))
    progress: fx16 (struct_fx16)
    ```
    """
    _pack_: ClassVar[int] = 1
    diffuse: int
    emission: int
    ambient: int
    diffR: int
    diffG: int
    diffB: int
    diffRDelta: int
    diffGDelta: int
    diffBDelta: int
    emiR: int
    emiG: int
    emiB: int
    emiRDelta: int
    emiGDelta: int
    emiBDelta: int
    ambiR: int
    ambiG: int
    amibB: int
    amibRDelta: int
    ambiGDelta: int
    ambiBDelta: int
    progress: fx16

class struct_charkart_field24_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    field10: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field14: int (POINTER(i))
    field18: int (POINTER(H))
    field1A: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    field10: int
    PADDING_0: list[int]
    field14: int
    field18: int
    field1A: int

class struct_charkart_t(Structure):
    """
    ```python
    characterId: int (POINTER(I))
    kartId: int (POINTER(i))
    characterNsbcaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    characterNsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    characterModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartTireModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartShadowModel: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    kartOffsetData: POINTER_T[struct_kofs_entry_t] (POINTER(struct_kofs_entry_t))
    field24: struct_charkart_field24_t (struct_charkart_field24_t)
    light: struct_light_t (struct_light_t)
    PADDING_0: list[int] (POINTER(B)[2])
    field54: int (POINTER(I))
    isKartInvisible: int (POINTER(i))
    isCharacterInvisible: int (POINTER(i))
    useSeparateTires: int (POINTER(i))
    inStarToonMode: int (POINTER(i))
    kartABC: int (POINTER(H))
    colors: struct_charkart_colors_t (struct_charkart_colors_t)
    PADDING_1: list[int] (POINTER(B)[2])
    field98: struct_anim_animator_t (struct_anim_animator_t)
    nsbtpAnimDisabled: int (POINTER(i))
    fieldB0: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    characterId: int
    kartId: int
    characterNsbcaAnim: POINTER_T[struct_anim_manager_t]
    characterNsbtpAnim: POINTER_T[struct_anim_manager_t]
    characterModel: POINTER_T[struct_model_t]
    kartModel: POINTER_T[struct_model_t]
    kartTireModel: POINTER_T[struct_model_t]
    kartShadowModel: POINTER_T[struct_model_t]
    kartOffsetData: POINTER_T[struct_kofs_entry_t]
    field24: struct_charkart_field24_t
    light: struct_light_t
    PADDING_0: list[int]
    field54: int
    isKartInvisible: int
    isCharacterInvisible: int
    useSeparateTires: int
    inStarToonMode: int
    kartABC: int
    colors: struct_charkart_colors_t
    PADDING_1: list[int]
    field98: struct_anim_animator_t
    nsbtpAnimDisabled: int
    fieldB0: int

class struct_choropu_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    setting1: int (POINTER(I))
    setting0: int (POINTER(I))
    fieldA8: int (POINTER(I))
    fieldAC: int (POINTER(i))
    fieldB0: int (POINTER(i))
    fieldB4: int (POINTER(i))
    rotZ: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    shadow: struct_objshadow_t (struct_objshadow_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    setting1: int
    setting0: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    fieldB4: int
    rotZ: int
    PADDING_0: list[int]
    shadow: struct_objshadow_t

class struct_cklcr_char_def_t(Structure):
    """
    ```python
    playerModelName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    enemyModelName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    emblemName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ```
    """
    _pack_: ClassVar[int] = 1
    playerModelName: POINTER_T[c_ubyte]
    enemyModelName: POINTER_T[c_ubyte]
    emblemName: POINTER_T[c_ubyte]

class struct_cklcr_kart_def_t(Structure):
    """
    ```python
    kartModelName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    kartShadowName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ```
    """
    _pack_: ClassVar[int] = 1
    kartModelName: POINTER_T[c_ubyte]
    kartShadowName: POINTER_T[c_ubyte]

class struct_col_entry_t(Structure):
    """
    ```python
    segmentRightEndpoint: int (POINTER(h))
    segmentLeftEndpoint: int (POINTER(h))
    zMax: fx32 (struct_fx32)
    zMin: fx32 (struct_fx32)
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    boundingSphereRadius: fx32 (struct_fx32)
    flags: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    object: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    segmentRightEndpoint: int
    segmentLeftEndpoint: int
    zMax: fx32
    zMin: fx32
    position: POINTER_T[struct_VecFx32]
    boundingSphereRadius: fx32
    flags: int
    PADDING_0: list[int]
    object: c_void_p

class struct_col_response_t(Structure):
    """
    ```python
    maxSomething: struct_VecFx32 (struct_VecFx32)
    minSomething: struct_VecFx32 (struct_VecFx32)
    distance: fx32 (struct_fx32)
    normal: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    maxSomething: struct_VecFx32
    minSomething: struct_VecFx32
    distance: fx32
    normal: struct_VecFx32

class struct_col_segment_left_endpoint_t(Structure):
    """
    ```python
    rightEndpoint: int (POINTER(B))
    colEntryId: int (POINTER(B))
    xPos: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    rightEndpoint: int
    colEntryId: int
    xPos: int

class struct_col_segment_right_endpoint_t(Structure):
    """
    ```python
    leftEndpoint: int (POINTER(B))
    minLeftEndpoint: int (POINTER(B))
    xPos: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    leftEndpoint: int
    minLeftEndpoint: int
    xPos: int

class struct_cow_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class struct_crab_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(H))
    rotZ: int (POINTER(H))
    counter: int (POINTER(i))
    bodyNsbtpFrame: fx32 (struct_fx32)
    handNsbtpFrame: fx32 (struct_fx32)
    fieldB0: struct_sinthing_t (struct_sinthing_t)
    fieldD0: struct_sinthing_t (struct_sinthing_t)
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    rotZ: int
    counter: int
    bodyNsbtpFrame: fx32
    handNsbtpFrame: fx32
    fieldB0: struct_sinthing_t
    fieldD0: struct_sinthing_t
    pathWalker: struct_pw_pathwalker_t
    state: int

class struct_crsmdl_t(Structure):
    """
    ```python
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    modelV: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    nsbtpAnim: struct_anim_manager_t (struct_anim_manager_t)
    nsbtaAnim: struct_anim_manager_t (struct_anim_manager_t)
    nsbtaAnimV: struct_anim_manager_t (struct_anim_manager_t)
    mtx: union_MtxFx43 (union_MtxFx43)
    modelHasPartialFog: int (POINTER(i))
    PADDING_0: list[int] (POINTER(B)[4])
    modelFogFlags: int (POINTER(l))
    modelVHasPartialFog: int (POINTER(i))
    modelVFogFlags: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    model: POINTER_T[struct_model_t]
    modelV: POINTER_T[struct_model_t]
    nsbtpAnim: struct_anim_manager_t
    nsbtaAnim: struct_anim_manager_t
    nsbtaAnimV: struct_anim_manager_t
    mtx: union_MtxFx43
    modelHasPartialFog: int
    PADDING_0: list[int]
    modelFogFlags: int
    modelVHasPartialFog: int
    modelVFogFlags: int
    PADDING_1: list[int]

class struct_dc_masterbright_t(Structure):
    """
    ```python
    state: int (POINTER(H))
    fadeType: int (POINTER(H))
    curFrame: int (POINTER(h))
    frameCount: int (POINTER(h))
    brightness: int (POINTER(h))
    fieldA: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    fadeType: int
    curFrame: int
    frameCount: int
    brightness: int
    fieldA: int

class struct_dce_t(Structure):
    """
    ```python
    mode: int (POINTER(I))
    oamBuf: POINTER_T[struct_GXOamAttr] (POINTER(struct_GXOamAttr))
    flags: int (POINTER(H))
    blurAmount: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    blurProgress: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mode: int
    oamBuf: POINTER_T[struct_GXOamAttr]
    flags: int
    blurAmount: int
    PADDING_0: int
    blurProgress: fx32

class struct_dcol_inst_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    lastMtx: union_MtxFx33 (union_MtxFx33)
    baseMtx: union_MtxFx33 (union_MtxFx33)
    lastPosition: struct_VecFx32 (struct_VecFx32)
    basePos: struct_VecFx32 (struct_VecFx32)
    size: struct_VecFx32 (struct_VecFx32)
    sizeZ2: fx32 (struct_fx32)
    isFloorYZ: int (POINTER(i))
    isFloorXZ: int (POINTER(i))
    isFloorXY: int (POINTER(i))
    isBoostPanel: int (POINTER(i))
    floorThreshold: fx32 (struct_fx32)
    field124: struct_VecFx32 (struct_VecFx32)
    field130: int (POINTER(I))
    shape: int (POINTER(I))
    field138: int (POINTER(I))
    field13C: int (POINTER(I))
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    lastMtx: union_MtxFx33
    baseMtx: union_MtxFx33
    lastPosition: struct_VecFx32
    basePos: struct_VecFx32
    size: struct_VecFx32
    sizeZ2: fx32
    isFloorYZ: int
    isFloorXZ: int
    isFloorXY: int
    isBoostPanel: int
    floorThreshold: fx32
    field124: struct_VecFx32
    field130: int
    shape: int
    field138: int
    field13C: int
    model: POINTER_T[struct_model_t]

class struct_display_config_3d_t(Structure):
    """
    ```python
    clearColor: int (POINTER(H))
    sortMode: int (POINTER(B))
    bufferMode: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    clearColor: int
    sortMode: int
    bufferMode: int

class struct_display_config_base_t(Structure):
    """
    ```python
    vblankWaitCount: int (POINTER(H))
    mainVisiblePlane: int (POINTER(H))
    subVisiblePlane: int (POINTER(H))
    mainDisplayMode: int (POINTER(H))
    mainBgMode: int (POINTER(H))
    mainBg03d: int (POINTER(H))
    subBgMode: int (POINTER(H))
    mainBgBank: int (POINTER(H))
    mainObjBank: int (POINTER(H))
    mainBgExtPlttBank: int (POINTER(H))
    mainObjExtPlttBank: int (POINTER(H))
    texBank: int (POINTER(H))
    texPlttBank: int (POINTER(H))
    clearImgBank: int (POINTER(H))
    subBgBank: int (POINTER(H))
    subObjBank: int (POINTER(H))
    subBgExtPlttBank: int (POINTER(H))
    subObjExtPlttBank: int (POINTER(H))
    arm7Bank: int (POINTER(H))
    lcdcBank: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    vblankWaitCount: int
    mainVisiblePlane: int
    subVisiblePlane: int
    mainDisplayMode: int
    mainBgMode: int
    mainBg03d: int
    subBgMode: int
    mainBgBank: int
    mainObjBank: int
    mainBgExtPlttBank: int
    mainObjExtPlttBank: int
    texBank: int
    texPlttBank: int
    clearImgBank: int
    subBgBank: int
    subObjBank: int
    subBgExtPlttBank: int
    subObjExtPlttBank: int
    arm7Bank: int
    lcdcBank: int

class struct_display_config_bg01_t(Structure):
    """
    ```python
    common: struct_display_config_bgcommon_t (struct_display_config_bgcommon_t)
    extPlttSlot: int (POINTER(H))
    unk: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    common: struct_display_config_bgcommon_t
    extPlttSlot: int
    unk: int

class struct_display_config_bg23_t(Structure):
    """
    ```python
    mode: int (POINTER(I))
    common: struct_display_config_bgcommon_t (struct_display_config_bgcommon_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mode: int
    common: struct_display_config_bgcommon_t

class struct_display_config_bgcommon_t(Structure):
    """
    ```python
    priority: int (POINTER(H))
    mosaic: int (POINTER(H))
    screenSize: int (POINTER(H))
    colorMode: int (POINTER(H))
    screenBase: int (POINTER(H))
    characterBase: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    priority: int
    mosaic: int
    screenSize: int
    colorMode: int
    screenBase: int
    characterBase: int

class struct_display_config_engine_t(Structure):
    """
    ```python
    bg0Config: struct_display_config_bg01_t (struct_display_config_bg01_t)
    bg1Config: struct_display_config_bg01_t (struct_display_config_bg01_t)
    bg2Config: struct_display_config_bg23_t (struct_display_config_bg23_t)
    bg3Config: struct_display_config_bg23_t (struct_display_config_bg23_t)
    objVRamModeChar: int (POINTER(H))
    objVRamModeBmp: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    bg0Config: struct_display_config_bg01_t
    bg1Config: struct_display_config_bg01_t
    bg2Config: struct_display_config_bg23_t
    bg3Config: struct_display_config_bg23_t
    objVRamModeChar: int
    objVRamModeBmp: int

class struct_display_config_t(Structure):
    """
    ```python
    baseConfig: struct_display_config_base_t (struct_display_config_base_t)
    mainConfig: struct_display_config_engine_t (struct_display_config_engine_t)
    config3d: POINTER_T[struct_display_config_3d_t] (POINTER(struct_display_config_3d_t))
    subConfig: struct_display_config_engine_t (struct_display_config_engine_t)
    fieldB4: int (POINTER(I))
    vblankFunc: Callable[[], None] (CFunctionType)
    PADDING_0: list[int] (POINTER(B)[4])
    frameStartTime: int (POINTER(L))
    vblankTime: int (POINTER(L))
    renderDuration: int (POINTER(I))
    lastTotalDuration: int (POINTER(I))
    lastRenderDuration: int (POINTER(I))
    flags: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    baseConfig: struct_display_config_base_t
    mainConfig: struct_display_config_engine_t
    config3d: POINTER_T[struct_display_config_3d_t]
    subConfig: struct_display_config_engine_t
    fieldB4: int
    vblankFunc: Callable[[], None]
    PADDING_0: list[int]
    frameStartTime: int
    vblankTime: int
    renderDuration: int
    lastTotalDuration: int
    lastRenderDuration: int
    flags: int
    PADDING_1: list[int]

class struct_dossun_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    state: int (POINTER(I))
    stateCounter: int (POINTER(i))
    someSpeed: fx32 (struct_fx32)
    floorY: fx32 (struct_fx32)
    isSmashing: int (POINTER(i))
    starHitAnimState: int (POINTER(I))
    rotYDelta: int (POINTER(h))
    rotY: int (POINTER(h))
    lastStarHitFrame: int (POINTER(I))
    noStarHitPlayerMask: int (POINTER(H))
    sinAng: int (POINTER(H))
    sinAmplitude: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    initialPathPoint: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    isHorizontalMoveType: int (POINTER(i))
    fieldF4: struct_VecFx32 (struct_VecFx32)
    field100: fx32 (struct_fx32)
    someAcceleration: fx32 (struct_fx32)
    anotherSpeed: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    state: int
    stateCounter: int
    someSpeed: fx32
    floorY: fx32
    isSmashing: int
    starHitAnimState: int
    rotYDelta: int
    rotY: int
    lastStarHitFrame: int
    noStarHitPlayerMask: int
    sinAng: int
    sinAmplitude: fx32
    pathwalker: struct_pw_pathwalker_t
    initialPathPoint: int
    PADDING_0: list[int]
    isHorizontalMoveType: int
    fieldF4: struct_VecFx32
    field100: fx32
    someAcceleration: fx32
    anotherSpeed: fx32

class struct_dptc_t(Structure):
    """
    ```python
    whiteDustCloudEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    blueSparkEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    contRedSparkEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    contRedSparkSmallEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    redSparkEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    redSparksSmallEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    contRedSparksCounter: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    field34: int (POINTER(i))
    contRedSparksActive: int (POINTER(i))
    whiteDustCloudsActive: int (POINTER(i))
    redSparksActive: int (POINTER(i))
    blueSparksActive: int (POINTER(i))
    redSparksCounter: int (POINTER(h))
    blueSparkCounter: int (POINTER(h))
    whiteDustCloudParticleId: int (POINTER(i))
    contRedSparkParticleId: int (POINTER(i))
    contRedSparkSmallParticleId: int (POINTER(i))
    redSparkParticleId: int (POINTER(i))
    redSparksSmallParticleId: int (POINTER(i))
    driverId: int (POINTER(H))
    field62: int (POINTER(H))
    field64: int (POINTER(i))
    startContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    suspendContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    resumeContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    killContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    field78: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    hideAllFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    showAllFunc: Callable[[POINTER_T[struct_dptc_t]], None] (CFunctionType)
    updateContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t], POINTER_T[struct_VecFx16], POINTER_T[struct_VecFx32]], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    whiteDustCloudEmitters: list[POINTER_T[struct_spa_emitter_t]]
    blueSparkEmitters: list[POINTER_T[struct_spa_emitter_t]]
    contRedSparkEmitters: list[POINTER_T[struct_spa_emitter_t]]
    contRedSparkSmallEmitters: list[POINTER_T[struct_spa_emitter_t]]
    redSparkEmitters: list[POINTER_T[struct_spa_emitter_t]]
    redSparksSmallEmitters: list[POINTER_T[struct_spa_emitter_t]]
    contRedSparksCounter: int
    PADDING_0: list[int]
    field34: int
    contRedSparksActive: int
    whiteDustCloudsActive: int
    redSparksActive: int
    blueSparksActive: int
    redSparksCounter: int
    blueSparkCounter: int
    whiteDustCloudParticleId: int
    contRedSparkParticleId: int
    contRedSparkSmallParticleId: int
    redSparkParticleId: int
    redSparksSmallParticleId: int
    driverId: int
    field62: int
    field64: int
    startContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    suspendContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    resumeContinuousRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    killContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    field78: Callable[[POINTER_T[struct_dptc_t]], None]
    hideAllFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    showAllFunc: Callable[[POINTER_T[struct_dptc_t]], None]
    updateContRedSparksFunc: Callable[[POINTER_T[struct_dptc_t], POINTER_T[struct_VecFx16], POINTER_T[struct_VecFx32]], None]

class struct_dram_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    startStopFrameCount: int (POINTER(H))
    spinFrameCount: int (POINTER(H))
    waitFrameCount: int (POINTER(H))
    angle: int (POINTER(H))
    angularSpeed: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    currentSpeed: fx32 (struct_fx32)
    startStopSpeed: fx32 (struct_fx32)
    speeds: list[int] (POINTER(h)[3])
    PADDING_1: list[int] (POINTER(B)[2])
    alignRemainder: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    startStopFrameCount: int
    spinFrameCount: int
    waitFrameCount: int
    angle: int
    angularSpeed: int
    PADDING_0: list[int]
    currentSpeed: fx32
    startStopSpeed: fx32
    speeds: list[int]
    PADDING_1: list[int]
    alignRemainder: int

class struct_driver_field450_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    field8: fx32 (struct_fx32)
    fieldC: int (POINTER(i))
    field10: int (POINTER(i))
    field14: int (POINTER(i))
    field18: fx32 (struct_fx32)
    field1C: fx32 (struct_fx32)
    field20: fx32 (struct_fx32)
    field24: fx32 (struct_fx32)
    prevLapProgress: int (POINTER(i))
    kaidanSfxAlternateCounter: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    field30: int (POINTER(i))
    field34: int (POINTER(i))
    sfxId: int (POINTER(i))
    computePitchOffsetFunc: Callable[[POINTER_T[struct_sfx_emitter_ex_params_t]], c_int] (CFunctionType)
    field40: struct_struc_334 (struct_struc_334)
    field68: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    PADDING_0: list[int]
    field8: fx32
    fieldC: int
    field10: int
    field14: int
    field18: fx32
    field1C: fx32
    field20: fx32
    field24: fx32
    prevLapProgress: int
    kaidanSfxAlternateCounter: int
    PADDING_1: list[int]
    field30: int
    field34: int
    sfxId: int
    computePitchOffsetFunc: Callable[[POINTER_T[struct_sfx_emitter_ex_params_t]], c_int]
    field40: struct_struc_334
    field68: int

class struct_driver_field514_field8C_entry_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    field8: int (POINTER(h))
    gapA: list[int] (POINTER(B)[2])
    fieldC: struct_struc_351 (struct_struc_351)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    field8: int
    gapA: list[int]
    fieldC: struct_struc_351

class struct_driver_net_state_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    fieldC: int (POINTER(H))
    fieldE: int (POINTER(H))
    field10: struct_VecFx32 (struct_VecFx32)
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: fx32 (struct_fx32)
    field28: int (POINTER(i))
    flags: int (POINTER(i))
    lastFlags: int (POINTER(i))
    field34: struct_VecFx32 (struct_VecFx32)
    driftRotY: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    field44: int (POINTER(i))
    field48: int (POINTER(I))
    field4C: quaternion_t (struct_quaternion_t)
    field5C: int (POINTER(h))
    PADDING_1: list[int] (POINTER(B)[2])
    field60: int (POINTER(i))
    field64: int (POINTER(i))
    gap68: list[int] (POINTER(B)[24])
    field80: struct_NNSFndList (struct_NNSFndList)
    field8C: struct_NNSFndList (struct_NNSFndList)
    field98: struct_VecFx32 (struct_VecFx32)
    fieldA4: int (POINTER(I))
    fieldA8: struct_VecFx32 (struct_VecFx32)
    fieldB4: int (POINTER(H))
    gapB6: list[int] (POINTER(B)[1])
    fieldB7: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    fieldC: int
    fieldE: int
    field10: struct_VecFx32
    field1C: int
    field20: int
    field24: fx32
    field28: int
    flags: int
    lastFlags: int
    field34: struct_VecFx32
    driftRotY: int
    PADDING_0: list[int]
    field44: int
    field48: int
    field4C: quaternion_t
    field5C: int
    PADDING_1: list[int]
    field60: int
    field64: int
    gap68: list[int]
    field80: struct_NNSFndList
    field8C: struct_NNSFndList
    field98: struct_VecFx32
    fieldA4: int
    fieldA8: struct_VecFx32
    fieldB4: int
    gapB6: list[int]
    fieldB7: int

class struct_driver_statistics_t(Structure):
    """
    ```python
    gotStartBoost: int (POINTER(i))
    powerSlideCount: int (POINTER(I))
    itemHitCount: int (POINTER(i))
    offRoadTime: int (POINTER(I))
    wallHitCount: int (POINTER(i))
    damageCount: int (POINTER(i))
    respawnCount: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    gotStartBoost: int
    powerSlideCount: int
    itemHitCount: int
    offRoadTime: int
    wallHitCount: int
    damageCount: int
    respawnCount: int

class struct_driver_t(Structure):
    """
    ```python
    soundEmitter: struct_sfx_emitter_t (struct_sfx_emitter_t)
    field44: int (POINTER(I))
    flags: int (POINTER(I))
    flags2: int (POINTER(I))
    direction: struct_VecFx32 (struct_VecFx32)
    drivingDirection: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    id: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    inputId: int (POINTER(I))
    field7C: int (POINTER(I))
    position: struct_VecFx32 (struct_VecFx32)
    lastPosition: struct_VecFx32 (struct_VecFx32)
    kartTiresPosition: struct_VecFx32 (struct_VecFx32)
    deltaPos: struct_VecFx32 (struct_VecFx32)
    deltaPosNormalized: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    fieldC8: fx32 (struct_fx32)
    targetMaxSpeed: fx32 (struct_fx32)
    maxSpeed: fx32 (struct_fx32)
    fieldD4: int (POINTER(I))
    slipstreamSpeedMultiplier: fx32 (struct_fx32)
    speedMultiplier: fx32 (struct_fx32)
    rotation: quaternion_t (struct_quaternion_t)
    fieldF0: quaternion_t (struct_quaternion_t)
    field100: quaternion_t (struct_quaternion_t)
    field110: quaternion_t (struct_quaternion_t)
    mainMtx: union_MtxFx43 (union_MtxFx43)
    field150: union_MtxFx43 (union_MtxFx43)
    colReaction: int (POINTER(I))
    field184: union_MtxFx43 (union_MtxFx43)
    charKartMtx: int (POINTER(I))
    colPos: struct_VecFx32 (struct_VecFx32)
    prevColPos: struct_VecFx32 (struct_VecFx32)
    colSphereSize: fx32 (struct_fx32)
    colSphereZOffset: fx32 (struct_fx32)
    netColPos: struct_VecFx32 (struct_VecFx32)
    lastNetColPos: struct_VecFx32 (struct_VecFx32)
    colPos2: struct_VecFx32 (struct_VecFx32)
    field1FC: struct_VecFx32 (struct_VecFx32)
    field208: POINTER_T[c_uint] (POINTER(POINTER(I)))
    field20C: list[c_void_p] (c_void_p[9])
    field230: Callable[[POINTER_T[struct_driver_t]], None] (CFunctionType)
    xRot: int (POINTER(h))
    yRot: int (POINTER(H))
    boostTimer: int (POINTER(h))
    field23A: int (POINTER(h))
    driftBoostCounter: int (POINTER(h))
    PADDING_1: list[int] (POINTER(B)[2])
    velocityMinusDirMultiplier: fx32 (struct_fx32)
    upDir: struct_VecFx32 (struct_VecFx32)
    field250: struct_VecFx32 (struct_VecFx32)
    velocityY: struct_VecFx32 (struct_VecFx32)
    fallsWaterForward: struct_VecFx32 (struct_VecFx32)
    fallsWaterStrength: fx32 (struct_fx32)
    forwardDir: struct_VecFx32 (struct_VecFx32)
    jumpDriftUp: struct_VecFx32 (struct_VecFx32)
    jumpDriftForward: struct_VecFx32 (struct_VecFx32)
    collisionMode: int (POINTER(I))
    maxSpeedFraction: fx32 (struct_fx32)
    deltaPosMag: fx32 (struct_fx32)
    speed: fx32 (struct_fx32)
    field2AC: fx32 (struct_fx32)
    driverHitCheckMask: int (POINTER(H))
    driverHitMask: int (POINTER(H))
    lastDriverHitMask: int (POINTER(H))
    gap2B6: list[int] (POINTER(B)[2])
    field2B8: int (POINTER(i))
    field2BC: int (POINTER(i))
    field2C0: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    leftRightDir: fx32 (struct_fx32)
    colEntryId1: int (POINTER(h))
    colEntryId2: int (POINTER(h))
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t] (POINTER(struct_physp_kart_params_t))
    charPhysicalParams: POINTER_T[struct_physp_char_params_t] (POINTER(struct_physp_char_params_t))
    turningAmount: fx32 (struct_fx32)
    field2D8: struct_VecFx32 (struct_VecFx32)
    field2E4: struct_VecFx32 (struct_VecFx32)
    field2F0: struct_VecFx32 (struct_VecFx32)
    driftLeftRightCount: int (POINTER(i))
    driftLeftCount: int (POINTER(H))
    driftRightCount: int (POINTER(H))
    driftDir1CountPtr: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    driftDir2CountPtr: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    driftLeftRightTimeout: int (POINTER(i))
    enemyState: POINTER_T[struct_enemy_t] (POINTER(struct_enemy_t))
    field314: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    field318: fx32 (struct_fx32)
    field31C: struct_VecFx32 (struct_VecFx32)
    field328: struct_VecFx32 (struct_VecFx32)
    field334: int (POINTER(I))
    field338: int (POINTER(H))
    PADDING_4: list[int] (POINTER(B)[2])
    field33C: int (POINTER(I))
    field340: fx32 (struct_fx32)
    field344: int (POINTER(I))
    field348: int (POINTER(I))
    field34C: quaternion_t (struct_quaternion_t)
    colReactionCounter: int (POINTER(h))
    PADDING_5: list[int] (POINTER(B)[2])
    field360: fx32 (struct_fx32)
    spinOutAngle: int (POINTER(H))
    spinOutSpinCount: int (POINTER(H))
    spinOutProgress: fx32 (struct_fx32)
    spinOutVelocity: int (POINTER(I))
    field370: int (POINTER(H))
    PADDING_6: list[int] (POINTER(B)[2])
    field374: struct_VecFx32 (struct_VecFx32)
    field380: int (POINTER(I))
    ghostFlickerPhase: int (POINTER(H))
    wallRotYSpeed: int (POINTER(h))
    driftRotY: int (POINTER(h))
    extraDrift: fx16 (struct_fx16)
    field38C: fx32 (struct_fx32)
    gap390: list[int] (POINTER(B)[4])
    field394: int (POINTER(I))
    field398: fx32 (struct_fx32)
    field39C: fx32 (struct_fx32)
    field3A0: fx32 (struct_fx32)
    tireRotX: int (POINTER(H))
    PADDING_7: list[int] (POINTER(B)[2])
    field3A8: int (POINTER(i))
    respawnCounter: int (POINTER(H))
    PADDING_8: list[int] (POINTER(B)[2])
    field3B0: struct_VecFx32 (struct_VecFx32)
    field3BC: int (POINTER(H))
    field3BE: int (POINTER(h))
    preRespawnCounter: int (POINTER(h))
    PADDING_9: list[int] (POINTER(B)[2])
    respawnId: int (POINTER(I))
    killTimer: int (POINTER(h))
    PADDING_10: list[int] (POINTER(B)[2])
    driverVoiceIdx: int (POINTER(I))
    kartABC: int (POINTER(h))
    field3D2: int (POINTER(h))
    field3D4: int (POINTER(h))
    PADDING_11: list[int] (POINTER(B)[2])
    place: int (POINTER(i))
    floorDriverColType: int (POINTER(I))
    floorColType: int (POINTER(I))
    floorColVariant: int (POINTER(i))
    field3E8: int (POINTER(h))
    PADDING_12: list[int] (POINTER(B)[2])
    yRotSpeedTarget: int (POINTER(I))
    yRotSpeed: int (POINTER(I))
    field3F4: fx32 (struct_fx32)
    field3F8: fx32 (struct_fx32)
    field3FC: int (POINTER(H))
    field3FE: int (POINTER(H))
    field400: int (POINTER(H))
    PADDING_13: list[int] (POINTER(B)[2])
    field404: fx32 (struct_fx32)
    field408: int (POINTER(I))
    respawnStartFrame: int (POINTER(I))
    respawnAPressFrame: int (POINTER(I))
    field414: fx32 (struct_fx32)
    field418: fx32 (struct_fx32)
    growBackScale: struct_VecFx32 (struct_VecFx32)
    thunderScale: struct_VecFx32 (struct_VecFx32)
    dossunYScale: fx32 (struct_fx32)
    mobjHitList: list[POINTER_T[struct_mobj_inst_t]] (POINTER(struct_mobj_inst_t)[2])
    mobjHitSfxTimeout: list[int] (POINTER(H)[2])
    mobjHitEmittedSfx: list[int] (POINTER(i)[2])
    smashDossun: POINTER_T[struct_mobj_inst_t] (POINTER(struct_mobj_inst_t))
    field450: struct_driver_field450_t (struct_driver_field450_t)
    field4BC: fx32 (struct_fx32)
    colFlagsMap2DShadow: int (POINTER(I))
    jumpPadSpeed: int (POINTER(I))
    field4C8: fx32 (struct_fx32)
    field4CC: int (POINTER(I))
    field4D0: int (POINTER(I))
    preStartEnginePower: fx32 (struct_fx32)
    fallsWaterDstId: int (POINTER(h))
    wallTouchTimeout: int (POINTER(h))
    floorTouchTimeout: int (POINTER(h))
    field4DE: int (POINTER(h))
    field4E0: int (POINTER(h))
    field4E2: int (POINTER(h))
    field4E4: int (POINTER(H))
    field4E6: int (POINTER(H))
    field4E8: fx32 (struct_fx32)
    field4EC: fx32 (struct_fx32)
    idkScale: struct_VecFx32 (struct_VecFx32)
    field4FC: int (POINTER(H))
    PADDING_14: list[int] (POINTER(B)[2])
    waterDepth: fx32 (struct_fx32)
    field504: int (POINTER(H))
    field506: int (POINTER(H))
    field508: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    field50C: POINTER_T[struct_quaternion_t] (POINTER(struct_quaternion_t))
    field510: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    netState: POINTER_T[struct_driver_net_state_t] (POINTER(struct_driver_net_state_t))
    field518: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    field534: c_void_p (c_void_p)
    timers: struct_driver_timers_t (struct_driver_timers_t)
    charKart: POINTER_T[struct_charkart_t] (POINTER(struct_charkart_t))
    field594: fx32 (struct_fx32)
    field598: int (POINTER(h))
    PADDING_15: list[int] (POINTER(B)[2])
    field59C: int (POINTER(I))
    field5A0: int (POINTER(H))
    gap5A2: list[int] (POINTER(B)[2])
    field5A4: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    soundEmitter: struct_sfx_emitter_t
    field44: int
    flags: int
    flags2: int
    direction: struct_VecFx32
    drivingDirection: struct_VecFx32
    velocity: struct_VecFx32
    id: int
    PADDING_0: list[int]
    inputId: int
    field7C: int
    position: struct_VecFx32
    lastPosition: struct_VecFx32
    kartTiresPosition: struct_VecFx32
    deltaPos: struct_VecFx32
    deltaPosNormalized: struct_VecFx32
    scale: struct_VecFx32
    fieldC8: fx32
    targetMaxSpeed: fx32
    maxSpeed: fx32
    fieldD4: int
    slipstreamSpeedMultiplier: fx32
    speedMultiplier: fx32
    rotation: quaternion_t
    fieldF0: quaternion_t
    field100: quaternion_t
    field110: quaternion_t
    mainMtx: union_MtxFx43
    field150: union_MtxFx43
    colReaction: int
    field184: union_MtxFx43
    charKartMtx: int
    colPos: struct_VecFx32
    prevColPos: struct_VecFx32
    colSphereSize: fx32
    colSphereZOffset: fx32
    netColPos: struct_VecFx32
    lastNetColPos: struct_VecFx32
    colPos2: struct_VecFx32
    field1FC: struct_VecFx32
    field208: POINTER_T[c_uint]
    field20C: list[c_void_p]
    field230: Callable[[POINTER_T[struct_driver_t]], None]
    xRot: int
    yRot: int
    boostTimer: int
    field23A: int
    driftBoostCounter: int
    PADDING_1: list[int]
    velocityMinusDirMultiplier: fx32
    upDir: struct_VecFx32
    field250: struct_VecFx32
    velocityY: struct_VecFx32
    fallsWaterForward: struct_VecFx32
    fallsWaterStrength: fx32
    forwardDir: struct_VecFx32
    jumpDriftUp: struct_VecFx32
    jumpDriftForward: struct_VecFx32
    collisionMode: int
    maxSpeedFraction: fx32
    deltaPosMag: fx32
    speed: fx32
    field2AC: fx32
    driverHitCheckMask: int
    driverHitMask: int
    lastDriverHitMask: int
    gap2B6: list[int]
    field2B8: int
    field2BC: int
    field2C0: int
    PADDING_2: list[int]
    leftRightDir: fx32
    colEntryId1: int
    colEntryId2: int
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t]
    charPhysicalParams: POINTER_T[struct_physp_char_params_t]
    turningAmount: fx32
    field2D8: struct_VecFx32
    field2E4: struct_VecFx32
    field2F0: struct_VecFx32
    driftLeftRightCount: int
    driftLeftCount: int
    driftRightCount: int
    driftDir1CountPtr: POINTER_T[c_ushort]
    driftDir2CountPtr: POINTER_T[c_ushort]
    driftLeftRightTimeout: int
    enemyState: POINTER_T[struct_enemy_t]
    field314: int
    PADDING_3: list[int]
    field318: fx32
    field31C: struct_VecFx32
    field328: struct_VecFx32
    field334: int
    field338: int
    PADDING_4: list[int]
    field33C: int
    field340: fx32
    field344: int
    field348: int
    field34C: quaternion_t
    colReactionCounter: int
    PADDING_5: list[int]
    field360: fx32
    spinOutAngle: int
    spinOutSpinCount: int
    spinOutProgress: fx32
    spinOutVelocity: int
    field370: int
    PADDING_6: list[int]
    field374: struct_VecFx32
    field380: int
    ghostFlickerPhase: int
    wallRotYSpeed: int
    driftRotY: int
    extraDrift: fx16
    field38C: fx32
    gap390: list[int]
    field394: int
    field398: fx32
    field39C: fx32
    field3A0: fx32
    tireRotX: int
    PADDING_7: list[int]
    field3A8: int
    respawnCounter: int
    PADDING_8: list[int]
    field3B0: struct_VecFx32
    field3BC: int
    field3BE: int
    preRespawnCounter: int
    PADDING_9: list[int]
    respawnId: int
    killTimer: int
    PADDING_10: list[int]
    driverVoiceIdx: int
    kartABC: int
    field3D2: int
    field3D4: int
    PADDING_11: list[int]
    place: int
    floorDriverColType: int
    floorColType: int
    floorColVariant: int
    field3E8: int
    PADDING_12: list[int]
    yRotSpeedTarget: int
    yRotSpeed: int
    field3F4: fx32
    field3F8: fx32
    field3FC: int
    field3FE: int
    field400: int
    PADDING_13: list[int]
    field404: fx32
    field408: int
    respawnStartFrame: int
    respawnAPressFrame: int
    field414: fx32
    field418: fx32
    growBackScale: struct_VecFx32
    thunderScale: struct_VecFx32
    dossunYScale: fx32
    mobjHitList: list[POINTER_T[struct_mobj_inst_t]]
    mobjHitSfxTimeout: list[int]
    mobjHitEmittedSfx: list[int]
    smashDossun: POINTER_T[struct_mobj_inst_t]
    field450: struct_driver_field450_t
    field4BC: fx32
    colFlagsMap2DShadow: int
    jumpPadSpeed: int
    field4C8: fx32
    field4CC: int
    field4D0: int
    preStartEnginePower: fx32
    fallsWaterDstId: int
    wallTouchTimeout: int
    floorTouchTimeout: int
    field4DE: int
    field4E0: int
    field4E2: int
    field4E4: int
    field4E6: int
    field4E8: fx32
    field4EC: fx32
    idkScale: struct_VecFx32
    field4FC: int
    PADDING_14: list[int]
    waterDepth: fx32
    field504: int
    field506: int
    field508: POINTER_T[struct_VecFx32]
    field50C: POINTER_T[struct_quaternion_t]
    field510: POINTER_T[struct_VecFx32]
    netState: POINTER_T[struct_driver_net_state_t]
    field518: struct_sfx_emitter_ex_params_t
    field534: c_void_p
    timers: struct_driver_timers_t
    charKart: POINTER_T[struct_charkart_t]
    field594: fx32
    field598: int
    PADDING_15: list[int]
    field59C: int
    field5A0: int
    gap5A2: list[int]
    field5A4: fx32

class struct_driver_timers_t(Structure):
    """
    ```python
    shroomBoostTimer: int (POINTER(h))
    thunderShrinkTimer: int (POINTER(h))
    thunderGrowTimer: int (POINTER(h))
    starTimer: int (POINTER(h))
    slipstreamStartTimer: int (POINTER(h))
    slipstreamTimer: int (POINTER(h))
    dossunGrowTimer: int (POINTER(h))
    dossunFlatTimer: int (POINTER(h))
    teresaTimer: int (POINTER(h))
    teresaFlickerInterval: int (POINTER(h))
    teresaFlickerIntervalUpdateTimer: int (POINTER(h))
    teresaFlickerTimer: int (POINTER(h))
    teresaFlickerIntervalUpdateWaitTime: int (POINTER(h))
    teresaFlickerIntervalStep: int (POINTER(h))
    gessoInkTimer: int (POINTER(h))
    killerFrameCounter: int (POINTER(h))
    field20: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    isKillerFinishing: int (POINTER(i))
    killerTargetPlace: int (POINTER(h))
    gap2A: list[int] (POINTER(B)[2])
    killerState: list[int] (POINTER(B)[44])
    ```
    """
    _pack_: ClassVar[int] = 1
    shroomBoostTimer: int
    thunderShrinkTimer: int
    thunderGrowTimer: int
    starTimer: int
    slipstreamStartTimer: int
    slipstreamTimer: int
    dossunGrowTimer: int
    dossunFlatTimer: int
    teresaTimer: int
    teresaFlickerInterval: int
    teresaFlickerIntervalUpdateTimer: int
    teresaFlickerTimer: int
    teresaFlickerIntervalUpdateWaitTime: int
    teresaFlickerIntervalStep: int
    gessoInkTimer: int
    killerFrameCounter: int
    field20: int
    PADDING_0: list[int]
    isKillerFinishing: int
    killerTargetPlace: int
    gap2A: list[int]
    killerState: list[int]

class struct_efbnr_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    counter: int (POINTER(i))
    nsbtaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    scale: fx32 (struct_fx32)
    state: int (POINTER(I))
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    driverHitTimeouts: list[int] (POINTER(i)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    counter: int
    nsbtaFrame: int
    PADDING_0: list[int]
    scale: fx32
    state: int
    pathwalker: struct_pw_pathwalker_t
    driverHitTimeouts: list[int]

class struct_efbub_logic_part_t(Structure):
    """
    ```python
    logicPart: struct_mobj_logic_part_t (struct_mobj_logic_part_t)
    field28: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    logicPart: struct_mobj_logic_part_t
    field28: int

class struct_efbub_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    waitTime: int (POINTER(i))
    lowYPos: fx32 (struct_fx32)
    rotation: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    highYPos: fx32 (struct_fx32)
    shadow: struct_objshadow_t (struct_objshadow_t)
    driverHitMask: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    emitter69: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    emitter70: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    emitterFail: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    waitTime: int
    lowYPos: fx32
    rotation: int
    PADDING_0: list[int]
    highYPos: fx32
    shadow: struct_objshadow_t
    driverHitMask: int
    PADDING_1: list[int]
    emitter69: POINTER_T[struct_spa_emitter_t]
    emitter70: POINTER_T[struct_spa_emitter_t]
    emitterFail: int

class struct_enemy_field140_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    driverFieldCC: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    field10: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    driverFieldCC: int
    field8: int
    fieldC: int
    field10: int

class struct_enemy_item_params_t(Structure):
    """
    ```python
    updateFunc: c_void_p (c_void_p)
    field4: int (POINTER(i))
    minTimeout: int (POINTER(H))
    timeoutRandomMax: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    updateFunc: c_void_p
    field4: int
    minTimeout: int
    timeoutRandomMax: int

class struct_enemy_item_state_t(Structure):
    """
    ```python
    slotItemTimeout: int (POINTER(H))
    dragItemTimeout: int (POINTER(H))
    slotItemParams: POINTER_T[struct_enemy_item_params_t] (POINTER(struct_enemy_item_params_t))
    dragItemParams: POINTER_T[struct_enemy_item_params_t] (POINTER(struct_enemy_item_params_t))
    fieldC: int (POINTER(i))
    lxPressed: int (POINTER(i))
    dpadUpPressed: int (POINTER(i))
    dpadDownPressed: int (POINTER(i))
    dpadUpCounter: int (POINTER(H))
    dpadDownCounter: int (POINTER(H))
    field20: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    slotItemTimeout: int
    dragItemTimeout: int
    slotItemParams: POINTER_T[struct_enemy_item_params_t]
    dragItemParams: POINTER_T[struct_enemy_item_params_t]
    fieldC: int
    lxPressed: int
    dpadUpPressed: int
    dpadDownPressed: int
    dpadUpCounter: int
    dpadDownCounter: int
    field20: int

class struct_enemy_rubberbanding_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    driverFieldCC: int (POINTER(i))
    rivalAggressiveness: int (POINTER(i))
    maxDriverFieldCC: int (POINTER(i))
    field10: int (POINTER(i))
    place: int (POINTER(i))
    field18: int (POINTER(i))
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    hasFailedStart: int (POINTER(i))
    hasStartBoost: int (POINTER(i))
    startBoostAmount: int (POINTER(H))
    field32: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    driverFieldCC: int
    rivalAggressiveness: int
    maxDriverFieldCC: int
    field10: int
    place: int
    field18: int
    field1C: int
    field20: int
    field24: int
    hasFailedStart: int
    hasStartBoost: int
    startBoostAmount: int
    field32: int

class struct_enemy_t(Structure):
    """
    ```python
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    driverId: int (POINTER(H))
    field6: int (POINTER(H))
    epoi: struct_struc_316_epoi (struct_struc_316_epoi)
    mepo: struct_struc_313_mepo (struct_struc_313_mepo)
    targetPos: struct_VecFx32 (struct_VecFx32)
    field50: struct_VecFx32 (struct_VecFx32)
    field5C: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    driftOffset: struct_VecFx32 (struct_VecFx32)
    driftEpoiRadiusScaleUpdateCounter: int (POINTER(H))
    driftEpoiRadiusScaleUpdateFrames: int (POINTER(H))
    field70: int (POINTER(i))
    driftEpoiRadiusScale: fx32 (struct_fx32)
    field78: int (POINTER(H))
    field7A: int (POINTER(H))
    field7C: int (POINTER(i))
    field80: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field84: int (POINTER(i))
    field88: int (POINTER(i))
    field8C: int (POINTER(i))
    driftState: int (POINTER(i))
    driftDirection: int (POINTER(i))
    field98: int (POINTER(i))
    field9C: int (POINTER(i))
    fieldA0: int (POINTER(i))
    fieldA4: int (POINTER(i))
    fieldA8: int (POINTER(i))
    fieldAC: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    targetDriver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    fieldB4: int (POINTER(i))
    fieldB8: int (POINTER(i))
    fieldBC: int (POINTER(i))
    targetBalloonCount: int (POINTER(H))
    balloonInflateMicTimeout: int (POINTER(H))
    isInflatingBalloon: int (POINTER(i))
    fieldC8: int (POINTER(H))
    fieldCA: int (POINTER(H))
    fieldCC: int (POINTER(i))
    targetShine: c_void_p (c_void_p)
    shineIdx: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    fieldD8: int (POINTER(i))
    fieldDC: struct_VecFx32 (struct_VecFx32)
    rubberbanding: struct_enemy_rubberbanding_t (struct_enemy_rubberbanding_t)
    itemState: struct_enemy_item_state_t (struct_enemy_item_state_t)
    field140: struct_enemy_field140_t (struct_enemy_field140_t)
    field154: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    driver: POINTER_T[struct_driver_t]
    driverId: int
    field6: int
    epoi: struct_struc_316_epoi
    mepo: struct_struc_313_mepo
    targetPos: struct_VecFx32
    field50: struct_VecFx32
    field5C: POINTER_T[struct_VecFx32]
    driftOffset: struct_VecFx32
    driftEpoiRadiusScaleUpdateCounter: int
    driftEpoiRadiusScaleUpdateFrames: int
    field70: int
    driftEpoiRadiusScale: fx32
    field78: int
    field7A: int
    field7C: int
    field80: int
    PADDING_0: list[int]
    field84: int
    field88: int
    field8C: int
    driftState: int
    driftDirection: int
    field98: int
    field9C: int
    fieldA0: int
    fieldA4: int
    fieldA8: int
    fieldAC: int
    PADDING_1: list[int]
    targetDriver: POINTER_T[struct_driver_t]
    fieldB4: int
    fieldB8: int
    fieldBC: int
    targetBalloonCount: int
    balloonInflateMicTimeout: int
    isInflatingBalloon: int
    fieldC8: int
    fieldCA: int
    fieldCC: int
    targetShine: c_void_p
    shineIdx: int
    PADDING_2: list[int]
    fieldD8: int
    fieldDC: struct_VecFx32
    rubberbanding: struct_enemy_rubberbanding_t
    itemState: struct_enemy_item_state_t
    field140: struct_enemy_field140_t
    field154: int

class struct_epipe_t(Structure):
    """
    ```python
    rotDieMObj: struct_rotdiemobj_t (struct_rotdiemobj_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    rotDieMObj: struct_rotdiemobj_t

class struct_expl_def_t(Structure):
    """
    ```python
    instanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    hasNsbca: int (POINTER(i))
    hasNsbma: int (POINTER(i))
    hasNsbta: int (POINTER(i))
    initInstFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None] (CFunctionType)
    updateInstFunc: Callable[[POINTER_T[struct_expl_inst_t]], None] (CFunctionType)
    instanceSize: int (POINTER(I))
    modelRes: struct_model_res_t (struct_model_res_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    instanceCount: int
    PADDING_0: list[int]
    hasNsbca: int
    hasNsbma: int
    hasNsbta: int
    initInstFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None]
    updateInstFunc: Callable[[POINTER_T[struct_expl_inst_t]], None]
    instanceSize: int
    modelRes: struct_model_res_t

class struct_expl_inst_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    model: struct_model_t (struct_model_t)
    position: struct_VecFx32 (struct_VecFx32)
    initFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None] (CFunctionType)
    updateFunc: Callable[[POINTER_T[struct_expl_inst_t]], None] (CFunctionType)
    state: int (POINTER(I))
    type: int (POINTER(I))
    nsbcaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbmaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    scale: struct_VecFx32 (struct_VecFx32)
    frameCounter: int (POINTER(I))
    lifeTime: int (POINTER(I))
    polygonId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    visible: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    model: struct_model_t
    position: struct_VecFx32
    initFunc: Callable[[POINTER_T[struct_expl_inst_t], int], None]
    updateFunc: Callable[[POINTER_T[struct_expl_inst_t]], None]
    state: int
    type: int
    nsbcaAnim: POINTER_T[struct_anim_manager_t]
    nsbmaAnim: POINTER_T[struct_anim_manager_t]
    nsbtaAnim: POINTER_T[struct_anim_manager_t]
    scale: struct_VecFx32
    frameCounter: int
    lifeTime: int
    polygonId: int
    PADDING_0: list[int]
    visible: int

class struct_expl_state_t(Structure):
    """
    ```python
    activeInstanceList: struct_NNSFndList (struct_NNSFndList)
    freeInstanceLists: list[struct_NNSFndList] (struct_NNSFndList[5])
    instances: list[POINTER_T[POINTER_T[struct_expl_inst_t]]] (POINTER(POINTER(struct_expl_inst_t))[5])
    curPolygonId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    activeInstanceList: struct_NNSFndList
    freeInstanceLists: list[struct_NNSFndList]
    instances: list[POINTER_T[POINTER_T[struct_expl_inst_t]]]
    curPolygonId: int
    PADDING_0: list[int]

class struct_fireball2_fireball_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    armRotZ: int (POINTER(H))
    ballRotZ: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    armRotZ: int
    ballRotZ: int

class struct_fireball2_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nrArms: int (POINTER(H))
    fireballsPerArm: int (POINTER(H))
    armAngleDistance: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fireballDistance: fx32 (struct_fx32)
    radius: fx32 (struct_fx32)
    rotSpeed: int (POINTER(H))
    rotation: int (POINTER(H))
    centerFireball: struct_fireball2_fireball_t (struct_fireball2_fireball_t)
    fireballs: list[struct_fireball2_fireball_t] (struct_fireball2_fireball_t[20][20])
    driverHitTimeouts: list[int] (POINTER(i)[8])
    playerDistanceFromRing: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nrArms: int
    fireballsPerArm: int
    armAngleDistance: int
    PADDING_0: list[int]
    fireballDistance: fx32
    radius: fx32
    rotSpeed: int
    rotation: int
    centerFireball: struct_fireball2_fireball_t
    fireballs: list[struct_fireball2_fireball_t]
    driverHitTimeouts: list[int]
    playerDistanceFromRing: fx32

class struct_flipper_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(i))
    modelFlip: int (POINTER(i))
    baseMatrices: list[union_MtxFx43] (union_MtxFx43[30])
    extraColMatrices: list[union_MtxFx43] (union_MtxFx43[30])
    ptclEmitterPositions: list[struct_VecFx32] (struct_VecFx32[30])
    ptclEmitterTargets: list[struct_VecFx32] (struct_VecFx32[30])
    waitCounter: int (POINTER(i))
    ballHitFrameCounter: int (POINTER(i))
    animFrame: int (POINTER(i))
    nsbtpFrame: int (POINTER(H))
    nsbtaFrame: int (POINTER(H))
    electricityActive: int (POINTER(i))
    state: int (POINTER(I))
    ptclEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    driverHitTimeouts: list[int] (POINTER(i)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    modelFlip: int
    baseMatrices: list[union_MtxFx43]
    extraColMatrices: list[union_MtxFx43]
    ptclEmitterPositions: list[struct_VecFx32]
    ptclEmitterTargets: list[struct_VecFx32]
    waitCounter: int
    ballHitFrameCounter: int
    animFrame: int
    nsbtpFrame: int
    nsbtaFrame: int
    electricityActive: int
    state: int
    ptclEmitter: POINTER_T[struct_spa_emitter_t]
    driverHitTimeouts: list[int]

class struct_fwdst_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    index: int (POINTER(H))
    ccDependentSetting: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    index: int
    ccDependentSetting: int

class struct_fx16(Structure):
    """
    ```python
    val: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    val: int

class struct_fx32(Structure):
    """
    ```python
    val: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    val: int

class struct_gesso_t(Structure):
    """
    ```python
    item: struct_it_item_inst_t (struct_it_item_inst_t)
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    driverSplashCount: list[int] (POINTER(B)[8])
    field138: int (POINTER(i))
    field13C: struct_VecFx32 (struct_VecFx32)
    field148: struct_VecFx32 (struct_VecFx32)
    field154: struct_VecFx32 (struct_VecFx32)
    field160: int (POINTER(i))
    field164: int (POINTER(i))
    field168: int (POINTER(i))
    field16C: int (POINTER(i))
    field170: int (POINTER(i))
    field174: struct_VecFx32 (struct_VecFx32)
    field180: struct_VecFx32 (struct_VecFx32)
    field18C: int (POINTER(i))
    gap190: int (POINTER(I))
    field194: int (POINTER(i))
    visible: int (POINTER(i))
    field19C: fx32 (struct_fx32)
    gap1A0: list[int] (POINTER(B)[20])
    ```
    """
    _pack_: ClassVar[int] = 1
    item: struct_it_item_inst_t
    driver: POINTER_T[struct_driver_t]
    driverSplashCount: list[int]
    field138: int
    field13C: struct_VecFx32
    field148: struct_VecFx32
    field154: struct_VecFx32
    field160: int
    field164: int
    field168: int
    field16C: int
    field170: int
    field174: struct_VecFx32
    field180: struct_VecFx32
    field18C: int
    gap190: int
    field194: int
    visible: int
    field19C: fx32
    gap1A0: list[int]

class struct_ghost_header_ex_t(Structure):
    """
    ```python
    header: struct_ghost_header_t (struct_ghost_header_t)
    emblem: list[int] (POINTER(B)[512])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_ghost_header_t
    emblem: list[int]

class struct_ghost_header_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    character: int (POINTER(L))
    kart: int (POINTER(L))
    course: int (POINTER(L))
    _4: int (POINTER(L))
    isValid: int (POINTER(L))
    flagsBit1: int (POINTER(L))
    flagsBit2_3: int (POINTER(L))
    _8: int (POINTER(L))
    minutes: int (POINTER(L))
    seconds: int (POINTER(L))
    milliseconds: int (POINTER(L))
    nickname: list[int] (POINTER(H)[10])
    lapTimes: list[struct_ghost_time_t] (struct_ghost_time_t[5])
    field2F: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    character: int
    kart: int
    course: int
    _4: int
    isValid: int
    flagsBit1: int
    flagsBit2_3: int
    _8: int
    minutes: int
    seconds: int
    milliseconds: int
    nickname: list[int]
    lapTimes: list[struct_ghost_time_t]
    field2F: int
    PADDING_0: int

class struct_ghost_time_t(Structure):
    """
    ```python
    field0: int (POINTER(B))
    field1: int (POINTER(B))
    field2: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field1: int
    field2: int

class struct_gmenu_config_t(Structure):
    """
    ```python
    loadUnknown: int (POINTER(i))
    unkFont: POINTER_T[struct_NNSG2dFont] (POINTER(struct_NNSG2dFont))
    field8: int (POINTER(I))
    fieldC: int (POINTER(I))
    field10: int (POINTER(I))
    loadSelectChoises: int (POINTER(i))
    selectChoisesFont: POINTER_T[struct_NNSG2dFont] (POINTER(struct_NNSG2dFont))
    loadSelectReturn: int (POINTER(i))
    loadBackground: int (POINTER(i))
    field24: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    loadUnknown: int
    unkFont: POINTER_T[struct_NNSG2dFont]
    field8: int
    fieldC: int
    field10: int
    loadSelectChoises: int
    selectChoisesFont: POINTER_T[struct_NNSG2dFont]
    loadSelectReturn: int
    loadBackground: int
    field24: int

class struct_gmenu_context_t(Structure):
    """
    ```python
    unknownLoaded: int (POINTER(i))
    selectChoisesLoaded: int (POINTER(i))
    selectReturnLoaded: int (POINTER(i))
    fieldC: int (POINTER(I))
    screenTmpBuf: list[int] (POINTER(H)[1024])
    charVramLeft: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    unknownLoaded: int
    selectChoisesLoaded: int
    selectReturnLoaded: int
    fieldC: int
    screenTmpBuf: list[int]
    charVramLeft: int

class struct_gmenu_select_return_context_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    field8: int (POINTER(I))
    fieldC: int (POINTER(I))
    screenTmpBuf: list[int] (POINTER(H)[1024])
    field810: int (POINTER(I))
    field814: int (POINTER(I))
    field818: int (POINTER(I))
    field81C: int (POINTER(I))
    field820: int (POINTER(i))
    seqArcIndex: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    screenTmpBuf: list[int]
    field810: int
    field814: int
    field818: int
    field81C: int
    field820: int
    seqArcIndex: int

class struct_grpconf_entry_t(Structure):
    """
    ```python
    objectId: int (POINTER(H))
    has3DModel: int (POINTER(H))
    nearClip: int (POINTER(H))
    farClip: int (POINTER(H))
    collisionType: int (POINTER(H))
    width: int (POINTER(H))
    height: int (POINTER(H))
    depth: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    objectId: int
    has3DModel: int
    nearClip: int
    farClip: int
    collisionType: int
    width: int
    height: int
    depth: int

class struct_heap_info_t(Structure):
    """
    ```python
    unknown: int (POINTER(I))
    memoryRegionStart: c_void_p (c_void_p)
    heapStart: c_void_p (c_void_p)
    heapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    processName: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    ```
    """
    _pack_: ClassVar[int] = 1
    unknown: int
    memoryRegionStart: c_void_p
    heapStart: c_void_p
    heapHandle: POINTER_T[struct_NNSiFndHeapHead]
    processName: POINTER_T[c_ubyte]

class struct_iball_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    rotZ: int (POINTER(i))
    fieldA4: int (POINTER(i))
    fieldA8: int (POINTER(i))
    fieldAC: int (POINTER(i))
    fieldB0: int (POINTER(i))
    fieldB4: int (POINTER(i))
    fieldB8: int (POINTER(i))
    elevation: int (POINTER(i))
    fieldC0: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    shadow: struct_objshadow_t (struct_objshadow_t)
    routePos: struct_VecFx32 (struct_VecFx32)
    clipAreaMask: int (POINTER(i))
    field12C: int (POINTER(i))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    rotZ: int
    fieldA4: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    fieldB4: int
    fieldB8: int
    elevation: int
    fieldC0: fx32
    pathwalker: struct_pw_pathwalker_t
    shadow: struct_objshadow_t
    routePos: struct_VecFx32
    clipAreaMask: int
    field12C: int
    state: int

class struct_idk_struct2_t(Structure):
    """
    ```python
    value: fx32 (struct_fx32)
    velocity: fx32 (struct_fx32)
    min: fx32 (struct_fx32)
    max: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    value: fx32
    velocity: fx32
    min: fx32
    max: fx32

class struct_idk_struct_t(Structure):
    """
    ```python
    value: fx32 (struct_fx32)
    velocity: fx32 (struct_fx32)
    reverse: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    value: fx32
    velocity: fx32
    reverse: int

class struct_input_pad_data_t(Structure):
    """
    ```python
    field0: int (POINTER(H))
    pressedKeys: int (POINTER(H))
    flags: int (POINTER(H))
    field6: int (POINTER(H))
    field8: int (POINTER(I))
    fieldC: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    pressedKeys: int
    flags: int
    field6: int
    field8: int
    fieldC: int

class struct_input_pad_t(Structure):
    """
    ```python
    triggeredKeys: int (POINTER(H))
    pressedKeys: int (POINTER(H))
    releasedKeys: int (POINTER(H))
    repeatedKeys: int (POINTER(H))
    repeatState: int (POINTER(H))
    repeatFrameCounter: int (POINTER(H))
    repeatMask: int (POINTER(H))
    repeatFirstFrame: int (POINTER(H))
    repeatNextFrame: int (POINTER(H))
    resetInvoked: int (POINTER(H))
    field14: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    resetStartTime: int (POINTER(L))
    field20: int (POINTER(I))
    field24: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    triggeredKeys: int
    pressedKeys: int
    releasedKeys: int
    repeatedKeys: int
    repeatState: int
    repeatFrameCounter: int
    repeatMask: int
    repeatFirstFrame: int
    repeatNextFrame: int
    resetInvoked: int
    field14: int
    PADDING_0: list[int]
    resetStartTime: int
    field20: int
    field24: int

class struct_input_rec_recording_entry_t(Structure):
    """
    ```python
    keys: int (POINTER(B))
    duration: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    keys: int
    duration: int

class struct_input_rec_recording_t(Structure):
    """
    ```python
    dataLength: int (POINTER(I))
    entries: list[struct_input_rec_recording_entry_t] (struct_input_rec_recording_entry_t[1764])
    ```
    """
    _pack_: ClassVar[int] = 1
    dataLength: int
    entries: list[struct_input_rec_recording_entry_t]

class struct_input_rec_t(Structure):
    """
    ```python
    recording: POINTER_T[struct_input_rec_recording_t] (POINTER(struct_input_rec_recording_t))
    curEntry: int (POINTER(H))
    waitCounter: int (POINTER(H))
    state: int (POINTER(I))
    isBufferClear: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    recording: POINTER_T[struct_input_rec_recording_t]
    curEntry: int
    waitCounter: int
    state: int
    isBufferClear: int

class struct_input_tpmic_t(Structure):
    """
    ```python
    curTp: struct_input_tpmic_tp_t (struct_input_tpmic_tp_t)
    prevTp: struct_input_tpmic_tp_t (struct_input_tpmic_tp_t)
    tpReleaseFrameCounter: int (POINTER(H))
    mic: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    curTp: struct_input_tpmic_tp_t
    prevTp: struct_input_tpmic_tp_t
    tpReleaseFrameCounter: int
    mic: int
    PADDING_0: int

class struct_input_tpmic_tp_t(Structure):
    """
    ```python
    tpX: int (POINTER(H))
    tpY: int (POINTER(H))
    tpValid: int (POINTER(H))
    field6: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    tpX: int
    tpY: int
    tpValid: int
    field6: int

class struct_input_unit_t(Structure):
    """
    ```python
    pad: struct_input_pad_t (struct_input_pad_t)
    inputRecorder: struct_input_rec_t (struct_input_rec_t)
    field38: int (POINTER(I))
    mode: int (POINTER(I))
    virtualPadKeys: int (POINTER(H))
    keyMask: int (POINTER(H))
    field44: int (POINTER(i))
    tpMic: struct_input_tpmic_t (struct_input_tpmic_t)
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    pad: struct_input_pad_t
    inputRecorder: struct_input_rec_t
    field38: int
    mode: int
    virtualPadKeys: int
    keyMask: int
    field44: int
    tpMic: struct_input_tpmic_t
    PADDING_0: list[int]

class struct_it_driver_dragitem_t(Structure):
    """
    ```python
    itemType: int (POINTER(i))
    itemConfigId: int (POINTER(i))
    field8: int (POINTER(i))
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t] (POINTER(struct_it_driver_item_status_t))
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    items: list[POINTER_T[struct_it_item_inst_t]] (POINTER(struct_it_item_inst_t)[3])
    itemCount: int (POINTER(i))
    field24: int (POINTER(i))
    driverId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field2C: union_MtxFx43 (union_MtxFx43)
    field5C: struct_VecFx32 (struct_VecFx32)
    field68: int (POINTER(i))
    field6C: struct_VecFx32 (struct_VecFx32)
    field78: int (POINTER(i))
    field7C: int (POINTER(i))
    field80: int (POINTER(i))
    field84: struct_VecFx32 (struct_VecFx32)
    field90: struct_VecFx32 (struct_VecFx32)
    field9C: struct_VecFx32 (struct_VecFx32)
    fieldA8: struct_VecFx32 (struct_VecFx32)
    fieldB4: struct_VecFx32 (struct_VecFx32)
    gapC0: list[int] (POINTER(B)[12])
    fieldCC: list[int] (POINTER(i)[3])
    fieldD8: struct_VecFx32 (struct_VecFx32)
    fieldE4: int (POINTER(i))
    fieldE8: int (POINTER(i))
    fieldEC: list[int] (POINTER(i)[16])
    field12C: list[int] (POINTER(i)[16])
    field16C: int (POINTER(i))
    field170: int (POINTER(i))
    field174: int (POINTER(H))
    field176: int (POINTER(H))
    field178: int (POINTER(i))
    field17C: int (POINTER(i))
    field180: struct_VecFx32 (struct_VecFx32)
    field18C: list[int] (POINTER(H)[3])
    field192: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    itemType: int
    itemConfigId: int
    field8: int
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t]
    driver: POINTER_T[struct_driver_t]
    items: list[POINTER_T[struct_it_item_inst_t]]
    itemCount: int
    field24: int
    driverId: int
    PADDING_0: list[int]
    field2C: union_MtxFx43
    field5C: struct_VecFx32
    field68: int
    field6C: struct_VecFx32
    field78: int
    field7C: int
    field80: int
    field84: struct_VecFx32
    field90: struct_VecFx32
    field9C: struct_VecFx32
    fieldA8: struct_VecFx32
    fieldB4: struct_VecFx32
    gapC0: list[int]
    fieldCC: list[int]
    fieldD8: struct_VecFx32
    fieldE4: int
    fieldE8: int
    fieldEC: list[int]
    field12C: list[int]
    field16C: int
    field170: int
    field174: int
    field176: int
    field178: int
    field17C: int
    field180: struct_VecFx32
    field18C: list[int]
    field192: int

class struct_it_driver_item_status_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    slotItemConfigId: int (POINTER(i))
    dragItemConfigId: int (POINTER(i))
    field18: POINTER_T[struct_it_driver_item_status_t] (POINTER(struct_it_driver_item_status_t))
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    field28: int (POINTER(i))
    field2C: int (POINTER(i))
    itemSlot: struct_it_driver_itemslot_t (struct_it_driver_itemslot_t)
    dragItem: struct_it_driver_dragitem_t (struct_it_driver_dragitem_t)
    field1EC: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ipoi: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    field1F4: int (POINTER(i))
    driverId: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    driverIndex: int (POINTER(i))
    isUsingShroom: int (POINTER(i))
    field208: int (POINTER(i))
    field20C: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    slotItemConfigId: int
    dragItemConfigId: int
    field18: POINTER_T[struct_it_driver_item_status_t]
    field1C: int
    field20: int
    field24: int
    field28: int
    field2C: int
    itemSlot: struct_it_driver_itemslot_t
    dragItem: struct_it_driver_dragitem_t
    field1EC: int
    PADDING_0: list[int]
    ipoi: POINTER_T[struct_mdat_itempoint_t]
    field1F4: int
    driverId: int
    PADDING_1: list[int]
    driver: POINTER_T[struct_driver_t]
    driverIndex: int
    isUsingShroom: int
    field208: int
    field20C: int

class struct_it_driver_itemslot_t(Structure):
    """
    ```python
    itemConfigId: int (POINTER(i))
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t] (POINTER(struct_it_driver_item_status_t))
    itemCount: int (POINTER(i))
    fieldC: int (POINTER(i))
    timeout: int (POINTER(H))
    field12: int (POINTER(H))
    items: list[POINTER_T[struct_it_item_inst_t]] (POINTER(struct_it_item_inst_t)[3])
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    itemConfigId: int
    driverItemStatus: POINTER_T[struct_it_driver_item_status_t]
    itemCount: int
    fieldC: int
    timeout: int
    field12: int
    items: list[POINTER_T[struct_it_item_inst_t]]
    field20: int
    field24: int

class struct_it_item_def_t(Structure):
    """
    ```python
    instanceSize: int (POINTER(I))
    limit: int (POINTER(I))
    field8: int (POINTER(I))
    instanceCount: int (POINTER(i))
    field10: int (POINTER(i))
    loadFunc: c_void_p (c_void_p)
    initInstanceFunc: c_void_p (c_void_p)
    field1C: c_void_p (c_void_p)
    field20: c_void_p (c_void_p)
    field24: c_void_p (c_void_p)
    updateFunc: c_void_p (c_void_p)
    renderFunc: c_void_p (c_void_p)
    visibilityFlagCalcFunc: c_void_p (c_void_p)
    field34: c_void_p (c_void_p)
    field38: c_void_p (c_void_p)
    destroyInstFunc: c_void_p (c_void_p)
    field40: int (POINTER(i))
    field44: int (POINTER(i))
    field48: c_void_p (c_void_p)
    field4C: int (POINTER(i))
    field50: c_void_p (c_void_p)
    gap54: int (POINTER(I))
    field58: c_void_p (c_void_p)
    field5C: int (POINTER(i))
    field60: int (POINTER(i))
    colSphereRadius: int (POINTER(i))
    sphereRadius1: int (POINTER(i))
    sphereRadius2: int (POINTER(i))
    field70: int (POINTER(i))
    scale: int (POINTER(i))
    field78: int (POINTER(i))
    field7C: int (POINTER(i))
    field80: int (POINTER(i))
    field84: int (POINTER(i))
    field88: int (POINTER(i))
    gap8C: int (POINTER(I))
    field90: int (POINTER(i))
    field94: int (POINTER(i))
    field98: int (POINTER(i))
    field9C: int (POINTER(i))
    fieldA0: int (POINTER(i))
    fieldA4: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    instanceSize: int
    limit: int
    field8: int
    instanceCount: int
    field10: int
    loadFunc: c_void_p
    initInstanceFunc: c_void_p
    field1C: c_void_p
    field20: c_void_p
    field24: c_void_p
    updateFunc: c_void_p
    renderFunc: c_void_p
    visibilityFlagCalcFunc: c_void_p
    field34: c_void_p
    field38: c_void_p
    destroyInstFunc: c_void_p
    field40: int
    field44: int
    field48: c_void_p
    field4C: int
    field50: c_void_p
    gap54: int
    field58: c_void_p
    field5C: int
    field60: int
    colSphereRadius: int
    sphereRadius1: int
    sphereRadius2: int
    field70: int
    scale: int
    field78: int
    field7C: int
    field80: int
    field84: int
    field88: int
    gap8C: int
    field90: int
    field94: int
    field98: int
    field9C: int
    fieldA0: int
    fieldA4: int

class struct_it_item_inst_t(Structure):
    """
    ```python
    sfxEmitter: struct_sfx_emitter_t (struct_sfx_emitter_t)
    type: int (POINTER(I))
    field48: int (POINTER(I))
    field4C: int (POINTER(H))
    field4E: int (POINTER(H))
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    flags: int (POINTER(I))
    field78: int (POINTER(H))
    field7A: int (POINTER(H))
    light: struct_light_t (struct_light_t)
    PADDING_0: list[int] (POINTER(B)[2])
    lightPtr: POINTER_T[struct_light_t] (POINTER(struct_light_t))
    mtx: union_MtxFx43 (union_MtxFx43)
    gapC4: list[int] (POINTER(B)[12])
    fieldD0: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    visibilityFlags: int (POINTER(I))
    alpha: int (POINTER(h))
    colEntryId: int (POINTER(H))
    fieldDC: int (POINTER(I))
    sphereSize: fx32 (struct_fx32)
    fieldE4: struct_VecFx32 (struct_VecFx32)
    fieldF0: struct_VecFx32 (struct_VecFx32)
    fieldFC: int (POINTER(I))
    field100: int (POINTER(I))
    field104: int (POINTER(I))
    field108: struct_VecFx32 (struct_VecFx32)
    field114: int (POINTER(H))
    field116: int (POINTER(H))
    field118: int (POINTER(H))
    field11A: int (POINTER(H))
    field11C: int (POINTER(I))
    field120: int (POINTER(I))
    field124: int (POINTER(I))
    field128DriverMask: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    sfxEmitter: struct_sfx_emitter_t
    type: int
    field48: int
    field4C: int
    field4E: int
    position: struct_VecFx32
    velocity: struct_VecFx32
    scale: struct_VecFx32
    flags: int
    field78: int
    field7A: int
    light: struct_light_t
    PADDING_0: list[int]
    lightPtr: POINTER_T[struct_light_t]
    mtx: union_MtxFx43
    gapC4: list[int]
    fieldD0: POINTER_T[struct_VecFx32]
    visibilityFlags: int
    alpha: int
    colEntryId: int
    fieldDC: int
    sphereSize: fx32
    fieldE4: struct_VecFx32
    fieldF0: struct_VecFx32
    fieldFC: int
    field100: int
    field104: int
    field108: struct_VecFx32
    field114: int
    field116: int
    field118: int
    field11A: int
    field11C: int
    field120: int
    field124: int
    field128DriverMask: int
    PADDING_1: list[int]

class struct_it_itemconfig_t(Structure):
    """
    ```python
    enabled: int (POINTER(i))
    wifiEnabled: int (POINTER(i))
    type: int (POINTER(I))
    count: int (POINTER(I))
    field10: int (POINTER(I))
    field14: int (POINTER(I))
    activateFunc: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    enabled: int
    wifiEnabled: int
    type: int
    count: int
    field10: int
    field14: int
    activateFunc: c_void_p

class struct_it_itemset_t(Structure):
    """
    ```python
    id: int (POINTER(I))
    instances: POINTER_T[struct_it_item_inst_t] (POINTER(struct_it_item_inst_t))
    totalInstanceCount: int (POINTER(I))
    itemParamsField10: int (POINTER(I))
    activeInstanceCount: int (POINTER(I))
    field14: int (POINTER(I))
    field18: int (POINTER(I))
    activeInstanceCount2: int (POINTER(I))
    limit: int (POINTER(I))
    renderFunc: c_void_p (c_void_p)
    visibilityFlagCalcFunc: c_void_p (c_void_p)
    itemParamsField70: int (POINTER(I))
    scale: fx32 (struct_fx32)
    itemParamsField78: int (POINTER(I))
    itemParamsField5C: int (POINTER(I))
    itemParamsFieldA4: int (POINTER(I))
    renderingDisabled: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    instances: POINTER_T[struct_it_item_inst_t]
    totalInstanceCount: int
    itemParamsField10: int
    activeInstanceCount: int
    field14: int
    field18: int
    activeInstanceCount2: int
    limit: int
    renderFunc: c_void_p
    visibilityFlagCalcFunc: c_void_p
    itemParamsField70: int
    scale: fx32
    itemParamsField78: int
    itemParamsField5C: int
    itemParamsFieldA4: int
    renderingDisabled: int

class struct_itnet_action_t_(Structure):
    """
    ```python
    data: list[int] (POINTER(B)[20])
    itemType: int (POINTER(I))
    action: int (POINTER(I))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    data: list[int]
    itemType: int
    action: int
    field1C: int

class struct_jn_msg_bmg_dat1_t(Structure):
    """
    ```python
    sectionHeader: struct_jn_msg_bmg_section_header_t (struct_jn_msg_bmg_section_header_t)
    stringData: list[int] (POINTER(H)[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    sectionHeader: struct_jn_msg_bmg_section_header_t
    stringData: list[int]

class struct_jn_msg_bmg_header_t(Structure):
    """
    ```python
    magic1: int (POINTER(I))
    magic2: int (POINTER(I))
    fileSize: int (POINTER(I))
    nrSections: int (POINTER(I))
    field10: int (POINTER(I))
    field14: int (POINTER(I))
    field18: int (POINTER(I))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic1: int
    magic2: int
    fileSize: int
    nrSections: int
    field10: int
    field14: int
    field18: int
    field1C: int

class struct_jn_msg_bmg_inf1_t(Structure):
    """
    ```python
    sectionHeader: struct_jn_msg_bmg_section_header_t (struct_jn_msg_bmg_section_header_t)
    nrEntries: int (POINTER(H))
    fieldA: int (POINTER(H))
    fieldC: int (POINTER(I))
    offsets: list[int] (POINTER(I)[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    sectionHeader: struct_jn_msg_bmg_section_header_t
    nrEntries: int
    fieldA: int
    fieldC: int
    offsets: list[int]

class struct_jn_msg_bmg_section_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    size: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    size: int

class struct_jn_msg_bmg_t(Structure):
    """
    ```python
    header: struct_jn_msg_bmg_header_t (struct_jn_msg_bmg_header_t)
    inf1: struct_jn_msg_bmg_inf1_t (struct_jn_msg_bmg_inf1_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jn_msg_bmg_header_t
    inf1: struct_jn_msg_bmg_inf1_t

class struct_jnui_bnbl_res_element_t(Structure):
    """
    ```python
    x: struct_jnui_coord_t (struct_jnui_coord_t)
    y: struct_jnui_coord_t (struct_jnui_coord_t)
    width: int (POINTER(B))
    height: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: struct_jnui_coord_t
    y: struct_jnui_coord_t
    width: int
    height: int

class struct_jnui_bnbl_res_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    unknown: int (POINTER(H))
    nrElements: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    unknown: int
    nrElements: int

class struct_jnui_bnbl_res_t(Structure):
    """
    ```python
    header: struct_jnui_bnbl_res_header_t (struct_jnui_bnbl_res_header_t)
    elements: list[struct_jnui_bnbl_res_element_t] (struct_jnui_bnbl_res_element_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jnui_bnbl_res_header_t
    elements: list[struct_jnui_bnbl_res_element_t]

class struct_jnui_bncl_res_element_t(Structure):
    """
    ```python
    x: struct_jnui_coord_t (struct_jnui_coord_t)
    y: struct_jnui_coord_t (struct_jnui_coord_t)
    cellId: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: struct_jnui_coord_t
    y: struct_jnui_coord_t
    cellId: int

class struct_jnui_bncl_res_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    unknown: int (POINTER(H))
    nrElements: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    unknown: int
    nrElements: int

class struct_jnui_bncl_res_t(Structure):
    """
    ```python
    header: struct_jnui_bncl_res_header_t (struct_jnui_bncl_res_header_t)
    elements: list[struct_jnui_bncl_res_element_t] (struct_jnui_bncl_res_element_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jnui_bncl_res_header_t
    elements: list[struct_jnui_bncl_res_element_t]

class struct_jnui_bnll_res_element_t(Structure):
    """
    ```python
    x: struct_jnui_coord_t (struct_jnui_coord_t)
    y: struct_jnui_coord_t (struct_jnui_coord_t)
    hSpace: int (POINTER(b))
    vSpace: int (POINTER(b))
    color: int (POINTER(H))
    palette: int (POINTER(H))
    font: int (POINTER(H))
    stringPtr: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: struct_jnui_coord_t
    y: struct_jnui_coord_t
    hSpace: int
    vSpace: int
    color: int
    palette: int
    font: int
    stringPtr: int

class struct_jnui_bnll_res_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    unknown: int (POINTER(H))
    nrElements: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    unknown: int
    nrElements: int

class struct_jnui_bnll_res_t(Structure):
    """
    ```python
    header: struct_jnui_bnll_res_header_t (struct_jnui_bnll_res_header_t)
    elements: list[struct_jnui_bnll_res_element_t] (struct_jnui_bnll_res_element_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_jnui_bnll_res_header_t
    elements: list[struct_jnui_bnll_res_element_t]

class struct_jnui_coord_t(Structure):
    """
    ```python
    coord: int (POINTER(h))
    origin: int (POINTER(h))
    unk: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    coord: int
    origin: int
    unk: int

class struct_jnui_label_t(Structure):
    """
    ```python
    charCanvas: struct_NNSG2dCharCanvas (struct_NNSG2dCharCanvas)
    textCanvas: struct_NNSG2dTextCanvas (struct_NNSG2dTextCanvas)
    charData: c_void_p (c_void_p)
    charDataLength: int (POINTER(I))
    charDataTileOffset: int (POINTER(I))
    width: int (POINTER(I))
    height: int (POINTER(I))
    cellData: POINTER_T[struct_NNSG2dCellDataWithBR] (POINTER(struct_NNSG2dCellDataWithBR))
    ```
    """
    _pack_: ClassVar[int] = 1
    charCanvas: struct_NNSG2dCharCanvas
    textCanvas: struct_NNSG2dTextCanvas
    charData: c_void_p
    charDataLength: int
    charDataTileOffset: int
    width: int
    height: int
    cellData: POINTER_T[struct_NNSG2dCellDataWithBR]

class struct_jnui_layout_element_t(Structure):
    """
    ```python
    visible: int (POINTER(i))
    offsetX: int (POINTER(h))
    offsetY: int (POINTER(h))
    usePosition: int (POINTER(i))
    positionX: int (POINTER(h))
    positionY: int (POINTER(h))
    useMtx: int (POINTER(i))
    baseMtx: union_MtxFx22 (union_MtxFx22)
    affineMtx: union_MtxFx22 (union_MtxFx22)
    useDoubleAffine: int (POINTER(i))
    subElement: int (POINTER(i))
    label: POINTER_T[struct_jnui_label_t] (POINTER(struct_jnui_label_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    visible: int
    offsetX: int
    offsetY: int
    usePosition: int
    positionX: int
    positionY: int
    useMtx: int
    baseMtx: union_MtxFx22
    affineMtx: union_MtxFx22
    useDoubleAffine: int
    subElement: int
    label: POINTER_T[struct_jnui_label_t]

class struct_kcol_header_t(Structure):
    """
    ```python
    posDataOffset: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    nrmDataOffset: POINTER_T[struct_VecFx16] (POINTER(struct_VecFx16))
    prismDataOffset: POINTER_T[struct_kcol_prism_data_t] (POINTER(struct_kcol_prism_data_t))
    blockDataOffset: POINTER_T[c_uint] (POINTER(POINTER(I)))
    prismThickness: fx32 (struct_fx32)
    areaMinPos: struct_VecFx32 (struct_VecFx32)
    areaXWidthMask: int (POINTER(I))
    areaYWidthMask: int (POINTER(I))
    areaZWidthMask: int (POINTER(I))
    blockWidthShift: int (POINTER(I))
    areaXBlocksShift: int (POINTER(I))
    areaXYBlocksShift: int (POINTER(I))
    sphereRadius: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    posDataOffset: POINTER_T[struct_VecFx32]
    nrmDataOffset: POINTER_T[struct_VecFx16]
    prismDataOffset: POINTER_T[struct_kcol_prism_data_t]
    blockDataOffset: POINTER_T[c_uint]
    prismThickness: fx32
    areaMinPos: struct_VecFx32
    areaXWidthMask: int
    areaYWidthMask: int
    areaZWidthMask: int
    blockWidthShift: int
    areaXBlocksShift: int
    areaXYBlocksShift: int
    sphereRadius: fx32

class struct_kcol_prism_data_t(Structure):
    """
    ```python
    height: fx32 (struct_fx32)
    posIdx: int (POINTER(H))
    fNrmIdx: int (POINTER(H))
    eNrm1Idx: int (POINTER(H))
    eNrm2Idx: int (POINTER(H))
    eNrm3Idx: int (POINTER(H))
    attribute: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    height: fx32
    posIdx: int
    fNrmIdx: int
    eNrm1Idx: int
    eNrm2Idx: int
    eNrm3Idx: int
    attribute: int

class struct_kofs_entry_t(Structure):
    """
    ```python
    tireName: list[int] (POINTER(B)[16])
    frontTireScale: fx32 (struct_fx32)
    tirePositions: list[struct_VecFx32] (struct_VecFx32[4])
    characterPositions: list[struct_VecFx32] (struct_VecFx32[13])
    ```
    """
    _pack_: ClassVar[int] = 1
    tireName: list[int]
    frontTireScale: fx32
    tirePositions: list[struct_VecFx32]
    characterPositions: list[struct_VecFx32]

class struct_kofs_t(Structure):
    """
    ```python
    entries: list[struct_kofs_entry_t] (struct_kofs_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    entries: list[struct_kofs_entry_t]

class struct_koopablock_t(Structure):
    """
    ```python
    dcolMObj: struct_dcol_inst_t (struct_dcol_inst_t)
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    speed: fx32 (struct_fx32)
    waitCounter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    dcolMObj: struct_dcol_inst_t
    pathWalker: struct_pw_pathwalker_t
    speed: fx32
    waitCounter: int
    PADDING_0: list[int]

class struct_kouragreen_t(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[364])
    sfxExParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    sfxExParams: struct_sfx_emitter_ex_params_t

class struct_kourared_t(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[600])
    sfxExParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    sfxExParams: struct_sfx_emitter_ex_params_t

class struct_kourawing_t(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[768])
    sfxExParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    sfxExParams: struct_sfx_emitter_ex_params_t

class struct_kuribo_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: fx32 (struct_fx32)
    direction: quaternion_t (struct_quaternion_t)
    targetDir: quaternion_t (struct_quaternion_t)
    squashRatio: fx32 (struct_fx32)
    squashVelocity: fx32 (struct_fx32)
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    frame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fieldF4: int (POINTER(i))
    dirInterpRatio: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    reappearAfterHit: int (POINTER(i))
    alpha: int (POINTER(H))
    field102: int (POINTER(h))
    field104: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: fx32
    direction: quaternion_t
    targetDir: quaternion_t
    squashRatio: fx32
    squashVelocity: fx32
    pathWalker: struct_pw_pathwalker_t
    frame: int
    PADDING_0: list[int]
    fieldF4: int
    dirInterpRatio: int
    PADDING_1: list[int]
    reappearAfterHit: int
    alpha: int
    field102: int
    field104: int

class struct_light_t(Structure):
    """
    ```python
    color: int (POINTER(H))
    r: int (POINTER(h))
    g: int (POINTER(h))
    b: int (POINTER(h))
    rDelta: int (POINTER(h))
    gDelta: int (POINTER(h))
    bDelta: int (POINTER(h))
    lightMask: int (POINTER(H))
    progress: fx16 (struct_fx16)
    ```
    """
    _pack_: ClassVar[int] = 1
    color: int
    r: int
    g: int
    b: int
    rDelta: int
    gDelta: int
    bDelta: int
    lightMask: int
    progress: fx16

class struct_list_link_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    list: POINTER_T[struct_NNSFndList] (POINTER(struct_NNSFndList))
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    list: POINTER_T[struct_NNSFndList]

class struct_max_align_t(Structure):
    """
    ```python
    __clang_max_align_nonce1: int (POINTER(l))
    __clang_max_align_nonce2: float (POINTER(d))
    ```
    """
    _pack_: ClassVar[int] = 1
    __clang_max_align_nonce1: int
    __clang_max_align_nonce2: float

class struct_mdat_clip_area_list_entry_t(Structure):
    """
    ```python
    entry: POINTER_T[struct_nkm_area_entry_t] (POINTER(struct_nkm_area_entry_t))
    next: POINTER_T[struct_mdat_clip_area_list_entry_t] (POINTER(struct_mdat_clip_area_list_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    entry: POINTER_T[struct_nkm_area_entry_t]
    next: POINTER_T[struct_mdat_clip_area_list_entry_t]

class struct_mdat_enemypath_data_t(Structure):
    """
    ```python
    points: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    firstPoint: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    lastPoint: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    points: POINTER_T[struct_mdat_enemypoint_t]
    firstPoint: POINTER_T[struct_mdat_enemypoint_t]
    lastPoint: POINTER_T[struct_mdat_enemypoint_t]

class struct_mdat_enemypoint_t(Structure):
    """
    ```python
    next: list[POINTER_T[struct_mdat_enemypoint_t]] (POINTER(struct_mdat_enemypoint_t)[3])
    previous: list[POINTER_T[struct_mdat_enemypoint_t]] (POINTER(struct_mdat_enemypoint_t)[3])
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    radius: fx32 (struct_fx32)
    settings: POINTER_T[struct_nkm_epoi_entry_settings_t] (POINTER(struct_nkm_epoi_entry_settings_t))
    nextCount: int (POINTER(H))
    previousCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: list[POINTER_T[struct_mdat_enemypoint_t]]
    previous: list[POINTER_T[struct_mdat_enemypoint_t]]
    position: POINTER_T[struct_VecFx32]
    radius: fx32
    settings: POINTER_T[struct_nkm_epoi_entry_settings_t]
    nextCount: int
    previousCount: int

class struct_mdat_itempath_data_t(Structure):
    """
    ```python
    points: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    firstPoint: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    lastPoint: POINTER_T[struct_mdat_itempoint_t] (POINTER(struct_mdat_itempoint_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    points: POINTER_T[struct_mdat_itempoint_t]
    firstPoint: POINTER_T[struct_mdat_itempoint_t]
    lastPoint: POINTER_T[struct_mdat_itempoint_t]

class struct_mdat_itempoint_t(Structure):
    """
    ```python
    next: list[POINTER_T[struct_mdat_itempoint_t]] (POINTER(struct_mdat_itempoint_t)[3])
    previous: list[POINTER_T[struct_mdat_itempoint_t]] (POINTER(struct_mdat_itempoint_t)[3])
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    radius: fx32 (struct_fx32)
    recalcIdx: int (POINTER(B))
    dirX: int (POINTER(b))
    dirY: int (POINTER(b))
    dirZ: int (POINTER(b))
    nextCount: int (POINTER(H))
    previousCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: list[POINTER_T[struct_mdat_itempoint_t]]
    previous: list[POINTER_T[struct_mdat_itempoint_t]]
    position: POINTER_T[struct_VecFx32]
    radius: fx32
    recalcIdx: int
    dirX: int
    dirY: int
    dirZ: int
    nextCount: int
    previousCount: int

class struct_mdat_mapdata_t(Structure):
    """
    ```python
    obji: POINTER_T[struct_nkm_obji_entry_t] (POINTER(struct_nkm_obji_entry_t))
    objiCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    path: POINTER_T[struct_nkm_path_entry_t] (POINTER(struct_nkm_path_entry_t))
    pathCount: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    poit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    poitCount: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    stag: POINTER_T[struct_nkm_stag_data_t] (POINTER(struct_nkm_stag_data_t))
    ktps: POINTER_T[struct_nkm_ktps_entry_t] (POINTER(struct_nkm_ktps_entry_t))
    ktpsCount: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    ktpj: POINTER_T[struct_nkm_ktpj_entry_t] (POINTER(struct_nkm_ktpj_entry_t))
    ktpjCount: int (POINTER(H))
    PADDING_4: list[int] (POINTER(B)[2])
    ktp2: POINTER_T[struct_nkm_ktp2_entry_t] (POINTER(struct_nkm_ktp2_entry_t))
    ktp2Count: int (POINTER(H))
    PADDING_5: list[int] (POINTER(B)[2])
    ktpc: POINTER_T[struct_nkm_ktpc_entry_t] (POINTER(struct_nkm_ktpc_entry_t))
    ktpcCount: int (POINTER(H))
    PADDING_6: list[int] (POINTER(B)[2])
    ktpm: POINTER_T[struct_nkm_ktpm_entry_t] (POINTER(struct_nkm_ktpm_entry_t))
    ktpmCount: int (POINTER(H))
    PADDING_7: list[int] (POINTER(B)[2])
    cpoi: POINTER_T[struct_nkm_cpoi_entry_t] (POINTER(struct_nkm_cpoi_entry_t))
    cpoiCount: int (POINTER(H))
    PADDING_8: list[int] (POINTER(B)[2])
    cpat: POINTER_T[struct_nkm_cpat_entry_t] (POINTER(struct_nkm_cpat_entry_t))
    cpatCount: int (POINTER(H))
    PADDING_9: list[int] (POINTER(B)[2])
    ipoi: union_nkm_ipoi_entry_pointer_t (union_nkm_ipoi_entry_pointer_t)
    ipoiCount: int (POINTER(H))
    PADDING_10: list[int] (POINTER(B)[2])
    ipat: POINTER_T[struct_nkm_ipat_entry_t] (POINTER(struct_nkm_ipat_entry_t))
    ipatCount: int (POINTER(H))
    PADDING_11: list[int] (POINTER(B)[2])
    epoi: POINTER_T[struct_nkm_epoi_entry_t] (POINTER(struct_nkm_epoi_entry_t))
    epoiCount: int (POINTER(H))
    PADDING_12: list[int] (POINTER(B)[2])
    epat: POINTER_T[struct_nkm_epat_entry_t] (POINTER(struct_nkm_epat_entry_t))
    epatCount: int (POINTER(H))
    PADDING_13: list[int] (POINTER(B)[2])
    area: POINTER_T[struct_nkm_area_entry_t] (POINTER(struct_nkm_area_entry_t))
    areaCount: int (POINTER(H))
    PADDING_14: list[int] (POINTER(B)[2])
    came: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameCount: int (POINTER(H))
    PADDING_15: list[int] (POINTER(B)[2])
    mepo: POINTER_T[struct_nkm_mepo_entry_t] (POINTER(struct_nkm_mepo_entry_t))
    mepoCount: int (POINTER(H))
    PADDING_16: list[int] (POINTER(B)[2])
    mepa: POINTER_T[struct_nkm_mepa_entry_t] (POINTER(struct_nkm_mepa_entry_t))
    mepaCount: int (POINTER(H))
    PADDING_17: list[int] (POINTER(B)[2])
    paths: POINTER_T[struct_mdat_path_t] (POINTER(struct_mdat_path_t))
    cpoiKeyCount: int (POINTER(H))
    cpatLastCpoiIndex: int (POINTER(H))
    cpatMaxSectionOrder: int (POINTER(H))
    unknown49: int (POINTER(B))
    unknown50: int (POINTER(B))
    enemyPathData: struct_mdat_enemypath_data_t (struct_mdat_enemypath_data_t)
    itemPathData: struct_mdat_itempath_data_t (struct_mdat_itempath_data_t)
    mgEnemyPathData: struct_mdat_mgenemypath_data_t (struct_mdat_mgenemypath_data_t)
    cameIntroFirstTopCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameIntroFirstBottomCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameType6: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameBattleIntroCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    cameMissionFinishCam: POINTER_T[struct_nkm_came_entry_t] (POINTER(struct_nkm_came_entry_t))
    clipAreaLists: list[POINTER_T[struct_mdat_clip_area_list_entry_t]] (POINTER(struct_mdat_clip_area_list_entry_t)[8])
    ktpjIndexTable: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    ktpcIndexTable: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    curMgRespawnId: int (POINTER(H))
    enemyRespawnRouteAreaCount: int (POINTER(H))
    trackLength: fx32 (struct_fx32)
    trackLengthDiv15000: int (POINTER(I))
    nkmVersion: int (POINTER(H))
    unknown141: int (POINTER(B))
    missionEndAreaCount: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    obji: POINTER_T[struct_nkm_obji_entry_t]
    objiCount: int
    PADDING_0: list[int]
    path: POINTER_T[struct_nkm_path_entry_t]
    pathCount: int
    PADDING_1: list[int]
    poit: POINTER_T[struct_nkm_poit_entry_t]
    poitCount: int
    PADDING_2: list[int]
    stag: POINTER_T[struct_nkm_stag_data_t]
    ktps: POINTER_T[struct_nkm_ktps_entry_t]
    ktpsCount: int
    PADDING_3: list[int]
    ktpj: POINTER_T[struct_nkm_ktpj_entry_t]
    ktpjCount: int
    PADDING_4: list[int]
    ktp2: POINTER_T[struct_nkm_ktp2_entry_t]
    ktp2Count: int
    PADDING_5: list[int]
    ktpc: POINTER_T[struct_nkm_ktpc_entry_t]
    ktpcCount: int
    PADDING_6: list[int]
    ktpm: POINTER_T[struct_nkm_ktpm_entry_t]
    ktpmCount: int
    PADDING_7: list[int]
    cpoi: POINTER_T[struct_nkm_cpoi_entry_t]
    cpoiCount: int
    PADDING_8: list[int]
    cpat: POINTER_T[struct_nkm_cpat_entry_t]
    cpatCount: int
    PADDING_9: list[int]
    ipoi: union_nkm_ipoi_entry_pointer_t
    ipoiCount: int
    PADDING_10: list[int]
    ipat: POINTER_T[struct_nkm_ipat_entry_t]
    ipatCount: int
    PADDING_11: list[int]
    epoi: POINTER_T[struct_nkm_epoi_entry_t]
    epoiCount: int
    PADDING_12: list[int]
    epat: POINTER_T[struct_nkm_epat_entry_t]
    epatCount: int
    PADDING_13: list[int]
    area: POINTER_T[struct_nkm_area_entry_t]
    areaCount: int
    PADDING_14: list[int]
    came: POINTER_T[struct_nkm_came_entry_t]
    cameCount: int
    PADDING_15: list[int]
    mepo: POINTER_T[struct_nkm_mepo_entry_t]
    mepoCount: int
    PADDING_16: list[int]
    mepa: POINTER_T[struct_nkm_mepa_entry_t]
    mepaCount: int
    PADDING_17: list[int]
    paths: POINTER_T[struct_mdat_path_t]
    cpoiKeyCount: int
    cpatLastCpoiIndex: int
    cpatMaxSectionOrder: int
    unknown49: int
    unknown50: int
    enemyPathData: struct_mdat_enemypath_data_t
    itemPathData: struct_mdat_itempath_data_t
    mgEnemyPathData: struct_mdat_mgenemypath_data_t
    cameIntroFirstTopCam: POINTER_T[struct_nkm_came_entry_t]
    cameIntroFirstBottomCam: POINTER_T[struct_nkm_came_entry_t]
    cameType6: POINTER_T[struct_nkm_came_entry_t]
    cameBattleIntroCam: POINTER_T[struct_nkm_came_entry_t]
    cameMissionFinishCam: POINTER_T[struct_nkm_came_entry_t]
    clipAreaLists: list[POINTER_T[struct_mdat_clip_area_list_entry_t]]
    ktpjIndexTable: POINTER_T[c_ushort]
    ktpcIndexTable: POINTER_T[c_ushort]
    curMgRespawnId: int
    enemyRespawnRouteAreaCount: int
    trackLength: fx32
    trackLengthDiv15000: int
    nkmVersion: int
    unknown141: int
    missionEndAreaCount: int

class struct_mdat_mgenemypath_data_t(Structure):
    """
    ```python
    points: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    firstPoint: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    lastPoint: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    points: POINTER_T[struct_mdat_mgenemypoint_t]
    firstPoint: POINTER_T[struct_mdat_mgenemypoint_t]
    lastPoint: POINTER_T[struct_mdat_mgenemypoint_t]

class struct_mdat_mgenemypoint_t(Structure):
    """
    ```python
    next: list[POINTER_T[struct_mdat_mgenemypoint_t]] (POINTER(struct_mdat_mgenemypoint_t)[8])
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    radius: fx32 (struct_fx32)
    settings: POINTER_T[struct_nkm_mepo_entry_settings_t] (POINTER(struct_nkm_mepo_entry_settings_t))
    nextCount: int (POINTER(H))
    nextIsNewPathMask: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: list[POINTER_T[struct_mdat_mgenemypoint_t]]
    position: POINTER_T[struct_VecFx32]
    radius: fx32
    settings: POINTER_T[struct_nkm_mepo_entry_settings_t]
    nextCount: int
    nextIsNewPathMask: int
    PADDING_0: int

class struct_mdat_path_t(Structure):
    """
    ```python
    path: POINTER_T[struct_nkm_path_entry_t] (POINTER(struct_nkm_path_entry_t))
    poit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: POINTER_T[struct_nkm_path_entry_t]
    poit: POINTER_T[struct_nkm_poit_entry_t]

class struct_mgcnt_driver_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    state: int (POINTER(I))
    position: struct_VecFx32 (struct_VecFx32)
    field18: int (POINTER(i))
    field1C: int (POINTER(i))
    field20: int (POINTER(I))
    field24: list[int] (POINTER(I)[8])
    field44: int (POINTER(H))
    mgDriverTeamId: int (POINTER(H))
    place: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    balloonShineCount: int (POINTER(i))
    balloonShineInventoryCount: int (POINTER(H))
    gap52: list[int] (POINTER(B)[18])
    micInflatingCounter: int (POINTER(i))
    keyInflating: int (POINTER(i))
    isInflating: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    state: int
    position: struct_VecFx32
    field18: int
    field1C: int
    field20: int
    field24: list[int]
    field44: int
    mgDriverTeamId: int
    place: int
    PADDING_0: list[int]
    balloonShineCount: int
    balloonShineInventoryCount: int
    gap52: list[int]
    micInflatingCounter: int
    keyInflating: int
    isInflating: int

class struct_mgcnt_t(Structure):
    """
    ```python
    drivers: list[struct_mgcnt_driver_t] (struct_mgcnt_driver_t[8])
    tryStealBalloonFunc: Callable[[int, int], c_int] (CFunctionType)
    field384: Callable[[int, int], None] (CFunctionType)
    onDamageFunc: Callable[[int, int], c_int] (CFunctionType)
    onKillFunc: Callable[[int], None] (CFunctionType)
    onEndFunc: Callable[[], None] (CFunctionType)
    gap394: list[int] (POINTER(B)[8])
    applyForceToDriverBalloonsFunc: Callable[[int, POINTER_T[struct_VecFx32]], None] (CFunctionType)
    collectableShineCount: int (POINTER(H))
    timeLimit: int (POINTER(H))
    shineRunnersRound: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    mgEndDelayCounter: int (POINTER(i))
    maxOwnedShineCount: int (POINTER(i))
    minOwnedShineCount: int (POINTER(i))
    winDriverTeamId: int (POINTER(i))
    lastShineMepoIdx: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    blncntDriverEntries: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    drivers: list[struct_mgcnt_driver_t]
    tryStealBalloonFunc: Callable[[int, int], c_int]
    field384: Callable[[int, int], None]
    onDamageFunc: Callable[[int, int], c_int]
    onKillFunc: Callable[[int], None]
    onEndFunc: Callable[[], None]
    gap394: list[int]
    applyForceToDriverBalloonsFunc: Callable[[int, POINTER_T[struct_VecFx32]], None]
    collectableShineCount: int
    timeLimit: int
    shineRunnersRound: int
    PADDING_0: list[int]
    mgEndDelayCounter: int
    maxOwnedShineCount: int
    minOwnedShineCount: int
    winDriverTeamId: int
    lastShineMepoIdx: int
    PADDING_1: list[int]
    blncntDriverEntries: c_void_p

class struct_mic_t(Structure):
    """
    ```python
    sampleBuffer: list[int] (POINTER(b)[1024])
    autoParam: struct_MICAutoParam (struct_MICAutoParam)
    frameCounter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    sampleBuffer: list[int]
    autoParam: struct_MICAutoParam
    frameCounter: int

class struct_mission_config_t(Structure):
    """
    ```python
    timeLimit: int (POINTER(H))
    rankTime: int (POINTER(H))
    timeTolerance: int (POINTER(h))
    id: int (POINTER(B))
    task: int (POINTER(B))
    course: int (POINTER(B))
    ccMode: int (POINTER(B))
    character: int (POINTER(B))
    kart: int (POINTER(B))
    menuId: int (POINTER(B))
    fieldD: int (POINTER(B))
    camParamsIdx: int (POINTER(B))
    targetValue: int (POINTER(B))
    winDelay: int (POINTER(H))
    gap12: int (POINTER(H))
    objectIds: list[int] (POINTER(H)[4])
    flags: int (POINTER(H))
    enemyCharacter: int (POINTER(B))
    enemyKart: int (POINTER(B))
    name: list[int] (POINTER(B)[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    timeLimit: int
    rankTime: int
    timeTolerance: int
    id: int
    task: int
    course: int
    ccMode: int
    character: int
    kart: int
    menuId: int
    fieldD: int
    camParamsIdx: int
    targetValue: int
    winDelay: int
    gap12: int
    objectIds: list[int]
    flags: int
    enemyCharacter: int
    enemyKart: int
    name: list[int]

class struct_mission_mr_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    nrMissions: int (POINTER(I))
    missions: list[struct_mission_config_t] (struct_mission_config_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    nrMissions: int
    missions: list[struct_mission_config_t]

class struct_mobj_config_t(Structure):
    """
    ```python
    driverCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_driver_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint] (CFunctionType)
    itemCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint] (CFunctionType)
    colType: int (POINTER(I))
    size: struct_VecFx32 (struct_VecFx32)
    sphereCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_VecFx32], fx32, POINTER_T[struct_VecFx32]], c_int] (CFunctionType)
    providesPushback: int (POINTER(i))
    logicType: int (POINTER(I))
    driverHitSfxId: int (POINTER(i))
    itemHitSfxId: int (POINTER(I))
    nearClip: fx32 (struct_fx32)
    farClip: fx32 (struct_fx32)
    has3DModel: int (POINTER(i))
    sfxAudibleMaxCamYDiff: fx32 (struct_fx32)
    sfxAudibleMinCamYDiff: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    driverCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_driver_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint]
    itemCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint]
    colType: int
    size: struct_VecFx32
    sphereCollideFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_VecFx32], fx32, POINTER_T[struct_VecFx32]], c_int]
    providesPushback: int
    logicType: int
    driverHitSfxId: int
    itemHitSfxId: int
    nearClip: fx32
    farClip: fx32
    has3DModel: int
    sfxAudibleMaxCamYDiff: fx32
    sfxAudibleMinCamYDiff: fx32

class struct_mobj_def_t(Structure):
    """
    ```python
    instanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    instanceSize: int (POINTER(I))
    instInitFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_nkm_obji_entry_t], c_void_p], None] (CFunctionType)
    configSetupFunc: Callable[[], POINTER_T[struct_mobj_config_t]] (CFunctionType)
    renderPartSetupFuncs: list[Callable[[], POINTER_T[struct_mobj_render_part_t]]] (CFunctionType[3])
    logicPartSetupFunc: Callable[[], POINTER_T[struct_mobj_logic_part_t]] (CFunctionType)
    config: POINTER_T[struct_mobj_config_t] (POINTER(struct_mobj_config_t))
    renderParts: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[3])
    logicPart: POINTER_T[struct_mobj_logic_part_t] (POINTER(struct_mobj_logic_part_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    instanceCount: int
    PADDING_0: list[int]
    instanceSize: int
    instInitFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_nkm_obji_entry_t], c_void_p], None]
    configSetupFunc: Callable[[], POINTER_T[struct_mobj_config_t]]
    renderPartSetupFuncs: list[Callable[[], POINTER_T[struct_mobj_render_part_t]]]
    logicPartSetupFunc: Callable[[], POINTER_T[struct_mobj_logic_part_t]]
    config: POINTER_T[struct_mobj_config_t]
    renderParts: list[POINTER_T[struct_mobj_render_part_t]]
    logicPart: POINTER_T[struct_mobj_logic_part_t]

class struct_mobj_inst_t(Structure):
    """
    ```python
    objectId: int (POINTER(H))
    flags: int (POINTER(H))
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    mtx: union_MtxFx43 (union_MtxFx43)
    size: struct_VecFx32 (struct_VecFx32)
    colEntryId: int (POINTER(h))
    alpha: int (POINTER(H))
    nearClip: fx32 (struct_fx32)
    farClip: fx32 (struct_fx32)
    sfxMaxDistanceSquare: int (POINTER(i))
    clipAreaMask: int (POINTER(I))
    visibilityFlags: int (POINTER(I))
    has3DModel: int (POINTER(H))
    rotY: int (POINTER(H))
    stateMachine: struct_state_machine_t (struct_state_machine_t)
    soundEmitter: POINTER_T[struct_sfx_emitter_t] (POINTER(struct_sfx_emitter_t))
    config: POINTER_T[struct_mobj_config_t] (POINTER(struct_mobj_config_t))
    objiEntry: POINTER_T[struct_nkm_obji_entry_t] (POINTER(struct_nkm_obji_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    objectId: int
    flags: int
    position: struct_VecFx32
    velocity: struct_VecFx32
    scale: struct_VecFx32
    mtx: union_MtxFx43
    size: struct_VecFx32
    colEntryId: int
    alpha: int
    nearClip: fx32
    farClip: fx32
    sfxMaxDistanceSquare: int
    clipAreaMask: int
    visibilityFlags: int
    has3DModel: int
    rotY: int
    stateMachine: struct_state_machine_t
    soundEmitter: POINTER_T[struct_sfx_emitter_t]
    config: POINTER_T[struct_mobj_config_t]
    objiEntry: POINTER_T[struct_nkm_obji_entry_t]

class struct_mobj_logic_part_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    mobjInstanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    globalInitFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None] (CFunctionType)
    globalPreUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None] (CFunctionType)
    instanceUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t], POINTER_T[struct_mobj_inst_t]], None] (CFunctionType)
    globalPostUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None] (CFunctionType)
    type: int (POINTER(I))
    thunderFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint] (CFunctionType)
    thunderObjResp: int (POINTER(I))
    thisPointer: POINTER_T[POINTER_T[struct_mobj_logic_part_t]] (POINTER(POINTER(struct_mobj_logic_part_t)))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    mobjInstanceCount: int
    PADDING_0: list[int]
    globalInitFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None]
    globalPreUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None]
    instanceUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t], POINTER_T[struct_mobj_inst_t]], None]
    globalPostUpdateFunc: Callable[[POINTER_T[struct_mobj_logic_part_t]], None]
    type: int
    thunderFunc: Callable[[POINTER_T[struct_mobj_inst_t], POINTER_T[struct_it_item_inst_t], POINTER_T[c_ubyte], POINTER_T[c_ubyte]], c_uint]
    thunderObjResp: int
    thisPointer: POINTER_T[POINTER_T[struct_mobj_logic_part_t]]

class struct_mobj_model_t(Structure):
    """
    ```python
    scale: struct_VecFx32 (struct_VecFx32)
    bbModel: POINTER_T[struct_bbm_model_t] (POINTER(struct_bbm_model_t))
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    shadowModel: POINTER_T[struct_shadowmodel_t] (POINTER(struct_shadowmodel_t))
    nsbmd: c_void_p (c_void_p)
    nsbcaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbmaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtaAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    scale: struct_VecFx32
    bbModel: POINTER_T[struct_bbm_model_t]
    model: POINTER_T[struct_model_t]
    shadowModel: POINTER_T[struct_shadowmodel_t]
    nsbmd: c_void_p
    nsbcaAnim: POINTER_T[struct_anim_manager_t]
    nsbtpAnim: POINTER_T[struct_anim_manager_t]
    nsbmaAnim: POINTER_T[struct_anim_manager_t]
    nsbtaAnim: POINTER_T[struct_anim_manager_t]

class struct_mobj_render_part_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    mobjInstanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    globalInitFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None] (CFunctionType)
    globalPreRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None] (CFunctionType)
    instanceRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t], POINTER_T[struct_mobj_inst_t], POINTER_T[union_MtxFx43], int], None] (CFunctionType)
    globalPostRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None] (CFunctionType)
    type: int (POINTER(I))
    isTranslucent: int (POINTER(i))
    isShadow: int (POINTER(i))
    alphaSortList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    thisPointer: POINTER_T[POINTER_T[struct_mobj_render_part_t]] (POINTER(POINTER(struct_mobj_render_part_t)))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    mobjInstanceCount: int
    PADDING_0: list[int]
    globalInitFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None]
    globalPreRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None]
    instanceRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t], POINTER_T[struct_mobj_inst_t], POINTER_T[union_MtxFx43], int], None]
    globalPostRenderFunc: Callable[[POINTER_T[struct_mobj_render_part_t]], None]
    type: int
    isTranslucent: int
    isShadow: int
    alphaSortList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    thisPointer: POINTER_T[POINTER_T[struct_mobj_render_part_t]]

class struct_mobj_state_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    mobjInstanceCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    renderPartList: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[24])
    renderPart3dList: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[24])
    renderPart2dList: list[POINTER_T[struct_mobj_render_part_t]] (POINTER(struct_mobj_render_part_t)[24])
    renderPartCount: int (POINTER(H))
    renderPart3dCount: int (POINTER(H))
    renderPart2dCount: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    field130: int (POINTER(I))
    logicPartList: list[POINTER_T[struct_mobj_logic_part_t]] (POINTER(struct_mobj_logic_part_t)[16])
    logicPartCount: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    field178: int (POINTER(I))
    hasKoopaBlock: int (POINTER(i))
    hasRotatingCylinder: int (POINTER(i))
    hasBridge: int (POINTER(i))
    hasWall: int (POINTER(i))
    pseudoItem: struct_it_item_inst_t (struct_it_item_inst_t)
    logicUpdateEnabled: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    mobjInstanceCount: int
    PADDING_0: list[int]
    renderPartList: list[POINTER_T[struct_mobj_render_part_t]]
    renderPart3dList: list[POINTER_T[struct_mobj_render_part_t]]
    renderPart2dList: list[POINTER_T[struct_mobj_render_part_t]]
    renderPartCount: int
    renderPart3dCount: int
    renderPart2dCount: int
    PADDING_1: list[int]
    field130: int
    logicPartList: list[POINTER_T[struct_mobj_logic_part_t]]
    logicPartCount: int
    PADDING_2: list[int]
    field178: int
    hasKoopaBlock: int
    hasRotatingCylinder: int
    hasBridge: int
    hasWall: int
    pseudoItem: struct_it_item_inst_t
    logicUpdateEnabled: int

class struct_mobj_table_entry_t(Structure):
    """
    ```python
    id: int (POINTER(I))
    def_: POINTER_T[struct_mobj_def_t] (POINTER(struct_mobj_def_t))
    arg: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    def_: POINTER_T[struct_mobj_def_t]
    arg: c_void_p

class struct_model_res_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    nsbmd: c_void_p (c_void_p)
    texRes: POINTER_T[struct_NNSG3dResTex_] (POINTER(struct_NNSG3dResTex_))
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    nsbmd: c_void_p
    texRes: POINTER_T[struct_NNSG3dResTex_]

class struct_model_t(Structure):
    """
    ```python
    renderObj: struct_NNSG3dRenderObj_ (struct_NNSG3dRenderObj_)
    cullReversed: int (POINTER(I))
    render1Mat1Shp: int (POINTER(i))
    res: struct_model_res_t (struct_model_res_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    renderObj: struct_NNSG3dRenderObj_
    cullReversed: int
    render1Mat1Shp: int
    res: struct_model_res_t

class struct_movetree_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    pointDuration: int (POINTER(i))
    counter: int (POINTER(i))
    speed: fx32 (struct_fx32)
    nsbcaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    nsbcaFrameDelta: int (POINTER(i))
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    shadow: struct_objshadow_t (struct_objshadow_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    pointDuration: int
    counter: int
    speed: fx32
    nsbcaFrame: int
    PADDING_0: list[int]
    nsbcaFrameDelta: int
    pathwalker: struct_pw_pathwalker_t
    state: int
    shadow: struct_objshadow_t

class struct_mpicn_def_t(Structure):
    """
    ```python
    createFunc: Callable[[], c_int] (CFunctionType)
    destroyFunc: Callable[[], None] (CFunctionType)
    updateFunc: Callable[[], None] (CFunctionType)
    renderFunc: Callable[[POINTER_T[struct_oam_buf_t]], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    createFunc: Callable[[], c_int]
    destroyFunc: Callable[[], None]
    updateFunc: Callable[[], None]
    renderFunc: Callable[[POINTER_T[struct_oam_buf_t]], None]

class struct_mpicn_icon_data_t(Structure):
    """
    ```python
    minPriority: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field4: int (POINTER(I))
    field8: int (POINTER(I))
    groupCount: int (POINTER(I))
    destroyFuncs: list[Callable[[], None]] (CFunctionType[49])
    updateFuncs: list[Callable[[], None]] (CFunctionType[49])
    renderFuncs: list[Callable[[POINTER_T[struct_oam_buf_t]], None]] (CFunctionType[49])
    ```
    """
    _pack_: ClassVar[int] = 1
    minPriority: int
    PADDING_0: list[int]
    field4: int
    field8: int
    groupCount: int
    destroyFuncs: list[Callable[[], None]]
    updateFuncs: list[Callable[[], None]]
    renderFuncs: list[Callable[[POINTER_T[struct_oam_buf_t]], None]]

class struct_mpicn_mobj_icon_cell_t(Structure):
    """
    ```python
    position: struct_vec2i_t (struct_vec2i_t)
    cell: POINTER_T[struct_NNSG2dCellData] (POINTER(struct_NNSG2dCellData))
    priority: int (POINTER(H))
    flipX: int (POINTER(H))
    rotation: int (POINTER(H))
    field12: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_vec2i_t
    cell: POINTER_T[struct_NNSG2dCellData]
    priority: int
    flipX: int
    rotation: int
    field12: int

class struct_mpicn_mobj_icon_group_t(Structure):
    """
    ```python
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]] (POINTER(POINTER(struct_mobj_inst_t)))
    cellCount: int (POINTER(I))
    mobjInstanceCount: int (POINTER(i))
    points: POINTER_T[struct_vec2i_t] (POINTER(struct_vec2i_t))
    cells: POINTER_T[struct_mpicn_mobj_icon_cell_t] (POINTER(struct_mpicn_mobj_icon_cell_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobjInstanceList: POINTER_T[POINTER_T[struct_mobj_inst_t]]
    cellCount: int
    mobjInstanceCount: int
    points: POINTER_T[struct_vec2i_t]
    cells: POINTER_T[struct_mpicn_mobj_icon_cell_t]

class struct_mrbarrier_t(Structure):
    """
    ```python
    dcolMObj: struct_dcol_inst_t (struct_dcol_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    dcolMObj: struct_dcol_inst_t

class struct_net_field_12F0_t_(Structure):
    """
    ```python
    gap0: list[int] (POINTER(B)[12])
    inetStatus: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    gap0: list[int]
    inetStatus: int

class struct_net_match_property_t_(Structure):
    """
    ```python
    value: int (POINTER(I))
    key: list[int] (POINTER(B)[16])
    field14: int (POINTER(B))
    gap15: list[int] (POINTER(B)[2])
    field16: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    value: int
    key: list[int]
    field14: int
    gap15: list[int]
    field16: int

class struct_net_match_status_t_(Structure):
    """
    ```python
    state: int (POINTER(I))
    PADDING_0: list[int] (POINTER(B)[4])
    rand: struct_MATHRandContext32 (struct_MATHRandContext32)
    gap1C: list[int] (POINTER(B)[20])
    field30: int (POINTER(I))
    field34: list[int] (POINTER(I)[4])
    gap44: list[int] (POINTER(B)[5])
    emblemNotSentAidMax: int (POINTER(B))
    gap4A: list[int] (POINTER(B)[16])
    receivedHellosBitmap: int (POINTER(B))
    receivedBitmap: int (POINTER(B))
    field5C: int (POINTER(B))
    field5D: int (POINTER(B))
    field5E: int (POINTER(B))
    field5F: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    PADDING_0: list[int]
    rand: struct_MATHRandContext32
    gap1C: list[int]
    field30: int
    field34: list[int]
    gap44: list[int]
    emblemNotSentAidMax: int
    gap4A: list[int]
    receivedHellosBitmap: int
    receivedBitmap: int
    field5C: int
    field5D: int
    field5E: int
    field5F: int
    PADDING_1: list[int]

class struct_net_menu_config_t_(Structure):
    """
    ```python
    field0: list[int] (POINTER(I)[4])
    field10: list[int] (POINTER(I)[4])
    selectedCourse: int (POINTER(I))
    field24: int (POINTER(I))
    field28: int (POINTER(I))
    vote: int (POINTER(I))
    gap30: list[int] (POINTER(B)[4])
    field34: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: list[int]
    field10: list[int]
    selectedCourse: int
    field24: int
    field28: int
    vote: int
    gap30: list[int]
    field34: int

class struct_net_menu_dgram_header_t_(Structure):
    """
    ```python
    opcode: int (POINTER(I))
    size: int (POINTER(I))
    aidSrc: int (POINTER(B))
    aidDest: int (POINTER(B))
    connectedAids: int (POINTER(B))
    fieldB: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    opcode: int
    size: int
    aidSrc: int
    aidDest: int
    connectedAids: int
    fieldB: int

class struct_net_menu_dgram_t_(Structure):
    """
    ```python
    header: struct_net_menu_dgram_header_t_ (struct_net_menu_dgram_header_t_)
    data: struct_net_menu_config_t_ (struct_net_menu_config_t_)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_net_menu_dgram_header_t_
    data: struct_net_menu_config_t_

class struct_net_menu_profile_dgram_t_(Structure):
    """
    ```python
    header: struct_net_menu_dgram_header_t_ (struct_net_menu_dgram_header_t_)
    profile: struct_struct_217AA00_field45C_t (struct_struct_217AA00_field45C_t)
    field238: int (POINTER(I))
    field23C: int (POINTER(I))
    field240: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_net_menu_dgram_header_t_
    profile: struct_struct_217AA00_field45C_t
    field238: int
    field23C: int
    field240: int

class struct_net_race_state_t(Structure):
    """
    ```python
    stateMachine: struct_state_machine_t (struct_state_machine_t)
    PADDING_0: list[int] (POINTER(B)[4])
    pingStatuses: list[struct_rnet_ping_t_] (struct_rnet_ping_t_[4])
    fieldF4: int (POINTER(I))
    lastSentAid: int (POINTER(H))
    heardFromBitmap: int (POINTER(B))
    fieldFB: int (POINTER(B))
    initialAidsBitmap: int (POINTER(B))
    fieldFD: int (POINTER(B))
    gapFE: list[int] (POINTER(B)[6])
    drivers: list[struct_struc_222] (struct_struc_222[4])
    itemActionSlots: list[struct_rnet_item_action_entry_t_] (struct_rnet_item_action_entry_t_[16])
    incomingItemActions: list[struct_rnet_item_action_entry_t_] (struct_rnet_item_action_entry_t_[4][16])
    itemActionProcessed: list[int] (POINTER(B)[4][16])
    bufferAvailable: int (POINTER(h))
    gap726: list[int] (POINTER(B)[2])
    frameCounter: int (POINTER(i))
    field72C: int (POINTER(i))
    gap730: list[int] (POINTER(B)[4])
    lastAidSent: int (POINTER(H))
    field_736: int (POINTER(H))
    idleTime: int (POINTER(H))
    nextAid: int (POINTER(B))
    gap73B: list[int] (POINTER(B)[3])
    field73E: int (POINTER(B))
    gap73F: int (POINTER(B))
    field740: list[int] (POINTER(H)[4])
    sendBufferHeader2: int (POINTER(B))
    connectedAidsBitmap: int (POINTER(B))
    field74A: list[int] (POINTER(B)[4])
    field74E: list[int] (POINTER(B)[4])
    gap752: list[int] (POINTER(B)[2])
    dwcSendBuffer: POINTER_T[struct_rnet_dgram_t_] (POINTER(struct_rnet_dgram_t_))
    packetNextState: int (POINTER(I))
    flags: int (POINTER(H))
    gap75E: list[int] (POINTER(B)[1])
    field75F: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    stateMachine: struct_state_machine_t
    PADDING_0: list[int]
    pingStatuses: list[struct_rnet_ping_t_]
    fieldF4: int
    lastSentAid: int
    heardFromBitmap: int
    fieldFB: int
    initialAidsBitmap: int
    fieldFD: int
    gapFE: list[int]
    drivers: list[struct_struc_222]
    itemActionSlots: list[struct_rnet_item_action_entry_t_]
    incomingItemActions: list[struct_rnet_item_action_entry_t_]
    itemActionProcessed: list[int]
    bufferAvailable: int
    gap726: list[int]
    frameCounter: int
    field72C: int
    gap730: list[int]
    lastAidSent: int
    field_736: int
    idleTime: int
    nextAid: int
    gap73B: list[int]
    field73E: int
    gap73F: int
    field740: list[int]
    sendBufferHeader2: int
    connectedAidsBitmap: int
    field74A: list[int]
    field74E: list[int]
    gap752: list[int]
    dwcSendBuffer: POINTER_T[struct_rnet_dgram_t_]
    packetNextState: int
    flags: int
    gap75E: list[int]
    field75F: int
    PADDING_1: list[int]

class struct_net_state_field_B2C_t_(Structure):
    """
    ```python
    control: list[int] (POINTER(B)[3508])
    fieldDB4: int (POINTER(B))
    fieldDB5: int (POINTER(B))
    gapDB6: list[int] (POINTER(B)[2])
    fieldDB8: int (POINTER(I))
    state: int (POINTER(I))
    region: struct_net_match_property_t_ (struct_net_match_property_t_)
    matchType: struct_net_match_property_t_ (struct_net_match_property_t_)
    fieldDF0: struct_net_match_property_t_ (struct_net_match_property_t_)
    elo: struct_net_match_property_t_ (struct_net_match_property_t_)
    numPlayersMatch: int (POINTER(B))
    nFriendsInMatchmaker: int (POINTER(B))
    fieldE22: int (POINTER(B))
    fieldE23: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    control: list[int]
    fieldDB4: int
    fieldDB5: int
    gapDB6: list[int]
    fieldDB8: int
    state: int
    region: struct_net_match_property_t_
    matchType: struct_net_match_property_t_
    fieldDF0: struct_net_match_property_t_
    elo: struct_net_match_property_t_
    numPlayersMatch: int
    nFriendsInMatchmaker: int
    fieldE22: int
    fieldE23: int

class struct_net_state_t_(Structure):
    """
    ```python
    heap: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    heapMem: c_void_p (c_void_p)
    stateMachine: int (POINTER(I))
    raceRecvBuffers: list[int] (POINTER(B)[128][4])
    profileDatagramBuffers: list[struct_net_menu_profile_dgram_t_] (struct_net_menu_profile_dgram_t_[4])
    fieldB2C: struct_net_state_field_B2C_t_ (struct_net_state_field_B2C_t_)
    matchStatus: struct_net_match_status_t_ (struct_net_match_status_t_)
    userData: c_void_p (c_void_p)
    friends: list[c_void_p] (c_void_p[60])
    friendStatuses: list[int] (POINTER(B)[60])
    friendListChanged: int (POINTER(i))
    menuRecvBuffers: list[struct_net_menu_dgram_t_] (struct_net_menu_dgram_t_[4])
    menuSendBuffers: list[struct_net_menu_dgram_t_] (struct_net_menu_dgram_t_[4])
    field1F20: struct_net_field_12F0_t_ (struct_net_field_12F0_t_)
    heapInitialized: int (POINTER(i))
    field1F34: int (POINTER(i))
    field1F38: int (POINTER(i))
    frameCount: int (POINTER(I))
    field1F40: int (POINTER(i))
    lastError: int (POINTER(i))
    field1F48: int (POINTER(i))
    field1F4C: int (POINTER(B))
    field1F4D: int (POINTER(B))
    field1F4E: list[int] (POINTER(B)[4])
    numConnections: int (POINTER(B))
    aidMax: int (POINTER(B))
    field1F54: int (POINTER(B))
    connectedAids: int (POINTER(B))
    newlyDisconnectedAidsBitmap: int (POINTER(B))
    lastFriendStatusFetched: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    heap: POINTER_T[struct_NNSiFndHeapHead]
    heapMem: c_void_p
    stateMachine: int
    raceRecvBuffers: list[int]
    profileDatagramBuffers: list[struct_net_menu_profile_dgram_t_]
    fieldB2C: struct_net_state_field_B2C_t_
    matchStatus: struct_net_match_status_t_
    userData: c_void_p
    friends: list[c_void_p]
    friendStatuses: list[int]
    friendListChanged: int
    menuRecvBuffers: list[struct_net_menu_dgram_t_]
    menuSendBuffers: list[struct_net_menu_dgram_t_]
    field1F20: struct_net_field_12F0_t_
    heapInitialized: int
    field1F34: int
    field1F38: int
    frameCount: int
    field1F40: int
    lastError: int
    field1F48: int
    field1F4C: int
    field1F4D: int
    field1F4E: list[int]
    numConnections: int
    aidMax: int
    field1F54: int
    connectedAids: int
    newlyDisconnectedAidsBitmap: int
    lastFriendStatusFetched: int
    PADDING_0: list[int]

class struct_nkdg_t(Structure):
    """
    ```python
    header: struct_ghost_header_t (struct_ghost_header_t)
    emblem: list[int] (POINTER(B)[512])
    inputData: struct_input_rec_recording_t (struct_input_rec_recording_t)
    padding: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_ghost_header_t
    emblem: list[int]
    inputData: struct_input_rec_recording_t
    padding: int

class struct_nkm_area_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    length: struct_VecFx32 (struct_VecFx32)
    xVector: struct_VecFx32 (struct_VecFx32)
    yVector: struct_VecFx32 (struct_VecFx32)
    zVector: struct_VecFx32 (struct_VecFx32)
    param0: int (POINTER(h))
    param1: int (POINTER(h))
    enemyPointId: int (POINTER(h))
    shape: int (POINTER(B))
    cameraId: int (POINTER(B))
    type: int (POINTER(B))
    field45: int (POINTER(B))
    field46: int (POINTER(B))
    field47: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    length: struct_VecFx32
    xVector: struct_VecFx32
    yVector: struct_VecFx32
    zVector: struct_VecFx32
    param0: int
    param1: int
    enemyPointId: int
    shape: int
    cameraId: int
    type: int
    field45: int
    field46: int
    field47: int

class struct_nkm_area_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_area_entry_t] (struct_nkm_area_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_area_entry_t]

class struct_nkm_came_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    target1: struct_VecFx32 (struct_VecFx32)
    target2: struct_VecFx32 (struct_VecFx32)
    fovBegin: int (POINTER(H))
    fovBeginSin: fx16 (struct_fx16)
    fovBeginCos: fx16 (struct_fx16)
    fovEnd: int (POINTER(H))
    fovEndSin: fx16 (struct_fx16)
    fovEndCos: fx16 (struct_fx16)
    fovSpeed: int (POINTER(h))
    type: int (POINTER(H))
    pathId: int (POINTER(h))
    routeSpeed: int (POINTER(h))
    targetSpeed: int (POINTER(H))
    duration: int (POINTER(H))
    next: int (POINTER(h))
    introFirst: int (POINTER(B))
    unknown: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    target1: struct_VecFx32
    target2: struct_VecFx32
    fovBegin: int
    fovBeginSin: fx16
    fovBeginCos: fx16
    fovEnd: int
    fovEndSin: fx16
    fovEndCos: fx16
    fovSpeed: int
    type: int
    pathId: int
    routeSpeed: int
    targetSpeed: int
    duration: int
    next: int
    introFirst: int
    unknown: int

class struct_nkm_came_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_came_entry_t] (struct_nkm_came_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_came_entry_t]

class struct_nkm_cpat_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[3])
    previous: list[int] (POINTER(B)[3])
    sectionOrder: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]
    sectionOrder: int
    PADDING_0: int

class struct_nkm_cpat_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_cpat_entry_t] (struct_nkm_cpat_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_cpat_entry_t]

class struct_nkm_cpoi_entry_t(Structure):
    """
    ```python
    x1: fx32 (struct_fx32)
    z1: fx32 (struct_fx32)
    x2: fx32 (struct_fx32)
    z2: fx32 (struct_fx32)
    sin: fx32 (struct_fx32)
    cos: fx32 (struct_fx32)
    distance: fx32 (struct_fx32)
    gotoSection: int (POINTER(h))
    startSection: int (POINTER(h))
    keyId: int (POINTER(h))
    respawnId: int (POINTER(B))
    flags: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    x1: fx32
    z1: fx32
    x2: fx32
    z2: fx32
    sin: fx32
    cos: fx32
    distance: fx32
    gotoSection: int
    startSection: int
    keyId: int
    respawnId: int
    flags: int

class struct_nkm_cpoi_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_cpoi_entry_t] (struct_nkm_cpoi_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_cpoi_entry_t]

class struct_nkm_epat_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[3])
    previous: list[int] (POINTER(B)[3])
    sectionOrder: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]
    sectionOrder: int

class struct_nkm_epat_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_epat_entry_t] (struct_nkm_epat_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_epat_entry_t]

class struct_nkm_epoi_entry_settings_t(Structure):
    """
    ```python
    drifting: int (POINTER(H))
    unknown1: int (POINTER(H))
    unknown2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    drifting: int
    unknown1: int
    unknown2: int

class struct_nkm_epoi_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    settings: struct_nkm_epoi_entry_settings_t (struct_nkm_epoi_entry_settings_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32
    settings: struct_nkm_epoi_entry_settings_t

class struct_nkm_epoi_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_epoi_entry_t] (struct_nkm_epoi_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_epoi_entry_t]

class struct_nkm_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    version: int (POINTER(H))
    headerLength: int (POINTER(H))
    offsets: list[int] (POINTER(I)[17])
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    version: int
    headerLength: int
    offsets: list[int]

class struct_nkm_ipat_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[3])
    previous: list[int] (POINTER(B)[3])
    sectionOrder: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]
    sectionOrder: int

class struct_nkm_ipat_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ipat_entry_t] (struct_nkm_ipat_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ipat_entry_t]

class struct_nkm_ipoi_entry_beta_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32

class struct_nkm_ipoi_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    recalcIdx: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32
    recalcIdx: int
    PADDING_0: list[int]

class struct_nkm_ipoi_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ipoi_entry_t] (struct_nkm_ipoi_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ipoi_entry_t]

class struct_nkm_ktp2_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    padding: int (POINTER(H))
    id: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    padding: int
    id: int

class struct_nkm_ktp2_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktp2_entry_t] (struct_nkm_ktp2_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktp2_entry_t]

class struct_nkm_ktpc_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    nextMepo: int (POINTER(h))
    id: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    nextMepo: int
    id: int

class struct_nkm_ktpc_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktpc_entry_t] (struct_nkm_ktpc_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktpc_entry_t]

class struct_nkm_ktpj_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    enemyPointId: int (POINTER(H))
    itemPointId: int (POINTER(H))
    id: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    enemyPointId: int
    itemPointId: int
    id: int
    PADDING_0: list[int]

class struct_nkm_ktpj_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktpj_entry_t] (struct_nkm_ktpj_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktpj_entry_t]

class struct_nkm_ktpm_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    padding: int (POINTER(H))
    id: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    padding: int
    id: int

class struct_nkm_ktpm_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktpm_entry_t] (struct_nkm_ktpm_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktpm_entry_t]

class struct_nkm_ktps_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    padding: int (POINTER(H))
    index: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    padding: int
    index: int

class struct_nkm_ktps_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_ktps_entry_t] (struct_nkm_ktps_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_ktps_entry_t]

class struct_nkm_mepa_entry_t(Structure):
    """
    ```python
    start: int (POINTER(H))
    length: int (POINTER(H))
    next: list[int] (POINTER(B)[8])
    previous: list[int] (POINTER(B)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    start: int
    length: int
    next: list[int]
    previous: list[int]

class struct_nkm_mepa_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_mepa_entry_t] (struct_nkm_mepa_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_mepa_entry_t]

class struct_nkm_mepo_entry_settings_t(Structure):
    """
    ```python
    drifting: int (POINTER(I))
    unknown1: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    drifting: int
    unknown1: int

class struct_nkm_mepo_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    radius: fx32 (struct_fx32)
    settings: struct_nkm_mepo_entry_settings_t (struct_nkm_mepo_entry_settings_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    radius: fx32
    settings: struct_nkm_mepo_entry_settings_t

class struct_nkm_mepo_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_mepo_entry_t] (struct_nkm_mepo_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_mepo_entry_t]

class struct_nkm_obji_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    rotation: struct_VecFx32 (struct_VecFx32)
    scale: struct_VecFx32 (struct_VecFx32)
    objectId: int (POINTER(H))
    pathId: int (POINTER(h))
    settings: list[int] (POINTER(h)[7])
    flags: int (POINTER(h))
    showsInTT: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    rotation: struct_VecFx32
    scale: struct_VecFx32
    objectId: int
    pathId: int
    settings: list[int]
    flags: int
    showsInTT: int
    PADDING_0: list[int]

class struct_nkm_obji_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_obji_entry_t] (struct_nkm_obji_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_obji_entry_t]

class struct_nkm_path_entry_t(Structure):
    """
    ```python
    id: int (POINTER(B))
    loop: int (POINTER(B))
    pointCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    loop: int
    pointCount: int

class struct_nkm_path_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_path_entry_t] (struct_nkm_path_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_path_entry_t]

class struct_nkm_poit_entry_t(Structure):
    """
    ```python
    position: struct_VecFx32 (struct_VecFx32)
    pointIndex: int (POINTER(B))
    unknown1: int (POINTER(B))
    duration: int (POINTER(h))
    _0: union_nkm_poit_entry_t_0 (union_nkm_poit_entry_t_0)
    ```
    """
    _pack_: ClassVar[int] = 1
    position: struct_VecFx32
    pointIndex: int
    unknown1: int
    duration: int
    _0: union_nkm_poit_entry_t_0

class struct_nkm_poit_entry_t_0_0(Structure):
    """
    ```python
    unknown2_s16: int (POINTER(h))
    unknown2_s16_hi: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    unknown2_s16: int
    unknown2_s16_hi: int

class struct_nkm_poit_t(Structure):
    """
    ```python
    header: struct_nkm_section_header_t (struct_nkm_section_header_t)
    entries: list[struct_nkm_poit_entry_t] (struct_nkm_poit_entry_t[0])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_section_header_t
    entries: list[struct_nkm_poit_entry_t]

class struct_nkm_section_header_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    count: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    count: int

class struct_nkm_stag_data_t(Structure):
    """
    ```python
    courseId: int (POINTER(H))
    nrLaps: int (POINTER(H))
    polePosition: int (POINTER(B))
    fogEnabled: int (POINTER(B))
    fogTableGenMode: int (POINTER(B))
    fogSlope: int (POINTER(B))
    unknown2: list[int] (POINTER(B)[8])
    fogDensity: fx32 (struct_fx32)
    fogColor: int (POINTER(I))
    kclColors: list[int] (POINTER(H)[4])
    mobjFarClip: fx32 (struct_fx32)
    frustumFar: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    courseId: int
    nrLaps: int
    polePosition: int
    fogEnabled: int
    fogTableGenMode: int
    fogSlope: int
    unknown2: list[int]
    fogDensity: fx32
    fogColor: int
    kclColors: list[int]
    mobjFarClip: fx32
    frustumFar: fx32

class struct_nkm_stag_t(Structure):
    """
    ```python
    magic: int (POINTER(I))
    data: struct_nkm_stag_data_t (struct_nkm_stag_data_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    magic: int
    data: struct_nkm_stag_data_t

class struct_nkm_t(Structure):
    """
    ```python
    header: struct_nkm_header_t (struct_nkm_header_t)
    obji: struct_nkm_obji_t (struct_nkm_obji_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_nkm_header_t
    obji: struct_nkm_obji_t

class struct_nkpg_t(Structure):
    """
    ```python
    header: struct_ghost_header_t (struct_ghost_header_t)
    inputData: list[int] (POINTER(B)[3532])
    ```
    """
    _pack_: ClassVar[int] = 1
    header: struct_ghost_header_t
    inputData: list[int]

class struct_nksy_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    gap4: list[int] (POINTER(B)[8])
    nickname: list[int] (POINTER(H)[10])
    unlockBits: list[int] (POINTER(B)[4])
    field24: int (POINTER(H))
    personalGhostBits: list[int] (POINTER(B)[4])
    downloadGhostBits: list[int] (POINTER(B)[4])
    nkfeBits: list[int] (POINTER(B)[2])
    gap30: int (POINTER(B))
    field31: int (POINTER(B))
    gap32: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    field34: int (POINTER(I))
    field38: int (POINTER(I))
    field3C: int (POINTER(I))
    field40: int (POINTER(I))
    field44: int (POINTER(I))
    field48: int (POINTER(I))
    dwcUserData: c_void_p (c_void_p)
    gap8C: list[int] (POINTER(B)[116])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    gap4: list[int]
    nickname: list[int]
    unlockBits: list[int]
    field24: int
    personalGhostBits: list[int]
    downloadGhostBits: list[int]
    nkfeBits: list[int]
    gap30: int
    field31: int
    gap32: int
    PADDING_0: int
    field34: int
    field38: int
    field3C: int
    field40: int
    field44: int
    field48: int
    dwcUserData: c_void_p
    gap8C: list[int]

class struct_nsk1_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    counter: int (POINTER(i))
    unkA4: list[int] (POINTER(B)[4])
    state: int (POINTER(I))
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    counter: int
    unkA4: list[int]
    state: int
    pathwalker: struct_pw_pathwalker_t

class struct_nsk2_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    counter: int (POINTER(i))
    state: int (POINTER(I))
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t] (POINTER(struct_sfx_emitter_ex_params_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    counter: int
    state: int
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t]

class struct_oam_buf_t(Structure):
    """
    ```python
    oam: list[struct_GXOamAttr] (struct_GXOamAttr[128])
    objCount: int (POINTER(H))
    affineCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    oam: list[struct_GXOamAttr]
    objCount: int
    affineCount: int

class struct_oam_buffers_t(Structure):
    """
    ```python
    mainOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    subOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mainOamBuf: struct_oam_buf_t
    subOamBuf: struct_oam_buf_t

class struct_objshadow_t(Structure):
    """
    ```python
    mtx: union_MtxFx43 (union_MtxFx43)
    alpha: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    mtx: union_MtxFx43
    alpha: int
    PADDING_0: list[int]

class struct_obpakkunsf_t(Structure):
    """
    ```python
    rotDieMObj: struct_rotdiemobj_t (struct_rotdiemobj_t)
    counter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    rotDieMObj: struct_rotdiemobj_t
    counter: int
    PADDING_0: list[int]

class struct_overlay_data_overlayinfo_t(Structure):
    """
    ```python
    id: int (POINTER(I))
    start: int (POINTER(I))
    end: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    id: int
    start: int
    end: int

class struct_overlay_data_t(Structure):
    """
    ```python
    curOverlay: int (POINTER(I))
    state: int (POINTER(I))
    overlays: list[struct_overlay_data_overlayinfo_t] (struct_overlay_data_overlayinfo_t[3])
    overlayInfo: struct_FSOverlayInfo (struct_FSOverlayInfo)
    overlayFile: struct_FSFile (struct_FSFile)
    overlayFrmHeap: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    overlayExpHeap: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    overlayRegionStart: int (POINTER(I))
    overlayRegionEnd: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    curOverlay: int
    state: int
    overlays: list[struct_overlay_data_overlayinfo_t]
    overlayInfo: struct_FSOverlayInfo
    overlayFile: struct_FSFile
    overlayFrmHeap: POINTER_T[struct_NNSiFndHeapHead]
    overlayExpHeap: POINTER_T[struct_NNSiFndHeapHead]
    overlayRegionStart: int
    overlayRegionEnd: int

class struct_pakkun_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    polygonId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    nsbcaFrame: int (POINTER(i))
    fieldA8: int (POINTER(i))
    fieldAC: int (POINTER(i))
    fieldB0: int (POINTER(i))
    state: int (POINTER(I))
    pathwalkers: list[struct_pw_pathwalker_t] (struct_pw_pathwalker_t[7])
    counter: int (POINTER(i))
    curPath: int (POINTER(H))
    pathCount: int (POINTER(H))
    field1BC: list[int] (POINTER(i)[7])
    field1D8: int (POINTER(i))
    mouthRotY: int (POINTER(i))
    mouthRotX: int (POINTER(i))
    field1E4: int (POINTER(i))
    field1E8: int (POINTER(i))
    field1EC: int (POINTER(i))
    scale: int (POINTER(i))
    scaleVelocity: int (POINTER(i))
    headElevation: int (POINTER(i))
    fireballElevation: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    polygonId: int
    PADDING_0: list[int]
    nsbcaFrame: int
    fieldA8: int
    fieldAC: int
    fieldB0: int
    state: int
    pathwalkers: list[struct_pw_pathwalker_t]
    counter: int
    curPath: int
    pathCount: int
    field1BC: list[int]
    field1D8: int
    mouthRotY: int
    mouthRotX: int
    field1E4: int
    field1E8: int
    field1EC: int
    scale: int
    scaleVelocity: int
    headElevation: int
    fireballElevation: int

class struct_pakkunfire_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    elevation: fx32 (struct_fx32)
    elevationVelocity: fx32 (struct_fx32)
    state: int (POINTER(I))
    emitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    pathwalker: struct_pw_pathwalker_t
    elevation: fx32
    elevationVelocity: fx32
    state: int
    emitter: POINTER_T[struct_spa_emitter_t]

class struct_pendulum_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    rotation: quaternion_t (struct_quaternion_t)
    prevPosition: struct_VecFx32 (struct_VecFx32)
    renderPos: struct_VecFx32 (struct_VecFx32)
    shadowMtx: union_MtxFx43 (union_MtxFx43)
    offsetY: fx32 (struct_fx32)
    swingRange: int (POINTER(H))
    swingVelocity: int (POINTER(H))
    angle: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    size: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    rotation: quaternion_t
    prevPosition: struct_VecFx32
    renderPos: struct_VecFx32
    shadowMtx: union_MtxFx43
    offsetY: fx32
    swingRange: int
    swingVelocity: int
    angle: int
    PADDING_0: list[int]
    size: struct_VecFx32

class struct_physp_char_params_t(Structure):
    """
    ```python
    field0: fx32 (struct_fx32)
    weight: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: fx32
    weight: fx32

class struct_physp_kart_params_t(Structure):
    """
    ```python
    colSphereSize: fx32 (struct_fx32)
    colSphereZOffset: fx32 (struct_fx32)
    gap8: list[int] (POINTER(B)[4])
    weight: fx16 (struct_fx16)
    driftBoostTime: int (POINTER(h))
    maxSpeed: fx32 (struct_fx32)
    baseAcceleration: fx32 (struct_fx32)
    field18: fx32 (struct_fx32)
    field1C: fx32 (struct_fx32)
    driftBaseAcceleration: fx32 (struct_fx32)
    field24: fx32 (struct_fx32)
    field28: fx32 (struct_fx32)
    deceleration: fx32 (struct_fx32)
    handling: fx16 (struct_fx16)
    drift: fx16 (struct_fx16)
    driftTurningCompensation: fx32 (struct_fx32)
    collisionVelocityMinusDirMultipliers: list[fx32] (struct_fx32[12])
    collisionSpeedMultipliers: list[fx32] (struct_fx32[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    colSphereSize: fx32
    colSphereZOffset: fx32
    gap8: list[int]
    weight: fx16
    driftBoostTime: int
    maxSpeed: fx32
    baseAcceleration: fx32
    field18: fx32
    field1C: fx32
    driftBaseAcceleration: fx32
    field24: fx32
    field28: fx32
    deceleration: fx32
    handling: fx16
    drift: fx16
    driftTurningCompensation: fx32
    collisionVelocityMinusDirMultipliers: list[fx32]
    collisionSpeedMultipliers: list[fx32]

class struct_physp_t(Structure):
    """
    ```python
    driverKartPhysicalParams: POINTER_T[struct_physp_kart_params_t] (POINTER(struct_physp_kart_params_t))
    driverCharPhysicalParams: POINTER_T[struct_physp_char_params_t] (POINTER(struct_physp_char_params_t))
    field8: int (POINTER(I))
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t] (POINTER(struct_physp_kart_params_t))
    charPhysicalParams: POINTER_T[struct_physp_char_params_t] (POINTER(struct_physp_char_params_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    driverKartPhysicalParams: POINTER_T[struct_physp_kart_params_t]
    driverCharPhysicalParams: POINTER_T[struct_physp_char_params_t]
    field8: int
    kartPhysicalParams: POINTER_T[struct_physp_kart_params_t]
    charPhysicalParams: POINTER_T[struct_physp_char_params_t]

class struct_picture_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbcaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    pictureType: int (POINTER(I))
    counter: int (POINTER(i))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbcaFrame: int
    PADDING_0: list[int]
    pictureType: int
    counter: int
    state: int

class struct_pole_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class struct_process_t(Structure):
    """
    ```python
    name: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    mainFunc: Callable[[c_void_p], c_int] (CFunctionType)
    exitFunc: Callable[[int], None] (CFunctionType)
    heapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    prevProcess: POINTER_T[struct_process_t] (POINTER(struct_process_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    name: POINTER_T[c_ubyte]
    mainFunc: Callable[[c_void_p], c_int]
    exitFunc: Callable[[int], None]
    heapHandle: POINTER_T[struct_NNSiFndHeapHead]
    prevProcess: POINTER_T[struct_process_t]

class struct_ptcm_camflashes_t(Structure):
    """
    ```python
    directions: list[struct_VecFx32] (struct_VecFx32[6])
    emitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[6])
    waitCounter: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    directions: list[struct_VecFx32]
    emitters: list[POINTER_T[struct_spa_emitter_t]]
    waitCounter: int
    PADDING_0: list[int]

class struct_puddle_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class struct_pukupuku_t(Structure):
    """
    ```python
    rdmobj: struct_rotdiemobj_t (struct_rotdiemobj_t)
    fieldB8: struct_VecFx32 (struct_VecFx32)
    fieldC4: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    shadow: struct_objshadow_t (struct_objshadow_t)
    fieldFC: int (POINTER(I))
    field100: fx32 (struct_fx32)
    field104: fx32 (struct_fx32)
    field108: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    rdmobj: struct_rotdiemobj_t
    fieldB8: struct_VecFx32
    fieldC4: int
    PADDING_0: list[int]
    shadow: struct_objshadow_t
    fieldFC: int
    field100: fx32
    field104: fx32
    field108: fx32

class struct_pw_path_part_t(Structure):
    """
    ```python
    p0: struct_VecFx32 (struct_VecFx32)
    p1: struct_VecFx32 (struct_VecFx32)
    p2: struct_VecFx32 (struct_VecFx32)
    p3: struct_VecFx32 (struct_VecFx32)
    length: fx32 (struct_fx32)
    oneDivLength: int (POINTER(i))
    hermLength: fx32 (struct_fx32)
    oneDivHermLength: int (POINTER(i))
    linLength: fx32 (struct_fx32)
    oneDivLinLength: int (POINTER(i))
    field48: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    p0: struct_VecFx32
    p1: struct_VecFx32
    p2: struct_VecFx32
    p3: struct_VecFx32
    length: fx32
    oneDivLength: int
    hermLength: fx32
    oneDivHermLength: int
    linLength: fx32
    oneDivLinLength: int
    field48: struct_VecFx32

class struct_pw_path_t(Structure):
    """
    ```python
    parts: POINTER_T[struct_pw_path_part_t] (POINTER(struct_pw_path_part_t))
    partCount: int (POINTER(I))
    loop: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    parts: POINTER_T[struct_pw_path_part_t]
    partCount: int
    loop: int

class struct_pw_pathwalker_t(Structure):
    """
    ```python
    path: POINTER_T[struct_pw_path_t] (POINTER(struct_pw_path_t))
    speed: fx32 (struct_fx32)
    pathId: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    partIdx: int (POINTER(I))
    partSpeed: int (POINTER(i))
    partProgress: int (POINTER(i))
    isForwards: int (POINTER(i))
    prevPoit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    curPoit: POINTER_T[struct_nkm_poit_entry_t] (POINTER(struct_nkm_poit_entry_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    path: POINTER_T[struct_pw_path_t]
    speed: fx32
    pathId: int
    PADDING_0: list[int]
    partIdx: int
    partSpeed: int
    partProgress: int
    isForwards: int
    prevPoit: POINTER_T[struct_nkm_poit_entry_t]
    curPoit: POINTER_T[struct_nkm_poit_entry_t]

class struct_pw_simple_pathwalker_t(Structure):
    """
    ```python
    pathPart: struct_pw_path_part_t (struct_pw_path_part_t)
    speed: fx32 (struct_fx32)
    partSpeed: int (POINTER(i))
    progress: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    pathPart: struct_pw_path_part_t
    speed: fx32
    partSpeed: int
    progress: int

class struct_quaternion_t(Structure):
    """
    ```python
    x: fx32 (struct_fx32)
    y: fx32 (struct_fx32)
    z: fx32 (struct_fx32)
    w: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx32
    y: fx32
    z: fx32
    w: fx32

class struct_r2d_race_mode_top_hud_state_t(Structure):
    """
    ```python
    _0: union_r2d_race_mode_top_hud_state_t_0 (union_r2d_race_mode_top_hud_state_t_0)
    mrTargetValue: int (POINTER(i))
    ghostAvailable: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: union_r2d_race_mode_top_hud_state_t_0
    mrTargetValue: int
    ghostAvailable: int

class struct_r2d_race_mode_top_hud_state_t_0_0(Structure):
    """
    ```python
    mgBalloonInflateFrame: int (POINTER(H))
    mgInventoryBalloonCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    mgBalloonInflateFrame: int
    mgInventoryBalloonCount: int

class struct_r2d_race_mode_top_hud_state_t_0_1(Structure):
    """
    ```python
    mgShineCount: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    mgShineCount: int

class struct_race_config_driver_t(Structure):
    """
    ```python
    character: int (POINTER(I))
    kart: int (POINTER(I))
    type: int (POINTER(I))
    team: int (POINTER(i))
    field10: int (POINTER(I))
    driverIndex: int (POINTER(I))
    ghostType: int (POINTER(I))
    field1C: int (POINTER(H))
    field1E: int (POINTER(b))
    field1F: int (POINTER(B))
    nickname: POINTER_T[c_ushort] (POINTER(POINTER(H)))
    emblemTex: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    field28: int (POINTER(I))
    useCustomEmblem: int (POINTER(B))
    field2D: int (POINTER(B))
    field2E: int (POINTER(B))
    field2F: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    character: int
    kart: int
    type: int
    team: int
    field10: int
    driverIndex: int
    ghostType: int
    field1C: int
    field1E: int
    field1F: int
    nickname: POINTER_T[c_ushort]
    emblemTex: POINTER_T[c_ubyte]
    field28: int
    useCustomEmblem: int
    field2D: int
    field2E: int
    field2F: int

class struct_race_config_t(Structure):
    """
    ```python
    course: int (POINTER(I))
    cup: int (POINTER(I))
    raceMode: int (POINTER(I))
    displayMode: int (POINTER(I))
    ccMode: int (POINTER(I))
    cpuMode: int (POINTER(I))
    mgMode: int (POINTER(I))
    rules: int (POINTER(I))
    courseMode: int (POINTER(I))
    taGhost: int (POINTER(I))
    mrConfig: struct_mission_config_t (struct_mission_config_t)
    mrLevel: int (POINTER(b))
    mrIndex: int (POINTER(b))
    field56: int (POINTER(B))
    isMirror: int (POINTER(b))
    teams: int (POINTER(b))
    field59: int (POINTER(B))
    field5A: int (POINTER(B))
    field5B: int (POINTER(B))
    rngSeed: int (POINTER(I))
    raceNr: int (POINTER(H))
    playerDriverId: int (POINTER(b))
    cpuDriverId: int (POINTER(B))
    lapCountOverride: int (POINTER(b))
    field65: int (POINTER(B))
    gap66: list[int] (POINTER(B)[2])
    drivers: list[struct_race_config_driver_t] (struct_race_config_driver_t[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    course: int
    cup: int
    raceMode: int
    displayMode: int
    ccMode: int
    cpuMode: int
    mgMode: int
    rules: int
    courseMode: int
    taGhost: int
    mrConfig: struct_mission_config_t
    mrLevel: int
    mrIndex: int
    field56: int
    isMirror: int
    teams: int
    field59: int
    field5A: int
    field5B: int
    rngSeed: int
    raceNr: int
    playerDriverId: int
    cpuDriverId: int
    lapCountOverride: int
    field65: int
    gap66: list[int]
    drivers: list[struct_race_config_driver_t]

class struct_race_driver_result_t(Structure):
    """
    ```python
    totalRankPoints: int (POINTER(H))
    globalPlace: int (POINTER(B))
    place: int (POINTER(B))
    rankPoints: int (POINTER(B))
    winCount: int (POINTER(B))
    raceTime: struct_race_time_t (struct_race_time_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    totalRankPoints: int
    globalPlace: int
    place: int
    rankPoints: int
    winCount: int
    raceTime: struct_race_time_t

class struct_race_driver_status_t(Structure):
    """
    ```python
    state: int (POINTER(I))
    lapFrameCounter: int (POINTER(I))
    field8: int (POINTER(I))
    lapTimes: list[struct_race_time_t] (struct_race_time_t[5])
    totalTime: struct_race_time_t (struct_race_time_t)
    curLap: int (POINTER(i))
    firstPlaceTime: int (POINTER(I))
    totalMilliseconds: int (POINTER(I))
    flags: int (POINTER(H))
    curCpoi: int (POINTER(H))
    lastCorrectKeyPoint: int (POINTER(h))
    curKeyPoint: int (POINTER(h))
    curCpat: int (POINTER(H))
    highestReachedLap: int (POINTER(H))
    place: int (POINTER(H))
    driverId: int (POINTER(H))
    field3CBit89: int (POINTER(H))
    PADDING_0: int (POINTER(B))
    skillRankPoints: int (POINTER(h))
    cpoiProgress: fx32 (struct_fx32)
    raceProgress: fx32 (struct_fx32)
    lapProgress: fx32 (struct_fx32)
    cpoiMask: list[int] (POINTER(I)[16])
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    lapFrameCounter: int
    field8: int
    lapTimes: list[struct_race_time_t]
    totalTime: struct_race_time_t
    curLap: int
    firstPlaceTime: int
    totalMilliseconds: int
    flags: int
    curCpoi: int
    lastCorrectKeyPoint: int
    curKeyPoint: int
    curCpat: int
    highestReachedLap: int
    place: int
    driverId: int
    field3CBit89: int
    PADDING_0: int
    skillRankPoints: int
    cpoiProgress: fx32
    raceProgress: fx32
    lapProgress: fx32
    cpoiMask: list[int]

class struct_race_multi_config_t(Structure):
    """
    ```python
    current: struct_race_config_t (struct_race_config_t)
    next: struct_race_config_t (struct_race_config_t)
    driverCount: int (POINTER(B))
    field3D1: int (POINTER(B))
    teamDriverCount: list[int] (POINTER(B)[2])
    field3D4: int (POINTER(B))
    field3D5: list[int] (POINTER(b)[2])
    field3D7: int (POINTER(B))
    nrRacesNrWins: int (POINTER(H))
    gap3DA: list[int] (POINTER(B)[2])
    courseQueue: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    courseQueueIdx: int (POINTER(B))
    field3E1: int (POINTER(B))
    personalGhostTime: struct_race_time_t (struct_race_time_t)
    personalGhostAvailable: int (POINTER(B))
    gap3E7: int (POINTER(B))
    ghostTime: struct_race_time_t (struct_race_time_t)
    ghostLapTimes: list[struct_race_time_t] (struct_race_time_t[5])
    ```
    """
    _pack_: ClassVar[int] = 1
    current: struct_race_config_t
    next: struct_race_config_t
    driverCount: int
    field3D1: int
    teamDriverCount: list[int]
    field3D4: int
    field3D5: list[int]
    field3D7: int
    nrRacesNrWins: int
    gap3DA: list[int]
    courseQueue: POINTER_T[c_ubyte]
    courseQueueIdx: int
    field3E1: int
    personalGhostTime: struct_race_time_t
    personalGhostAvailable: int
    gap3E7: int
    ghostTime: struct_race_time_t
    ghostLapTimes: list[struct_race_time_t]

class struct_race_results_t(Structure):
    """
    ```python
    driverResults: list[struct_race_driver_result_t] (struct_race_driver_result_t[8][4])
    totalSkillRankPoints: int (POINTER(I))
    teamResults: list[struct_race_team_result_t] (struct_race_team_result_t[2][4])
    field164: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    driverResults: list[struct_race_driver_result_t]
    totalSkillRankPoints: int
    teamResults: list[struct_race_team_result_t]
    field164: int

class struct_race_skill_rankpoints_t(Structure):
    """
    ```python
    rankTimeDeltaPoints: int (POINTER(i))
    firstPlacePercentagePoints: int (POINTER(i))
    startBoostPoints: int (POINTER(i))
    powerSlidePoints: int (POINTER(i))
    itemHitPoints: int (POINTER(i))
    offRoadTimePoints: int (POINTER(i))
    wallHitPoints: int (POINTER(i))
    damagePoints: int (POINTER(i))
    respawnPoints: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    rankTimeDeltaPoints: int
    firstPlacePercentagePoints: int
    startBoostPoints: int
    powerSlidePoints: int
    itemHitPoints: int
    offRoadTimePoints: int
    wallHitPoints: int
    damagePoints: int
    respawnPoints: int

class struct_race_state_t(Structure):
    """
    ```python
    state: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    frameCounter: int (POINTER(I))
    frameCounter2: int (POINTER(i))
    frameCounterModulo8: int (POINTER(i))
    isOddFrame: int (POINTER(i))
    frameCounterModuloDriverCount: int (POINTER(i))
    toonTableOffset: int (POINTER(I))
    toonTableUpdateCounter: int (POINTER(I))
    darkeningFogState: int (POINTER(I))
    prevDarkeningFogState: int (POINTER(I))
    isCamAnimMode: int (POINTER(i))
    isCamAnimSingleScreen: int (POINTER(i))
    field30: int (POINTER(I))
    field34: int (POINTER(I))
    isAwardStaffRoll: int (POINTER(i))
    field3C: int (POINTER(I))
    light0Dir: struct_VecFx16 (struct_VecFx16)
    PADDING_1: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    state: int
    PADDING_0: list[int]
    frameCounter: int
    frameCounter2: int
    frameCounterModulo8: int
    isOddFrame: int
    frameCounterModuloDriverCount: int
    toonTableOffset: int
    toonTableUpdateCounter: int
    darkeningFogState: int
    prevDarkeningFogState: int
    isCamAnimMode: int
    isCamAnimSingleScreen: int
    field30: int
    field34: int
    isAwardStaffRoll: int
    field3C: int
    light0Dir: struct_VecFx16
    PADDING_1: list[int]

class struct_race_status_t(Structure):
    """
    ```python
    time: struct_race_status_time_t (struct_race_status_time_t)
    rankTimeGp: int (POINTER(H))
    finishedDriverCount: int (POINTER(H))
    field10: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    driverStatus: list[struct_race_driver_status_t] (struct_race_driver_status_t[8])
    placeDriverIds: list[int] (POINTER(b)[8])
    PADDING_1: list[int] (POINTER(B)[4])
    safeRng: struct_MATHRandContext32 (struct_MATHRandContext32)
    rngSeed: int (POINTER(I))
    PADDING_2: list[int] (POINTER(B)[4])
    randomRng: struct_MATHRandContext32 (struct_MATHRandContext32)
    stableRng: struct_MATHRandContext32 (struct_MATHRandContext32)
    rankTimeGpRtt: POINTER_T[struct_ranktime_gp_t] (POINTER(struct_ranktime_gp_t))
    resultsStored: int (POINTER(i))
    camAnimComplete: int (POINTER(i))
    cpoiKeyPointProgress: POINTER_T[fx32] (POINTER(struct_fx32))
    gap4D8: list[int] (POINTER(B)[4])
    rankPointRpt: POINTER_T[struct_rankpoint_t] (POINTER(struct_rankpoint_t))
    missionResult: int (POINTER(I))
    oneDivCpatSegmentCount: fx32 (struct_fx32)
    oneDivNrLaps: fx32 (struct_fx32)
    useTimeLimit: int (POINTER(i))
    uncontrollable: int (POINTER(i))
    timeLimit: int (POINTER(I))
    field4F8: int (POINTER(B))
    field4F9: int (POINTER(B))
    mrWinDelayCounter: int (POINTER(H))
    mrLoseDelayCounter: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    skillRankPoints: struct_race_skill_rankpoints_t (struct_race_skill_rankpoints_t)
    PADDING_4: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    time: struct_race_status_time_t
    rankTimeGp: int
    finishedDriverCount: int
    field10: int
    PADDING_0: list[int]
    driverStatus: list[struct_race_driver_status_t]
    placeDriverIds: list[int]
    PADDING_1: list[int]
    safeRng: struct_MATHRandContext32
    rngSeed: int
    PADDING_2: list[int]
    randomRng: struct_MATHRandContext32
    stableRng: struct_MATHRandContext32
    rankTimeGpRtt: POINTER_T[struct_ranktime_gp_t]
    resultsStored: int
    camAnimComplete: int
    cpoiKeyPointProgress: POINTER_T[fx32]
    gap4D8: list[int]
    rankPointRpt: POINTER_T[struct_rankpoint_t]
    missionResult: int
    oneDivCpatSegmentCount: fx32
    oneDivNrLaps: fx32
    useTimeLimit: int
    uncontrollable: int
    timeLimit: int
    field4F8: int
    field4F9: int
    mrWinDelayCounter: int
    mrLoseDelayCounter: int
    PADDING_3: list[int]
    skillRankPoints: struct_race_skill_rankpoints_t
    PADDING_4: list[int]

class struct_race_status_time_t(Structure):
    """
    ```python
    frameCounter: int (POINTER(I))
    timeRunning: int (POINTER(i))
    lapTime: struct_race_time_t (struct_race_time_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    frameCounter: int
    timeRunning: int
    lapTime: struct_race_time_t

class struct_race_team_result_t(Structure):
    """
    ```python
    totalRankPoints: int (POINTER(H))
    winCount: int (POINTER(B))
    flags: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    totalRankPoints: int
    winCount: int
    flags: int

class struct_race_time_t(Structure):
    """
    ```python
    milliseconds: int (POINTER(H))
    minutes: int (POINTER(B))
    seconds: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    milliseconds: int
    minutes: int
    seconds: int

class struct_rainstar_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbtaFrame: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbtaFrame: int
    PADDING_0: list[int]

class struct_rankpoint_entry_t(Structure):
    """
    ```python
    points: list[int] (POINTER(B)[8])
    ```
    """
    _pack_: ClassVar[int] = 1
    points: list[int]

class struct_rankpoint_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    fileSize: int (POINTER(I))
    entries: list[struct_rankpoint_entry_t] (struct_rankpoint_entry_t[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    fileSize: int
    entries: list[struct_rankpoint_entry_t]

class struct_ranktime_gp_entry_t(Structure):
    """
    ```python
    courseId: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    rankTime50cc: int (POINTER(H))
    rankTime100cc: int (POINTER(H))
    rankTime150cc: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    courseId: int
    PADDING_0: int
    rankTime50cc: int
    rankTime100cc: int
    rankTime150cc: int

class struct_ranktime_gp_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    fileSize: int (POINTER(I))
    courseCount: int (POINTER(H))
    rankTimeDeltaFactor: int (POINTER(H))
    firstPlacePercentageFactor: int (POINTER(H))
    startBoostFactor: int (POINTER(H))
    powerSlideFactor: int (POINTER(H))
    itemHitFactor: int (POINTER(H))
    offRoadTimeFactor: int (POINTER(H))
    wallHitFactor: int (POINTER(H))
    damageFactor: int (POINTER(H))
    respawnFactor: int (POINTER(H))
    courseRankTimes: list[struct_ranktime_gp_entry_t] (struct_ranktime_gp_entry_t[1])
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    fileSize: int
    courseCount: int
    rankTimeDeltaFactor: int
    firstPlacePercentageFactor: int
    startBoostFactor: int
    powerSlideFactor: int
    itemHitFactor: int
    offRoadTimeFactor: int
    wallHitFactor: int
    damageFactor: int
    respawnFactor: int
    courseRankTimes: list[struct_ranktime_gp_entry_t]

class struct_result_t(Structure):
    """
    ```python
    mainOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    subOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    raceMode: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mainOamBuf: struct_oam_buf_t
    subOamBuf: struct_oam_buf_t
    raceMode: int

class struct_rnet_aid_map_t(Structure):
    """
    ```python
    driverToAid: list[int] (POINTER(b)[4])
    initialAids: int (POINTER(B))
    initialized: int (POINTER(B))
    aidToDriver: list[int] (POINTER(b)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    driverToAid: list[int]
    initialAids: int
    initialized: int
    aidToDriver: list[int]

class struct_rnet_dgram_t_(Structure):
    """
    ```python
    src: int (POINTER(B))
    dst: int (POINTER(B))
    op: int (POINTER(B))
    field1: int (POINTER(B))
    field2: int (POINTER(B))
    field3: int (POINTER(B))
    data: list[int] (POINTER(B)[104])
    ```
    """
    _pack_: ClassVar[int] = 1
    src: int
    dst: int
    op: int
    field1: int
    field2: int
    field3: int
    data: list[int]

class struct_rnet_driver_item_action_buffer_t_(Structure):
    """
    ```python
    itemActions: list[int] (POINTER(B)[16])
    itemEventData: list[int] (POINTER(B)[48])
    ```
    """
    _pack_: ClassVar[int] = 1
    itemActions: list[int]
    itemEventData: list[int]

class struct_rnet_driver_state_field20_t_(Structure):
    """
    ```python
    field1: int (POINTER(H))
    field2: int (POINTER(H))
    field3: int (POINTER(H))
    field4: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    field1: int
    field2: int
    field3: int
    field4: int

class struct_rnet_driver_state_t_(Structure):
    """
    ```python
    field0: int (POINTER(I))
    raceProgress: int (POINTER(I))
    state: struct_struc_351 (struct_struc_351)
    field20: list[struct_rnet_driver_state_field20_t_] (struct_rnet_driver_state_field20_t_[4])
    itemActionsBuffer: struct_rnet_driver_item_action_buffer_t_ (struct_rnet_driver_item_action_buffer_t_)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    raceProgress: int
    state: struct_struc_351
    field20: list[struct_rnet_driver_state_field20_t_]
    itemActionsBuffer: struct_rnet_driver_item_action_buffer_t_

class struct_rnet_item_action_entry_t_(Structure):
    """
    ```python
    field0: int (POINTER(I))
    buffer: c_void_p (c_void_p)
    filled: int (POINTER(B))
    item: int (POINTER(B))
    action: int (POINTER(B))
    size: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    buffer: c_void_p
    filled: int
    item: int
    action: int
    size: int

class struct_rnet_packet_sync_t_(Structure):
    """
    ```python
    srcAid: int (POINTER(H))
    gap2: list[int] (POINTER(B)[2])
    PADDING_0: list[int] (POINTER(B)[4])
    field4: int (POINTER(L))
    fieldC: int (POINTER(L))
    field14: int (POINTER(L))
    field1C: int (POINTER(I))
    field20: int (POINTER(I))
    field24: int (POINTER(I))
    PADDING_1: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    srcAid: int
    gap2: list[int]
    PADDING_0: list[int]
    field4: int
    fieldC: int
    field14: int
    field1C: int
    field20: int
    field24: int
    PADDING_1: list[int]

class struct_rnet_ping_t_(Structure):
    """
    ```python
    data: struct_rnet_packet_sync_t_ (struct_rnet_packet_sync_t_)
    field28: list[int] (POINTER(I)[2])
    field30: int (POINTER(I))
    field34: int (POINTER(B))
    field35: int (POINTER(B))
    field36: int (POINTER(B))
    field37: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    data: struct_rnet_packet_sync_t_
    field28: list[int]
    field30: int
    field34: int
    field35: int
    field36: int
    field37: int

class struct_rotcyl_params_t(Structure):
    """
    ```python
    isXZFloor: int (POINTER(i))
    sizeX: fx32 (struct_fx32)
    sizeY: fx32 (struct_fx32)
    type: int (POINTER(I))
    dcolFloorThreshold: int (POINTER(I))
    dcolField138: int (POINTER(I))
    sfxId: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    isXZFloor: int
    sizeX: fx32
    sizeY: fx32
    type: int
    dcolFloorThreshold: int
    dcolField138: int
    sfxId: int

class struct_rotcyl_t(Structure):
    """
    ```python
    dcol: struct_dcol_inst_t (struct_dcol_inst_t)
    startStopDuration: int (POINTER(H))
    rotateDuration: int (POINTER(H))
    idleDuration: int (POINTER(H))
    rotYVelocity: int (POINTER(h))
    velocityProgress: fx32 (struct_fx32)
    startStopSpeed: fx32 (struct_fx32)
    field154: int (POINTER(I))
    type: int (POINTER(I))
    sfxId: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    dcol: struct_dcol_inst_t
    startStopDuration: int
    rotateDuration: int
    idleDuration: int
    rotYVelocity: int
    velocityProgress: fx32
    startStopSpeed: fx32
    field154: int
    type: int
    sfxId: int

class struct_rotdiemobj_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    dieMinY: fx32 (struct_fx32)
    dieYAccel: fx32 (struct_fx32)
    dieRotZDir: int (POINTER(i))
    dieRotZ: int (POINTER(H))
    dieRotZSpeed: int (POINTER(H))
    dieInitialYVelo: fx32 (struct_fx32)
    fieldB4: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    dieMinY: fx32
    dieYAccel: fx32
    dieRotZDir: int
    dieRotZ: int
    dieRotZSpeed: int
    dieInitialYVelo: fx32
    fieldB4: fx32

class struct_rptc_col_effect_t(Structure):
    """
    ```python
    variants: list[struct_rptc_col_effect_variant_t] (struct_rptc_col_effect_variant_t[2])
    func: Callable[[POINTER_T[struct_rptc_col_effect_variant_t], int, POINTER_T[struct_driver_t]], c_int] (CFunctionType)
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    variants: list[struct_rptc_col_effect_variant_t]
    func: Callable[[POINTER_T[struct_rptc_col_effect_variant_t], int, POINTER_T[struct_driver_t]], c_int]
    field1C: int

class struct_rptc_col_effect_variant_t(Structure):
    """
    ```python
    emitterCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    emitterIds: list[int] (POINTER(I)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    emitterCount: int
    PADDING_0: list[int]
    emitterIds: list[int]

class struct_rptc_driver_effect_controller_t(Structure):
    """
    ```python
    emitterId: int (POINTER(i))
    tireEmitterIds: list[int] (POINTER(i)[2])
    emitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    tireEmitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2][2])
    field20: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[2])
    wallLeafEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    bulletBillEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    electricEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    tireEmitterPositions: list[struct_VecFx32] (struct_VecFx32[2])
    tireEmitterAxes: list[struct_VecFx16] (struct_VecFx16[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    emitterId: int
    tireEmitterIds: list[int]
    emitter: POINTER_T[struct_spa_emitter_t]
    tireEmitters: list[POINTER_T[struct_spa_emitter_t]]
    field20: list[POINTER_T[struct_spa_emitter_t]]
    wallLeafEmitter: POINTER_T[struct_spa_emitter_t]
    bulletBillEmitter: POINTER_T[struct_spa_emitter_t]
    electricEmitter: POINTER_T[struct_spa_emitter_t]
    tireEmitterPositions: list[struct_VecFx32]
    tireEmitterAxes: list[struct_VecFx16]

class struct_rptc_rainbow_effect_t(Structure):
    """
    ```python
    emitters: list[POINTER_T[struct_spa_emitter_t]] (POINTER(struct_spa_emitter_t)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    emitters: list[POINTER_T[struct_spa_emitter_t]]

class struct_sanbo_part_t(Structure):
    """
    ```python
    dieingPosition: struct_VecFx32 (struct_VecFx32)
    dieingVelocity: struct_VecFx32 (struct_VecFx32)
    scaleXY: fx32 (struct_fx32)
    rotZSinThing: struct_sinthing_t (struct_sinthing_t)
    rotZ: int (POINTER(i))
    rotZSpeed: int (POINTER(i))
    wiggleWaitCounter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    dieingPosition: struct_VecFx32
    dieingVelocity: struct_VecFx32
    scaleXY: fx32
    rotZSinThing: struct_sinthing_t
    rotZ: int
    rotZSpeed: int
    wiggleWaitCounter: int

class struct_sanbo_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    pwWaitCounter: int (POINTER(i))
    hitTimeout: int (POINTER(i))
    resurrectionWaitCounter: int (POINTER(i))
    sfxTimeout: int (POINTER(i))
    bodyParts: list[struct_sanbo_part_t] (struct_sanbo_part_t[4])
    bodyPartCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    pwSpeed: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    pwWaitCounter: int
    hitTimeout: int
    resurrectionWaitCounter: int
    sfxTimeout: int
    bodyParts: list[struct_sanbo_part_t]
    bodyPartCount: int
    PADDING_0: list[int]
    pwSpeed: fx32
    pathwalker: struct_pw_pathwalker_t
    state: int

class struct_save_core_t(Structure):
    """
    ```python
    status: int (POINTER(I))
    error: int (POINTER(I))
    backupLock: int (POINTER(I))
    isEnabled: int (POINTER(i))
    isBusy: int (POINTER(i))
    transferType: int (POINTER(I))
    backupSrcDst: int (POINTER(I))
    originalError: int (POINTER(I))
    originalSrcDst: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    originalTimestamp: int (POINTER(H))
    field26: int (POINTER(H))
    readDst: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    readSrc: int (POINTER(I))
    readLen: int (POINTER(I))
    readBlockSignature: int (POINTER(I))
    readBlockIsHeader: int (POINTER(i))
    field3C: int (POINTER(I))
    writeSrc: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    writeDst: int (POINTER(I))
    writeLength: int (POINTER(I))
    field4C: int (POINTER(I))
    writeBlockIsHeader: int (POINTER(i))
    callbackArg: c_void_p (c_void_p)
    field58: int (POINTER(I))
    field5C: int (POINTER(I))
    tmpBuf: c_void_p (c_void_p)
    testByte: c_void_p (c_void_p)
    realDst: int (POINTER(I))
    field6C: int (POINTER(B))
    field6D: int (POINTER(B))
    field6E: int (POINTER(B))
    field6F: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    status: int
    error: int
    backupLock: int
    isEnabled: int
    isBusy: int
    transferType: int
    backupSrcDst: int
    originalError: int
    originalSrcDst: POINTER_T[c_ubyte]
    originalTimestamp: int
    field26: int
    readDst: POINTER_T[c_ubyte]
    readSrc: int
    readLen: int
    readBlockSignature: int
    readBlockIsHeader: int
    field3C: int
    writeSrc: POINTER_T[c_ubyte]
    writeDst: int
    writeLength: int
    field4C: int
    writeBlockIsHeader: int
    callbackArg: c_void_p
    field58: int
    field5C: int
    tmpBuf: c_void_p
    testByte: c_void_p
    realDst: int
    field6C: int
    field6D: int
    field6E: int
    field6F: int

class struct_save_data_t(Structure):
    """
    ```python
    nksy: POINTER_T[struct_nksy_t] (POINTER(struct_nksy_t))
    nkem: POINTER_T[c_ubyte] (POINTER(POINTER(B)))
    nkgp: int (POINTER(I))
    nkta: int (POINTER(I))
    nkmr: int (POINTER(I))
    nkpg: POINTER_T[struct_nkpg_t] (POINTER(struct_nkpg_t))
    nkdg: POINTER_T[struct_nkdg_t] (POINTER(struct_nkdg_t))
    staffGhost: POINTER_T[struct_nkdg_t] (POINTER(struct_nkdg_t))
    nkfl: int (POINTER(I))
    nkfe: int (POINTER(I))
    isBusy: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    blockErrorFlags: int (POINTER(H))
    error: int (POINTER(I))
    field30: list[int] (POINTER(B)[4])
    field34: list[int] (POINTER(B)[4])
    field38: int (POINTER(B))
    field39: int (POINTER(B))
    unk3A: list[int] (POINTER(B)[2])
    field3C: int (POINTER(B))
    unk3D: list[int] (POINTER(B)[3])
    field40: int (POINTER(I))
    field44: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    nksy: POINTER_T[struct_nksy_t]
    nkem: POINTER_T[c_ubyte]
    nkgp: int
    nkta: int
    nkmr: int
    nkpg: POINTER_T[struct_nkpg_t]
    nkdg: POINTER_T[struct_nkdg_t]
    staffGhost: POINTER_T[struct_nkdg_t]
    nkfl: int
    nkfe: int
    isBusy: int
    PADDING_0: int
    blockErrorFlags: int
    error: int
    field30: list[int]
    field34: list[int]
    field38: int
    field39: int
    unk3A: list[int]
    field3C: int
    unk3D: list[int]
    field40: int
    field44: int

class struct_sblln_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    scale: fx32 (struct_fx32)
    scaleDelta: fx32 (struct_fx32)
    counter: int (POINTER(i))
    driver: POINTER_T[struct_driver_t] (POINTER(struct_driver_t))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    scale: fx32
    scaleDelta: fx32
    counter: int
    driver: POINTER_T[struct_driver_t]
    state: int

class struct_scene_def_t(Structure):
    """
    ```python
    initFunc: Callable[[POINTER_T[struct_scene_manager_t]], None] (CFunctionType)
    updateFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None] (CFunctionType)
    finalizeFunc: Callable[[POINTER_T[struct_scene_manager_t]], None] (CFunctionType)
    vblankFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None] (CFunctionType)
    preSleepFunc: Callable[[], None] (CFunctionType)
    postSleepFunc: Callable[[], None] (CFunctionType)
    fadeInLength: int (POINTER(h))
    fadeOutLength: int (POINTER(h))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    initFunc: Callable[[POINTER_T[struct_scene_manager_t]], None]
    updateFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None]
    finalizeFunc: Callable[[POINTER_T[struct_scene_manager_t]], None]
    vblankFunc: Callable[[POINTER_T[struct_scene_manager_t], int], None]
    preSleepFunc: Callable[[], None]
    postSleepFunc: Callable[[], None]
    fadeInLength: int
    fadeOutLength: int
    field1C: int

class struct_scene_manager_t(Structure):
    """
    ```python
    previousScene: int (POINTER(h))
    currentScene: int (POINTER(h))
    nextScene: int (POINTER(h))
    ```
    """
    _pack_: ClassVar[int] = 1
    previousScene: int
    currentScene: int
    nextScene: int

class struct_scene_proc_t(Structure):
    """
    ```python
    overlayId: int (POINTER(I))
    nextOverlayId: int (POINTER(I))
    sceneId: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    soundHeap: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    overlayId: int
    nextOverlayId: int
    sceneId: int
    PADDING_0: list[int]
    soundHeap: c_void_p

class struct_scene_state_t(Structure):
    """
    ```python
    threadStack: POINTER_T[c_uint] (POINTER(POINTER(I)))
    PADDING_0: list[int] (POINTER(B)[4])
    thread: struct__OSThread (struct__OSThread)
    threadQueue: struct__OSThreadQueue (struct__OSThreadQueue)
    preSleepCallback: struct_PMiSleepCallbackInfo (struct_PMiSleepCallbackInfo)
    postSleepCallback: struct_PMiSleepCallbackInfo (struct_PMiSleepCallbackInfo)
    sceneFrameCounter: int (POINTER(i))
    totalFrameCounter: int (POINTER(i))
    curSceneDef: struct_scene_def_t (struct_scene_def_t)
    state: int (POINTER(I))
    isLcdOff: int (POINTER(i))
    gap114: list[int] (POINTER(B)[4])
    field118: int (POINTER(I))
    field11C: int (POINTER(I))
    field120: int (POINTER(b))
    gap121: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    threadStack: POINTER_T[c_uint]
    PADDING_0: list[int]
    thread: struct__OSThread
    threadQueue: struct__OSThreadQueue
    preSleepCallback: struct_PMiSleepCallbackInfo
    postSleepCallback: struct_PMiSleepCallbackInfo
    sceneFrameCounter: int
    totalFrameCounter: int
    curSceneDef: struct_scene_def_t
    state: int
    isLcdOff: int
    gap114: list[int]
    field118: int
    field11C: int
    field120: int
    gap121: list[int]

class struct_secondhand_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    curRotation: quaternion_t (struct_quaternion_t)
    baseRotation: quaternion_t (struct_quaternion_t)
    startStopFrameCount: int (POINTER(H))
    oneDirFrameCount: int (POINTER(H))
    waitFrameCount: int (POINTER(H))
    baseVelocity: int (POINTER(h))
    velocity: fx32 (struct_fx32)
    acceleration: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    curRotation: quaternion_t
    baseRotation: quaternion_t
    startStopFrameCount: int
    oneDirFrameCount: int
    waitFrameCount: int
    baseVelocity: int
    velocity: fx32
    acceleration: fx32

class struct_seq_handle_t(Structure):
    """
    ```python
    seqLoadInfo: struct_seq_load_info_t (struct_seq_load_info_t)
    handle: struct_NNSSndHandle (struct_NNSSndHandle)
    heapState: POINTER_T[struct_seq_heap_state_t] (POINTER(struct_seq_heap_state_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    seqLoadInfo: struct_seq_load_info_t
    handle: struct_NNSSndHandle
    heapState: POINTER_T[struct_seq_heap_state_t]

class struct_seq_heap_state_t(Structure):
    """
    ```python
    seqLoadInfo: struct_seq_load_info_t (struct_seq_load_info_t)
    heapLevel: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    seqLoadInfo: struct_seq_load_info_t
    heapLevel: int

class struct_seq_load_info_t(Structure):
    """
    ```python
    seqId: int (POINTER(I))
    bank1: int (POINTER(I))
    bank2: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    seqId: int
    bank1: int
    bank2: int

class struct_sfsn_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    state1Counter: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    state0Counter: int (POINTER(i))
    spawnPos: struct_VecFx32 (struct_VecFx32)
    angle: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    state: int (POINTER(I))
    ptclEmitterA: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ptclEmitterB: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    state1Counter: int
    PADDING_0: list[int]
    state0Counter: int
    spawnPos: struct_VecFx32
    angle: int
    PADDING_1: list[int]
    state: int
    ptclEmitterA: POINTER_T[struct_spa_emitter_t]
    ptclEmitterB: POINTER_T[struct_spa_emitter_t]

class struct_sfx_base_params_t(Structure):
    """
    ```python
    maxDistance: int (POINTER(I))
    fadePart1EndDistance: int (POINTER(I))
    fadePart1EndVolume: int (POINTER(I))
    fadeStartDistance: int (POINTER(I))
    maxVolume: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    maxDistance: int
    fadePart1EndDistance: int
    fadePart1EndVolume: int
    fadeStartDistance: int
    maxVolume: int

class struct_sfx_emitter_ex_params_t(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    pitchOffset: int (POINTER(I))
    fieldC: int (POINTER(I))
    unk10: list[int] (POINTER(B)[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    pitchOffset: int
    fieldC: int
    unk10: list[int]

class struct_sfx_emitter_ex_t(Structure):
    """
    ```python
    emitter: struct_sfx_emitter_t (struct_sfx_emitter_t)
    exParams: struct_sfx_emitter_ex_params_t (struct_sfx_emitter_ex_params_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    emitter: struct_sfx_emitter_t
    exParams: struct_sfx_emitter_ex_params_t

class struct_sfx_emitter_t(Structure):
    """
    ```python
    listLink: struct_list_link_t (struct_list_link_t)
    soundList: struct_NNSFndList (struct_NNSFndList)
    field18: int (POINTER(I))
    field1C: struct_list_link_t (struct_list_link_t)
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    startFunc: c_void_p (c_void_p)
    updateFunc: c_void_p (c_void_p)
    field34: int (POINTER(H))
    field36: int (POINTER(H))
    field38: int (POINTER(I))
    sfxParamIdx: int (POINTER(B))
    field3D: list[int] (POINTER(B)[3])
    squareDistance: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    listLink: struct_list_link_t
    soundList: struct_NNSFndList
    field18: int
    field1C: struct_list_link_t
    position: POINTER_T[struct_VecFx32]
    startFunc: c_void_p
    updateFunc: c_void_p
    field34: int
    field36: int
    field38: int
    sfxParamIdx: int
    field3D: list[int]
    squareDistance: int

class struct_sfx_params_t(Structure):
    """
    ```python
    maxDistance: int (POINTER(i))
    fadePart1EndDistance: int (POINTER(i))
    fadePart1EndVolume: int (POINTER(I))
    fadeStartDistance: int (POINTER(i))
    maxVolume: int (POINTER(i))
    fadePart1Factor: fx32 (struct_fx32)
    fadePart2Factor: fx32 (struct_fx32)
    field1C: int (POINTER(I))
    maxDistanceSquare: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    maxDistance: int
    fadePart1EndDistance: int
    fadePart1EndVolume: int
    fadeStartDistance: int
    maxVolume: int
    fadePart1Factor: fx32
    fadePart2Factor: fx32
    field1C: int
    maxDistanceSquare: int

class struct_sfx_sound_t(Structure):
    """
    ```python
    poolHandle: struct_sp_handle_t (struct_sp_handle_t)
    listLink: struct_list_link_t (struct_list_link_t)
    pitch: int (POINTER(h))
    sfxId: int (POINTER(H))
    seqArcId: int (POINTER(B))
    field19: int (POINTER(B))
    volume: int (POINTER(B))
    field1B: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    poolHandle: struct_sp_handle_t
    listLink: struct_list_link_t
    pitch: int
    sfxId: int
    seqArcId: int
    field19: int
    volume: int
    field1B: int

class struct_shadowmodel_t(Structure):
    """
    ```python
    model: struct_model_t (struct_model_t)
    polygonId: int (POINTER(H))
    alpha: int (POINTER(H))
    flags: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    model: struct_model_t
    polygonId: int
    alpha: int
    flags: int
    PADDING_0: list[int]

class struct_shinc_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    hasSpawned: int (POINTER(i))
    fieldA4: int (POINTER(I))
    counter: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    hasSpawned: int
    fieldA4: int
    counter: int

class struct_sinthing_t(Structure):
    """
    ```python
    phase: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    value: fx32 (struct_fx32)
    velocity: fx32 (struct_fx32)
    baseOffset: fx32 (struct_fx32)
    amplitude: fx32 (struct_fx32)
    amplitudeVelocity: fx32 (struct_fx32)
    phaseVelocity: int (POINTER(i))
    phaseAcceleration: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    phase: int
    PADDING_0: list[int]
    value: fx32
    velocity: fx32
    baseOffset: fx32
    amplitude: fx32
    amplitudeVelocity: fx32
    phaseVelocity: int
    phaseAcceleration: int

class struct_snd_unkstruct_field0_t(Structure):
    """
    ```python
    sfxId: int (POINTER(I))
    position: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    sfxParamsId: int (POINTER(I))
    squareDistance: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    sfxId: int
    position: POINTER_T[struct_VecFx32]
    sfxParamsId: int
    squareDistance: int

class struct_snd_unkstruct_t(Structure):
    """
    ```python
    field0: struct_snd_unkstruct_field0_t (struct_snd_unkstruct_field0_t)
    position: struct_VecFx32 (struct_VecFx32)
    soundHandle: struct_NNSSndHandle (struct_NNSSndHandle)
    field20: int (POINTER(I))
    field24: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: struct_snd_unkstruct_field0_t
    position: struct_VecFx32
    soundHandle: struct_NNSSndHandle
    field20: int
    field24: int

class struct_snowman_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    headRotEnabled: int (POINTER(i))
    headRotZ: int (POINTER(i))
    headRotZVelocity: int (POINTER(i))
    counter: int (POINTER(i))
    headElevationProgress: fx32 (struct_fx32)
    bottomScale: fx32 (struct_fx32)
    headElevation: fx32 (struct_fx32)
    headElevationVelocity: fx32 (struct_fx32)
    headMaxElevation: fx32 (struct_fx32)
    headMinElevation: fx32 (struct_fx32)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    headRotEnabled: int
    headRotZ: int
    headRotZVelocity: int
    counter: int
    headElevationProgress: fx32
    bottomScale: fx32
    headElevation: fx32
    headElevationVelocity: fx32
    headMaxElevation: fx32
    headMinElevation: fx32
    state: int

class struct_sound_pool_t(Structure):
    """
    ```python
    nrElements: int (POINTER(i))
    elements1Idx: int (POINTER(I))
    elements1: c_void_p (c_void_p)
    elements: c_void_p (c_void_p)
    elementSize: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    nrElements: int
    elements1Idx: int
    elements1: c_void_p
    elements: c_void_p
    elementSize: int

class struct_sound_var_t(Structure):
    """
    ```python
    value: int (POINTER(h))
    field2: int (POINTER(h))
    field4: int (POINTER(i))
    id: int (POINTER(b))
    PADDING_0: list[int] (POINTER(B)[3])
    ```
    """
    _pack_: ClassVar[int] = 1
    value: int
    field2: int
    field4: int
    id: int
    PADDING_0: list[int]

class struct_sp_handle_t(Structure):
    """
    ```python
    handle: struct_NNSSndHandle (struct_NNSSndHandle)
    age: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    handle: struct_NNSSndHandle
    age: int

class struct_spa_emitter_data_t(Structure):
    """
    ```python
    resource: POINTER_T[struct_spa_res_emitter_t] (POINTER(struct_spa_res_emitter_t))
    scaleAnim: POINTER_T[struct_spa_res_emitter_scaleanim_t] (POINTER(struct_spa_res_emitter_scaleanim_t))
    colorAnim: POINTER_T[struct_spa_res_emitter_coloranim_t] (POINTER(struct_spa_res_emitter_coloranim_t))
    alphaAnim: POINTER_T[struct_spa_res_emitter_alphaanim_t] (POINTER(struct_spa_res_emitter_alphaanim_t))
    texAnim: POINTER_T[struct_spa_res_emitter_texanim_t] (POINTER(struct_spa_res_emitter_texanim_t))
    childData: POINTER_T[struct_spa_res_emitter_child_t] (POINTER(struct_spa_res_emitter_child_t))
    fieldFuncs: POINTER_T[struct_spa_transform_func_arg_pair_t] (POINTER(struct_spa_transform_func_arg_pair_t))
    fieldFuncCount: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    resource: POINTER_T[struct_spa_res_emitter_t]
    scaleAnim: POINTER_T[struct_spa_res_emitter_scaleanim_t]
    colorAnim: POINTER_T[struct_spa_res_emitter_coloranim_t]
    alphaAnim: POINTER_T[struct_spa_res_emitter_alphaanim_t]
    texAnim: POINTER_T[struct_spa_res_emitter_texanim_t]
    childData: POINTER_T[struct_spa_res_emitter_child_t]
    fieldFuncs: POINTER_T[struct_spa_transform_func_arg_pair_t]
    fieldFuncCount: int
    PADDING_0: list[int]

class struct_spa_emitter_t(Structure):
    """
    ```python
    listLink: struct_spa_list_link_t (struct_spa_list_link_t)
    mainParticleList: struct_spa_list_t (struct_spa_list_t)
    childParticleList: struct_spa_list_t (struct_spa_list_t)
    emitterData: POINTER_T[struct_spa_emitter_data_t] (POINTER(struct_spa_emitter_data_t))
    _0: union_spa_emitter_t_0 (union_spa_emitter_t_0)
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    particleVelocity: struct_VecFx32 (struct_VecFx32)
    age: int (POINTER(H))
    lastEmissionFraction: fx16 (struct_fx16)
    axis: struct_VecFx16 (struct_VecFx16)
    particleRotation: int (POINTER(H))
    emissionCount: fx32 (struct_fx32)
    radius: fx32 (struct_fx32)
    length: fx32 (struct_fx32)
    particlePosVeloMag: fx32 (struct_fx32)
    particleAxisVeloMag: fx32 (struct_fx32)
    particleScale: fx32 (struct_fx32)
    particleLifetime: int (POINTER(H))
    color: int (POINTER(H))
    collisionPlaneYOverride: fx32 (struct_fx32)
    texS: fx16 (struct_fx16)
    texT: fx16 (struct_fx16)
    childTexS: fx16 (struct_fx16)
    childTexT: fx16 (struct_fx16)
    emissionInterval: int (POINTER(I))
    particleAlpha: int (POINTER(I))
    updateMoment: int (POINTER(I))
    field80Unk2: int (POINTER(I))
    axisRight: struct_VecFx16 (struct_VecFx16)
    axisUp: struct_VecFx16 (struct_VecFx16)
    callbackFunc: Callable[[POINTER_T[struct_spa_emitter_t], int], None] (CFunctionType)
    userData: int (POINTER(I))
    _1: union_spa_emitter_t_1 (union_spa_emitter_t_1)
    ```
    """
    _pack_: ClassVar[int] = 1
    listLink: struct_spa_list_link_t
    mainParticleList: struct_spa_list_t
    childParticleList: struct_spa_list_t
    emitterData: POINTER_T[struct_spa_emitter_data_t]
    _0: union_spa_emitter_t_0
    position: struct_VecFx32
    velocity: struct_VecFx32
    particleVelocity: struct_VecFx32
    age: int
    lastEmissionFraction: fx16
    axis: struct_VecFx16
    particleRotation: int
    emissionCount: fx32
    radius: fx32
    length: fx32
    particlePosVeloMag: fx32
    particleAxisVeloMag: fx32
    particleScale: fx32
    particleLifetime: int
    color: int
    collisionPlaneYOverride: fx32
    texS: fx16
    texT: fx16
    childTexS: fx16
    childTexT: fx16
    emissionInterval: int
    particleAlpha: int
    updateMoment: int
    field80Unk2: int
    axisRight: struct_VecFx16
    axisUp: struct_VecFx16
    callbackFunc: Callable[[POINTER_T[struct_spa_emitter_t], int], None]
    userData: int
    _1: union_spa_emitter_t_1

class struct_spa_emitter_t_0_0(Structure):
    """
    ```python
    shouldDie: int (POINTER(I))
    disableEmission: int (POINTER(I))
    disableUpdates: int (POINTER(I))
    disableRendering: int (POINTER(I))
    startedEmitting: int (POINTER(I))
    _5: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    shouldDie: int
    disableEmission: int
    disableUpdates: int
    disableRendering: int
    startedEmitting: int
    _5: int

class struct_spa_list_link_t(Structure):
    """
    ```python
    next: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    prev: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    next: POINTER_T[struct_spa_list_link_t]
    prev: POINTER_T[struct_spa_list_link_t]

class struct_spa_list_t(Structure):
    """
    ```python
    head: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    count: int (POINTER(I))
    tail: POINTER_T[struct_spa_list_link_t] (POINTER(struct_spa_list_link_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    head: POINTER_T[struct_spa_list_link_t]
    count: int
    tail: POINTER_T[struct_spa_list_link_t]

class struct_spa_particle_t(Structure):
    """
    ```python
    listLink: struct_spa_list_link_t (struct_spa_list_link_t)
    position: struct_VecFx32 (struct_VecFx32)
    velocity: struct_VecFx32 (struct_VecFx32)
    rotation: int (POINTER(H))
    rotationVelocity: int (POINTER(h))
    maxAge: int (POINTER(H))
    age: int (POINTER(H))
    progressSpeedLoop: int (POINTER(H))
    progressSpeedNoLoop: int (POINTER(H))
    textureId: int (POINTER(B))
    progressOffset: int (POINTER(B))
    baseAlpha: int (POINTER(H))
    alpha: int (POINTER(H))
    polygonId: int (POINTER(H))
    baseScale: fx32 (struct_fx32)
    scale: fx16 (struct_fx16)
    color: int (POINTER(H))
    basePosition: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    listLink: struct_spa_list_link_t
    position: struct_VecFx32
    velocity: struct_VecFx32
    rotation: int
    rotationVelocity: int
    maxAge: int
    age: int
    progressSpeedLoop: int
    progressSpeedNoLoop: int
    textureId: int
    progressOffset: int
    baseAlpha: int
    alpha: int
    polygonId: int
    baseScale: fx32
    scale: fx16
    color: int
    basePosition: struct_VecFx32

class struct_spa_particleset_t(Structure):
    """
    ```python
    allocFunc: Callable[[int], c_void_p] (CFunctionType)
    activeEmitterList: struct_spa_list_t (struct_spa_list_t)
    freeEmitterList: struct_spa_list_t (struct_spa_list_t)
    freeParticleList: struct_spa_list_t (struct_spa_list_t)
    emitterData: POINTER_T[struct_spa_emitter_data_t] (POINTER(struct_spa_emitter_data_t))
    textureData: POINTER_T[struct_spa_texture_data_t] (POINTER(struct_spa_texture_data_t))
    resEmitterCount: int (POINTER(H))
    resTexCount: int (POINTER(H))
    maxEmitterCount: int (POINTER(H))
    maxParticleCount: int (POINTER(H))
    firstPolygonId: int (POINTER(I))
    lastPolygonId: int (POINTER(I))
    curPolygonId: int (POINTER(I))
    constPolygonId: int (POINTER(I))
    reverseRenderOrder: int (POINTER(I))
    unknown: int (POINTER(I))
    polygonAttr: int (POINTER(I))
    curEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    cameraMtx: POINTER_T[union_MtxFx43] (POINTER(union_MtxFx43))
    frameIndex: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    allocFunc: Callable[[int], c_void_p]
    activeEmitterList: struct_spa_list_t
    freeEmitterList: struct_spa_list_t
    freeParticleList: struct_spa_list_t
    emitterData: POINTER_T[struct_spa_emitter_data_t]
    textureData: POINTER_T[struct_spa_texture_data_t]
    resEmitterCount: int
    resTexCount: int
    maxEmitterCount: int
    maxParticleCount: int
    firstPolygonId: int
    lastPolygonId: int
    curPolygonId: int
    constPolygonId: int
    reverseRenderOrder: int
    unknown: int
    polygonAttr: int
    curEmitter: POINTER_T[struct_spa_emitter_t]
    cameraMtx: POINTER_T[union_MtxFx43]
    frameIndex: int
    PADDING_0: list[int]

class struct_spa_res_emitter_alphaanim_t(Structure):
    """
    ```python
    initialAlpha: int (POINTER(H))
    peakAlpha: int (POINTER(H))
    endingAlpha: int (POINTER(H))
    _3: int (POINTER(H))
    randomness: int (POINTER(H))
    loop: int (POINTER(H))
    _6: int (POINTER(H))
    inCompletedTiming: int (POINTER(H))
    outStartTiming: int (POINTER(B))
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    initialAlpha: int
    peakAlpha: int
    endingAlpha: int
    _3: int
    randomness: int
    loop: int
    _6: int
    inCompletedTiming: int
    outStartTiming: int
    padding: int

class struct_spa_res_emitter_child_t(Structure):
    """
    ```python
    applyEmitterField: int (POINTER(H))
    useScaleAnim: int (POINTER(H))
    hasAlphaFade: int (POINTER(H))
    rotInheritMode: int (POINTER(H))
    followEmitter: int (POINTER(H))
    useChildColor: int (POINTER(H))
    particleType: int (POINTER(H))
    rotMtxMode: int (POINTER(H))
    quadDirection: int (POINTER(H))
    _9: int (POINTER(H))
    initVelocityRandomness: int (POINTER(h))
    targetScale: fx16 (struct_fx16)
    lifeTime: int (POINTER(H))
    velocityInheritRatio: int (POINTER(B))
    scale: int (POINTER(B))
    color: int (POINTER(H))
    emissionVolume: int (POINTER(B))
    emissionTime: int (POINTER(B))
    emissionInterval: int (POINTER(B))
    textureId: int (POINTER(B))
    texRepeatShiftS: int (POINTER(I))
    texRepeatShiftT: int (POINTER(I))
    texFlipS: int (POINTER(I))
    texFlipT: int (POINTER(I))
    centerDirPolygon: int (POINTER(I))
    _25: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    applyEmitterField: int
    useScaleAnim: int
    hasAlphaFade: int
    rotInheritMode: int
    followEmitter: int
    useChildColor: int
    particleType: int
    rotMtxMode: int
    quadDirection: int
    _9: int
    initVelocityRandomness: int
    targetScale: fx16
    lifeTime: int
    velocityInheritRatio: int
    scale: int
    color: int
    emissionVolume: int
    emissionTime: int
    emissionInterval: int
    textureId: int
    texRepeatShiftS: int
    texRepeatShiftT: int
    texFlipS: int
    texFlipT: int
    centerDirPolygon: int
    _25: int

class struct_spa_res_emitter_coloranim_t(Structure):
    """
    ```python
    initialColor: int (POINTER(H))
    endingColor: int (POINTER(H))
    inCompletedTiming: int (POINTER(B))
    peakTiming: int (POINTER(B))
    outStartTiming: int (POINTER(B))
    field7: int (POINTER(B))
    isRandom: int (POINTER(H))
    loop: int (POINTER(H))
    interpolate: int (POINTER(H))
    _9: int (POINTER(H))
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    initialColor: int
    endingColor: int
    inCompletedTiming: int
    peakTiming: int
    outStartTiming: int
    field7: int
    isRandom: int
    loop: int
    interpolate: int
    _9: int
    padding: int

class struct_spa_res_emitter_field_collision_t(Structure):
    """
    ```python
    collisionPlaneY: fx32 (struct_fx32)
    bounceCoef: fx16 (struct_fx16)
    behavior: int (POINTER(H))
    _3: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    collisionPlaneY: fx32
    bounceCoef: fx16
    behavior: int
    _3: int

class struct_spa_res_emitter_field_convergence_t(Structure):
    """
    ```python
    convergencePos: struct_VecFx32 (struct_VecFx32)
    convergenceRatio: fx16 (struct_fx16)
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    convergencePos: struct_VecFx32
    convergenceRatio: fx16
    padding: int

class struct_spa_res_emitter_field_gravity_t(Structure):
    """
    ```python
    gravity: struct_VecFx16 (struct_VecFx16)
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    gravity: struct_VecFx16
    padding: int

class struct_spa_res_emitter_field_magnet_t(Structure):
    """
    ```python
    magnetPos: struct_VecFx32 (struct_VecFx32)
    magnetPower: fx16 (struct_fx16)
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    magnetPos: struct_VecFx32
    magnetPower: fx16
    padding: int

class struct_spa_res_emitter_field_random_t(Structure):
    """
    ```python
    strength: struct_VecFx16 (struct_VecFx16)
    interval: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    strength: struct_VecFx16
    interval: int

class struct_spa_res_emitter_field_spin_t(Structure):
    """
    ```python
    rotation: int (POINTER(H))
    type: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    rotation: int
    type: int

class struct_spa_res_emitter_flags_t(Structure):
    """
    ```python
    emitterShape: int (POINTER(I))
    particleType: int (POINTER(I))
    axisDirType: int (POINTER(I))
    hasScaleAnim: int (POINTER(I))
    hasColorAnim: int (POINTER(I))
    hasAlphaAnim: int (POINTER(I))
    hasTexAnim: int (POINTER(I))
    hasRandomParticleDeltaRotation: int (POINTER(I))
    hasRandomParticleRotation: int (POINTER(I))
    emitterIsOneTime: int (POINTER(I))
    particlesFollowEmitter: int (POINTER(I))
    hasChildParticles: int (POINTER(I))
    rotMtxMode: int (POINTER(I))
    quadDirection: int (POINTER(I))
    randomizeParticleProgressOffset: int (POINTER(I))
    renderChildParticlesFirst: int (POINTER(I))
    dontRenderMainParticles: int (POINTER(I))
    relativePosAsRotOrigin: int (POINTER(I))
    hasFieldGravity: int (POINTER(I))
    hasFieldRandom: int (POINTER(I))
    hasFieldMagnetic: int (POINTER(I))
    hasFieldSpin: int (POINTER(I))
    hasFieldCollision: int (POINTER(I))
    hasFieldConvergence: int (POINTER(I))
    useConstPolygonIdForMainParticles: int (POINTER(I))
    useConstPolygonIdForChildParticles: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    emitterShape: int
    particleType: int
    axisDirType: int
    hasScaleAnim: int
    hasColorAnim: int
    hasAlphaAnim: int
    hasTexAnim: int
    hasRandomParticleDeltaRotation: int
    hasRandomParticleRotation: int
    emitterIsOneTime: int
    particlesFollowEmitter: int
    hasChildParticles: int
    rotMtxMode: int
    quadDirection: int
    randomizeParticleProgressOffset: int
    renderChildParticlesFirst: int
    dontRenderMainParticles: int
    relativePosAsRotOrigin: int
    hasFieldGravity: int
    hasFieldRandom: int
    hasFieldMagnetic: int
    hasFieldSpin: int
    hasFieldCollision: int
    hasFieldConvergence: int
    useConstPolygonIdForMainParticles: int
    useConstPolygonIdForChildParticles: int

class struct_spa_res_emitter_scaleanim_t(Structure):
    """
    ```python
    initialScale: fx16 (struct_fx16)
    intermediateScale: fx16 (struct_fx16)
    endingScale: fx16 (struct_fx16)
    inCompletedTiming: int (POINTER(B))
    scaleOutStartTime: int (POINTER(B))
    loop: int (POINTER(H))
    _6: int (POINTER(H))
    padding: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    initialScale: fx16
    intermediateScale: fx16
    endingScale: fx16
    inCompletedTiming: int
    scaleOutStartTime: int
    loop: int
    _6: int
    padding: int

class struct_spa_res_emitter_t(Structure):
    """
    ```python
    flags: struct_spa_res_emitter_flags_t (struct_spa_res_emitter_flags_t)
    position: struct_VecFx32 (struct_VecFx32)
    emissionCount: fx32 (struct_fx32)
    emitterRadius: fx32 (struct_fx32)
    emitterLength: fx32 (struct_fx32)
    emitterAxis: struct_VecFx16 (struct_VecFx16)
    color: int (POINTER(H))
    particlePosVeloMag: fx32 (struct_fx32)
    particleAxisVeloMag: fx32 (struct_fx32)
    particleBaseScale: fx32 (struct_fx32)
    aspectRatio: fx16 (struct_fx16)
    emissionStartTime: int (POINTER(H))
    minRotVelocity: int (POINTER(h))
    maxRotVelocity: int (POINTER(h))
    particleRotation: int (POINTER(H))
    padding1: int (POINTER(H))
    emissionTime: int (POINTER(H))
    particleLifetime: int (POINTER(H))
    particleScaleRandomness: int (POINTER(B))
    particleLifetimeRandomness: int (POINTER(B))
    particleVeloMagRandomness: int (POINTER(B))
    padding2: int (POINTER(B))
    emissionInterval: int (POINTER(B))
    particleAlpha: int (POINTER(B))
    airResistance: int (POINTER(B))
    textureId: int (POINTER(B))
    loopFrame: int (POINTER(L))
    dirBillboardScale: int (POINTER(L))
    texRepeatShiftS: int (POINTER(L))
    texRepeatShiftT: int (POINTER(L))
    scaleMode: int (POINTER(L))
    centerDirPolygon: int (POINTER(L))
    texFlipS: int (POINTER(L))
    texFlipT: int (POINTER(L))
    _34: int (POINTER(L))
    quadXOffset: fx16 (struct_fx16)
    quadYZOffset: fx16 (struct_fx16)
    _0: union_spa_res_emitter_t_0 (union_spa_res_emitter_t_0)
    ```
    """
    _pack_: ClassVar[int] = 1
    flags: struct_spa_res_emitter_flags_t
    position: struct_VecFx32
    emissionCount: fx32
    emitterRadius: fx32
    emitterLength: fx32
    emitterAxis: struct_VecFx16
    color: int
    particlePosVeloMag: fx32
    particleAxisVeloMag: fx32
    particleBaseScale: fx32
    aspectRatio: fx16
    emissionStartTime: int
    minRotVelocity: int
    maxRotVelocity: int
    particleRotation: int
    padding1: int
    emissionTime: int
    particleLifetime: int
    particleScaleRandomness: int
    particleLifetimeRandomness: int
    particleVeloMagRandomness: int
    padding2: int
    emissionInterval: int
    particleAlpha: int
    airResistance: int
    textureId: int
    loopFrame: int
    dirBillboardScale: int
    texRepeatShiftS: int
    texRepeatShiftT: int
    scaleMode: int
    centerDirPolygon: int
    texFlipS: int
    texFlipT: int
    _34: int
    quadXOffset: fx16
    quadYZOffset: fx16
    _0: union_spa_res_emitter_t_0

class struct_spa_res_emitter_texanim_t(Structure):
    """
    ```python
    frames: list[int] (POINTER(B)[8])
    frameCount: int (POINTER(I))
    frameDuration: int (POINTER(I))
    isRandom: int (POINTER(I))
    loop: int (POINTER(I))
    _5: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    frames: list[int]
    frameCount: int
    frameDuration: int
    isRandom: int
    loop: int
    _5: int

class struct_spa_res_header_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    version: int (POINTER(I))
    emitterCount: int (POINTER(H))
    textureCount: int (POINTER(H))
    fieldC: int (POINTER(I))
    emitterBlockLength: int (POINTER(I))
    textureBlockLength: int (POINTER(I))
    textureBlockOffset: int (POINTER(I))
    field1C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    version: int
    emitterCount: int
    textureCount: int
    fieldC: int
    emitterBlockLength: int
    textureBlockLength: int
    textureBlockOffset: int
    field1C: int

class struct_spa_res_texture_params_t(Structure):
    """
    ```python
    format: int (POINTER(I))
    width: int (POINTER(I))
    height: int (POINTER(I))
    repeat: int (POINTER(I))
    flip: int (POINTER(I))
    pltt0Transparent: int (POINTER(I))
    refTexData: int (POINTER(I))
    refTexId: int (POINTER(I))
    _8: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    format: int
    width: int
    height: int
    repeat: int
    flip: int
    pltt0Transparent: int
    refTexData: int
    refTexId: int
    _8: int

class struct_spa_res_texture_t(Structure):
    """
    ```python
    signature: int (POINTER(I))
    texParams: struct_spa_res_texture_params_t (struct_spa_res_texture_params_t)
    texSize: int (POINTER(I))
    plttOffset: int (POINTER(I))
    plttSize: int (POINTER(I))
    plttIdxOffset: int (POINTER(I))
    plttIdxSize: int (POINTER(I))
    blockSize: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    signature: int
    texParams: struct_spa_res_texture_params_t
    texSize: int
    plttOffset: int
    plttSize: int
    plttIdxOffset: int
    plttIdxSize: int
    blockSize: int

class struct_spa_texture_data_t(Structure):
    """
    ```python
    resource: POINTER_T[struct_spa_res_texture_t] (POINTER(struct_spa_res_texture_t))
    texVramAddr: int (POINTER(I))
    plttVramAddr: int (POINTER(I))
    texParams: struct_spa_res_texture_params_t (struct_spa_res_texture_params_t)
    width: int (POINTER(H))
    height: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    resource: POINTER_T[struct_spa_res_texture_t]
    texVramAddr: int
    plttVramAddr: int
    texParams: struct_spa_res_texture_params_t
    width: int
    height: int

class struct_spa_transform_func_arg_pair_t(Structure):
    """
    ```python
    func: Callable[[c_void_p, POINTER_T[struct_spa_particle_t], POINTER_T[struct_VecFx32], POINTER_T[struct_spa_emitter_t]], None] (CFunctionType)
    resData: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    func: Callable[[c_void_p, POINTER_T[struct_spa_particle_t], POINTER_T[struct_VecFx32], POINTER_T[struct_spa_emitter_t]], None]
    resData: c_void_p

class struct_spi_t(Structure):
    """
    ```python
    tpSampleBuf: list[struct_TPData] (struct_TPData[5])
    curTp: struct_TPData (struct_TPData)
    tpAutoSamplingEnabled: int (POINTER(i))
    micAutoSamplingEnabled: int (POINTER(i))
    micAutoSamplingPaused: int (POINTER(i))
    micInputDetected: int (POINTER(i))
    PADDING_0: int (POINTER(B))
    gap34: list[int] (POINTER(B)[8])
    PADDING_1: list[int] (POINTER(B)[3])
    micData: POINTER_T[struct_mic_t] (POINTER(struct_mic_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    tpSampleBuf: list[struct_TPData]
    curTp: struct_TPData
    tpAutoSamplingEnabled: int
    micAutoSamplingEnabled: int
    micAutoSamplingPaused: int
    micInputDetected: int
    PADDING_0: int
    gap34: list[int]
    PADDING_1: list[int]
    micData: POINTER_T[struct_mic_t]

class struct_ssm_state_t(Structure):
    """
    ```python
    vblankFunc: Callable[[], None] (CFunctionType)
    renderFunc: Callable[[POINTER_T[struct_scene_manager_t]], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    vblankFunc: Callable[[], None]
    renderFunc: Callable[[POINTER_T[struct_scene_manager_t]], None]

class struct_ssm_t(Structure):
    """
    ```python
    frameCounter: int (POINTER(i))
    changingState: int (POINTER(i))
    prevState: int (POINTER(I))
    curState: int (POINTER(I))
    nextState: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    frameCounter: int
    changingState: int
    prevState: int
    curState: int
    nextState: int

class struct_state_machine_state_t(Structure):
    """
    ```python
    initFunc: Callable[[c_void_p], None] (CFunctionType)
    stateFunc: Callable[[c_void_p], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    initFunc: Callable[[c_void_p], None]
    stateFunc: Callable[[c_void_p], None]

class struct_state_machine_t(Structure):
    """
    ```python
    states: POINTER_T[struct_state_machine_state_t] (POINTER(struct_state_machine_state_t))
    counter: int (POINTER(I))
    userData: c_void_p (c_void_p)
    nrStates: int (POINTER(H))
    curState: int (POINTER(H))
    nextState: int (POINTER(H))
    gotoNextState: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    states: POINTER_T[struct_state_machine_state_t]
    counter: int
    userData: c_void_p
    nrStates: int
    curState: int
    nextState: int
    gotoNextState: int

class struct_struc_222(Structure):
    """
    ```python
    netDriverState: struct_rnet_driver_state_t_ (struct_rnet_driver_state_t_)
    field68: struct_struc_222_field_68_t_ (struct_struc_222_field_68_t_)
    status: int (POINTER(i))
    field84: int (POINTER(H))
    field86a: int (POINTER(B))
    place: int (POINTER(B))
    field87: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    netDriverState: struct_rnet_driver_state_t_
    field68: struct_struc_222_field_68_t_
    status: int
    field84: int
    field86a: int
    place: int
    field87: int

class struct_struc_222_field_68_t_(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    frameCounter: int (POINTER(I))
    fieldC: int (POINTER(H))
    fieldE: int (POINTER(H))
    field10: int (POINTER(I))
    field14: int (POINTER(H))
    gap16: list[int] (POINTER(B)[2])
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    frameCounter: int
    fieldC: int
    fieldE: int
    field10: int
    field14: int
    gap16: list[int]

class struct_struc_252(Structure):
    """
    ```python
    field0: int (POINTER(H))
    tp: int (POINTER(H))
    gap4: list[int] (POINTER(B)[2])
    flags: int (POINTER(B))
    mic: int (POINTER(B))
    field7: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    tp: int
    gap4: list[int]
    flags: int
    mic: int
    field7: int

class struct_struc_313_mepo(Structure):
    """
    ```python
    nextMepo: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    curMepo: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    direction: struct_VecFx32 (struct_VecFx32)
    areaMepo: POINTER_T[struct_mdat_mgenemypoint_t] (POINTER(struct_mdat_mgenemypoint_t))
    areaMepoValid: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    nextMepo: POINTER_T[struct_mdat_mgenemypoint_t]
    curMepo: POINTER_T[struct_mdat_mgenemypoint_t]
    direction: struct_VecFx32
    areaMepo: POINTER_T[struct_mdat_mgenemypoint_t]
    areaMepoValid: int

class struct_struc_316_epoi(Structure):
    """
    ```python
    nextEpoi: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    curEpoi: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    direction: struct_VecFx32 (struct_VecFx32)
    areaEpoi: POINTER_T[struct_mdat_enemypoint_t] (POINTER(struct_mdat_enemypoint_t))
    areaEpoiValid: int (POINTER(i))
    driverId: int (POINTER(H))
    field1E: int (POINTER(B))
    field1F: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    nextEpoi: POINTER_T[struct_mdat_enemypoint_t]
    curEpoi: POINTER_T[struct_mdat_enemypoint_t]
    direction: struct_VecFx32
    areaEpoi: POINTER_T[struct_mdat_enemypoint_t]
    areaEpoiValid: int
    driverId: int
    field1E: int
    field1F: int

class struct_struc_334(Structure):
    """
    ```python
    field0: int (POINTER(i))
    field4: int (POINTER(i))
    field8: int (POINTER(i))
    fieldC: int (POINTER(i))
    field10: int (POINTER(i))
    field14: int (POINTER(i))
    field18: int (POINTER(i))
    field1C: int (POINTER(i))
    field20: int (POINTER(i))
    field24: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    fieldC: int
    field10: int
    field14: int
    field18: int
    field1C: int
    field20: int
    field24: int

class struct_struc_351(Structure):
    """
    ```python
    posX: int (POINTER(h))
    posY: int (POINTER(h))
    posZ: int (POINTER(h))
    speed: int (POINTER(h))
    driftRotY: int (POINTER(h))
    yRot: int (POINTER(H))
    flags: int (POINTER(I))
    field514field48: int (POINTER(i))
    field514field44: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    posX: int
    posY: int
    posZ: int
    speed: int
    driftRotY: int
    yRot: int
    flags: int
    field514field48: int
    field514field44: int

class struct_struct_217AA00_field1E4C_entry_t(Structure):
    """
    ```python
    unk0: list[int] (POINTER(B)[6])
    field6: int (POINTER(H))
    ```
    """
    _pack_: ClassVar[int] = 1
    unk0: list[int]
    field6: int

class struct_struct_217AA00_field45C_t(Structure):
    """
    ```python
    nickName: list[int] (POINTER(H)[10])
    emblem: list[int] (POINTER(B)[512])
    hasEmblem: int (POINTER(B))
    PADDING_0: int (POINTER(B))
    field216: int (POINTER(H))
    exchangeToken: c_void_p (c_void_p)
    unlockBits: list[int] (POINTER(B)[4])
    field228: int (POINTER(B))
    _7: int (POINTER(B))
    field229: int (POINTER(B))
    field22A: int (POINTER(B))
    field22B: int (POINTER(B))
    ```
    """
    _pack_: ClassVar[int] = 1
    nickName: list[int]
    emblem: list[int]
    hasEmblem: int
    PADDING_0: int
    field216: int
    exchangeToken: c_void_p
    unlockBits: list[int]
    field228: int
    _7: int
    field229: int
    field22A: int
    field22B: int

class struct_struct_217AA00_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    field4: int (POINTER(I))
    field8: int (POINTER(I))
    unkC: list[int] (POINTER(B)[1062])
    field432: int (POINTER(H))
    field434: int (POINTER(H))
    field436: int (POINTER(H))
    field438: int (POINTER(B))
    field439: int (POINTER(B))
    field43A: int (POINTER(B))
    field43B: int (POINTER(B))
    field43C: int (POINTER(B))
    unk43D: list[int] (POINTER(B)[23])
    field454: int (POINTER(H))
    field456: int (POINTER(B))
    field457: int (POINTER(B))
    field458: int (POINTER(B))
    unk459: list[int] (POINTER(B)[3])
    field45C: list[struct_struct_217AA00_field45C_t] (struct_struct_217AA00_field45C_t[8])
    unk15BC: list[int] (POINTER(B)[12])
    field15C8: POINTER_T[struct_struc_252] (POINTER(struct_struc_252))
    unk15CC: list[int] (POINTER(B)[42])
    field15F6: int (POINTER(B))
    unk15F7: list[int] (POINTER(B)[2133])
    field1E4C: list[struct_struct_217AA00_field1E4C_entry_t] (struct_struct_217AA00_field1E4C_entry_t[8])
    field1E8C: list[int] (POINTER(H)[8])
    unk1E9C: list[int] (POINTER(B)[20])
    field1EB0: int (POINTER(I))
    unk1EB4: list[int] (POINTER(B)[52])
    field1EE8: struct_MATHRandContext32 (struct_MATHRandContext32)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    field4: int
    field8: int
    unkC: list[int]
    field432: int
    field434: int
    field436: int
    field438: int
    field439: int
    field43A: int
    field43B: int
    field43C: int
    unk43D: list[int]
    field454: int
    field456: int
    field457: int
    field458: int
    unk459: list[int]
    field45C: list[struct_struct_217AA00_field45C_t]
    unk15BC: list[int]
    field15C8: POINTER_T[struct_struc_252]
    unk15CC: list[int]
    field15F6: int
    unk15F7: list[int]
    field1E4C: list[struct_struct_217AA00_field1E4C_entry_t]
    field1E8C: list[int]
    unk1E9C: list[int]
    field1EB0: int
    unk1EB4: list[int]
    field1EE8: struct_MATHRandContext32

class struct_struct_217B488_driver_config_t(Structure):
    """
    ```python
    characterId: int (POINTER(I))
    kartId: int (POINTER(I))
    field8: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    characterId: int
    kartId: int
    field8: int

class struct_struct_217B488_t(Structure):
    """
    ```python
    titleMenuSkipIntro: int (POINTER(I))
    field4: int (POINTER(I))
    singlePlayerMenuTarget: int (POINTER(I))
    ghostReceive: int (POINTER(i))
    field10: int (POINTER(I))
    field14: int (POINTER(I))
    unk18: int (POINTER(I))
    field1C: int (POINTER(I))
    driverConfigs: list[struct_struct_217B488_driver_config_t] (struct_struct_217B488_driver_config_t[4])
    unk50: int (POINTER(I))
    field54: int (POINTER(B))
    PADDING_0: list[int] (POINTER(B)[3])
    field58: int (POINTER(I))
    playedCourses: list[int] (POINTER(I)[5])
    field70: int (POINTER(I))
    field74: int (POINTER(I))
    useDLResult: int (POINTER(i))
    playerGlobalRank: int (POINTER(i))
    gpRank: int (POINTER(I))
    cup: int (POINTER(I))
    ccMode: int (POINTER(I))
    mirrorMode: int (POINTER(I))
    playerCharacter: int (POINTER(I))
    playerKart: int (POINTER(I))
    courseTimes: list[struct_race_time_t] (struct_race_time_t[4])
    playerTotalRankPoints: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    driverCharacters: list[int] (POINTER(I)[8])
    driverKarts: list[int] (POINTER(I)[8])
    unkEC: list[int] (POINTER(B)[32])
    heyhoPaletteRows: list[int] (POINTER(I)[8])
    field12C: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    titleMenuSkipIntro: int
    field4: int
    singlePlayerMenuTarget: int
    ghostReceive: int
    field10: int
    field14: int
    unk18: int
    field1C: int
    driverConfigs: list[struct_struct_217B488_driver_config_t]
    unk50: int
    field54: int
    PADDING_0: list[int]
    field58: int
    playedCourses: list[int]
    field70: int
    field74: int
    useDLResult: int
    playerGlobalRank: int
    gpRank: int
    cup: int
    ccMode: int
    mirrorMode: int
    playerCharacter: int
    playerKart: int
    courseTimes: list[struct_race_time_t]
    playerTotalRankPoints: int
    PADDING_1: list[int]
    driverCharacters: list[int]
    driverKarts: list[int]
    unkEC: list[int]
    heyhoPaletteRows: list[int]
    field12C: int

class struct_sun_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fireSnakeSpawnCount: int (POINTER(I))
    fireSnakeSpawnRotY: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    waitCounter: int (POINTER(i))
    rotZA: int (POINTER(I))
    rotZB: int (POINTER(H))
    nsbcaFrame: int (POINTER(H))
    nsbcaAnimSpeed: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fireSnakeSpawnCount: int
    fireSnakeSpawnRotY: int
    PADDING_0: list[int]
    waitCounter: int
    rotZA: int
    rotZB: int
    nsbcaFrame: int
    nsbcaAnimSpeed: fx32
    pathwalker: struct_pw_pathwalker_t
    state: int

class struct_sysdat_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    language: int (POINTER(I))
    seqHandle: struct_seq_handle_t (struct_seq_handle_t)
    isSeqPlaying: int (POINTER(i))
    isSeqLoaded: int (POINTER(i))
    isMBChild: int (POINTER(i))
    useG3dFastDma: int (POINTER(i))
    PADDING_0: int (POINTER(I))
    overlayRelatedNum: int (POINTER(I))
    dtcmHeapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    field28: int (POINTER(h))
    nickName: list[int] (POINTER(H)[0])
    nickNameLength: int (POINTER(H))
    favoriteColor: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    activatedRaceMenuOption: int (POINTER(i))
    backLightTop: int (POINTER(I))
    backLightBottom: int (POINTER(I))
    field50: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    field54: int (POINTER(I))
    field58: int (POINTER(I))
    field5C: int (POINTER(I))
    PADDING_3: list[int] (POINTER(B)[4])
    random: struct_MATHRandContext32 (struct_MATHRandContext32)
    field78: int (POINTER(I))
    PADDING_4: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    language: int
    seqHandle: struct_seq_handle_t
    isSeqPlaying: int
    isSeqLoaded: int
    isMBChild: int
    useG3dFastDma: int
    PADDING_0: int
    overlayRelatedNum: int
    dtcmHeapHandle: POINTER_T[struct_NNSiFndHeapHead]
    field28: int
    nickName: list[int]
    nickNameLength: int
    favoriteColor: int
    PADDING_1: list[int]
    activatedRaceMenuOption: int
    backLightTop: int
    backLightBottom: int
    field50: int
    PADDING_2: list[int]
    field54: int
    field58: int
    field5C: int
    PADDING_3: list[int]
    random: struct_MATHRandContext32
    field78: int
    PADDING_4: list[int]

class struct_teresa_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: struct_VecFx32 (struct_VecFx32)
    alpha: int (POINTER(H))
    nsbtpFrame: int (POINTER(H))
    flip: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    state1Counter: int (POINTER(i))
    fieldB8: int (POINTER(i))
    fieldBC: struct_sinthing_t (struct_sinthing_t)
    fieldDC: struct_sinthing_t (struct_sinthing_t)
    fieldFC: struct_idk_struct2_t (struct_idk_struct2_t)
    field10C: int (POINTER(I))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: struct_VecFx32
    alpha: int
    nsbtpFrame: int
    flip: int
    PADDING_0: list[int]
    state1Counter: int
    fieldB8: int
    fieldBC: struct_sinthing_t
    fieldDC: struct_sinthing_t
    fieldFC: struct_idk_struct2_t
    field10C: int
    state: int

class struct_title_state_t(Structure):
    """
    ```python
    stateMachine: struct_ssm_t (struct_ssm_t)
    states: list[struct_ssm_state_t] (struct_ssm_state_t[7])
    inactivityCounter: int (POINTER(i))
    introFinished: int (POINTER(I))
    selectedButton: int (POINTER(I))
    selectedBeforeActivation: int (POINTER(i))
    bottomRowLeftRight: int (POINTER(I))
    outEffectOffset: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    introFrame: int (POINTER(I))
    layoutElements: POINTER_T[struct_jnui_layout_element_t] (POINTER(struct_jnui_layout_element_t))
    layoutBncl: POINTER_T[struct_jnui_bncl_res_t] (POINTER(struct_jnui_bncl_res_t))
    layoutBnbl: POINTER_T[struct_jnui_bnbl_res_t] (POINTER(struct_jnui_bnbl_res_t))
    layoutBnll: POINTER_T[struct_jnui_bnll_res_t] (POINTER(struct_jnui_bnll_res_t))
    mainPalette: POINTER_T[struct_NNSG2dPaletteData] (POINTER(struct_NNSG2dPaletteData))
    mainBgData: POINTER_T[struct_NNSG2dCharacterData] (POINTER(struct_NNSG2dCharacterData))
    subPalette: POINTER_T[struct_NNSG2dPaletteData] (POINTER(struct_NNSG2dPaletteData))
    subBgData: POINTER_T[struct_NNSG2dCharacterData] (POINTER(struct_NNSG2dCharacterData))
    mainScreenData: POINTER_T[struct_NNSG2dScreenData] (POINTER(struct_NNSG2dScreenData))
    mainScreenData2: POINTER_T[struct_NNSG2dScreenData] (POINTER(struct_NNSG2dScreenData))
    subScreenData: POINTER_T[struct_NNSG2dScreenData] (POINTER(struct_NNSG2dScreenData))
    padding: list[int] (POINTER(B)[12])
    subObjPalette: POINTER_T[struct_NNSG2dPaletteData] (POINTER(struct_NNSG2dPaletteData))
    subObjCharacterData: POINTER_T[struct_NNSG2dCharacterData] (POINTER(struct_NNSG2dCharacterData))
    cellDataBank: POINTER_T[struct_NNSG2dCellDataBank] (POINTER(struct_NNSG2dCellDataBank))
    padding2: int (POINTER(I))
    mainOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    subOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    field8B8: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    stateMachine: struct_ssm_t
    states: list[struct_ssm_state_t]
    inactivityCounter: int
    introFinished: int
    selectedButton: int
    selectedBeforeActivation: int
    bottomRowLeftRight: int
    outEffectOffset: int
    PADDING_0: list[int]
    introFrame: int
    layoutElements: POINTER_T[struct_jnui_layout_element_t]
    layoutBncl: POINTER_T[struct_jnui_bncl_res_t]
    layoutBnbl: POINTER_T[struct_jnui_bnbl_res_t]
    layoutBnll: POINTER_T[struct_jnui_bnll_res_t]
    mainPalette: POINTER_T[struct_NNSG2dPaletteData]
    mainBgData: POINTER_T[struct_NNSG2dCharacterData]
    subPalette: POINTER_T[struct_NNSG2dPaletteData]
    subBgData: POINTER_T[struct_NNSG2dCharacterData]
    mainScreenData: POINTER_T[struct_NNSG2dScreenData]
    mainScreenData2: POINTER_T[struct_NNSG2dScreenData]
    subScreenData: POINTER_T[struct_NNSG2dScreenData]
    padding: list[int]
    subObjPalette: POINTER_T[struct_NNSG2dPaletteData]
    subObjCharacterData: POINTER_T[struct_NNSG2dCharacterData]
    cellDataBank: POINTER_T[struct_NNSG2dCellDataBank]
    padding2: int
    mainOamBuf: struct_oam_buf_t
    subOamBuf: struct_oam_buf_t
    field8B8: int

class struct_townmonte_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbtpFrame: int (POINTER(H))
    sfxId: int (POINTER(H))
    fieldA4: struct_idk_struct_t (struct_idk_struct_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbtpFrame: int
    sfxId: int
    fieldA4: struct_idk_struct_t

class struct_traffic_params_t(Structure):
    """
    ```python
    field0: fx32 (struct_fx32)
    field4: fx32 (struct_fx32)
    field8: fx32 (struct_fx32)
    fieldC: fx32 (struct_fx32)
    field10: fx32 (struct_fx32)
    field14: fx32 (struct_fx32)
    field18: fx32 (struct_fx32)
    field1C: fx32 (struct_fx32)
    model: POINTER_T[POINTER_T[struct_model_t]] (POINTER(POINTER(struct_model_t)))
    shadowModel: POINTER_T[POINTER_T[struct_shadowmodel_t]] (POINTER(POINTER(struct_shadowmodel_t)))
    nsbtpAnim: POINTER_T[POINTER_T[struct_anim_manager_t]] (POINTER(POINTER(struct_anim_manager_t)))
    field2C: int (POINTER(I))
    field30: int (POINTER(I))
    field34: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: fx32
    field4: fx32
    field8: fx32
    fieldC: fx32
    field10: fx32
    field14: fx32
    field18: fx32
    field1C: fx32
    model: POINTER_T[POINTER_T[struct_model_t]]
    shadowModel: POINTER_T[POINTER_T[struct_shadowmodel_t]]
    nsbtpAnim: POINTER_T[POINTER_T[struct_anim_manager_t]]
    field2C: int
    field30: int
    field34: c_void_p

class struct_traffic_renderpart_t(Structure):
    """
    ```python
    renderPart: struct_mobj_render_part_t (struct_mobj_render_part_t)
    playerIpatDir: struct_VecFx32 (struct_VecFx32)
    updateIpatCulling: int (POINTER(i))
    performIpatCulling: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    renderPart: struct_mobj_render_part_t
    playerIpatDir: struct_VecFx32
    updateIpatCulling: int
    performIpatCulling: int

class struct_traffic_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(i))
    fieldA4: quaternion_t (struct_quaternion_t)
    fieldB4: quaternion_t (struct_quaternion_t)
    fieldC4: quaternion_t (struct_quaternion_t)
    fieldD4: int (POINTER(i))
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    initialPoint: int (POINTER(h))
    fieldFE: int (POINTER(h))
    field100: fx32 (struct_fx32)
    field104: fx32 (struct_fx32)
    field108: fx32 (struct_fx32)
    field10C: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field110: fx32 (struct_fx32)
    field114: fx32 (struct_fx32)
    field118: fx32 (struct_fx32)
    field11C: fx32 (struct_fx32)
    field120: fx32 (struct_fx32)
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    shadowModel: POINTER_T[struct_shadowmodel_t] (POINTER(struct_shadowmodel_t))
    nsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtpFrame: int (POINTER(H))
    light: struct_light_t (struct_light_t)
    field144: struct_VecFx32 (struct_VecFx32)
    field150: int (POINTER(H))
    field152: int (POINTER(H))
    params: POINTER_T[struct_traffic_params_t] (POINTER(struct_traffic_params_t))
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t] (POINTER(struct_sfx_emitter_ex_params_t))
    field15C: int (POINTER(i))
    field160: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    fieldA4: quaternion_t
    fieldB4: quaternion_t
    fieldC4: quaternion_t
    fieldD4: int
    pathWalker: struct_pw_pathwalker_t
    initialPoint: int
    fieldFE: int
    field100: fx32
    field104: fx32
    field108: fx32
    field10C: int
    PADDING_0: list[int]
    field110: fx32
    field114: fx32
    field118: fx32
    field11C: fx32
    field120: fx32
    model: POINTER_T[struct_model_t]
    shadowModel: POINTER_T[struct_shadowmodel_t]
    nsbtpAnim: POINTER_T[struct_anim_manager_t]
    nsbtpFrame: int
    light: struct_light_t
    field144: struct_VecFx32
    field150: int
    field152: int
    params: POINTER_T[struct_traffic_params_t]
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t]
    field15C: int
    field160: int

class struct_trl_point_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    size: fx32 (struct_fx32)
    age: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    position: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    size: fx32
    age: int
    PADDING_0: list[int]
    position: struct_VecFx32

class struct_trl_state_t(Structure):
    """
    ```python
    activeTrailList: struct_NNSFndList (struct_NNSFndList)
    freeTrailList: struct_NNSFndList (struct_NNSFndList)
    freePointList: struct_NNSFndList (struct_NNSFndList)
    texture: struct_model_res_t (struct_model_res_t)
    polygonAttr: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    activeTrailList: struct_NNSFndList
    freeTrailList: struct_NNSFndList
    freePointList: struct_NNSFndList
    texture: struct_model_res_t
    polygonAttr: int

class struct_trl_texparams_t(Structure):
    """
    ```python
    texImageParam: int (POINTER(I))
    field4: list[int] (POINTER(B)[20])
    plttAddress: int (POINTER(I))
    width: fx32 (struct_fx32)
    height: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    texImageParam: int
    field4: list[int]
    plttAddress: int
    width: fx32
    height: fx32

class struct_trl_trail_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    pointList: struct_NNSFndList (struct_NNSFndList)
    targetPosition: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    shouldDie: int (POINTER(i))
    initialPointSize: fx32 (struct_fx32)
    driverId: int (POINTER(I))
    driverOffset: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    pointList: struct_NNSFndList
    targetPosition: POINTER_T[struct_VecFx32]
    shouldDie: int
    initialPointSize: fx32
    driverId: int
    driverOffset: struct_VecFx32

class struct_trophy_t(Structure):
    """
    ```python
    trophyId: int (POINTER(H))
    trophyRank: int (POINTER(H))
    rotY: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    rotZ: struct_sinthing_t (struct_sinthing_t)
    trophyModel: struct_model_t (struct_model_t)
    trophyNsbtpAnim: struct_anim_manager_t (struct_anim_manager_t)
    identity: union_MtxFx43 (union_MtxFx43)
    light0DirX: fx16 (struct_fx16)
    light1DirX: fx16 (struct_fx16)
    light0DirY: fx16 (struct_fx16)
    light1DirY: fx16 (struct_fx16)
    light0DirZ: fx16 (struct_fx16)
    light1DirZ: fx16 (struct_fx16)
    sparkleEmitterPos: struct_VecFx32 (struct_VecFx32)
    sparkleEmitterRadius: fx32 (struct_fx32)
    sparkleEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    goldConfettiEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    silverConfettiEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    trophyId: int
    trophyRank: int
    rotY: int
    PADDING_0: list[int]
    rotZ: struct_sinthing_t
    trophyModel: struct_model_t
    trophyNsbtpAnim: struct_anim_manager_t
    identity: union_MtxFx43
    light0DirX: fx16
    light1DirX: fx16
    light0DirY: fx16
    light1DirY: fx16
    light0DirZ: fx16
    light1DirZ: fx16
    sparkleEmitterPos: struct_VecFx32
    sparkleEmitterRadius: fx32
    sparkleEmitter: POINTER_T[struct_spa_emitter_t]
    goldConfettiEmitter: POINTER_T[struct_spa_emitter_t]
    silverConfettiEmitter: POINTER_T[struct_spa_emitter_t]

class struct_vec2_t(Structure):
    """
    ```python
    x: fx32 (struct_fx32)
    y: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx32
    y: fx32

class struct_vec2i_t(Structure):
    """
    ```python
    x: int (POINTER(i))
    y: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: int
    y: int

class struct_vram_wvr_stat_t(Structure):
    """
    ```python
    status: int (POINTER(I))
    callbackFunc: Callable[[int], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    status: int
    callbackFunc: Callable[[int], None]

class struct_water_splash_state_t(Structure):
    """
    ```python
    splashY: fx32 (struct_fx32)
    nsbmd: c_void_p (c_void_p)
    nsbca: c_void_p (c_void_p)
    nsbma: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    splashY: fx32
    nsbmd: c_void_p
    nsbca: c_void_p
    nsbma: c_void_p

class struct_water_splash_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class struct_water_state_t(Structure):
    """
    ```python
    waterAPosition: struct_VecFx32 (struct_VecFx32)
    waterCPosition: struct_VecFx32 (struct_VecFx32)
    basePosition: struct_VecFx32 (struct_VecFx32)
    state: int (POINTER(I))
    tideAmplitude: fx32 (struct_fx32)
    tidePhase: int (POINTER(H))
    tideSpeed: int (POINTER(H))
    tideProgress: fx32 (struct_fx32)
    field34: int (POINTER(H))
    field36: int (POINTER(H))
    field38: int (POINTER(H))
    field3A: int (POINTER(H))
    waterMovePhase: int (POINTER(H))
    field3E: int (POINTER(H))
    waterMoveSpeed: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    waterAMoveDistance: fx32 (struct_fx32)
    waterCMoveDistance: fx32 (struct_fx32)
    field4C: fx32 (struct_fx32)
    waterCMovePhaseDifference: int (POINTER(H))
    field52: int (POINTER(H))
    waterAFirst: int (POINTER(i))
    waterAAlpha: int (POINTER(H))
    waterCAlpha: int (POINTER(H))
    field5C: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    waterANsbmd: c_void_p (c_void_p)
    waterCNsbmd: c_void_p (c_void_p)
    waterAModel: struct_model_t (struct_model_t)
    waterCModel: struct_model_t (struct_model_t)
    transformMtx: union_MtxFx43 (union_MtxFx43)
    isDiveable: int (POINTER(i))
    waterEfctNsbmd: c_void_p (c_void_p)
    waterEfctNsbca: c_void_p (c_void_p)
    waterEfctNsbma: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    waterAPosition: struct_VecFx32
    waterCPosition: struct_VecFx32
    basePosition: struct_VecFx32
    state: int
    tideAmplitude: fx32
    tidePhase: int
    tideSpeed: int
    tideProgress: fx32
    field34: int
    field36: int
    field38: int
    field3A: int
    waterMovePhase: int
    field3E: int
    waterMoveSpeed: int
    PADDING_0: list[int]
    waterAMoveDistance: fx32
    waterCMoveDistance: fx32
    field4C: fx32
    waterCMovePhaseDifference: int
    field52: int
    waterAFirst: int
    waterAAlpha: int
    waterCAlpha: int
    field5C: int
    PADDING_1: list[int]
    waterANsbmd: c_void_p
    waterCNsbmd: c_void_p
    waterAModel: struct_model_t
    waterCModel: struct_model_t
    transformMtx: union_MtxFx43
    isDiveable: int
    waterEfctNsbmd: c_void_p
    waterEfctNsbca: c_void_p
    waterEfctNsbma: c_void_p

class struct_water_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class struct_wbox_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: struct_VecFx32 (struct_VecFx32)
    fieldAC: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fieldB0: struct_VecFx32 (struct_VecFx32)
    floorNormal: struct_VecFx32 (struct_VecFx32)
    rotY: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    fieldCC: struct_VecFx32 (struct_VecFx32)
    fieldD8: struct_VecFx32 (struct_VecFx32)
    fieldE4: struct_VecFx32 (struct_VecFx32)
    fieldF0: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    fieldF4: struct_VecFx32 (struct_VecFx32)
    field100: struct_VecFx32 (struct_VecFx32)
    field10C: int (POINTER(H))
    field10E: int (POINTER(H))
    field110: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    shadow: struct_objshadow_t (struct_objshadow_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: struct_VecFx32
    fieldAC: int
    PADDING_0: list[int]
    fieldB0: struct_VecFx32
    floorNormal: struct_VecFx32
    rotY: int
    PADDING_1: list[int]
    fieldCC: struct_VecFx32
    fieldD8: struct_VecFx32
    fieldE4: struct_VecFx32
    fieldF0: int
    PADDING_2: list[int]
    fieldF4: struct_VecFx32
    field100: struct_VecFx32
    field10C: int
    field10E: int
    field110: int
    PADDING_3: list[int]
    shadow: struct_objshadow_t

class sun_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fireSnakeSpawnCount: int (POINTER(I))
    fireSnakeSpawnRotY: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    waitCounter: int (POINTER(i))
    rotZA: int (POINTER(I))
    rotZB: int (POINTER(H))
    nsbcaFrame: int (POINTER(H))
    nsbcaAnimSpeed: fx32 (struct_fx32)
    pathwalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fireSnakeSpawnCount: int
    fireSnakeSpawnRotY: int
    PADDING_0: list[int]
    waitCounter: int
    rotZA: int
    rotZB: int
    nsbcaFrame: int
    nsbcaAnimSpeed: fx32
    pathwalker: struct_pw_pathwalker_t
    state: int

class sysdat_t(Structure):
    """
    ```python
    field0: int (POINTER(I))
    language: int (POINTER(I))
    seqHandle: struct_seq_handle_t (struct_seq_handle_t)
    isSeqPlaying: int (POINTER(i))
    isSeqLoaded: int (POINTER(i))
    isMBChild: int (POINTER(i))
    useG3dFastDma: int (POINTER(i))
    PADDING_0: int (POINTER(I))
    overlayRelatedNum: int (POINTER(I))
    dtcmHeapHandle: POINTER_T[struct_NNSiFndHeapHead] (POINTER(struct_NNSiFndHeapHead))
    field28: int (POINTER(h))
    nickName: list[int] (POINTER(H)[0])
    nickNameLength: int (POINTER(H))
    favoriteColor: int (POINTER(B))
    PADDING_1: list[int] (POINTER(B)[3])
    activatedRaceMenuOption: int (POINTER(i))
    backLightTop: int (POINTER(I))
    backLightBottom: int (POINTER(I))
    field50: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    field54: int (POINTER(I))
    field58: int (POINTER(I))
    field5C: int (POINTER(I))
    PADDING_3: list[int] (POINTER(B)[4])
    random: struct_MATHRandContext32 (struct_MATHRandContext32)
    field78: int (POINTER(I))
    PADDING_4: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: int
    language: int
    seqHandle: struct_seq_handle_t
    isSeqPlaying: int
    isSeqLoaded: int
    isMBChild: int
    useG3dFastDma: int
    PADDING_0: int
    overlayRelatedNum: int
    dtcmHeapHandle: POINTER_T[struct_NNSiFndHeapHead]
    field28: int
    nickName: list[int]
    nickNameLength: int
    favoriteColor: int
    PADDING_1: list[int]
    activatedRaceMenuOption: int
    backLightTop: int
    backLightBottom: int
    field50: int
    PADDING_2: list[int]
    field54: int
    field58: int
    field5C: int
    PADDING_3: list[int]
    random: struct_MATHRandContext32
    field78: int
    PADDING_4: list[int]

class teresa_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: struct_VecFx32 (struct_VecFx32)
    alpha: int (POINTER(H))
    nsbtpFrame: int (POINTER(H))
    flip: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    state1Counter: int (POINTER(i))
    fieldB8: int (POINTER(i))
    fieldBC: struct_sinthing_t (struct_sinthing_t)
    fieldDC: struct_sinthing_t (struct_sinthing_t)
    fieldFC: struct_idk_struct2_t (struct_idk_struct2_t)
    field10C: int (POINTER(I))
    state: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: struct_VecFx32
    alpha: int
    nsbtpFrame: int
    flip: int
    PADDING_0: list[int]
    state1Counter: int
    fieldB8: int
    fieldBC: struct_sinthing_t
    fieldDC: struct_sinthing_t
    fieldFC: struct_idk_struct2_t
    field10C: int
    state: int

class title_state_t(Structure):
    """
    ```python
    stateMachine: struct_ssm_t (struct_ssm_t)
    states: list[struct_ssm_state_t] (struct_ssm_state_t[7])
    inactivityCounter: int (POINTER(i))
    introFinished: int (POINTER(I))
    selectedButton: int (POINTER(I))
    selectedBeforeActivation: int (POINTER(i))
    bottomRowLeftRight: int (POINTER(I))
    outEffectOffset: int (POINTER(h))
    PADDING_0: list[int] (POINTER(B)[2])
    introFrame: int (POINTER(I))
    layoutElements: POINTER_T[struct_jnui_layout_element_t] (POINTER(struct_jnui_layout_element_t))
    layoutBncl: POINTER_T[struct_jnui_bncl_res_t] (POINTER(struct_jnui_bncl_res_t))
    layoutBnbl: POINTER_T[struct_jnui_bnbl_res_t] (POINTER(struct_jnui_bnbl_res_t))
    layoutBnll: POINTER_T[struct_jnui_bnll_res_t] (POINTER(struct_jnui_bnll_res_t))
    mainPalette: POINTER_T[struct_NNSG2dPaletteData] (POINTER(struct_NNSG2dPaletteData))
    mainBgData: POINTER_T[struct_NNSG2dCharacterData] (POINTER(struct_NNSG2dCharacterData))
    subPalette: POINTER_T[struct_NNSG2dPaletteData] (POINTER(struct_NNSG2dPaletteData))
    subBgData: POINTER_T[struct_NNSG2dCharacterData] (POINTER(struct_NNSG2dCharacterData))
    mainScreenData: POINTER_T[struct_NNSG2dScreenData] (POINTER(struct_NNSG2dScreenData))
    mainScreenData2: POINTER_T[struct_NNSG2dScreenData] (POINTER(struct_NNSG2dScreenData))
    subScreenData: POINTER_T[struct_NNSG2dScreenData] (POINTER(struct_NNSG2dScreenData))
    padding: list[int] (POINTER(B)[12])
    subObjPalette: POINTER_T[struct_NNSG2dPaletteData] (POINTER(struct_NNSG2dPaletteData))
    subObjCharacterData: POINTER_T[struct_NNSG2dCharacterData] (POINTER(struct_NNSG2dCharacterData))
    cellDataBank: POINTER_T[struct_NNSG2dCellDataBank] (POINTER(struct_NNSG2dCellDataBank))
    padding2: int (POINTER(I))
    mainOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    subOamBuf: struct_oam_buf_t (struct_oam_buf_t)
    field8B8: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    stateMachine: struct_ssm_t
    states: list[struct_ssm_state_t]
    inactivityCounter: int
    introFinished: int
    selectedButton: int
    selectedBeforeActivation: int
    bottomRowLeftRight: int
    outEffectOffset: int
    PADDING_0: list[int]
    introFrame: int
    layoutElements: POINTER_T[struct_jnui_layout_element_t]
    layoutBncl: POINTER_T[struct_jnui_bncl_res_t]
    layoutBnbl: POINTER_T[struct_jnui_bnbl_res_t]
    layoutBnll: POINTER_T[struct_jnui_bnll_res_t]
    mainPalette: POINTER_T[struct_NNSG2dPaletteData]
    mainBgData: POINTER_T[struct_NNSG2dCharacterData]
    subPalette: POINTER_T[struct_NNSG2dPaletteData]
    subBgData: POINTER_T[struct_NNSG2dCharacterData]
    mainScreenData: POINTER_T[struct_NNSG2dScreenData]
    mainScreenData2: POINTER_T[struct_NNSG2dScreenData]
    subScreenData: POINTER_T[struct_NNSG2dScreenData]
    padding: list[int]
    subObjPalette: POINTER_T[struct_NNSG2dPaletteData]
    subObjCharacterData: POINTER_T[struct_NNSG2dCharacterData]
    cellDataBank: POINTER_T[struct_NNSG2dCellDataBank]
    padding2: int
    mainOamBuf: struct_oam_buf_t
    subOamBuf: struct_oam_buf_t
    field8B8: int

class townmonte_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    nsbtpFrame: int (POINTER(H))
    sfxId: int (POINTER(H))
    fieldA4: struct_idk_struct_t (struct_idk_struct_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    nsbtpFrame: int
    sfxId: int
    fieldA4: struct_idk_struct_t

class traffic_params_t(Structure):
    """
    ```python
    field0: fx32 (struct_fx32)
    field4: fx32 (struct_fx32)
    field8: fx32 (struct_fx32)
    fieldC: fx32 (struct_fx32)
    field10: fx32 (struct_fx32)
    field14: fx32 (struct_fx32)
    field18: fx32 (struct_fx32)
    field1C: fx32 (struct_fx32)
    model: POINTER_T[POINTER_T[struct_model_t]] (POINTER(POINTER(struct_model_t)))
    shadowModel: POINTER_T[POINTER_T[struct_shadowmodel_t]] (POINTER(POINTER(struct_shadowmodel_t)))
    nsbtpAnim: POINTER_T[POINTER_T[struct_anim_manager_t]] (POINTER(POINTER(struct_anim_manager_t)))
    field2C: int (POINTER(I))
    field30: int (POINTER(I))
    field34: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    field0: fx32
    field4: fx32
    field8: fx32
    fieldC: fx32
    field10: fx32
    field14: fx32
    field18: fx32
    field1C: fx32
    model: POINTER_T[POINTER_T[struct_model_t]]
    shadowModel: POINTER_T[POINTER_T[struct_shadowmodel_t]]
    nsbtpAnim: POINTER_T[POINTER_T[struct_anim_manager_t]]
    field2C: int
    field30: int
    field34: c_void_p

class traffic_renderpart_t(Structure):
    """
    ```python
    renderPart: struct_mobj_render_part_t (struct_mobj_render_part_t)
    playerIpatDir: struct_VecFx32 (struct_VecFx32)
    updateIpatCulling: int (POINTER(i))
    performIpatCulling: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    renderPart: struct_mobj_render_part_t
    playerIpatDir: struct_VecFx32
    updateIpatCulling: int
    performIpatCulling: int

class traffic_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: int (POINTER(i))
    fieldA4: quaternion_t (struct_quaternion_t)
    fieldB4: quaternion_t (struct_quaternion_t)
    fieldC4: quaternion_t (struct_quaternion_t)
    fieldD4: int (POINTER(i))
    pathWalker: struct_pw_pathwalker_t (struct_pw_pathwalker_t)
    initialPoint: int (POINTER(h))
    fieldFE: int (POINTER(h))
    field100: fx32 (struct_fx32)
    field104: fx32 (struct_fx32)
    field108: fx32 (struct_fx32)
    field10C: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    field110: fx32 (struct_fx32)
    field114: fx32 (struct_fx32)
    field118: fx32 (struct_fx32)
    field11C: fx32 (struct_fx32)
    field120: fx32 (struct_fx32)
    model: POINTER_T[struct_model_t] (POINTER(struct_model_t))
    shadowModel: POINTER_T[struct_shadowmodel_t] (POINTER(struct_shadowmodel_t))
    nsbtpAnim: POINTER_T[struct_anim_manager_t] (POINTER(struct_anim_manager_t))
    nsbtpFrame: int (POINTER(H))
    light: struct_light_t (struct_light_t)
    field144: struct_VecFx32 (struct_VecFx32)
    field150: int (POINTER(H))
    field152: int (POINTER(H))
    params: POINTER_T[struct_traffic_params_t] (POINTER(struct_traffic_params_t))
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t] (POINTER(struct_sfx_emitter_ex_params_t))
    field15C: int (POINTER(i))
    field160: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: int
    fieldA4: quaternion_t
    fieldB4: quaternion_t
    fieldC4: quaternion_t
    fieldD4: int
    pathWalker: struct_pw_pathwalker_t
    initialPoint: int
    fieldFE: int
    field100: fx32
    field104: fx32
    field108: fx32
    field10C: int
    PADDING_0: list[int]
    field110: fx32
    field114: fx32
    field118: fx32
    field11C: fx32
    field120: fx32
    model: POINTER_T[struct_model_t]
    shadowModel: POINTER_T[struct_shadowmodel_t]
    nsbtpAnim: POINTER_T[struct_anim_manager_t]
    nsbtpFrame: int
    light: struct_light_t
    field144: struct_VecFx32
    field150: int
    field152: int
    params: POINTER_T[struct_traffic_params_t]
    sfxEmitterExParams: POINTER_T[struct_sfx_emitter_ex_params_t]
    field15C: int
    field160: int

class trl_point_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    size: fx32 (struct_fx32)
    age: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    position: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    size: fx32
    age: int
    PADDING_0: list[int]
    position: struct_VecFx32

class trl_state_t(Structure):
    """
    ```python
    activeTrailList: struct_NNSFndList (struct_NNSFndList)
    freeTrailList: struct_NNSFndList (struct_NNSFndList)
    freePointList: struct_NNSFndList (struct_NNSFndList)
    texture: struct_model_res_t (struct_model_res_t)
    polygonAttr: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    activeTrailList: struct_NNSFndList
    freeTrailList: struct_NNSFndList
    freePointList: struct_NNSFndList
    texture: struct_model_res_t
    polygonAttr: int

class trl_texparams_t(Structure):
    """
    ```python
    texImageParam: int (POINTER(I))
    field4: list[int] (POINTER(B)[20])
    plttAddress: int (POINTER(I))
    width: fx32 (struct_fx32)
    height: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    texImageParam: int
    field4: list[int]
    plttAddress: int
    width: fx32
    height: fx32

class trl_trail_t(Structure):
    """
    ```python
    link: struct_NNSFndLink (struct_NNSFndLink)
    pointList: struct_NNSFndList (struct_NNSFndList)
    targetPosition: POINTER_T[struct_VecFx32] (POINTER(struct_VecFx32))
    shouldDie: int (POINTER(i))
    initialPointSize: fx32 (struct_fx32)
    driverId: int (POINTER(I))
    driverOffset: struct_VecFx32 (struct_VecFx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    link: struct_NNSFndLink
    pointList: struct_NNSFndList
    targetPosition: POINTER_T[struct_VecFx32]
    shouldDie: int
    initialPointSize: fx32
    driverId: int
    driverOffset: struct_VecFx32

class trophy_t(Structure):
    """
    ```python
    trophyId: int (POINTER(H))
    trophyRank: int (POINTER(H))
    rotY: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    rotZ: struct_sinthing_t (struct_sinthing_t)
    trophyModel: struct_model_t (struct_model_t)
    trophyNsbtpAnim: struct_anim_manager_t (struct_anim_manager_t)
    identity: union_MtxFx43 (union_MtxFx43)
    light0DirX: fx16 (struct_fx16)
    light1DirX: fx16 (struct_fx16)
    light0DirY: fx16 (struct_fx16)
    light1DirY: fx16 (struct_fx16)
    light0DirZ: fx16 (struct_fx16)
    light1DirZ: fx16 (struct_fx16)
    sparkleEmitterPos: struct_VecFx32 (struct_VecFx32)
    sparkleEmitterRadius: fx32 (struct_fx32)
    sparkleEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    goldConfettiEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    silverConfettiEmitter: POINTER_T[struct_spa_emitter_t] (POINTER(struct_spa_emitter_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    trophyId: int
    trophyRank: int
    rotY: int
    PADDING_0: list[int]
    rotZ: struct_sinthing_t
    trophyModel: struct_model_t
    trophyNsbtpAnim: struct_anim_manager_t
    identity: union_MtxFx43
    light0DirX: fx16
    light1DirX: fx16
    light0DirY: fx16
    light1DirY: fx16
    light0DirZ: fx16
    light1DirZ: fx16
    sparkleEmitterPos: struct_VecFx32
    sparkleEmitterRadius: fx32
    sparkleEmitter: POINTER_T[struct_spa_emitter_t]
    goldConfettiEmitter: POINTER_T[struct_spa_emitter_t]
    silverConfettiEmitter: POINTER_T[struct_spa_emitter_t]

class union_FSArchive_name(Union):
    """
    ```python
    ptr: list[int] (POINTER(B)[4])
    pack: int (POINTER(I))
    ```
    """
    _pack_: ClassVar[int] = 1
    ptr: list[int]
    pack: int

class union_FSDirEntry_0(Union):
    """
    ```python
    file_id: struct_FSFileID (struct_FSFileID)
    dir_id: struct_FSDirPos (struct_FSDirPos)
    ```
    """
    _pack_: ClassVar[int] = 1
    file_id: struct_FSFileID
    dir_id: struct_FSDirPos

class union_FSFile_arg(Union):
    """
    ```python
    readfile: struct_FSReadFileInfo (struct_FSReadFileInfo)
    writefile: struct_FSWriteFileInfo (struct_FSWriteFileInfo)
    seekdir: struct_FSSeekDirInfo (struct_FSSeekDirInfo)
    readdir: struct_FSReadDirInfo (struct_FSReadDirInfo)
    findpath: struct_FSFindPathInfo (struct_FSFindPathInfo)
    getpath: struct_FSGetPathInfo (struct_FSGetPathInfo)
    openfilefast: struct_FSOpenFileFastInfo (struct_FSOpenFileFastInfo)
    openfiledirect: struct_FSOpenFileDirectInfo (struct_FSOpenFileDirectInfo)
    closefile: struct_FSCloseFileInfo (struct_FSCloseFileInfo)
    PADDING_0: list[int] (POINTER(B)[20])
    ```
    """
    _pack_: ClassVar[int] = 1
    readfile: struct_FSReadFileInfo
    writefile: struct_FSWriteFileInfo
    seekdir: struct_FSSeekDirInfo
    readdir: struct_FSReadDirInfo
    findpath: struct_FSFindPathInfo
    getpath: struct_FSGetPathInfo
    openfilefast: struct_FSOpenFileFastInfo
    openfiledirect: struct_FSOpenFileDirectInfo
    closefile: struct_FSCloseFileInfo
    PADDING_0: list[int]

class union_FSFile_prop(Union):
    """
    ```python
    file: struct_FSFile_0_file (struct_FSFile_0_file)
    dir: struct_FSFile_0_dir (struct_FSFile_0_dir)
    ```
    """
    _pack_: ClassVar[int] = 1
    file: struct_FSFile_0_file
    dir: struct_FSFile_0_dir

class union_FSFindPathInfo_result(Union):
    """
    ```python
    file: POINTER_T[struct_FSFileID] (POINTER(struct_FSFileID))
    dir: POINTER_T[struct_FSDirPos] (POINTER(struct_FSDirPos))
    ```
    """
    _pack_: ClassVar[int] = 1
    file: POINTER_T[struct_FSFileID]
    dir: POINTER_T[struct_FSDirPos]

class union_GXOamAttr_0(Union):
    """
    ```python
    attr01: int (POINTER(I))
    _0: struct_GXOamAttr_0_0 (struct_GXOamAttr_0_0)
    _1: struct_GXOamAttr_0_1 (struct_GXOamAttr_0_1)
    _2: struct_GXOamAttr_0_2 (struct_GXOamAttr_0_2)
    ```
    """
    _pack_: ClassVar[int] = 1
    attr01: int
    _0: struct_GXOamAttr_0_0
    _1: struct_GXOamAttr_0_1
    _2: struct_GXOamAttr_0_2

class union_GXOamAttr_1(Union):
    """
    ```python
    _0: struct_GXOamAttr_1_0 (struct_GXOamAttr_1_0)
    attr23: int (POINTER(I))
    _1: struct_GXOamAttr_1_1 (struct_GXOamAttr_1_1)
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_GXOamAttr_1_0
    attr23: int
    _1: struct_GXOamAttr_1_1

class union_MtxFx22(Union):
    """
    ```python
    _0: struct_MtxFx22_0 (struct_MtxFx22_0)
    m: list[fx32] (struct_fx32[2][2])
    a: list[fx32] (struct_fx32[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_MtxFx22_0
    m: list[fx32]
    a: list[fx32]

class union_MtxFx33(Union):
    """
    ```python
    _0: struct_MtxFx33_0 (struct_MtxFx33_0)
    m: list[fx32] (struct_fx32[3][3])
    a: list[fx32] (struct_fx32[9])
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_MtxFx33_0
    m: list[fx32]
    a: list[fx32]

class union_MtxFx43(Union):
    """
    ```python
    _0: struct_MtxFx43_0 (struct_MtxFx43_0)
    m: list[fx32] (struct_fx32[3][4])
    a: list[fx32] (struct_fx32[12])
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_MtxFx43_0
    m: list[fx32]
    a: list[fx32]

class union_NNSG3dResDataBlockHeader__0(Union):
    """
    ```python
    kind: int (POINTER(I))
    chr: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    kind: int
    chr: list[int]

class union__mbstate_t___value(Union):
    """
    ```python
    __wch: int (POINTER(i))
    __wchb: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    __wch: int
    __wchb: list[int]

class union_nkm_ipoi_entry_pointer_t(Union):
    """
    ```python
    final: POINTER_T[struct_nkm_ipoi_entry_t] (POINTER(struct_nkm_ipoi_entry_t))
    beta: POINTER_T[struct_nkm_ipoi_entry_beta_t] (POINTER(struct_nkm_ipoi_entry_beta_t))
    ```
    """
    _pack_: ClassVar[int] = 1
    final: POINTER_T[struct_nkm_ipoi_entry_t]
    beta: POINTER_T[struct_nkm_ipoi_entry_beta_t]

class union_nkm_poit_entry_t_0(Union):
    """
    ```python
    unknown2: int (POINTER(I))
    _0: struct_nkm_poit_entry_t_0_0 (struct_nkm_poit_entry_t_0_0)
    ```
    """
    _pack_: ClassVar[int] = 1
    unknown2: int
    _0: struct_nkm_poit_entry_t_0_0

class union_r2d_race_mode_top_hud_state_t_0(Union):
    """
    ```python
    _0: struct_r2d_race_mode_top_hud_state_t_0_0 (struct_r2d_race_mode_top_hud_state_t_0_0)
    _1: struct_r2d_race_mode_top_hud_state_t_0_1 (struct_r2d_race_mode_top_hud_state_t_0_1)
    place: int (POINTER(i))
    mrCurrentValue: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    _0: struct_r2d_race_mode_top_hud_state_t_0_0
    _1: struct_r2d_race_mode_top_hud_state_t_0_1
    place: int
    mrCurrentValue: int

class union_spa_emitter_t_0(Union):
    """
    ```python
    flags: int (POINTER(I))
    _0: struct_spa_emitter_t_0_0 (struct_spa_emitter_t_0_0)
    ```
    """
    _pack_: ClassVar[int] = 1
    flags: int
    _0: struct_spa_emitter_t_0_0

class union_spa_emitter_t_1(Union):
    """
    ```python
    userWorkU32: int (POINTER(I))
    userWorkU16: list[int] (POINTER(H)[2])
    userWorkU8: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    userWorkU32: int
    userWorkU16: list[int]
    userWorkU8: list[int]

class union_spa_res_emitter_t_0(Union):
    """
    ```python
    userDataU32: int (POINTER(I))
    userDataU16: list[int] (POINTER(H)[2])
    userDataU8: list[int] (POINTER(B)[4])
    ```
    """
    _pack_: ClassVar[int] = 1
    userDataU32: int
    userDataU16: list[int]
    userDataU8: list[int]

class vec2_t(Structure):
    """
    ```python
    x: fx32 (struct_fx32)
    y: fx32 (struct_fx32)
    ```
    """
    _pack_: ClassVar[int] = 1
    x: fx32
    y: fx32

class vec2i_t(Structure):
    """
    ```python
    x: int (POINTER(i))
    y: int (POINTER(i))
    ```
    """
    _pack_: ClassVar[int] = 1
    x: int
    y: int

class vram_wvr_stat_t(Structure):
    """
    ```python
    status: int (POINTER(I))
    callbackFunc: Callable[[int], None] (CFunctionType)
    ```
    """
    _pack_: ClassVar[int] = 1
    status: int
    callbackFunc: Callable[[int], None]

class water_splash_state_t(Structure):
    """
    ```python
    splashY: fx32 (struct_fx32)
    nsbmd: c_void_p (c_void_p)
    nsbca: c_void_p (c_void_p)
    nsbma: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    splashY: fx32
    nsbmd: c_void_p
    nsbca: c_void_p
    nsbma: c_void_p

class water_splash_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class water_state_t(Structure):
    """
    ```python
    waterAPosition: struct_VecFx32 (struct_VecFx32)
    waterCPosition: struct_VecFx32 (struct_VecFx32)
    basePosition: struct_VecFx32 (struct_VecFx32)
    state: int (POINTER(I))
    tideAmplitude: fx32 (struct_fx32)
    tidePhase: int (POINTER(H))
    tideSpeed: int (POINTER(H))
    tideProgress: fx32 (struct_fx32)
    field34: int (POINTER(H))
    field36: int (POINTER(H))
    field38: int (POINTER(H))
    field3A: int (POINTER(H))
    waterMovePhase: int (POINTER(H))
    field3E: int (POINTER(H))
    waterMoveSpeed: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    waterAMoveDistance: fx32 (struct_fx32)
    waterCMoveDistance: fx32 (struct_fx32)
    field4C: fx32 (struct_fx32)
    waterCMovePhaseDifference: int (POINTER(H))
    field52: int (POINTER(H))
    waterAFirst: int (POINTER(i))
    waterAAlpha: int (POINTER(H))
    waterCAlpha: int (POINTER(H))
    field5C: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    waterANsbmd: c_void_p (c_void_p)
    waterCNsbmd: c_void_p (c_void_p)
    waterAModel: struct_model_t (struct_model_t)
    waterCModel: struct_model_t (struct_model_t)
    transformMtx: union_MtxFx43 (union_MtxFx43)
    isDiveable: int (POINTER(i))
    waterEfctNsbmd: c_void_p (c_void_p)
    waterEfctNsbca: c_void_p (c_void_p)
    waterEfctNsbma: c_void_p (c_void_p)
    ```
    """
    _pack_: ClassVar[int] = 1
    waterAPosition: struct_VecFx32
    waterCPosition: struct_VecFx32
    basePosition: struct_VecFx32
    state: int
    tideAmplitude: fx32
    tidePhase: int
    tideSpeed: int
    tideProgress: fx32
    field34: int
    field36: int
    field38: int
    field3A: int
    waterMovePhase: int
    field3E: int
    waterMoveSpeed: int
    PADDING_0: list[int]
    waterAMoveDistance: fx32
    waterCMoveDistance: fx32
    field4C: fx32
    waterCMovePhaseDifference: int
    field52: int
    waterAFirst: int
    waterAAlpha: int
    waterCAlpha: int
    field5C: int
    PADDING_1: list[int]
    waterANsbmd: c_void_p
    waterCNsbmd: c_void_p
    waterAModel: struct_model_t
    waterCModel: struct_model_t
    transformMtx: union_MtxFx43
    isDiveable: int
    waterEfctNsbmd: c_void_p
    waterEfctNsbca: c_void_p
    waterEfctNsbma: c_void_p

class water_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t

class wbox_t(Structure):
    """
    ```python
    mobj: struct_mobj_inst_t (struct_mobj_inst_t)
    fieldA0: struct_VecFx32 (struct_VecFx32)
    fieldAC: int (POINTER(H))
    PADDING_0: list[int] (POINTER(B)[2])
    fieldB0: struct_VecFx32 (struct_VecFx32)
    floorNormal: struct_VecFx32 (struct_VecFx32)
    rotY: int (POINTER(H))
    PADDING_1: list[int] (POINTER(B)[2])
    fieldCC: struct_VecFx32 (struct_VecFx32)
    fieldD8: struct_VecFx32 (struct_VecFx32)
    fieldE4: struct_VecFx32 (struct_VecFx32)
    fieldF0: int (POINTER(H))
    PADDING_2: list[int] (POINTER(B)[2])
    fieldF4: struct_VecFx32 (struct_VecFx32)
    field100: struct_VecFx32 (struct_VecFx32)
    field10C: int (POINTER(H))
    field10E: int (POINTER(H))
    field110: int (POINTER(H))
    PADDING_3: list[int] (POINTER(B)[2])
    shadow: struct_objshadow_t (struct_objshadow_t)
    ```
    """
    _pack_: ClassVar[int] = 1
    mobj: struct_mobj_inst_t
    fieldA0: struct_VecFx32
    fieldAC: int
    PADDING_0: list[int]
    fieldB0: struct_VecFx32
    floorNormal: struct_VecFx32
    rotY: int
    PADDING_1: list[int]
    fieldCC: struct_VecFx32
    fieldD8: struct_VecFx32
    fieldE4: struct_VecFx32
    fieldF0: int
    PADDING_2: list[int]
    fieldF4: struct_VecFx32
    field100: struct_VecFx32
    field10C: int
    field10E: int
    field110: int
    PADDING_3: list[int]
    shadow: struct_objshadow_t