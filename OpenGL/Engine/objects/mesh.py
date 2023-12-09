import numpy as np


from OpenGL import GL
from OpenGL.GL import shaders


class Mesh:
    """
        A mesh that can represent an obj model.
    """

    def __init__(self, filename: str):
        """
            Initialize the mesh.
        """

        # x, y, z, s, t, nx, ny, nz
        self.vertices = self.loadMesh(filename)
        self.vertex_count = len(self.vertices)//8
        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)

        # self.vertices
        self.vbo = glGenBuffers(1)
        GL.glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        GL.glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        # position
        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))




if __name__ == "__main__":
    self.vertices = Mesh("objects/objectsMesh/cubeMesh.obj")
    print(self.vertices)
