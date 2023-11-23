import sys
from shaderStr import shaderStr
import Engine
import numpy
import sdl2


def getFlagData():
    inputChoice = input("1. swe \n2. dan \n3. fin\n Input: ")

    if inputChoice == "1":
        vertexData = numpy.array([
            # Vertex Positions
            # x      # y      # z     # w

            # background
            -0.5,    0.3,    0.0,    1.0,
            -0.5,    -0.3,   0.0,    1.0,
            0.5,    -0.3,    0.0,    1.0,

            0.5,     0.3,    0.0,    1.0,
            -0.5,    0.3,    0.0,    1.0,
            0.5,    -0.3,    0.0,    1.0,


            # stripes
            -0.3,   0.3,      0.0,   1.0,
            -0.23,   0.3,      0.0,   1.0,
            -0.3,   -0.3,     0.0,   1.0,

            -0.3,    -0.3,     0.0,   1.0,
            -0.23,    -0.3,     0.0,   1.0,
            -0.23,     0.3,     0.0,   1.0,

            -0.5,     0.05,     0.0,   1.0,
            -0.5,    -0.05,     0.0,   1.0,
            0.5,    -0.05,     0.0,   1.0,

            -0.5,     0.05,     0.0,   1.0,
            0.5,      0.05,     0.0,   1.0,
            0.5,      -0.05,     0.0,   1.0,


            # Vertex Colours
            # R       # G     # B     # A
            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,

            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,

            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0,

            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0,

            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0,

            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0,
            0.9,      1.0,    0.0,    1.0
        ], dtype=numpy.float32)
        return vertexData

    elif inputChoice == "2":
        vertexData = numpy.array([
            # Vertex Positions
            # x      # y      # z     # w

            # background
            -0.5,    0.3,    0.0,    1.0,
            -0.5,    -0.3,   0.0,    1.0,
            0.5,    -0.3,    0.0,    1.0,

            0.5,     0.3,    0.0,    1.0,
            -0.5,    0.3,    0.0,    1.0,
            0.5,    -0.3,    0.0,    1.0,


            # stripes
            -0.3,   0.3,      0.0,   1.0,
            -0.23,   0.3,      0.0,   1.0,
            -0.3,   -0.3,     0.0,   1.0,

            -0.3,    -0.3,     0.0,   1.0,
            -0.23,    -0.3,     0.0,   1.0,
            -0.23,     0.3,     0.0,   1.0,

            -0.5,     0.05,     0.0,   1.0,
            -0.5,    -0.05,     0.0,   1.0,
            0.5,    -0.05,     0.0,   1.0,

            -0.5,     0.05,     0.0,   1.0,
            0.5,      0.05,     0.0,   1.0,
            0.5,      -0.05,     0.0,   1.0,


            # Vertex Colours
            # R       # G     # B     # A
            1.0,      0.0,    0.0,    1.0,
            1.0,      0.0,    0.0,    1.0,
            1.0,      0.0,    0.0,    1.0,

            1.0,      0.0,    0.0,    1.0,
            1.0,      0.0,    0.0,    1.0,
            1.0,      0.0,    0.0,    1.0,

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
            1.0,      1.0,    1.0,    1.0
        ], dtype=numpy.float32)
        return vertexData
    elif inputChoice == "3":
        vertexData = numpy.array([
            # Vertex Positions
            # x      # y      # z     # w

            # background
            -0.5,    0.3,    0.0,    1.0,
            -0.5,    -0.3,   0.0,    1.0,
            0.5,    -0.3,    0.0,    1.0,

            0.5,     0.3,    0.0,    1.0,
            -0.5,    0.3,    0.0,    1.0,
            0.5,    -0.3,    0.0,    1.0,


            # stripes
            -0.3,   0.3,      0.0,   1.0,
            -0.23,   0.3,      0.0,   1.0,
            -0.3,   -0.3,     0.0,   1.0,

            -0.3,    -0.3,     0.0,   1.0,
            -0.23,    -0.3,     0.0,   1.0,
            -0.23,     0.3,     0.0,   1.0,

            -0.5,     0.05,     0.0,   1.0,
            -0.5,    -0.05,     0.0,   1.0,
            0.5,    -0.05,     0.0,   1.0,

            -0.5,     0.05,     0.0,   1.0,
            0.5,      0.05,     0.0,   1.0,
            0.5,      -0.05,     0.0,   1.0,


            # Vertex Colours
            # R       # G     # B     # A
            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,

            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,
            0.0,      0.0,    1.0,    1.0,

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
            1.0,      1.0,    1.0,    1.0
        ], dtype=numpy.float32)
        return vertexData


def getVertexData():
    vertexData = getFlagData()

    return vertexData


def run():
    shadersStrings = shaderStr()

    vertexData = getVertexData()

    vertexShaderStr = shadersStrings.getVertexShader()
    fragmentShaderStr = shadersStrings.getFragmentShader()

    Engine.run(vertexData, vertexShaderStr, fragmentShaderStr)


if __name__ == "__main__":
    sys.exit(run())
