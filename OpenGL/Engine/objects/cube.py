import numpy as np

from objects.baseObj import baseObj3D


class cube3D(baseObj3D):
    def __init__(self, r, g, b, a):
        super().__init__()
        self.vertices = self.cubeMesh(r, g, b, a)

    def changeSideColor(self, side: int, r: float, g: float, b:float, a: float=1) -> None:
        """
        Change the color of a side of the cube.

        Args:
            side (int): 0-5 for each side
            r (float): 0-1
            g (float): 0-1
            b (float): 0-1
            a (float, optional): 0-1. Defaults to 1.
        """
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
