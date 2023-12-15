import Engine

import numpy as np
from objects.cube import cube3D
from objects.prism import prism3D
from objects.sphere import sphere3D
from scene import Scene
from camera import Camera


def run():
    # get camera position
    with open("shaders/vertex.txt", "r") as f:
        vertexShaderStr = f.read()
    with open("shaders/fragment.txt", "r") as f:
        fragmentShaderStr = f.read()

    cubeLeft = cube3D(1.0, 0.0, 0.0, 1.0)
    cubeMiddle = cube3D(0.0, 1.0, 0.0, 1.0)
    cubeRight = cube3D(0.0, 0.0, 1.0, 1.0)

    cubeLeft.translate(-2.5, 0, 0)
    cubeMiddle.translate(0, 0, 0)
    cubeRight.translate(2.5, 0, 0)

    cubeLeft.rotate(45, 0, 0)
    cubeMiddle.rotate(0, 45, 0)
    cubeRight.rotate(0, 0, 45)

    for sidie in range(6):
        from random import random
        cubeLeft.changeSideColor(sidie, random(), random(), random())
        cubeMiddle.changeSideColor(sidie, random(), random(), random())
        cubeRight.changeSideColor(sidie, random(), random(), random())

    floor = cube3D(0.0, 0.0, 0.0, 1.0)
    floor.translate(0, -1.5, 0)
    floor.setColor(0.8, 0.8, 0.8)
    floor.scale(25, 0, 25)

    objects = [cubeLeft, cubeMiddle, cubeRight, floor]

    initCameraPos = [2, 5, 2]
    camTarget = [0, 0, 0]
    camera = Camera(initCameraPos, camTarget)

    scene = Scene(objects, camera)

    Engine.run(scene, vertexShaderStr, fragmentShaderStr)


if __name__ == "__main__":
    run()
