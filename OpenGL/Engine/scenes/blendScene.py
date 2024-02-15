
from objects.cube import cube3D
from scene import Scene
from camera import Camera
from light import Light

from math import sin
from time import time


def scene():
    StationaryCube = cube3D()
    movingCube = cube3D()
    movingCube.translate(1, 0, 0)
    movingCube.rotate(45, 45, 0)
    movingCube.scaleAll(0.75)

    objects = [StationaryCube, movingCube]

    camera = Camera(initialPos=[0.0, 0.0, 5.0])
    # light settings
    initLightPos = [0.0, 0.0, 0.0]
    ambInt = 0.3
    ambCol = [1.0, 1.0, 1.0]

    light = Light(initLightPos, ambInt, ambCol)
    scene = Scene(objects, camera, light)

    return scene
