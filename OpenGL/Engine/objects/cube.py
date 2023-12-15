import numpy as np

from objects.baseObj import baseObj3D
from helpers import normalize


class cube3D(baseObj3D):
    def __init__(self, r, g, b, a):
        super().__init__()
        # self.data = self.loadMesh("objects\objectsMesh\cubeMesh.obj")

        self.vertices = self.cubeMesh(r, g, b, a)

    def loadMesh(self, mesh_path):
        self.vertices, self.faces = loadObjMesh(mesh_path)
        return self.vertices, self.faces

    def changeSideColor(self, side, r, g, b, a=1):
        # verticies length
        colorsStart = len(self.vertices) // 2
        colorsStart += side * 24

        for i in range(colorsStart, colorsStart + 24, 4):
            self.vertices[i] = r
            self.vertices[i + 1] = g
            self.vertices[i + 2] = b
            self.vertices[i + 3] = a
    

    def cubeMesh(self, r, g, b, a):
        vertexData = np.array([
            # Vertex Positions
            # x      # y      # z     # w

            # front
            -0.5,    0.5,    0.5,    1.0,
            -0.5,    -0.5,   0.5,    1.0,
            0.5,    -0.5,    0.5,    1.0,

            0.5,      0.5,    0.5,    1.0,
            -0.5,    0.5,    0.5,    1.0,
            0.5,     -0.5,    0.5,    1.0,

            # back
            -0.5,    0.5,    -0.5,    1.0,
            -0.5,    -0.5,   -0.5,    1.0,
            0.5,    -0.5,    -0.5,    1.0,

            0.5,      0.5,    -0.5,    1.0,
            -0.5,    0.5,    -0.5,    1.0,
            0.5,     -0.5,    -0.5,    1.0,

            # left
            -0.5,    0.5,    -0.5,    1.0,
            -0.5,    -0.5,   -0.5,    1.0,
            -0.5,    -0.5,    0.5,    1.0,

            -0.5,      0.5,    0.5,    1.0,
            -0.5,    0.5,    -0.5,    1.0,
            -0.5,     -0.5,    0.5,    1.0,

            # right
            0.5,    0.5,    -0.5,    1.0,
            0.5,    -0.5,   -0.5,    1.0,
            0.5,    -0.5,    0.5,    1.0,

            0.5,      0.5,    0.5,    1.0,
            0.5,    0.5,    -0.5,    1.0,
            0.5,     -0.5,    0.5,    1.0,

            # bottom
            -0.5,    -0.5,    -0.5,    1.0,
            -0.5,    -0.5,   0.5,    1.0,
            0.5,    -0.5,    0.5,    1.0,

            0.5,      -0.5,    -0.5,    1.0,
            -0.5,    -0.5,    -0.5,    1.0,
            0.5,     -0.5,    0.5,    1.0,

            # top
            -0.5,    0.5,    -0.5,    1.0,
            -0.5,    0.5,   0.5,    1.0,
            0.5,    0.5,    0.5,    1.0,

            0.5,      0.5,    -0.5,    1.0,
            -0.5,    0.5,    -0.5,    1.0,
            0.5,     0.5,    0.5,    1.0,



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
