
import numpy as np
from helpers import *


class Camera:
    def __init__(self, initialPos, camTarget) -> None:

        self.initCameraPos = np.array(initialPos, dtype=np.float32)
        self.cameraPos = self.initCameraPos

        self.cameraTarget = np.array(camTarget, dtype=np.float32)
        self.upvector = np.array([0.0, 1.0, 0.0], dtype=np.float32)

        self.fov = np.radians(60)
        self.aspect_ratio = 4.0 / 3.0
        self.near = 1
        self.far = 1000

    def getViewMatrix(self):
        # https://learnopengl.com/Getting-started/Camera
        # initial camera pos

        # point to origin
        self.cameraDirection = normalize(np.subtract(
            self.cameraPos, self.cameraTarget))

        self.cameraRight = normalize(
            np.cross(self.upvector, self.cameraDirection))

        self.cameraUp = np.cross(self.cameraDirection, self.cameraRight)

        self.getLookAtMatrix()

        return self.cameraMatrix

    def getLookAtMatrix(self):
        # https://i.imgur.com/0MrTyAu.png

        mat1 = np.identity(4)
        mat2 = np.identity(4)

        # replace top 3x3 of the mat 1 matrix with mat2
        mat1[:3, :3] = np.array(
            [self.cameraRight, self.cameraUp, self.cameraDirection])

        # replace the last column of mat1 with the negative of the camera position
        mat2[:3, 3] = np.array(self.cameraPos * -1)

        self.cameraMatrix = mat1 @ mat2

    def getPerspectiveMatrix(self):
        """
        Create a perspective projection matrix.

        Parameters:
        fov -- Field of View, in radians
        aspect_ratio -- Aspect ratio of the viewport
        near -- Near clipping plane
        far -- Far clipping plane
        """
        f = 1.0 / np.tan(self.fov / 2)
        matrix = np.zeros((4, 4))
        matrix[0, 0] = f / self.aspect_ratio
        matrix[1, 1] = f
        matrix[2, 2] = (self.far + self.near) / (self.near - self.far)
        matrix[2, 3] = (2 * self.far * self.near) / (self.near - self.far)
        matrix[3, 2] = -1
        return matrix

    def moveCamera(self):
        from time import time
        from math import cos, sin

        radius = 5
        camX = sin(time()) * radius * self.initCameraPos[0]
        camY = self.initCameraPos[1]
        camZ = cos(time()) * radius * self.initCameraPos[2]

        # self.cameraPos = np.array([camX, 0.0, camZ], dtype=np.float32)
        self.cameraPos = np.array([camX, camY, camZ], dtype=np.float32)
