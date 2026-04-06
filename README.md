# py-desmume-mkds

A Python library for the DeSmuME Nintendo DS emulator, enhanced with deep memory introspection, PyTorch integration, and 3D environment analysis specifically tailored for Mario Kart DS.

This fork extends the standard `py-desmume` library by introducing direct `ctypes` mappings to the game's internal data structures (drivers, camera, maps, and collision data) and provides hardware-accelerated utilities for raycasting, screen-space projection, and coordinate transformation.

## Features

* **Complete DeSmuME Standard API**: Full access to emulation controls, keypad input mapping, savestates, and framebuffer extraction.
* **Direct Memory Structure Mapping**: Extracted internal Mario Kart DS pointers mapped seamlessly to Python objects using `ctypes`.
* **Fixed-Point to Tensor Conversion**: Automatic, on-the-fly conversion of Nintendo DS `fx32`/`fx16` fixed-point coordinate structures to scaled PyTorch tensors.
* **Hardware-Accelerated Raycasting**: Batched `torch.vmap` ray-triangle intersection testing using the track's native collision geometry (KCL).
* **3D to 2D Screen Projection**: Helper functions to convert 3D world coordinates into 2D screen-space pixel coordinates using the game's actual camera matrix.
* **Track Octree Traversal**: Search the game's KCL octree to query floor and wall geometry properties at specific world coordinates.

## Installation

**Build Requirements:**

* **Linux:** SDL2 >= 2.0.14, zlib, libpcap, soundtouch, openal-soft, glib2, meson
* **macOS:** `brew install sdl2 meson glib gcc`
* **Windows:** Visual Studio 2019 or later

> Please refer to the original fork's guide for more detailed build instructions for your specific device

You can build the library from source by running setup via pip, which will compile the C++ emulator core and bind it to Python.

```bash
pip install py-desmume-mkds --no-build-isolation
```

Or, if you have cloned the repo locally,
```bash
pip install -e . --no-build-isolation
```
> [!IMPORTANT]
> It is important you do not trigger a build within a venv or else you may run into issues where the os cannot locate meson, hence the `--no-build-isolation`

---

## Detailed Usage: Memory Access & `ctypes` Bindings

This fork differentiates itself by providing extreme, low-level access to Mario Kart DS structures in memory. Memory interaction comes in two forms: **Standard Access** and **Structured Ctypes Access**.

### 1. Initialization

Instead of the standard `DeSmuME` class, you instantiate the enhanced `MarioKart` class, which requires PyTorch for tensor math:

```python
import torch
from desmume.emulator_mkds import MarioKart

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the emulator with raycasting parameters
emu = MarioKart("mariokart.nds", max_dist=100.0, n_rays=8, device=device)

```

### 2. Standard Memory Access

Standard memory reading/writing works out of the box using Python slices and handles. This is useful for simple byte/word level interaction.

```python
# Access raw unsigned/signed bytes
player_byte = emu.memory.unsigned[0x0217ACF8]

# Access slices of memory
health_data = emu.memory.signed[0x02000000:0x02000010]

# Write memory
emu.memory.unsigned[0x02000000] = 255

```

### 3. Structured `ctypes` Mapping (MKDS Specific)

To read the complex game states, the fork provides `MarioKart_Memory` (accessible via `emu.memory`). Instead of manual byte offsets, it maps predefined C-structs directly onto the emulator's `MAIN_MEM` (the 16MB region starting at `0x02000000`).

#### How it works under the hood

The `_read_struct` method binds a ctypes `Structure` directly to the `memoryview` of the emulator's running memory buffer:

```python
struct = struct_t.from_buffer(self.memoryview, addr - 0x02000000)

```

This means reading a struct property requires **zero-copy overhead**—it directly queries the emulator's live memory.

#### Accessing Game Data

The emulator lazily reads and caches the pointers to the primary game structs:

```python
# 1. Driver State (Positions, speed, inputs)
driver = emu.memory.driver
print(driver.position) # Outputs current 3D position

# 2. Camera Data (FOV, Aspect Ratio, Transformation Matrix)
camera = emu.memory.camera
print(emu.memory.get_camera_settings())

# 3. Race Data (Laps, Driver placements, Current Checkpoints)
status = emu.memory.race_status

# 4. Map & Collision Data
map_info = emu.memory.map_data
octree_header = emu.memory.collision_header

```

### 4. The `as_tensor` Fixed-Point Interceptor

The Nintendo DS lacks a floating-point unit and relies on fixed-point arithmetic (specifically `fx32` and `fx16`).

To make this seamless for machine learning and math processing, this fork uses an `as_tensor` class decorator (found in `mkds.py`).

**How `as_tensor` alters struct behavior:**
When you access an attribute on a decorated struct (like `driver.position` or `camera.mtx`), `as_tensor` intercepts the `__getattribute__` call:

1. It checks if the underlying `ctypes` type is a custom vector/matrix (e.g., `VecFx32`, `union_MtxFx43`, `fx32`).
2. It wraps the raw buffer directly into a `torch.Tensor` via `torch.frombuffer`.
3. It multiplies the tensor by the hardware scale factor: `FX32_SCALE_FACTOR` (`1 / 4096`).
4. It reshapes the tensor automatically (e.g., `4x3` for a transformation matrix).

**Example:**

```python
# Accessing the driver's transformation matrix
# Normally, this would be a flat ctypes array of integers
matrix = emu.memory.driver.mainMtx 

# Thanks to `as_tensor`, this returns a formatted PyTorch Tensor of floats:
# tensor([[ 1.0000,  0.0000,  0.0000],
#         [ 0.0000,  1.0000,  0.0000],
#         [ 0.0000,  0.0000,  1.0000],
#         [ 12.534, -5.2001,  45.002]], device='cuda:0')

```

---

## Advanced Emulation Features

### Track Raycasting

Because all geometry is loaded into PyTorch via the collision header parsers, you can generate physical obstacle rays dynamically.

```python
# Cast rays outwards from the driver to find walls/floors
raycast_data = emu.memory.obstacle_info(n_rays=8, max_dist=200.0)

# Returns distance to nearest wall, hit positions, and validity masks
print(raycast_data["distance"])

```

### Screen Projections

Easily map 3D tensors back into the DS's 256x192 2D pixel space using the game's actual internal camera projection matrix.

```python
# Convert 3D world coordinates to 2D pixel coordinates
point_3d = torch.tensor([[100.0, 50.0, -20.0]], device=device)
screen_data = emu.memory.project_to_screen(point_3d)

pixel_x, pixel_y = screen_data["screen"][0][:2]
is_on_screen = screen_data["mask"][0]

```

### KCL Octree Search

You can manually traverse the game's internal spatial partitioning octree to find which triangle primitives cover a specific coordinate.

```python
# Look up collision triangles at specific XYZ coordinates
point = (100.0, -50.0, 200.0)
triangle_indices = emu.memory.collision_search(point)

```
