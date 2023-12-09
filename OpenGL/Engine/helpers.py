
import numpy as np


def normalize(v):   return v / np.linalg.norm(v)


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
