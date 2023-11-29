from Engine import Engine
from Engine import shaderStr


def getVertexData():
    pass
    # return vertexData


def run():
    shadersStrings = shaderStr()

    vertexData = getVertexData()

    vertexShaderStr = shadersStrings.getVertexShader()
    fragmentShaderStr = shadersStrings.getFragmentShader()

    Engine.run(vertexData, vertexShaderStr, fragmentShaderStr)


if __name__ == "__main__":
    run()
