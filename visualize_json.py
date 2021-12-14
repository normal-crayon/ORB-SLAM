import os
import sys

import json
from display import Display3D
import numpy as np
import cv2
from slam import SLAM
import time


if __name__=="__main__":

    W = 1024
    H = 520
    F = float(os.getenv("F", "525"))
    K = np.array([[F, 0, W//2,], [0, F, H//2], [0, 0, 1]])
    disp3d = Display3D()
    slam  = SLAM(W, H, K)

    if len(sys.argv) < 2:
        print("%s  <map.json>" % sys.argv[0])

    slam.mapp.deserialize(open(sys.argv[1]).read())
    while True:
       disp3d.paint(slam.mapp)
       time.sleep(1)





