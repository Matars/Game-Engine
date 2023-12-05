import numpy as np


class Transformer:
    @staticmethod
    def translate(dx, dy, dz):
        """
        Translates the model by applying the given translation factors.

        Args:
            dx, dy, dz (float): The translation factors along the x, y, and z axes.
        """
        translationMatrix = np.identity(4)
        translationMatrix[3, 0] = dx
        translationMatrix[3, 1] = dy
        translationMatrix[3, 2] = dz

        return translationMatrix

    @staticmethod
    def rotate(angleX, angleY, angleZ):
        # https://i.imgur.com/0cu8maY.png
        """
        Rotates the model by applying the given rotation angle around the given axis.

        Args:
            angleX, angleY, angleZ (float): The rotation angles around the x, y, and z axes.

        """

        # turn the angles into radians
        angleX = np.radians(angleX)
        angleY = np.radians(angleY)
        angleZ = np.radians(angleZ)

        Rz = np.identity(4)
        Ry = np.identity(4)
        Rx = np.identity(4)

        Rz[0, 0] = np.cos(angleZ)
        Rz[0, 1] = -np.sin(angleZ)
        Rz[1, 0] = np.sin(angleZ)
        Rz[1, 1] = np.cos(angleZ)

        Ry[0, 0] = np.cos(angleY)
        Ry[0, 2] = np.sin(angleY)
        Ry[2, 0] = -np.sin(angleY)
        Ry[2, 2] = np.cos(angleY)

        Rx[1, 1] = np.cos(angleX)
        Rx[1, 2] = -np.sin(angleX)
        Rx[2, 1] = np.sin(angleX)
        Rx[2, 2] = np.cos(angleX)

        rotationMatrix = Rz @ Ry @ Rx

        return rotationMatrix

    @staticmethod
    def scale(dx, dy, dz):
        """
        Scales the model by applying the given scale factors.

        Args:
            dx, dy, dz (float): The scale factors along the x, y, and z axes.
        """
        scaleMatrix = np.identity(4)
        scaleMatrix[0, 0] = dx
        scaleMatrix[1, 1] = dy
        scaleMatrix[2, 2] = dz

        return scaleMatrix
