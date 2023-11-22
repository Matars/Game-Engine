#!/usr/bin/python2.7
"""Quick hack of 'modern' OpenGL example using pysdl2 and pyopengl

Based on

pysdl2 OpenGL example
http://www.arcsynthesis.org/gltut/Basics/Tut02%20Vertex%20Attributes.html
http://schi.iteye.com/blog/1969710
"""
import sys
import ctypes
import numpy

from OpenGL import GL, GLU
from OpenGL.GL import shaders
from OpenGL.arrays import vbo

import sdl2
from sdl2 import video
from numpy import array
from sdl2 import SDL_KEYDOWN, SDL_KEYUP, SDL_Keysym

from Triangle import Triangle


def initialize():
    global shaderProgram
    global VAO
    global VBO

    vertexShader = shaders.compileShader("""
# version 330

layout (location = 0) in vec4 position;
layout (location = 1) in vec4 color;

out vec4 vertexColor; // Pass color to the fragment shader

void main() {
    gl_Position = position;
    vertexColor = color;
}

""", GL.GL_VERTEX_SHADER)

    fragmentShader = shaders.compileShader("""
# version 330

in vec4 vertexColor;
out vec4 outputColour;

void main() {
    outputColour = vertexColor;
}

""", GL.GL_FRAGMENT_SHADER)

    VAO = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(VAO)

    shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)


def render(triangles):
    global shaderProgram
    global VAO
    GL.glClearColor(0.2, 0.2, 0.2, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    # active shader program
    for triangle in triangles:
        triangle.render(shaderProgram)


def run():
    if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
        print(sdl2.SDL_GetError())
        return -1

    window = sdl2.SDL_CreateWindow(b"OpenGL demo",
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED, 800, 600,
                                   sdl2.SDL_WINDOW_OPENGL)
    if not window:
        print(sdl2.SDL_GetError())
        return -1

    # Force OpenGL 3.3 'core' context.
    # Must set *before* creating GL context!
    video.SDL_GL_SetAttribute(video.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
    video.SDL_GL_SetAttribute(video.SDL_GL_CONTEXT_MINOR_VERSION, 3)
    video.SDL_GL_SetAttribute(video.SDL_GL_CONTEXT_PROFILE_MASK,
                              video.SDL_GL_CONTEXT_PROFILE_CORE)
    context = sdl2.SDL_GL_CreateContext(window)

    # Setup GL shaders, data, etc.
    initialize()

    # sweden
    FlagBackground = numpy.array([0, 0, 1, 1.0], dtype=numpy.float32)
    FlagStripes = numpy.array([1, 1, 0, 1.0], dtype=numpy.float32)

    # danish
    # FlagBackground = numpy.array([1, 0, 0, 1.0], dtype=numpy.float32)
    # FlagStripes = numpy.array([1, 1, 1, 1.0], dtype=numpy.float32)

    # finish
    # FlagBackground = numpy.array([0, 0, 1, 1.0], dtype=numpy.float32)
    # FlagStripes = numpy.array([1, 1, 1, 1.0], dtype=numpy.float32)

    bg = numpy.array([0.2, 0.2, 0.2, 1.0], dtype=numpy.float32)

    rectangle_specs = [
        {'offset': numpy.array(
            [-1, -0.5], dtype=numpy.float32), 'color': FlagBackground},
        {'offset': numpy.array(
            [-0.5, -0.5], dtype=numpy.float32), 'color': FlagStripes},
        {'offset': numpy.array(
            [0, -0.5], dtype=numpy.float32), 'color': FlagBackground},
        {'offset': numpy.array(
            [0.5, -0.5], dtype=numpy.float32), 'color': FlagBackground},

        {'offset': numpy.array([-1, 0], dtype=numpy.float32),
         'color': FlagStripes},
        {'offset': numpy.array(
            [-0.5, 0], dtype=numpy.float32), 'color': FlagStripes},
        {'offset': numpy.array([0, 0], dtype=numpy.float32),
         'color': FlagStripes},
        {'offset': numpy.array(
            [0.5, 0], dtype=numpy.float32), 'color': FlagStripes},

        {'offset': numpy.array(
            [-1, 0.5], dtype=numpy.float32), 'color': FlagBackground},
        {'offset': numpy.array(
            [-0.5, 0.5], dtype=numpy.float32), 'color': FlagStripes},
        {'offset': numpy.array([0, 0.5], dtype=numpy.float32),
         'color': FlagBackground},
        {'offset': numpy.array(
            [0.5, 0.5], dtype=numpy.float32), 'color': FlagBackground},

        {'offset': numpy.array([-1, 1], dtype=numpy.float32), 'color': bg},
        {'offset': numpy.array([-0.5, 1], dtype=numpy.float32), 'color': bg},
        {'offset': numpy.array([0, 1], dtype=numpy.float32), 'color': bg},
        {'offset': numpy.array([0.5, 1], dtype=numpy.float32), 'color': bg},

    ]

    triangles = createRectangles(rectangle_specs)

    event = sdl2.SDL_Event()
    running = True

    while running:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                running = False
            if event.type == SDL_KEYDOWN:
                move_vertices(event.key.keysym.sym, triangles)

        render(triangles)

        sdl2.SDL_GL_SwapWindow(window)
        sdl2.SDL_Delay(10)

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()
    return 0


def rectangle(offset, color):
    # offset: numpy array like numpy.array([offset_x, offset_y])
    # color: numpy array like numpy.array([r, g, b, a])
    scale = 0.5
    width = 0.336 * scale
    height = 0.5 * scale
    offset = offset * scale

    triangles = [
        Triangle(numpy.array([
            -width + offset[0],  width +
            offset[1],  0.0, 1.0, color[0], color[1], color[2], color[3],
            width + offset[0], -height +
            offset[1], 0.0, 1.0, color[0], color[1], color[2], color[3],
            -width + offset[0], -height +
            offset[1], 0.0, 1.0, color[0], color[1], color[2], color[3],
        ], dtype=numpy.float32)),
        Triangle(numpy.array([
            -width + offset[0],  width +
            offset[1],  0.0, 1.0, color[0], color[1], color[2], color[3],
            width + offset[0],  width +
            offset[1],  0.0, 1.0, color[0], color[1], color[2], color[3],
            width + offset[0], -height +
            offset[1], 0.0, 1.0, color[0], color[1], color[2], color[3],
        ], dtype=numpy.float32))
    ]
    return triangles


def createRectangles(specs):
    all_triangles = []
    for spec in specs:
        offset, color = spec['offset'], spec['color']
        triangles = rectangle(offset, color)
        all_triangles.extend(triangles)
    return all_triangles


def move_vertices(key_sym, triangles, move_distance=0.1):
    direction = {
        sdl2.SDLK_w: (0, move_distance),  # Move up
        sdl2.SDLK_s: (0, -move_distance),  # Move down
        sdl2.SDLK_a: (-move_distance, 0),  # Move left
        sdl2.SDLK_d: (move_distance, 0)   # Move right
    }.get(key_sym, (0, 0))

    dx, dy = direction
    for triangle in triangles:
        # Update the vertex positions
        triangle.vertexData[::8] += dx
        triangle.vertexData[1::8] += dy

        # Update the buffer with new data
        triangle.update_buffer()


if __name__ == "__main__":
    sys.exit(run())
