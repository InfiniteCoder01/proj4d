import moderngl as mgl
import numpy as np
import pygame as pg

from buffer import *
from shapes import *
from views import *

# Init
pg.init()
pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)
pg.display.set_caption("Proj4D")
ctx = mgl.create_context()
ctx.enable(mgl.DEPTH_TEST)
clock = pg.time.Clock()

# Generate stuff
prog = gen_prog(ctx, 4)
basis = create_vao(ctx, prog, basis(4))
cube = create_vao(ctx, prog, cube((1.0, 1.0, 1.0, 1.0), 4))
transforms = TweenMatrix(np.eye(5))
transforms.to(upgrade_matrix(isometric3d, 5))

running = True
while running:
    ms = clock.tick(30)
    dt = ms / 1000.0

    transforms.update(dt)

    width, height = pg.display.get_surface().get_size() # type: ignore
    prog['u_aspect'].value = width / height # type: ignore
    prog['u_transforms'].value = transforms.mat.ravel().tolist() # type: ignore

    ctx.clear(0.1, 0.1, 0.1)
    basis.render(mode=mgl.LINES)
    cube.render(mode=mgl.TRIANGLES)
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.unicode == 'q': running = False
            elif event.unicode == ' ':
                transforms.to(isometric4d)

pg.quit()
