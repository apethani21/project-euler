import time
import requests
import pickle
import numpy as np

start_time = time.time()


def get_triangles():
    r = requests.get("https://projecteuler.net/project/resources/p102_triangles.txt")
    r.raise_for_status()
    points = r.content.decode().split("\n")
    points = [triangle_pair for triangle_pair in points if len(triangle_pair) > 0]
    points = [list(map(int, triangle_pair.split(","))) for triangle_pair in points]
    points = [[[point[i], point[i+1]] for i in range(0, 5, 2)] for point in points]
    with open('triangles.pickle', 'wb') as f:
        pickle.dump(points, f)


def read_triangles():
    with open('triangles.pickle', 'rb') as f:
        triangles = pickle.load(f)
    return triangles


def check_triangle_contains_origin(triangle):
    determinants = []
    determinants.append(int(np.linalg.det(np.array([triangle[0],
                                                    triangle[1]]))))
    determinants.append(int(np.linalg.det(np.array([triangle[1],
                                                    triangle[2]]))))
    determinants.append(int(np.linalg.det(np.array([triangle[2],
                                                    triangle[0]]))))
    return (all([det > 0 for det in determinants])
            or all([det < 0 for det in determinants]))

triangles = read_triangles()
total = sum([check_triangle_contains_origin(triangle)
             for triangle in triangles])
print(f"{total} of the triangles contain the origin.")


end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))