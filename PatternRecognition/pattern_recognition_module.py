import cv2
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

contractionSteps = 4
relaxSteps = 4

class patternRecognition:
    def __init__(self, x, y, z):
        self.position = ["0 - left shoulder", "1 - right shoulder", "2 - left elbow", "3 - right elbow",
                         "4 - left wrist", "5 - right wrist", "6 - left hip", "7 - right hip"]
        self.x = x[11:17] + x[23:25]
        self.y = y[11:17] + y[23:25]
        self.z = z[11:17] + z[23:25]
        self.ptrn = -1
        self.angleBuf = []
        self.leftContractionCnt, self.rightContractionCnt,\
            self.leftRelaxCnt, self.rightRelaxCnt= 0, 0, 0, 0
        self.leftContractionFlag, self.leftRelaxFlag, self.rightContractionFlag, self.rightRelaxFlag = False, False, False, False

    def getLen(self, p1, p2):
        return math.sqrt((self.x[p1] - self.x[p2]) ** 2 + (self.y[p1] - self.y[p2]) ** 2)
    def getAngleWithLen(self, a, b, c):
        return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    def getAngleAndDirOfNode(self, nodeNum):
        dir = 0
        if nodeNum == 2 and self.y[4] > self.y[0]: dir = 1
        elif nodeNum == 3 and self.y[5] > self.y[1]: dir = 1

        return [self.getAngleWithLen(self.getLen((nodeNum - 2) % 8, nodeNum),
                                    self.getLen(nodeNum, (nodeNum + 2) % 8),
                                    self.getLen((nodeNum + 2) % 8, (nodeNum - 2)) % 8), dir]

    def detectPtrnFromImage(self):
        # left shoulder, right shoulder, left elbow, right elbow
        self.angleBuf.append([self.getAngleAndDirOfNode(0), self.getAngleAndDirOfNode(1),
                              self.getAngleAndDirOfNode(2), self.getAngleAndDirOfNode(3)])

    def detectPtrnFromVideo(self):
        self.detectPtrnFromImage()

        # pose detection per each image
        # code

        # pose detection per images(video)
        # if left arm contraction steps is max --> "left arm contraction"!
        if self.leftContractionCnt == contractionSteps:
            self.leftContractionCnt = 0
            self.angleBuf = []
            self.leftContractionFlag = True
        # if right arm contraction steps is max --> "right arm contraction"!
        elif self.rightContractionCnt == contractionSteps:
            self.rightContractionCnt = 0
            self.angleBuf = []
            self.rightContractionFlag = True

        # if left arm relax steps is max --> "left arm relax"!
        if self.leftRelaxCnt == relaxSteps:
            self.leftRelaxCnt = 0
            self.angleBuf = []
            self.leftRelaxFlag = True
        # if right arm contraction steps is max --> right arm contraction"!
        elif self.rightRelaxCnt == relaxSteps:
            self.rightRelaxCnt = 0
            self.angleBuf = []
            self.rightRelaxFlag = True

        # pattern detection
        # 1 ->
        # 2 ->
        # 1 -> left arm contraction and relax
        # 2 -> right arm contraction and relax
        # 0 -> nothing
        if self.leftContractionFlag and self.leftRelaxFlag: return 1
        elif self.rightContractionFlag and self.rightRelaxFlag: return 2
        else: return 0