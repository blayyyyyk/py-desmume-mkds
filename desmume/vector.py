import torch
import numpy as np


def ray_triangle_intersection(
    vertices: torch.Tensor,
    ray_origin: torch.Tensor,
    ray_direction: torch.Tensor,
    culling: bool = False,
    epsilon: float = 1e-6,
) -> torch.Tensor:
    """
    PyTorch vmap-compatible Möller-Trumbore intersection.

    Args:
        vertices: (3, 3) Tensor
        ray_origin: (3,) Tensor
        ray_direction: (3,) Tensor
        culling: bool (Static python argument, not a Tensor)
        epsilon: float

    Returns:
        Tensor of shape (3,) containing [t, u, v].
        Contains [NaN, NaN, NaN] if no intersection occurs.
    """
    v0, v1, v2 = vertices[0], vertices[1], vertices[2]

    edge1 = v1 - v0
    edge2 = v2 - v0

    pvec = torch.linalg.cross(ray_direction, edge2)

    det = torch.dot(edge1, pvec)

    if culling:
        # Culling: determinant must be positive and > epsilon
        valid_det = det > epsilon
    else:
        # No Culling: determinant must be non-zero (abs > epsilon)
        valid_det = torch.abs(det) > epsilon

    safe_det = torch.where(valid_det, det, torch.ones_like(det))
    inv_det = 1.0 / safe_det

    tvec = ray_origin - v0
    u = torch.dot(tvec, pvec) * inv_det
    valid_u = (u >= 0.0) & (u <= 1.0)

    qvec = torch.linalg.cross(tvec, edge1)
    v = torch.dot(ray_direction, qvec) * inv_det
    valid_v = (v >= 0.0) & (u + v <= 1.0)

    t = torch.dot(edge2, qvec) * inv_det
    valid_t = t > epsilon  # Intersection must be strictly in front of camera

    is_hit = valid_det & valid_u & valid_v & valid_t

    result = torch.stack([t, u, v])

    nan_tensor = torch.full_like(result, float("nan"))

    return torch.where(is_hit, result, nan_tensor)


def ray_line_intersection(O, D, P1, P2, eps=1e-8):
    """
    Find intersection of a ray (O + tD, t>=0)
    with a line segment between P1 and P2.

    All inputs are torch tensors of shape (..., 2)
    and can be batched.
    """
    # Direction of the segment
    v = P2 - P1

    # 2D cross product helper (scalar)
    def cross(a, b):
        return a[..., 0] * b[..., 1] - a[..., 1] * b[..., 0]

    # Compute determinant
    denom = cross(D, v)  # parallel if denom == 0

    # Compute relative position
    w = P1 - O

    t = cross(w, v) / (denom + eps)
    u = cross(w, D) / (denom + eps)

    # Compute intersection point
    intersection = O + t.unsqueeze(-1) * D

    # Valid if:
    valid = (denom.abs() > eps) & (t >= 0) & (u >= 0) & (u <= 1)

    return intersection, valid


def generate_plane_vectors(
    n_rays: int,
    sweep_angle_deg: float,
    rotation_matrix: np.ndarray,
    origin: np.ndarray,
    plane_indices: tuple[int, int] = (2, 0),  # Default: Forward (Z) to Right (X)
):
    """
    Generates a fan of rays using a rotation matrix to define the orientation.

    Args:
        n_rays: Number of rays to generate.
        sweep_angle_deg: Total field of view (e.g., 120 means +/- 60 deg).
        rotation_matrix: (3, 3) or (B, 3, 3) Matrix where columns are basis vectors.
                         - Col 0: Right (X)
                         - Col 1: Up (Y)
                         - Col 2: Forward (Z)
        origin: (3,) or (B, 3) Ray starting positions.
        plane_indices: Tuple (center_idx, side_idx) defining the sweep plane.
                       - (2, 0) = Horizontal Sweep (Forward -> Right)
                       - (2, 1) = Vertical Sweep (Forward -> Up)

    Returns:
        origins: (N, 3) or (B, N, 3)
        directions: (N, 3) or (B, N, 3) Normalized
    """
    # 1. Handle Batching
    # If input is unbatched (3,3), unsqueeze to (1,3,3) for uniform logic
    is_batched = rotation_matrix.ndim == 3
    if not is_batched:
        rotation_matrix = rotation_matrix[None, ...]
        origin = origin[None, ...]

    B = rotation_matrix.shape[0]

    # 2. Extract Basis Vectors from Matrix Columns
    # R[:, :, i] grabs the i-th column (the i-th basis vector)
    center_idx, side_idx = plane_indices

    # Shape: (B, 3)
    vec_center = rotation_matrix[:, :, center_idx]
    vec_side = rotation_matrix[:, :, side_idx]

    # 3. Generate Angles
    half_sweep = sweep_angle_deg / 2.0
    angles = np.linspace(-half_sweep, half_sweep, n_rays)
    rads = np.deg2rad(angles)

    # 4. Reshape for Broadcasting
    # We want: (B, 1, 3) * (1, N, 1) -> (B, N, 3)

    # Basis vectors: (B, 1, 3)
    vec_center = vec_center[:, None, ...]
    vec_side = vec_side[:, None, ...]

    # Trig values: (1, N, 1)
    cos_t = np.cos(rads).reshape(1, n_rays, 1)
    sin_t = np.sin(rads).reshape(1, n_rays, 1)

    # 5. Linear Combination (The Sweep)
    # v = Center * cos(t) + Side * sin(t)
    directions = (vec_center * cos_t) + (vec_side * sin_t)

    # Normalize (just in case floating point drift occurred)
    directions = directions / (np.linalg.norm(directions, axis=-1, keepdims=True) + 1e-8)

    # 6. Expand Origins
    # Origin (B, 3) -> (B, N, 3)
    origins = origin[:, None, ...].repeat(n_rays, axis=1)

    # 7. Remove batch dim if input was single
    if not is_batched:
        return origins.squeeze(0), directions.squeeze(0)

    return origins, directions
