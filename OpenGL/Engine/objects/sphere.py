
import numpy as np
from OpenGL import GL
from math import cos, sin, pi

from objects.baseObj import baseObj3D

import numpy as np

# UNUSED

class sphere3D(baseObj3D):
    def __init__(self, radius, mun_segments):
        self.vertices = self.sphereMesh(radius, mun_segments)

        self.transform(np.identity(4))

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
            GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, int(self.vertices.nbytes / 4))

        finally:
            # Cleanup (just in case)
            GL.glBindVertexArray(0)
            GL.glUseProgram(0)

    def sphereMesh(self, radius, num_segments):
        """
        Generates the vertices for a sphere.

        Args:
            radius (float): The radius of the sphere.
            num_segments (int): The number of segments to divide the sphere into.

        Returns:
            numpy.ndarray: The vertices of the sphere.
        """
        vertices = []

        for i in range(num_segments):
            lat = pi * i / num_segments - pi / 2
            for j in range(num_segments):
                lon = 2 * pi * j / num_segments

                dx = radius * cos(lat) * cos(lon)
                dy = radius * cos(lat) * sin(lon)
                dz = radius * sin(lat)

                vertices.extend([dx, dy, dz, 1.0])  # 1.0 for w-coordinate

        for i in range(len(vertices) // 4):
            vertices.extend([1.0, 0.0, 0.0, 1.0])  # red

        return np.array(vertices, dtype=np.float32)
