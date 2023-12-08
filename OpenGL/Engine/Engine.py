#!/usr/bin/python2.7
"""Quick hack of 'modern' OpenGL example using pysdl2 and pyopengl

Based on

pysdl2 OpenGL example
http://www.arcsynthesis.org/gltut/Basics/Tut02%20Vertex%20Attributes.html
http://schi.iteye.com/blog/1969710
"""
from camera import Camera
import sys
import ctypes

from OpenGL import GL, GLU
from OpenGL.GL import shaders
from OpenGL.arrays import vbo

import sdl2
from sdl2 import video
import numpy as np

from helpers import *
from camera import Camera


# use tralstion matrix to move the object istead
def move_vertices(obj, key_sym, move_distance=0.1):
    direction = {
        sdl2.SDLK_w: (0, move_distance),  # Move up
        sdl2.SDLK_s: (0, -move_distance),  # Move down
        sdl2.SDLK_a: (-move_distance, 0),  # Move left
        sdl2.SDLK_d: (move_distance, 0)   # Move right
    }.get(key_sym, (0, 0))

    dx, dy = direction

    for i in range(0,  len(obj.vertices) // 2, 4):
        obj.vertices[i] += dx
        obj.vertices[i + 1] += dy


camera = Camera()


def render(objects):
    GL.glClearColor(0.2, 0.2, 0.2, 1)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    for obj in objects:
        obj.display(camera) 


def run(objects, vertexShaderStr, fragmentShaderStr):
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
    for obj in objects:
        obj.initialize(vertexShaderStr, fragmentShaderStr)

    event = sdl2.SDL_Event()
    running = True
    while running:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                running = False
            if event.type == sdl2.SDL_KEYDOWN:
                for obj in objects:
                    move_vertices(obj, event.key.keysym.sym)
                    obj.initialize(vertexShaderStr, fragmentShaderStr)

        render(objects)

        sdl2.SDL_GL_SwapWindow(window)
        sdl2.SDL_Delay(10)

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(run())
