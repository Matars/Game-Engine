
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


def loadObjMesh(mesh_path):
    '''
    Loads a mesh from an obj file

    taken from https://www.programcreek.com/python/?CodeExample=load+obj example 4 
    '''
    vertex_data = []
    face_data = []
    for line in open(mesh_path, "r"):
        if line.startswith('#'):
            continue
        values = line.split()
        if not values:
            continue
        if values[0] == 'v':
            v = list(map(float, values[1:4]))
            vertex_data.append(v)
        elif values[0] == 'f':
            f = list(map(lambda x: int(x.split('/')[0]),  values[1:4]))
            face_data.append(f)
    vertices = np.array(vertex_data, dtype=np.float32)
    faces = np.array(face_data, dtype=np.float32)
    return vertices, faces


if __name__ == "__main__":
    vertices, faces = loadObjMesh("objects\objectsMesh\cubeMesh.obj")
    print(vertices)
    print(faces)
