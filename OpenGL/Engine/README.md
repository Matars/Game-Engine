# OpenGL Game Engine

This is a simple OpenGL game engine built in Python. It provides basic functionality for creating 3D objects and rendering them in a scene.

## Movement

use wasd for movement and arrow keys for direction movement

## Features

- Basic 3D object creation
- Object transformations: Translation, Rotation, Scaling
- Scene rendering
- Camera controls

## Code Structure

`main.py`: Entry point of the application, run this to view the scene

`Engine.py`: Contains the main game loop and initialization logic.

`scene.py`: Defines the Scene class for managing and rendering 3D objects and a camera.

`camera.py`: Defines the Camera class for controlling the view into the scene.

`objects/`: Contains classes for different types of 3D objects and a baseObj class that is inhereted by the other object classes

`shaders/`: Contains GLSL shader programs.
