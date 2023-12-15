from OpenGL import GL, GLU


class Scene:
    def __init__(self, objects, camera):
        self.objects = objects
        self.lights = []
        self.camera = camera

    def render(self):
        GL.glClearColor(0.2, 0.2, 0.2, 1)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        for obj in self.objects:
            obj.display(self.camera)

        for obj in self.objects[:-1]:
            obj.rotate(1, 1, 1)

    def initializeObjects(self, vertexShaderStr, fragmentShaderStr):
        for obj in self.objects:
            obj.initialize(vertexShaderStr, fragmentShaderStr)
