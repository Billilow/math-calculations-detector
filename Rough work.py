import sys

import cv2
sys.path.append('..')


from lib.ros_environment import ROSEnvironment
from lib.camera_v2 import Camera
from imutils.object_detection import non_max_suppression
import argparse

from PIL import Image
import pyocr
import pyocr.builders
import numpy as np
import sympy as sp


def main():
    # We need to initalize ROS environment for Robot and camera to connect/communicate
    ROSEnvironment()

    #Initialize and start camera
    camera = Camera()
    camera.start()
