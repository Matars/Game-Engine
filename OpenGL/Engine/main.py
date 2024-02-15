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

    # objects = createPaintingObjects()
    objects = createFromMesh()

    # camera settings
    initCameraPos = [0, 0, 20]
    camTarget = [0, 0, 0]

    # light settings
    initLightPos = [0.0, 0.0, 0.0]
    ambInt = 0.3
    ambCol = [1.0, 1.0, 1.0]

    camera = Camera(initCameraPos, camTarget)
    light = Light(initLightPos, ambInt, ambCol)

    scene = Scene(objects, camera, light)

    Engine.run(scene, vertexShaderStr, fragmentShaderStr)


def createPaintingObjects() -> list[cube3D]:

    painting_edvard = cube3D("gfx/Edvard_Munch.jpeg")
    painting_franz = cube3D("gfx/Franz_von_Stuck.jpeg")

    wall1 = cube3D("gfx/bricks.png")
    wall2 = cube3D("gfx/bricks.png")
    wall3 = cube3D("gfx/bricks.png")
    wall4 = cube3D("gfx/bricks.png")

    wall1.scale(50, 30, 0.1)

    wall2.rotate(0, 90, 0)
    wall2.translate(-25, 0, 20)
    wall2.scale(50, 30, 0.1)

    wall3.translate(0, 0, 50)
    wall3.scale(50, 30, 0.1)

    wall4.rotate(0, 90, 0)
    wall4.translate(-25, 0, -20)
    wall4.scale(50, 30, 0.2)

    # the kiss
    painting_thekiss = cube3D("gfx/the_kiss.png")
    frame_thekiss = cube3D("gfx/frame1.png")

    frame_thekiss.scale(10, 17, 0.1)
    painting_thekiss.scale(9, 16, 0.1)

    painting_thekiss.translate(0, 0, 2)
    frame_thekiss.translate(0, 0, 1)

    # vince
    painting_vince = cube3D("gfx/Vincent.jpeg")
    frame_vince = cube3D("gfx/frame2.png")

    painting_vince.rotate(0, -90, 0)
    frame_vince.rotate(0, -90, 0)

    painting_vince.translate(25, 0, -19)
    frame_vince.translate(25, 0, -19.5)

    frame_vince.scale(10, 17, 0.1)
    painting_vince.scale(9, 16, 0.1)

    # franz
    painting_franz = cube3D("gfx/Franz_von_Stuck.jpeg")
    frame_franz = cube3D("gfx/frame3.png")

    painting_franz.rotate(0, 90, 0)
    frame_franz.rotate(0, 90, 0)

    painting_franz.translate(-25, 0, -19)
    frame_franz.translate(-25, 0, -19.5)

    painting_franz.scale(9, 16, 0.1)
    frame_franz.scale(10, 17, 0.1)

    # evard
    painting_edvard = cube3D("gfx/Edvard_Munch.jpeg")
    frame_edvard = cube3D("gfx/frame4.png")

    painting_edvard.translate(0, 0, 49.5)
    frame_edvard.translate(0, 0, 49.7)

    frame_edvard.scale(10, 17, 0.1)
    painting_edvard.scale(9, 16, 0.1)

    objects = [wall1, wall2, wall3, wall4, painting_thekiss, frame_thekiss, painting_vince,
               frame_vince, painting_franz, frame_franz, painting_edvard, frame_edvard]

    return objects


def createFromMesh() -> list[cube3D]:
    # create a cube
    cube = cube3D("gfx/plane.png")

    return [cube]


if __name__ == "__main__":
    run()
