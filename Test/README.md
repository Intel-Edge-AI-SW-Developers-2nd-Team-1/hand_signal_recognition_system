# TEST

## Process
0. Generate x, y, z (empty list)

1. Generate PoseEstimation object as pe

2. Generate detector to use webcam : createPoseLandmarkerObject()

3. Generate cam to use webcam : cameraOn()

4. Read a frame from video through webcam readFrameFromCamera()

5. Release : camaraOff()

## Class
- PoseEstimation


## Module
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PoseEstimation.pose_estimation_module import PoseEstimation
```