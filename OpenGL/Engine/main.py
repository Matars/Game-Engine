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

    cubeRed = cube3D(1.0, 0.0, 0.0, 1.0)
    cubeGreen = cube3D(0.0, 1.0, 0.0, 1.0)
    cubeBlue = cube3D(0.0, 0.0, 1.0, 1.0)

    cubeRed.scaleAll(0.15)
    cubeGreen.scaleAll(0.15)
    cubeBlue.scaleAll(0.15)

    cubeRed.translate(-2.5, 0, 0)
    cubeGreen.translate(0, 0, 0)
    cubeBlue.translate(2.5, 0, 0)

    cubeRed.rotate(45, 0, 0)
    cubeGreen.rotate(0, 45, 0)
    cubeBlue.rotate(0, 0, 45)

    for sidie in range(6):
        from random import random
        cubeRed.changeSideColor(sidie, random(), random(), random())
        cubeGreen.changeSideColor(sidie, random(), random(), random())
        cubeBlue.changeSideColor(sidie, random(), random(), random())

    floor = cube3D(0.0, 0.0, 0.0, 1.0)
    floor.translate(0, -0.5, 0)
    floor.setColor(0.8, 0.8, 0.8)
    floor.scale(5, 0, 5)

    objects = [cubeRed, cubeGreen, cubeBlue, floor]

    Engine.run(objects, vertexShaderStr, fragmentShaderStr)


if __name__ == "__main__":
    run()
