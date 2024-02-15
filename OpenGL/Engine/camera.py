
import numpy as np

import sdl2


def normalize(v): return v / np.linalg.norm(v)


class Camera:
    def __init__(self, initialPos: list[float, float, float] = [0, 0, 0], camTarget: list[float, float, float] = [0, 0, 0]) -> None:

        self.initCameraPos = np.array(initialPos, dtype=np.float32)
        self.cameraTarget = camTarget

        self.cameraPos = self.initCameraPos

        self.upvector = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        self.cameraFront = np.array([0.0, 0.0, -1.0], dtype=np.float32)

        self.fov = np.radians(60)
        self.aspect_ratio = 4.0 / 3.0
        self.near = 1
        self.far = 1000

        self.sensitivity = 0.1
        self.yaw = -90.0
        self.pitch = 0.0

    def getViewMatrix(self) -> np.ndarray:
        """
        Create a view matrix.

        Returns:
            np.ndarray: view matrix

        References:
            https://learnopengl.com/Getting-started/Camera
        """
        # self.cameraDirection = normalize(np.subtract(
        #     self.cameraPos, self.cameraTarget))

        self.cameraDirection = -self.cameraFront

        self.cameraRight = normalize(
            np.cross(self.upvector, self.cameraDirection))

        self.cameraUp = np.cross(self.cameraDirection, self.cameraRight)

        self.cameraMatrix = self.getLookAtMatrix()

        return self.cameraMatrix

    def getLookAtMatrix(self) -> np.ndarray:
        """
        Create a look at matrix.

        Returns:
            np.ndarray: LookAt matrix

        References:
            https://i.imgur.com/0MrTyAu.png
        """

        mat1 = np.identity(4)
        mat2 = np.identity(4)

        # replace top 3x3 of the mat 1 matrix with mat2
        # self.cameraDirection = self.cameraPos + self.cameraFront

        mat1[:3, :3] = np.array(
            [self.cameraRight, self.cameraUp, self.cameraDirection])

        # replace the last column of mat1 with the negative of the camera position
        mat2[:3, 3] = np.array(-self.cameraPos)

        return mat1 @ mat2

    def getPerspectiveMatrix(self) -> np.ndarray:
        """
        Create a perspective projection matrix.

        Returns:
            np.ndarray: Perspective projection matrix

        Args:
            fov: Field of View, in radians
            aspect_ratio: Aspect ratio of the viewport
            near: Near clipping plane
            far: Far clipping plane
        """
        f = 1.0 / np.tan(self.fov / 2)
        matrix = np.zeros((4, 4))
        matrix[0, 0] = f / self.aspect_ratio
        matrix[1, 1] = f
        matrix[2, 2] = (self.far + self.near) / (self.near - self.far)
        matrix[2, 3] = (2 * self.far * self.near) / (self.near - self.far)
        matrix[3, 2] = -1
        return matrix

    def moveCamera(self) -> None:
        """
        Move the camera in a circle around the target.
        """
        from time import time
        from math import cos, sin

        radius = 5
        camX = sin(time()) * radius * self.initCameraPos[0]
        camY = self.initCameraPos[1]
        camZ = cos(time()) * radius * self.initCameraPos[2]

        # self.cameraPos = np.array([camX, 0.0, camZ], dtype=np.float32)
        self.cameraPos = np.array([camX, camY, camZ], dtype=np.float32)

    def process_mouse_movement(self, xoffset, yoffset, constrainPitch=True):
        xoffset *= self.sensitivity
        yoffset *= self.sensitivity

        self.yaw += xoffset
        self.pitch += yoffset

        # Make sure that when pitch is out of bounds, screen doesn't get flipped
        if constrainPitch:
            if self.pitch > 89.0:
                self.pitch = 89.0
            if self.pitch < -89.0:
                self.pitch = -89.0

        self.update_camera_vectors()

    def update_camera_vectors(self):
        front = self.cameraFront
        front[0] = np.cos(np.radians(self.yaw)) * \
            np.cos(np.radians(self.pitch))
        front[1] = np.sin(np.radians(self.pitch))
        front[2] = np.sin(np.radians(self.yaw)) * \
            np.cos(np.radians(self.pitch))

        self.cameraFront = normalize(front)


class CameraController:
    def __init__(self, scene):
        self.camera = scene.getCamera()
        self.moveSpeed = 0.5
        self.turnSpeed = 0.5

    def handle_keys(self):
        keys = sdl2.SDL_GetKeyboardState(None)

        if keys[sdl2.SDL_SCANCODE_W]:
            self.camera.cameraPos += self.moveSpeed * self.camera.cameraFront
        if keys[sdl2.SDL_SCANCODE_S]:
            self.camera.cameraPos -= self.moveSpeed * self.camera.cameraFront
        if keys[sdl2.SDL_SCANCODE_A]:
            self.camera.cameraPos -= normalize(
                np.cross(self.camera.cameraFront, self.camera.upvector)) * self.moveSpeed
        if keys[sdl2.SDL_SCANCODE_D]:
            self.camera.cameraPos += normalize(
                np.cross(self.camera.cameraFront, self.camera.upvector)) * self.moveSpeed

        if keys[sdl2.SDL_SCANCODE_UP] or keys[sdl2.SDL_SCANCODE_I]:
            self.camera.process_mouse_movement(0, 10)
        if keys[sdl2.SDL_SCANCODE_DOWN] or keys[sdl2.SDL_SCANCODE_K]:
            self.camera.process_mouse_movement(0, -10)
        if keys[sdl2.SDL_SCANCODE_LEFT] or keys[sdl2.SDL_SCANCODE_J]:
            self.camera.process_mouse_movement(-10, 0)
        if keys[sdl2.SDL_SCANCODE_RIGHT] or keys[sdl2.SDL_SCANCODE_L]:
            self.camera.process_mouse_movement(10, 0)
