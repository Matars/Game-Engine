
import numpy as np

# Define vertices for the pyramid
vertices = np.array([
    [0.0, 0.0, -40.0],
    [-40.0, 0.0, 0.0],
    [40.0, 0.0, 0.0],

    [0.0, 0.0, 40.0],
    [40.0, 0.0, 0.0],
    [-40.0, 0.0, 0.0],
    
    # Side 1
    [0.0, 60.0, 0.0],
    [0.0, 0.0, 40.0],
    [-40.0, 0.0, 0.0],

    # Side 2
    [0.0, 60.0, 0.0],
    [-40.0, 0.0, 0.0],
    [0.0, 0.0, -40.0],
    
    # Side 3
    [0.0, 60.0, 0.0],
    [0.0, 0.0, -40.0],
    [40.0, 0.0, 0.0],

    # Side 4
    [0.0, 60.0, 0.0],
    [40.0, 0.0, 0.0],
    [0.0, 0.0, 40.0],
])

# Initialize an array to hold the normals for each face
face_normals = np.zeros((vertices.shape[0] // 3, 3), dtype=np.float32)

# Iterate over the vertices in steps of 3 to compute each face's normal
for i in range(0, vertices.shape[0], 3):
    v1 = vertices[i]
    v2 = vertices[i + 1]
    v3 = vertices[i + 2]

    # Compute vectors for two edges of the triangle
    edge1 = v2 - v1
    edge2 = v3 - v1

    # Use the cross product to get the normal
    normal = np.cross(edge1, edge2)
    normal = normal / np.linalg.norm(normal)  # Normalize the normal

    # Assign the computed normal to the corresponding face
    face_normals[i // 3] = normal

# Now face_normals contains the normal for each face
# Print the normals for each face
# for i in range(face_normals.shape[0]):
#     print(f"Face {i + 1} normal: {face_normals[i]}")


# calculate the light factor for each face

# define light pos
light_pos = np.array([50.0, 100.0, 100.0])

# define ambient light
ambient_light = np.array([0.5, 0.5, 0.4])

# define light color
light_color = np.array([1.0, 1.0, 1.0])

# define object material
ka = 0.25
kd = 1.0
alpha = 32


# define the function to calculate the light factor
def light_factor(normal):
    # calculate the light direction
    light_dir = light_pos - normal

    # normalize the light direction
    light_dir = light_dir / np.linalg.norm(light_dir)

    # calculate the dot product of the light direction and the normal
    dot_product = np.dot(light_dir, normal)

    # calculate the light factor
    light_factor = ka * ambient_light + kd * light_color * dot_product

    return light_factor


# # calculate the light factor for each face
# for i in range(face_normals.shape[0]):
#     print(f"Face {i + 1} light factor: {light_factor(face_normals[i])}")


# define moonlight color
moonlight_color = np.array([0.2, 0.2, 0.3])

# define lantern pos
lantern_pos = np.array([0.0, 10.0, 50.0])

# define lantern color
lantern_color = np.array([1.0, 1.0, 1.0]) * 0.25  # Multiply by the intensity

# redefine the function to calculate the light factor
def light_factor(normal):
    # calculate the light direction
    light_dir = lantern_pos - normal

    # normalize the light direction
    light_dir = light_dir / np.linalg.norm(light_dir)

    # calculate the dot product of the light direction and the normal
    dot_product = np.dot(light_dir, normal)

    # calculate the light factor
    light_factor = ka * moonlight_color + kd * lantern_color * dot_product

    return light_factor

# calculate the light factor for each face
for i in range(face_normals.shape[0]):
    print(f"Face {i + 1} light factor: {light_factor(face_normals[i])}")