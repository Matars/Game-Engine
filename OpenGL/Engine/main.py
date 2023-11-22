import sys
from shaderStr import shaderStr
import Engine
import numpy


def getVertexData():

    # sweden
    FlagBackground = numpy.array([0, 0, 1, 1.0], dtype=numpy.float32)
    FlagStripes = numpy.array([1, 1, 0, 1.0], dtype=numpy.float32)

    # danish
    # FlagBackground = numpy.array([1, 0, 0, 1.0], dtype=numpy.float32)
    # FlagStripes = numpy.array([1, 1, 1, 1.0], dtype=numpy.float32)

    # finish
    # FlagBackground = numpy.array([0, 0, 1, 1.0], dtype=numpy.float32)
    # FlagStripes = numpy.array([1, 1, 1, 1.0], dtype=numpy.float32)

    bg = numpy.array([0.2, 0.2, 0.2, 1.0], dtype=numpy.float32)

    rectangle_specs = [
        {'offset': numpy.array(
            [-1, -0.5], dtype=numpy.float32), 'color': FlagBackground},
        {'offset': numpy.array(
            [-0.5, -0.5], dtype=numpy.float32), 'color': FlagStripes},
        {'offset': numpy.array(
            [0, -0.5], dtype=numpy.float32), 'color': FlagBackground},
        {'offset': numpy.array(
            [0.5, -0.5], dtype=numpy.float32), 'color': FlagBackground},

        {'offset': numpy.array([-1, 0], dtype=numpy.float32),
         'color': FlagStripes},
        {'offset': numpy.array(
            [-0.5, 0], dtype=numpy.float32), 'color': FlagStripes},
        {'offset': numpy.array([0, 0], dtype=numpy.float32),
         'color': FlagStripes},
        {'offset': numpy.array(
            [0.5, 0], dtype=numpy.float32), 'color': FlagStripes},

        {'offset': numpy.array(
            [-1, 0.5], dtype=numpy.float32), 'color': FlagBackground},
        {'offset': numpy.array(
            [-0.5, 0.5], dtype=numpy.float32), 'color': FlagStripes},
        {'offset': numpy.array([0, 0.5], dtype=numpy.float32),
         'color': FlagBackground},
        {'offset': numpy.array(
            [0.5, 0.5], dtype=numpy.float32), 'color': FlagBackground},

        {'offset': numpy.array([-1, 1], dtype=numpy.float32), 'color': bg},
        {'offset': numpy.array([-0.5, 1], dtype=numpy.float32), 'color': bg},
        {'offset': numpy.array([0, 1], dtype=numpy.float32), 'color': bg},
        {'offset': numpy.array([0.5, 1], dtype=numpy.float32), 'color': bg},

    ]

    vertexData = createRectangles(rectangle_specs)

    return vertexData


def createRectangles(specs):
    all_triangles = []
    for spec in specs:
        offset, color = spec['offset'], spec['color']
        triangles = rectangle(offset, color)
        all_triangles.extend(triangles)
    return numpy.array(all_triangles)


def rectangle(offset, color):
    # offset: numpy array like numpy.array([offset_x, offset_y])
    # color: numpy array like numpy.array([r, g, b, a])
    scale = 0.5
    width = 0.336 * scale
    height = 0.5 * scale
    offset = offset * scale

    triangles = [
        numpy.array([
            -width + offset[0],  width +
            offset[1],  0.0, 1.0, color[0], color[1], color[2], color[3],
            width + offset[0], -height +
            offset[1], 0.0, 1.0, color[0], color[1], color[2], color[3],
            -width + offset[0], -height +
            offset[1], 0.0, 1.0, color[0], color[1], color[2], color[3],
        ], dtype=numpy.float32),
        numpy.array([
            -width + offset[0],  width +
            offset[1],  0.0, 1.0, color[0], color[1], color[2], color[3],
            width + offset[0],  width +
            offset[1],  0.0, 1.0, color[0], color[1], color[2], color[3],
            width + offset[0], -height +
            offset[1], 0.0, 1.0, color[0], color[1], color[2], color[3],
        ], dtype=numpy.float32)
    ]
    return triangles


def run():
    shadersStrings = shaderStr()

    vertexData = getVertexData()

    vertexShaderStr = shadersStrings.getVertexShader()
    fragmentShaderStr = shadersStrings.getFragmentShader()

    Engine.run(vertexData, vertexShaderStr, fragmentShaderStr)


if __name__ == "__main__":
    sys.exit(run())
