
import numpy as np
from helpers import *


class Camera:
    def __init__(self) -> None:
        self.cameraPos = np.array([0.0, 1.0, 3.0], dtype=np.float32)
        self.cameraTarget = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.upvector = np.array([0.0, 1.0, 0.0], dtype=np.float32)

        self.fov = np.radians(60)
        self.aspect_ratio = 4.0 / 3.0
        self.near = 1
        self.far = 100.0

    def getViewMatrix(self):
        # https://learnopengl.com/Getting-started/Camera
        # initial camera pos

        # point to origin
        cameraDirection = normalize(np.subtract(
            self.cameraPos, self.cameraTarget))

        cameraRight = normalize(np.cross(self.upvector, cameraDirection))

        cameraUp = np.cross(cameraDirection, cameraRight)

        cameraMatrix = self.getLookAtMatrix(
            cameraRight, cameraUp, cameraDirection, self.cameraPos)

        return cameraMatrix
    
    def getLookAtMatrix(self, rightVector, upVector, DirVector, cameraPos):
        # https://i.imgur.com/0MrTyAu.png

        mat1 = np.identity(4)
        mat2 = np.identity(4)

        # replace top 3x3 of the mat 1 matrix with mat2
        mat1[:3, :3] = np.array([rightVector, upVector, DirVector])

        # replace the last column of mat1 with the negative of the camera position
        mat2[:3, 3] = np.array(cameraPos * -1)

        cameraMatrix = mat2 @ mat1
        return cameraMatrix



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

        radius = 1
        camX = sin(time()) * radius
        camZ = cos(time()) * radius

        # self.cameraPos = np.array([camX, 0.0, camZ], dtype=np.float32)
        self.cameraPos = np.array([camX, 0.5, 3], dtype=np.float32)
