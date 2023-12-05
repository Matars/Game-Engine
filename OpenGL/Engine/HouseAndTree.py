import Engine

import numpy as np
from objects.cube import cube3D
from objects.prism import prism3D
from objects.sphere import sphere3D


def run():
    # get camera position
    with open("shaders/vertex.txt", "r") as f:
        vertexShaderStr = f.read()
    with open("shaders/fragment.txt", "r") as f:
        fragmentShaderStr = f.read()

    houseBox = cube3D(0.0, 0.0, 1.0, 1.0)

    houseBox.scaleAll(0.15)
    houseBox.rotate(45, 45, 0)
    houseBox.scale(1, 2, 2)
    houseBox.translate(2, -0.5, 0)

    roof = prism3D()
    roof.scaleAll(0.2)
    roof.rotate(45, 45, 0)
    roof.scale(1, 2, 1.7)
    roof.translate(1.5, 1, 0)

    treebase = cube3D(0.3, 0.25, 0.0, 1.0)
    treebase.scaleAll(0.1)
    treebase.rotate(45, 45, 0)
    treebase.scale(0.5, 2.5, 0.5)
    treebase.translate(-15, -0.5, 0)

    tree = cube3D(0, 1, 0, 1)
    tree.scaleAll(0.1)
    tree.rotate(45, 45, 0)
    tree.scale(1.5, 2, 1.7)
    tree.translate(-5, 1, 0)

    # circle and spehre r broken
    objects = [houseBox, roof, treebase, tree]

    Engine.run(objects, vertexShaderStr, fragmentShaderStr)


if __name__ == "__main__":
    run()
