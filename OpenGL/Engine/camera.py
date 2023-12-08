
import numpy as np
from helpers import *


class Camera:
    def __init__(self) -> None:
        self.cameraPos = np.array([0.0, 1.0, 3.0], dtype=np.float32)
        self.cameraTarget = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.upvector = np.array([0.0, 1.0, 0.0], dtype=np.float32)

    def getLookMatrix(self):
        # https://learnopengl.com/Getting-started/Camera
        # initial camera pos

        # point to origin

        cameraDirection = normalize(np.subtract(self.cameraPos, self.cameraTarget))

        cameraRight = normalize(np.cross(self.upvector, cameraDirection))

        cameraUp = np.cross(cameraDirection, cameraRight)

        cameraMatrix = getLookAtMatrix(
            cameraRight, cameraUp, cameraDirection, self.cameraPos)

        return cameraMatrix

    def getProjectionMatrix(self):
        import glm

        return glm.perspective(glm.radians(45), 800 / 600, 0.1, 100.0)

    def moveCamera(self):
        from time import time
        from math import cos, sin

        radius = 5
        camX = sin(time()) * radius
        camZ = cos(time()) * radius

        self.cameraPos = np.array([camX, 0.0, camZ], dtype=np.float32)
