import numpy as np

sqrt2 = np.sqrt(2)
sqrt3 = np.sqrt(3)
sqrt6 = np.sqrt(6)

def rotation(angle: float, dimensions: int, plane: tuple[int, int]):
    angle = np.deg2rad(angle)
    mat = np.eye(dimensions)
    mat[plane[0]][plane[0]] = np.cos(angle)
    mat[plane[1]][plane[0]] = -np.sin(angle)
    mat[plane[0]][plane[1]] = np.sin(angle)
    mat[plane[1]][plane[1]] = np.cos(angle)
    return mat

def upgrade_matrix(mat: np.ndarray, dimensions: int):
    new_mat = np.eye(dimensions, dtype=mat.dtype)
    r, c = mat.shape
    new_mat[:r, :c] = mat[:r, :c]
    return new_mat

isometric3d = rotation(-35.264, 4, (1, 2)) @ rotation(-45, 4, (0, 2))
isometric4d = rotation(-45, 5, (0, 2)) @ rotation(-45, 5, (1, 3))

class TweenMatrix:
    def __init__(self, mat: np.ndarray):
        self.mat = mat
        self.a = mat
        self.b = mat
        self.t = 1.0

    def update(self, dt: float):
        self.t = min(self.t + dt, 1.0)
        self.mat = self.a * (1.0 - self.t) + self.b * self.t
    
    def to(self, mat: np.ndarray):
        self.a = self.mat
        self.b = mat
        self.t = 0.0
