import ctypes
from OpenGL import GL


class Triangle:
    def __init__(self, vertexData):
        self.vertexData = vertexData
        self.VAO = None
        self.VBO = None
        self.setup()

    def setup(self):
        self.VAO = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.VAO)

        self.VBO = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.VBO)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertexData.nbytes, self.vertexData, GL.GL_STATIC_DRAW)

        # Position attribute
        GL.glEnableVertexAttribArray(0)
        # 32 = stride, each vertex has 8 floats (4 for position, 4 for color)
        GL.glVertexAttribPointer(0, 4, GL.GL_FLOAT, GL.GL_FALSE, 32, None)

        # Color attribute
        GL.glEnableVertexAttribArray(1)
        # 16 = offset, color data starts after the first 4 floats
        GL.glVertexAttribPointer(1, 4, GL.GL_FLOAT, GL.GL_FALSE, 32, ctypes.c_void_p(16))

        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glBindVertexArray(0)

    def render(self, shaderProgram):
        GL.glUseProgram(shaderProgram)
        GL.glBindVertexArray(self.VAO)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
        GL.glBindVertexArray(0)
        GL.glUseProgram(0)

    def update_buffer(self):
        # Bind the VAO and VBO
        GL.glBindVertexArray(self.VAO)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.VBO)

        # Update the buffer data
        GL.glBufferSubData(GL.GL_ARRAY_BUFFER, 0, self.vertexData.nbytes, self.vertexData)

        # Unbind the VAO and VBO
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glBindVertexArray(0)
