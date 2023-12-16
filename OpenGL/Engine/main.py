import Engine

from objects.cube import cube3D
from scene import Scene
from camera import Camera


def run():
    # get camera position
    with open("shaders/vertex.txt", "r") as f:
        vertexShaderStr = f.read()
    with open("shaders/fragment.txt", "r") as f:
        fragmentShaderStr = f.read()

    objects = createObjects()

    initCameraPos = [2, 5, 2]
    camTarget = [0, 0, 0]
    camera = Camera(initCameraPos, camTarget)

    scene = Scene(objects, camera)

    Engine.run(scene, vertexShaderStr, fragmentShaderStr)


def createObjects() -> list[cube3D]:
    """
    Create a list of objects to be rendered.

    Returns:
        list[cube3D]: Three cubes and a floor.
    """
    cubeLeft = cube3D(1.0, 0.0, 0.0, 1.0)
    cubeMiddle = cube3D(0.0, 1.0, 0.0, 1.0)
    cubeRight = cube3D(0.0, 0.0, 1.0, 1.0)

    cubeLeft.translate(-2.5, 0, 0)
    cubeMiddle.translate(0, 0, 0)
    cubeRight.translate(2.5, 0, 0)

    cubeMiddle.scale(2, 2, 2)

    cubeLeft.rotate(45, 0, 0)
    cubeMiddle.rotate(0, 45, 0)
    cubeRight.rotate(0, 0, 45)

    for side in range(6):
        from random import random
        cubeLeft.changeSideColor(side, random(), random(), random())
        cubeMiddle.changeSideColor(side, random(), random(), random())
        cubeRight.changeSideColor(side, random(), random(), random())

    floor = cube3D(0.0, 0.0, 0.0, 1.0)
    floor.translate(0, -1.5, 0)
    floor.setColor(0.8, 0.8, 0.8)
    floor.scale(25, 0, 25)

    objects = [cubeLeft, cubeMiddle, cubeRight, floor]
    return objects


if __name__ == "__main__":
    run()
