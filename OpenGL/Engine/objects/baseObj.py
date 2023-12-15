import sys
import ctypes

from OpenGL import GL
from OpenGL.GL import shaders

import numpy as np

import numpy as np


class baseObj3D():
    def __init__(self):
        self.model = np.identity(4)
        self.shaderProgram = None
        self.vao = None
        self.vbo = None
        self.ebo = None  # unused
        self.vertices = None
        self.faces = None  # unused

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

    def transform(self, matrix: np.ndarray) -> None:
        """
        Transforms the model by applying the given transformation matrix.

        Args:
            matrix: A 4x4 transformation matrix.
        """

        self.model = matrix @ self.model

    def translate(self, dx: float, dy: float, dz: float) -> None:
        """
        Translates the model by applying the given translation factors.

        Args:
            dx, dy, dz: The translation factors along the x, y, and z axes.
        """
        translationMatrix = np.identity(4)
        translationMatrix[3, 0] = dx
        translationMatrix[3, 1] = dy
        translationMatrix[3, 2] = dz

        self.transform(translationMatrix)

    def rotate(self, angleX: float, angleY: float, angleZ: float) -> None:
        from math import cos, sin
        """
        Rotates the model by applying the given rotation angle around the given axis.

        Args:
            angleX, angleY, angleZ: The rotation angles around the x, y, and z axes.

        References:
            https://i.imgur.com/0cu8maY.png

        """

        # turn the angles into radians
        angleX = np.radians(angleX)
        angleY = np.radians(angleY)
        angleZ = np.radians(angleZ)

        Rz = np.identity(4)
        Ry = np.identity(4)
        Rx = np.identity(4)

        Rz[0, 0] = cos(angleZ)
        Rz[0, 1] = -sin(angleZ)
        Rz[1, 0] = sin(angleZ)
        Rz[1, 1] = cos(angleZ)

        Ry[0, 0] = cos(angleY)
        Ry[0, 2] = sin(angleY)
        Ry[2, 0] = -sin(angleY)
        Ry[2, 2] = cos(angleY)

        Rx[1, 1] = cos(angleX)
        Rx[1, 2] = -sin(angleX)
        Rx[2, 1] = sin(angleX)
        Rx[2, 2] = cos(angleX)

        rotationMatrix = Rz @ Ry @ Rx

        self.transform(rotationMatrix)

    def scale(self, dx: float, dy: float, dz: float) -> None:
        """
        Scales the model by applying the given scale factors.

        Args:
            dx, dy, dz: The scale factors along the x, y, and z axes.
        """
        scaleMatrix = np.identity(4)
        scaleMatrix[0, 0] = dx
        scaleMatrix[1, 1] = dy
        scaleMatrix[2, 2] = dz

        self.transform(scaleMatrix)

    def scaleAll(self, s: float) -> None:
        """
        Scales the model by applying the given scale factor to all axes.

        Args:
            s (float): scale factor
        """
        self.scale(s, s, s)

    def setColor(self, r: float, g: float, b: float, a: float = 1) -> None:
        """
        Sets the color of the object.

        Args:
            r (float): 0-1
            g (float): 0-1
            b (float): 0-1
            a (float, optional): 0-1. Defaults to 1.
        """
        # verticies length
        colorsStart = len(self.vertices) // 2

        for i in range(colorsStart, len(self.vertices), 4):
            self.vertices[i] = r
            self.vertices[i + 1] = g
            self.vertices[i + 2] = b
            self.vertices[i + 3] = a

    # -----------------------------

    def display(self, camera) -> None:
        """
        Displays the object.

        Args:
            camera (Camera): The camera object.
        """

        LookMatrix = camera.getViewMatrix()
        PerspectiveMatrix = camera.getPerspectiveMatrix()

        # active shader program
        GL.glUseProgram(self.shaderProgram)

        # set the model matrix
        modelLoc = GL.glGetUniformLocation(self.shaderProgram, "model")
        cameraLoc = GL.glGetUniformLocation(self.shaderProgram, "viewMatrix")
        persLoc = GL.glGetUniformLocation(self.shaderProgram, "perspective")

        # not sure why but setting transpose to true breaks it
        GL.glUniformMatrix4fv(modelLoc, 1, False, self.model)
        GL.glUniformMatrix4fv(persLoc, 1, True, PerspectiveMatrix)
        GL.glUniformMatrix4fv(cameraLoc, 1, True, LookMatrix)

        try:

            # Activate the object
            GL.glBindVertexArray(self.vao)

            # draw triangle
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_FILL)

            GL.glDrawArrays(GL.GL_TRIANGLES, 0, int(self.vertices.nbytes / 16))

            # update camera position
            camera.moveCamera()

        finally:
            # Cleanup (just in case)
            GL.glBindVertexArray(0)
            GL.glUseProgram(0)
