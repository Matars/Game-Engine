import sys
import ctypes

from OpenGL import GL
from OpenGL.GL import shaders

import numpy as np

from OpenGL.GL import *
from PIL import Image

from objects.objectsMesh.loadMeshTesting import loadMesh


class cube3D():
    def __init__(self, img_path=None):
        self.model = np.identity(4)
        self.vertices = self.cubeMesh()
        # self.vertices = loadMesh("objects\objectsMesh\plane.obj")

        self.shaderProgram = None
        self.vao = None
        self.vbo = None
        self.ebo = None  # unused
        self.faces = None  # unused
        self.textureID = None
        self.img_path = img_path

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
        # - size of each vertex: 3      (vec3)
        # - type of vertices: float
        # - do not normalize            (ignore for now)
        # - stride: 0                   (there is no space between vertices)
        # - offset: None                (start from the first element; no offset)
        GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 8*4, None)

        # The same for the second attribute: the color of each vertex
        GL.glEnableVertexAttribArray(1)

        # The last parameter is actually a pointer
        GL.glVertexAttribPointer(
            1, 3, GL.GL_FLOAT, GL.GL_FALSE, 8*4, ctypes.c_void_p(3*4))

        # Enable the third attribute
        GL.glEnableVertexAttribArray(2)

        # Describe the third attribute: the texture coordinates
        GL.glVertexAttribPointer(
            2, 2, GL.GL_FLOAT, GL.GL_FALSE, 8*4, ctypes.c_void_p(6*4))

        # Cleanup (just in case)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glBindVertexArray(0)

    def transform(self, matrix: np.ndarray) -> None:
        """
        Transforms the model by applying the given transformation matrix.

        Args:
            matrix: A 4x4 transformation matrix.
        """

        self.model = self.model @ matrix

    def translate(self, dx: float, dy: float, dz: float) -> None:
        """
        Translates the model by applying the given translation factors.

        Args:
            dx, dy, dz: The translation factors along the x, y, and z axes.
        """
        translationMatrix = np.identity(4)
        translationMatrix[0, 3] = dx
        translationMatrix[1, 3] = dy
        translationMatrix[2, 3] = dz

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

    # -----------------------------

    def configure_texture(self, image_path):
        # Load the image
        image = Image.open(image_path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()

        # Generate a new texture ID
        self.textureID = glGenTextures(1)

        # Bind the texture
        glBindTexture(GL_TEXTURE_2D, self.textureID)

        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Specify the texture image
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width,
                     image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        # Generate mipmaps
        glGenerateMipmap(GL_TEXTURE_2D)

    def cubeMesh(self):
        verticies = np.array([
            # Vertex Positions
            # x    y     z     nx    ny   nz, u, v

            -0.5, -0.5, -0.5,  0.0,  0.0, -1.0, 0.0, 0.0,
            0.5, -0.5, -0.5,  0.0,  0.0, -1.0, 1.0, 0.0,
            0.5,  0.5, -0.5,  0.0,  0.0, -1.0, 1.0, 1.0,
            0.5,  0.5, -0.5,  0.0,  0.0, -1.0, 1.0, 1.0,
            -0.5,  0.5, -0.5,  0.0,  0.0, -1.0, 0.0, 1.0,
            -0.5, -0.5, -0.5,  0.0,  0.0, -1.0, 0.0, 0.0,

            -0.5, -0.5,  0.5,  0.0,  0.0, 1.0, 0.0, 0.0,
            0.5, -0.5,  0.5,  0.0,  0.0, 1.0, 1.0, 0.0,
            0.5,  0.5,  0.5,  0.0,  0.0, 1.0, 1.0, 1.0,
            0.5,  0.5,  0.5,  0.0,  0.0, 1.0, 1.0, 1.0,
            -0.5,  0.5,  0.5,  0.0,  0.0, 1.0, 0.0, 1.0,
            -0.5, -0.5,  0.5,  0.0,  0.0, 1.0, 0.0, 0.0,

            -0.5,  0.5,  0.5, -1.0,  0.0,  0.0, 0.0, 0.0,
            -0.5,  0.5, -0.5, -1.0,  0.0,  0.0, 1.0, 0.0,
            -0.5, -0.5, -0.5, -1.0,  0.0,  0.0, 1.0, 1.0,
            -0.5, -0.5, -0.5, -1.0,  0.0,  0.0, 1.0, 1.0,
            -0.5, -0.5,  0.5, -1.0,  0.0,  0.0, 0.0, 1.0,
            -0.5,  0.5,  0.5, -1.0,  0.0,  0.0, 0.0, 0.0,

            0.5,  0.5,  0.5,  1.0,  0.0,  0.0,  0.0, 0.0,
            0.5,  0.5, -0.5,  1.0,  0.0,  0.0,  0.0, 1.0,
            0.5, -0.5, -0.5,  1.0,  0.0,  0.0,  1.0, 1.0,
            0.5, -0.5, -0.5,  1.0,  0.0,  0.0,  1.0, 1.0,
            0.5, -0.5,  0.5,  1.0,  0.0,  0.0,  1.0, 0.0,
            0.5,  0.5,  0.5,  1.0,  0.0,  0.0,  0.0, 0.0,

            -0.5, -0.5, -0.5,  0.0, -1.0,  0.0, 0.0, 0.0,
            0.5, -0.5, -0.5,  0.0, -1.0,  0.0,  0.0, 1.0,
            0.5, -0.5,  0.5,  0.0, -1.0,  0.0,  1.0, 1.0,
            0.5, -0.5,  0.5,  0.0, -1.0,  0.0,  1.0, 1.0,
            -0.5, -0.5,  0.5,  0.0, -1.0,  0.0, 1.0, 0.0,
            -0.5, -0.5, -0.5,  0.0, -1.0,  0.0, 0.0, 0.0,

            -0.5,  0.5, -0.5,  0.0,  1.0,  0.0,  0.0, 0.0,
            0.5,  0.5, -0.5,  0.0,  1.0,  0.0,  0.0, 1.0,
            0.5,  0.5,  0.5,  0.0,  1.0,  0.0,  1.0, 1.0,
            0.5,  0.5,  0.5,  0.0,  1.0,  0.0,  1.0, 1.0,
            -0.5,  0.5,  0.5,  0.0,  1.0,  0.0,  1.0, 0.0,
            -0.5,  0.5, -0.5,  0.0,  1.0,  0.0,  0.0, 0.0

        ], dtype=np.float32)

        return verticies


    def display(self, camera, light) -> None:
        """
        Displays the object.

        Args:
            camera (Camera): The camera object.
            light (Light): The light object.
        """

        LookMatrix = camera.getViewMatrix()
        PerspectiveMatrix = camera.getPerspectiveMatrix()

        # active shader program
        GL.glUseProgram(self.shaderProgram)

        # set the model matrix
        modelLoc = GL.glGetUniformLocation(self.shaderProgram, "model")
        cameraLoc = GL.glGetUniformLocation(self.shaderProgram, "viewMatrix")
        persLoc = GL.glGetUniformLocation(self.shaderProgram, "perspective")
        texture_location = GL.glGetUniformLocation(
            self.shaderProgram, "theTexture")

        GL.glUniformMatrix4fv(modelLoc, 1, True, self.model)
        GL.glUniformMatrix4fv(persLoc, 1, True, PerspectiveMatrix)
        GL.glUniformMatrix4fv(cameraLoc, 1, True, LookMatrix)

        lightpos = GL.glGetUniformLocation(self.shaderProgram, "lightPos")
        ambpos = GL.glGetUniformLocation(self.shaderProgram, "ambInt")
        ambcolpos = GL.glGetUniformLocation(self.shaderProgram, "ambCol")

        GL.glUniform3fv(lightpos, 1, light.getPos())
        GL.glUniform3fv(ambcolpos, 1, light.getAmbCol())
        GL.glUniform1f(ambpos, light.getAmbInt())

        GL.glUniform1i(texture_location, 0)

        try:

            # Activate the object
            GL.glBindVertexArray(self.vao)

            if self.textureID is None and self.img_path is not None:
                self.configure_texture(self.img_path)
                GL.glBindTexture(GL.GL_TEXTURE_2D, self.textureID)

            # draw triangle
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_FILL)

            GL.glDrawArrays(GL.GL_TRIANGLES, 0, int(self.vertices.nbytes / 16))

        finally:
            # Cleanup (just in case)
            GL.glBindVertexArray(0)
            GL.glUseProgram(0)
