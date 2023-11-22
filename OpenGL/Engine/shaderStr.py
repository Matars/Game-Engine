

class shaderStr:
    def __init__(self):
        self.vertexShader = """
#version 330

layout (location=0) in vec4 position;
layout (location=1) in vec4 colour;

smooth out vec4 theColour;

void main()
{
    gl_Position = position;
    theColour = colour;
}
"""
        self.fragmentShader = """
#version 330

out vec4 outputColour;
smooth in vec4 theColour;

void main()
{
    outputColour = theColour;
}
"""

    def getVertexShader(self):
        return self.vertexShader

    def getFragmentShader(self):
        return self.fragmentShader
