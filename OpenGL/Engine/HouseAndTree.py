import Engine

import numpy as np
from obj.cube import cube
from obj.prism import prism


def run():
    # get camera position
    with open("shaders/vertex.txt", "r") as f:
        vertexShaderStr = f.read()
    with open("shaders/fragment.txt", "r") as f:
        fragmentShaderStr = f.read()

    vertexData = cube()
    houseBox = Engine.openGL3dObject(vertexData)

    houseBox.scaleAll(0.15)
    houseBox.rotate(45, 45, 0)
    houseBox.scale(1, 2, 2)
    houseBox.translate(2, -0.5, 0)

    vertexData = prism()
    roof = Engine.openGL3dObject(vertexData)
    roof.scaleAll(0.2)
    roof.rotate(45, 45, 0)
    roof.scale(1, 1.5, 1.7)
    roof.translate(1.5, 1, 0)

    objects = [roof, houseBox]

    Engine.run(objects, vertexShaderStr, fragmentShaderStr)


if __name__ == "__main__":
    run()
