import sys
import ctypes

from OpenGL import GL
from OpenGL.GL import shaders

import numpy as np

from helpers import *
from Transformer import Transformer

import numpy as np


class baseObj3D():
    def __init__(self):
        self.model = np.identity(4)
        self.shaderProgram = None
        self.vao = None
        self.vbo = None
        self.ebo = None
        self.vertices = None
        self.faces = None

        # probably should not be here
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
        # unsure of the correct order here
        self.model = matrix @ self.model

    def translate(self, dx, dy, dz):
        matrix = Transformer.translate(dx, dy, dz)
        self.transform(matrix)

    def rotate(self, angleX, angleY, angleZ):
        matrix = Transformer.rotate(angleX, angleY, angleZ)
        self.transform(matrix)

    def scale(self, dx, dy, dz):
        matrix = Transformer.scale(dx, dy, dz)
        self.transform(matrix)

    def scaleAll(self, s):
        self.scale(s, s, s)

    # -----------------------------

    def setColor(self, r, g, b, a):
        for i in range(int(self.vertices.nbytes // 2), len(self.vertices), 4):
            self.vertices[i] = r
            self.vertices[i + 1] = g
            self.vertices[i + 2] = b
            self.vertices[i + 3] = a

    def display(self, camera):

        LookMatrix = camera.getViewMatrix()

        fov = np.radians(60)
        aspect_ratio = 4.0 / 3.0
        near = 0.1
        far = 100.0

        PerspectiveMatrix = camera.getPerspectiveMatrix(
            fov, aspect_ratio, near, far)

        # active shader program
        GL.glUseProgram(self.shaderProgram)

        # set the model matrix
        modelLoc = GL.glGetUniformLocation(self.shaderProgram, "model")
        cameraLoc = GL.glGetUniformLocation(self.shaderProgram, "viewMatrix")
        persLoc = GL.glGetUniformLocation(self.shaderProgram, "perspective")

        GL.glUniformMatrix4fv(modelLoc, 1, False, self.model)
        GL.glUniformMatrix4fv(persLoc, 1, True, PerspectiveMatrix)
        GL.glUniformMatrix4fv(cameraLoc, 1, True, LookMatrix)

        try:

            # Activate the object
            GL.glBindVertexArray(self.vao)

            # draw triangle
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)

            GL.glDrawArrays(GL.GL_TRIANGLES, 0, int(self.vertices.nbytes / 16))

            # update camera position
            camera.moveCamera()

        finally:
            # Cleanup (just in case)
            GL.glBindVertexArray(0)
            GL.glUseProgram(0)
