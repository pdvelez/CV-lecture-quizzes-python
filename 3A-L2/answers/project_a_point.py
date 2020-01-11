import cv2
import numpy as np

# Project a point from 3D to 2D using a matrix operation

# Given: Point p in 3-space [x y z], and focal length f
# Return: Location of projected point on 2D image plane [u v]


def project_point(p, f):
    # TODO: Define and apply projection matrix
    H = np.array([[1, 0, 0,    0],
                  [0, 1, 0,    0],
                  [0, 0, 1./f, 0]])

    p2 = np.hstack((p, np.array([[1]])))
    res = np.dot(H, p2.T)
    return res[0, 0] / res[2, 0], res[1, 0] / res[2, 0]

# Test: Given point and focal length (units: mm)
p = np.array([[200, 100, 120]])
f = 50

print( project_point(p, f))
