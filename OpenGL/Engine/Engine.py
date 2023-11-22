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

shaderProgram = None
VAO = None
VBO = None


def initialize(vertexData, vertexShaderStr, fragmentShaderStr):
    global shaderProgram
    global VAO
    global VBO
    global vertecies

    vertecies = int(len(vertexData) / 8)

    VAO = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(VAO)

    vertexShader = shaders.compileShader(vertexShaderStr, GL.GL_VERTEX_SHADER)
    fragmentShader = shaders.compileShader(
        fragmentShaderStr, GL.GL_FRAGMENT_SHADER)

    shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)

    # Allocate a buffer to contain the triangle's vertices and make it active ("bind" it)
    VBO = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)

    # Transfer the triangle's vertices to the GPU (i.e. the buffer you allocated)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, vertexData.nbytes, vertexData,
                    GL.GL_STATIC_DRAW)

    # Enable the first attribute of the triangle: the position of each vertex
    GL.glEnableVertexAttribArray(0)

    # Describe the first attribute: the position
    # - location: 0                 (remember the shader?)
    # - size of each vertex: 4      (vec4)
    # - type of vertices: float
    # - do not normalize            (ignore for now)
    # - stride: 0                   (there is no space between vertices)
    # - offset: None                (start from the first element; no offset)
    GL.glVertexAttribPointer(0, 4, GL.GL_FLOAT, GL.GL_FALSE, 0, None)

    # The same for the second attribute: the color of each vertex
    GL.glEnableVertexAttribArray(1)

    # The last parameter is actually a pointer
    GL.glVertexAttribPointer(
        1, 4, GL.GL_FLOAT, GL.GL_FALSE, 0, ctypes.c_void_p(48))

    # Cleanup (just in case)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
    GL.glBindVertexArray(0)


def render():
    global shaderProgram
    global VAO

    GL.glClearColor(0.2, 0.2, 0.2, 1)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    # active shader program
    GL.glUseProgram(shaderProgram)

    try:
        # Activate the object
        GL.glBindVertexArray(VAO)

        # draw triangle
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, vertecies)

    finally:
        # Cleanup (just in case)
        GL.glBindVertexArray(0)
        GL.glUseProgram(0)


def run(vertexData, vertexShaderStr, fragmentShaderStr):
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
    initialize(vertexData, vertexShaderStr, fragmentShaderStr)

    event = sdl2.SDL_Event()
    running = True
    while running:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                running = False

        render()

        sdl2.SDL_GL_SwapWindow(window)
        sdl2.SDL_Delay(10)

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(run())
