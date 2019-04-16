#! /usr/bin/env python
import numpy as np
from math import cos, sin



if __name__ == "__main__":
    P = []
    Q = []
    # read paired points
    with open("pair_points.txt", 'rb') as f:
        for line in f.readlines():
            [x,y] = line.strip().split()
            P.append([float(a) for a in x.split(',')])
            Q.append([float(a) for a in y.split(',')])

    P = np.array(P)
    Q = np.array(Q)

    # calculate matrix for svd 
    H = np.dot(P, Q.T)

    # svd
    U, S, Vt = np.linalg.svd(H)

    # calculate Rotation matrix
    R_new = np.dot(Vt.T ,U.T)

    # print
    print(R_new)
    # wirte to file
    np.savetxt("result.txt", R, fmt="%.3f")
