Vector = tuple[float, ...] | list[float]
Color = tuple[float, float, float, float] | list[float]

def vertex(
    position: Vector,
    color: Color,
    normal: Vector | None = None
):
    if normal is None: normal = [0.0] * len(position)
    assert len(position) == len(normal), "Position and normal have different dimensions: %d and %d" % (len(position), len(normal))
    return list(position) + list(color) + list(normal)

def line(a: Vector, b: Vector, color: Color):
    return (
        vertex(a, color) +
        vertex(b, color)
    )

def basis(dimensions: int):
    COLORS = [
        (1.0, 0.0, 0.0, 1.0),
        (0.0, 1.0, 0.0, 1.0),
        (0.0, 0.0, 1.0, 1.0),
        (0.7, 0.0, 0.7, 1.0)
    ]

    assert dimensions <= len(COLORS), "Not enough colors to represent all dimensions (%d)!" % dimensions

    data = []
    origin = [0.0] * dimensions
    for i in range(dimensions):
        axis = [0.0] * dimensions
        axis[i] = 1.0
        data += line(origin, axis, COLORS[i])
    return data

def cube(color: Color, dimensions: int):
    vo = [0.0] * dimensions
    vx = [0.0] * dimensions
    vy = [0.0] * dimensions
    vz = [0.0] * dimensions
    vxy = [0.0] * dimensions
    vxz = [0.0] * dimensions
    vyz = [0.0] * dimensions
    vxyz = [0.0] * dimensions
    vx[0] = vy[1] = vz[2] = vxy[0] = vxy[1] = vxz[0] = vxz[2] = vyz[1] = vyz[2] = vxyz[0] = vxyz[1] = vxyz[2] = 1.0

    nx = [0.0] * dimensions
    ny = [0.0] * dimensions
    nz = [0.0] * dimensions
    nmx = [0.0] * dimensions
    nmy = [0.0] * dimensions
    nmz = [0.0] * dimensions
    nx[0] = ny[1] = nz[2] = 1.0
    nmx[0] = nmy[1] = nmz[2] = -1.0
    return (
        vertex(vo, color, nmz) +
        vertex(vx, color, nmz) +
        vertex(vxy, color, nmz) +
        vertex(vo, color, nmz) +
        vertex(vxy, color, nmz) +
        vertex(vy, color, nmz) +

        vertex(vz, color, nz) +
        vertex(vxz, color, nz) +
        vertex(vxyz, color, nz) +
        vertex(vz, color, nz) +
        vertex(vxyz, color, nz) +
        vertex(vyz, color, nz) +

        vertex(vo, color, nmx) +
        vertex(vz, color, nmx) +
        vertex(vyz, color, nmx) +
        vertex(vo, color, nmx) +
        vertex(vyz, color, nmx) +
        vertex(vy, color, nmx) +

        vertex(vx, color, nx) +
        vertex(vxz, color, nx) +
        vertex(vxyz, color, nx) +
        vertex(vx, color, nx) +
        vertex(vxyz, color, nx) +
        vertex(vxy, color, nx) +

        vertex(vo, color, nmy) +
        vertex(vx, color, nmy) +
        vertex(vxz, color, nmy) +
        vertex(vo, color, nmy) +
        vertex(vxz, color, nmy) +
        vertex(vz, color, nmy) +

        vertex(vy, color, ny) +
        vertex(vxy, color, ny) +
        vertex(vxyz, color, ny) +
        vertex(vy, color, ny) +
        vertex(vxyz, color, ny) +
        vertex(vyz, color, ny)
    )

