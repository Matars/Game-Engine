from OpenGL import GL, GLU
from camera import CameraController


class Scene:
    def __init__(self, objects, camera, light):
        self.objects = objects
        self.camera = camera
        self.light = light
        self.controller = CameraController(self)

    def render(self):
        GL.glClearColor(0.2, 0.2, 0.2, 1)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        self.controller.handle_keys()

        for obj in self.objects:
            obj.display(self.camera, self.light)

    def initializeObjects(self, vertexShaderStr, fragmentShaderStr):
        for obj in self.objects:
            obj.initialize(vertexShaderStr, fragmentShaderStr)

    def getObjects(self):
        return self.objects

    def getCamera(self):
        return self.camera
