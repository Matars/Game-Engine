import Engine

from objects.cube import cube3D
from scene import Scene
from camera import Camera
from light import Light

def run():
    # get camera position
    with open("shaders/vertex.txt", "r") as f:
        vertexShaderStr = f.read()
    with open("shaders/fragment.txt", "r") as f:
        fragmentShaderStr = f.read()

    # objects = createObjects()
    objects = createPaintingObjects()

    initCameraPos = [0, 0, 20]
    camTarget = [0, 0, 0]
    initLightPos = [0.0, 0.0, 0.0]
    
    camera = Camera(initCameraPos, camTarget)
    light = Light(initLightPos)

    scene = Scene(objects, camera, light)

    Engine.run(scene, vertexShaderStr, fragmentShaderStr)


def createPaintingObjects() -> list[cube3D]:

    painting = cube3D()

    painting.scale(9, 16, 0.1)

    objects = [painting]

    return objects


if __name__ == "__main__":
    run()
