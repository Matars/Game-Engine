
import numpy as np
from helpers import *


class Camera:
    def __init__(self) -> None:
        self.cameraPos = np.array([0.0, 1.0, 3.0], dtype=np.float32)
        self.cameraTarget = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.upvector = np.array([0.0, 1.0, 0.0], dtype=np.float32)

    def getViewMatrix(self):
        # https://learnopengl.com/Getting-started/Camera
        # initial camera pos

        # point to origin
        cameraDirection = normalize(np.subtract(
            self.cameraPos, self.cameraTarget))

        cameraRight = normalize(np.cross(self.upvector, cameraDirection))

        cameraUp = np.cross(cameraDirection, cameraRight)

        cameraMatrix = getLookAtMatrix(
            cameraRight, cameraUp, cameraDirection, self.cameraPos)

        return cameraMatrix

    def getPerspectiveMatrix(self, fov, aspect_ratio, near, far):
        """
        Create a perspective projection matrix.

        Parameters:
        fov -- Field of View, in radians
        aspect_ratio -- Aspect ratio of the viewport
        near -- Near clipping plane
        far -- Far clipping plane
        """
        f = 1.0 / np.tan(fov / 2)
        matrix = np.zeros((4, 4))
        matrix[0, 0] = f / aspect_ratio
        matrix[1, 1] = f
        matrix[2, 2] = (far + near) / (near - far)
        matrix[2, 3] = (2 * far * near) / (near - far)
        matrix[3, 2] = -1
        return matrix

    def moveCamera(self):
        from time import time
        from math import cos, sin

        radius = 1
        camX = sin(time()) * radius
        camZ = cos(time()) * radius

        # self.cameraPos = np.array([camX, 0.0, camZ], dtype=np.float32)
        self.cameraPos = np.array([camX, 0.5, 3+camZ], dtype=np.float32)
