import numpy as np

from objects.baseObj import baseObj3D
from helpers import loadObjMesh


class cube3D(baseObj3D):
    def __init__(self, r, g, b, a):
        super().__init__()
        # self.data = self.loadMesh("objects\objectsMesh\cubeMesh.obj")
        # self.vertices = self.data[0]
        # self.faces = self.data[1]
        self.vertices = self.cubeMesh(r, g, b, a)

    def loadMesh(self, mesh_path):
        self.vertices, self.faces = loadObjMesh(mesh_path)
        return self.vertices, self.faces

    def cubeMesh(self, r, g, b, a):
        vertexData = np.array([
            # Vertex Positions
            # x      # y      # z     # w

            # front
            -1,    1,    1,    1.0,
            -1,    -1,   1,    1.0,
            1,    -1,    1,    1.0,

            1,      1,    1,    1.0,
            -1,    1,    1,    1.0,
            1,     -1,    1,    1.0,

            # back
            -1,    1,    -1,    1.0,
            -1,    -1,   -1,    1.0,
            1,    -1,    -1,    1.0,

            1,      1,    -1,    1.0,
            -1,    1,    -1,    1.0,
            1,     -1,    -1,    1.0,

            # left
            -1,    1,    -1,    1.0,
            -1,    -1,   -1,    1.0,
            -1,    -1,    1,    1.0,

            -1,      1,    1,    1.0,
            -1,    1,    -1,    1.0,
            -1,     -1,    1,    1.0,

            # right
            1,    1,    -1,    1.0,
            1,    -1,   -1,    1.0,
            1,    -1,    1,    1.0,

            1,      1,    1,    1.0,
            1,    1,    -1,    1.0,
            1,     -1,    1,    1.0,

            # bottom
            -1,    -1,    -1,    1.0,
            -1,    -1,   1,    1.0,
            1,    -1,    1,    1.0,

            1,      -1,    -1,    1.0,
            -1,    -1,    -1,    1.0,
            1,     -1,    1,    1.0,

            # top
            -1,    1,    -1,    1.0,
            -1,    1,   1,    1.0,
            1,    1,    1,    1.0,

            1,      1,    -1,    1.0,
            -1,    1,    -1,    1.0,
            1,     1,    1,    1.0,



            # Vertex Colours
            # R       # G     # B     # A
            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,

            r,      g,    b,    a,
            r,      g,    b,    a,
            r,      g,    b,    a,
        ], dtype=np.float32)

        return vertexData
