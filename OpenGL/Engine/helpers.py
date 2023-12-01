
import numpy as np


def normalize(vector): return vector / np.linalg.norm(vector)


def getLookAtMatrix(rightVector, upVector, DirVector, cameraPos):
    # https://i.imgur.com/0MrTyAu.png

    mat1 = np.identity(4)
    mat2 = np.identity(4)

    # replace top 3x3 of the mat 1 matrix with mat2
    mat1[:3, :3] = np.array([rightVector, upVector, DirVector])

    # replace the last column of mat1 with the negative of the camera position
    mat2[:3, 3] = np.array(cameraPos * -1)

    cameraMatrix = mat2 @ mat1
    return cameraMatrix
