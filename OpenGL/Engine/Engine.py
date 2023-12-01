#!/usr/bin/python2.7
"""Quick hack of 'modern' OpenGL example using pysdl2 and pyopengl

Based on

pysdl2 OpenGL example
http://www.arcsynthesis.org/gltut/Basics/Tut02%20Vertex%20Attributes.html
http://schi.iteye.com/blog/1969710
"""
import sys
import ctypes

from OpenGL import GL, GLU
from OpenGL.GL import shaders
from OpenGL.arrays import vbo

import sdl2
from sdl2 import video
import numpy as np

from helpers import *


class openGL3dObject():
    # TODO: move to a different file should not be in engine.py
    def __init__(self, vertices):
        self.vertices = vertices
        self.shaderProgram = None
        self.vao = None
        self.vbo = None
        self.ebo = None
        self.model = np.identity(4)

        self.transform(np.identity(4))

    def initialize(self, vertexShaderStr, fragmentShaderStr):
        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)

        vertexShader = shaders.compileShader(
            vertexShaderStr, GL.GL_VERTEX_SHADER)
        fragmentShader = shaders.compileShader(
            fragmentShaderStr, GL.GL_FRAGMENT_SHADER)

        self.shaderProgram = shaders.compileProgram(
            vertexShader, fragmentShader)

        # Allocate a buffer to contain the triangle's vertices and make it active ("bind" it)
        self.vbo = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)

        # Transfer the triangle's vertices to the GPU (i.e. the buffer you allocated)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices,
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
        GL.glVertexAttribPointer(0, 4, GL.GL_FLOAT, GL.GL_TRUE, 0, None)

        # The same for the second attribute: the color of each vertex
        GL.glEnableVertexAttribArray(1)

        # The last parameter is actually a pointer
        GL.glVertexAttribPointer(
            # this line says that the color starts half way thorugh the vertex data
            1, 4, GL.GL_FLOAT, GL.GL_TRUE, 0, ctypes.c_void_p(int(self.vertices.nbytes / 2)))

        # Cleanup (just in case)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glBindVertexArray(0)

    # -----------------------------

    def transform(self, matrix):
        """
        Transforms the model by applying the given transformation matrix.

        Args:
            matrix (np.ndarray): A 4x4 transformation matrix.
        """
        cameraMatrix = moveCamera()
        self.model = matrix @ self.model

    def translate(self, dx, dy, dz):
        """
        Translates the model by applying the given translation factors.

        Args:
            dx, dy, dz (float): The translation factors along the x, y, and z axes.
        """
        translationMatrix = np.identity(4)
        translationMatrix[3, 0] = dx
        translationMatrix[3, 1] = dy
        translationMatrix[3, 2] = dz
        self.transform(translationMatrix)

    def rotate(self, angleX, angleY, angleZ):
        # https://i.imgur.com/0cu8maY.png
        """
        Rotates the model by applying the given rotation angle around the given axis.

        Args:
            angleX, angleY, angleZ (float): The rotation angles around the x, y, and z axes.

        """

        # turn the angles into radians
        angleX = np.radians(angleX)
        angleY = np.radians(angleY)
        angleZ = np.radians(angleZ)

        Rz = np.identity(4)
        Ry = np.identity(4)
        Rx = np.identity(4)

        Rz[0, 0] = np.cos(angleZ)
        Rz[0, 1] = -np.sin(angleZ)
        Rz[1, 0] = np.sin(angleZ)
        Rz[1, 1] = np.cos(angleZ)

        Ry[0, 0] = np.cos(angleY)
        Ry[0, 2] = np.sin(angleY)
        Ry[2, 0] = -np.sin(angleY)
        Ry[2, 2] = np.cos(angleY)

        Rx[1, 1] = np.cos(angleX)
        Rx[1, 2] = -np.sin(angleX)
        Rx[2, 1] = np.sin(angleX)
        Rx[2, 2] = np.cos(angleX)

        rotationMatrix = Rz @ Ry @ Rx

        self.transform(rotationMatrix)

    def scale(self, dx, dy, dz):
        """
        Scales the model by applying the given scale factors.

        Args:
            dx, dy, dz (float): The scale factors along the x, y, and z axes.
        """
        scaleMatrix = np.identity(4)
        scaleMatrix[0, 0] = dx
        scaleMatrix[1, 1] = dy
        scaleMatrix[2, 2] = dz
        self.transform(scaleMatrix)

    def scaleAll(self, s):
        self.scale(s, s, s)

    # -----------------------------

    def display(self):

        # active shader program
        GL.glUseProgram(self.shaderProgram)

        # set the model matrix
        modelLoc = GL.glGetUniformLocation(self.shaderProgram, "model")

        GL.glUniformMatrix4fv(modelLoc, 1, True, self.model)

        try:
            # Activate the object
            GL.glBindVertexArray(self.vao)

            # draw triangle
            GL.glDrawArrays(GL.GL_TRIANGLES, 0, int(self.vertices.nbytes / 16))

        finally:
            # Cleanup (just in case)
            GL.glBindVertexArray(0)
            GL.glUseProgram(0)


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


# CAMERA LOGIC BELOW
# TODO: move to a different file should not be in engine.py

def moveCamera():
    # https://learnopengl.com/Getting-started/Camera
    # initial camera pos
    cameraPos = np.array([0.0, 1.0, 3.0], dtype=np.float32)

    # point to origin
    cameraTarget = np.array([0.0, 0.0, 0.0], dtype=np.float32)

    cameraDirection = normalize(np.subtract(cameraPos, cameraTarget))

    upvector = np.array([0.0, 1.0, 0.0], dtype=np.float32)
    cameraRight = normalize(np.cross(upvector, cameraDirection))

    cameraUp = np.cross(cameraDirection, cameraRight)

    cameraModel = getLookAtMatrix(cameraRight, cameraUp, cameraDirection, cameraPos)

    return cameraModel

# CAMERA LOGIC ABOVE


def render(objects):
    GL.glClearColor(0.2, 0.2, 0.2, 1)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    for obj in objects:
        obj.display()


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
    # sys.exit(run())
    moveCamera()
