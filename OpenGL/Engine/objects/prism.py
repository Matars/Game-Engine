import numpy as np

from objects.baseObj import baseObj3D

# UNUSED

class prism3D(baseObj3D):
    def __init__(self):
        super().__init__()
        self.vertices = self.prismMesh()

    def prismMesh(self):
        vertexData = np.array([
            # Vertex Positions
            # x      # y      # z     # w
            # bottom
            -1,    -1,    -1,    1.0,
            -1,    -1,   1,    1.0,
            1,    -1,    1,    1.0,

            1,      -1,    -1,    1.0,
            -1,    -1,    -1,    1.0,
            1,     -1,    1,    1.0,

            # front
            0,    1,    1,    1.0,
            -1,    -1,   1,    1.0,
            1,    -1,    1,    1.0,

            # back
            0,    1,    -1,    1.0,
            -1,    -1,   -1,    1.0,
            1,    -1,    -1,    1.0,

            # left
            0,    1,    -1,    1.0,
            -1,    -1,   -1,    1.0,
            -1,    -1,    1,    1.0,

            0,    1,    -1,    1.0,
            -1,   -1,    1,    1.0,
            0,    1,    1,    1.0,

            # right
            0,    1,    -1,    1.0,
            1,    -1,   -1,    1.0,
            1,    -1,    1,    1.0,

            0,    1,    -1,    1.0,
            1,   -1,    1,    1.0,
            0,    1,    1,    1.0,




            # Vertex Colours
            # R       # G     # B     # A
            0.0,      0.0,    0.0,    1.0,
            0.0,      0.0,    0.0,    1.0,
            0.0,      0.0,    0.0,    1.0,

            0.0,      0.0,    0.0,    1.0,
            0.0,      0.0,    0.0,    1.0,
            0.0,      0.0,    0.0,    1.0,

            1.0,      0.0,    1.0,    1.0,
            1.0,      0.0,    1.0,    1.0,
            1.0,      0.0,    1.0,    1.0,

            1.0,      0.0,    1.0,    1.0,
            1.0,      0.0,    1.0,    1.0,
            1.0,      0.0,    1.0,    1.0,

            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,

            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,

            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,

            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,
            1.0,      1.0,    1.0,    1.0,], dtype=np.float32)

        return vertexData
