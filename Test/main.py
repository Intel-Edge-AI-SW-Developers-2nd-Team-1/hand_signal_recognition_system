import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PoseEstimation.pose_estimation_module import poseEstimation

if __name__ == '__main__':
    x, y, z = [], [], []
    pe = poseEstimation(x, y, z)
    detector = pe.createPoseLandmarkerObject()
    cap = pe.cameraOn()
    pe.readFrameFromCamera(cap, detector)
    pe.camaraOff()
