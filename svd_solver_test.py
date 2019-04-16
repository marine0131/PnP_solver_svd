#! /usr/bin/env python
import numpy as np
from math import cos, sin
import os



if __name__ == "__main__":
    roll = 0
    pitch = 0
    yaw = 45.0 / 57.3

    R = np.array([[cos(pitch)*cos(yaw),-cos(roll)*sin(yaw)+sin(roll)*sin(pitch)*cos(yaw),sin(roll)*sin(yaw)+cos(roll)*sin(pitch)*cos(yaw)],
        [cos(pitch)*sin(yaw),cos(roll)*cos(yaw)+sin(roll)*sin(pitch)*sin(yaw),-sin(roll)*cos(yaw)+cos(roll)*sin(pitch)*sin(yaw)],
        [-sin(pitch),sin(roll)*cos(pitch),cos(roll)*cos(pitch)]])

    P = np.random.random((3,5))
    Q = np.dot(R, P)

    H = np.dot(P, Q.T)

    U, S, Vt = np.linalg.svd(H)

    R_new = np.dot(Vt.T ,U.T)

    print(R_new)
    if not os.path.exists("./result.txt"):
        os.system(r'touch %s' %"./result.txt")
    np.savetxt("./result.txt",R_new, fmt="%.3f")
