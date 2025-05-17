import moderngl as mgl
import numpy as np

def create_vao(ctx: mgl.Context, prog: mgl.Program, data: list[float]):
    vbo = ctx.buffer(np.array(data, dtype='f'))
    return ctx.vertex_array(prog, vbo, 'in_pos', 'in_col', 'in_norm')

def gen_prog(ctx: mgl.Context, dim: int):
    dim1 = dim + 1
    dim1sq = dim1 * dim1
    prog = ctx.program(
        vertex_shader='''
            #version 330
            in float in_pos[DIM];
            in vec4 in_col;
            in float in_norm[DIM];
            uniform float u_transforms[DIM1SQ];
            uniform float u_aspect;

            out vec4 col;
        
            void main() {
                vec3 pos = vec3(0.0);
                for (int i = 0; i < DIM; i++) {
                    pos.x += in_pos[i] * u_transforms[i];
                    pos.y += in_pos[i] * u_transforms[i + DIM1];
                }
                pos += vec3(u_transforms[DIM], u_transforms[DIM + DIM1], 0.0);

                for (int i = 2; i < 3; i++) {
                    for (int j = 0; j < DIM; j++) {
                        pos.z += in_pos[j] * u_transforms[j + i * DIM1];
                    }
                    pos.z += u_transforms[DIM + i * DIM1];
                }
                pos.z *= -0.1;

                float shade = 0.0;
                float light = 0.0;
                for (int i = 0; i < DIM; i++) light += i * i;
                for (int i = 0; i < DIM; i++) {
                    shade += in_norm[i] * (float(i) / sqrt(light));
                }
                shade = 0.7 + shade * 0.3;

                gl_Position = vec4(pos / vec3(u_aspect, 1.0, 1.0), 1.0);
                col = in_col * shade;
            }
        '''
        .replace("DIM1SQ", str(dim1sq))
        .replace("DIM1", str(dim1))
        .replace("DIM", str(dim)),
        fragment_shader='''
            #version 330
            in vec4 col;
            out vec4 fragColor;

            void main() {
                fragColor = col;
            }
        '''
    )
    prog['u_transforms'].array_length = dim1sq # type: ignore
    return prog
