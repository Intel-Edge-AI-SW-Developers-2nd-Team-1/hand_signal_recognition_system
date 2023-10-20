import math

contractionSteps = 4
relaxSteps = 4

class PatternRecognition:
    def __init__(self):
        self.position = ["0 - right shoulder", "1 - left shoulder", "2 - right elbow", "3 - left elbow",
                         "4 - right wrist", "5 - left wrist", "6 - right hip", "7 - left hip"]
        self.ptrn = 0
        self.angleBuf = []
        self.leftContractionCnt, self.rightContractionCnt,\
            self.leftRelaxCnt, self.rightRelaxCnt= 0, 0, 0, 0
        self.leftContractionFlag, self.leftRelaxFlag, self.rightContractionFlag, self.rightRelaxFlag = False, False, False, False
        self.leftAttentionFlag, self.rightAttentionFlag = False, False

    def setPosition(self, x, y, z):
        self.x, self.y, self.z = x[1:9], y[1:9], z[1:9]

    def getLen(self, p1, p2):
        return math.sqrt((self.x[p1] - self.x[p2]) ** 2 + (self.y[p1] - self.y[p2]) ** 2)
    def getAngleWithLen(self, a, b, c):
        return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) / 3.14 * 180

    def getAngleAndDirOfNode(self, nodeNum):
        dir = 0
        if nodeNum == 2 and self.y[4] > self.y[0]: dir = 1
        elif nodeNum == 3 and self.y[5] > self.y[1]: dir = 1

        return [self.getAngleWithLen(self.getLen((nodeNum - 2) % 8, nodeNum),
                                    self.getLen(nodeNum, (nodeNum + 2) % 8),
                                    self.getLen((nodeNum + 2) % 8, (nodeNum - 2) % 8)), dir]

    def detectPtrnFromImage(self):
        # left shoulder, right shoulder, left elbow, right elbow
        self.angleBuf = [self.getAngleAndDirOfNode(0), self.getAngleAndDirOfNode(1),
                              self.getAngleAndDirOfNode(2), self.getAngleAndDirOfNode(3)]
        #print(self.angleBuf)

    def detectAttentionProc(self):
        if self.angleBuf[0][0] < 20: self.leftAttentionFlag = True # left shoulder -> 45도 미만 -> left attention flag on
        else: self.leftAttentionFlag = False # left shoulder -> 45도 이상 -> left attention flag off

        if self.angleBuf[1][0] < 20: self.rightAttentionFlag = True # right shoulder -> 45도 미만 -> right attention flag on
        else: self.rightAttentionFlag = False # right shoulder -> 45도 이상 -> right attention flag off

    def detectContractionProc(self):
        if 105 < self.angleBuf[2][0] <= 120 and self.angleBuf[2][1] and not self.leftContractionCnt:
            self.leftContractionCnt += 1 # left elbow -> 120도 ~ 105도 -> left contraction count ++ if count is 0
        elif 90 < self.angleBuf[2][0] <= 105 and self.angleBuf[2][1] and self.leftContractionCnt == 1:
            self.leftContractionCnt += 1 # left elbow -> 105도 ~ 90도 -> left contraction count ++ if count is 1
        elif 75 < self.angleBuf[2][0] <= 90 and self.angleBuf[2][1] and self.leftContractionCnt == 2:
            self.leftContractionCnt += 1 # left elbow -> 90도 ~ 75도 -> left contraction count ++ if count is 2
        elif 60 <= self.angleBuf[2][0] <= 75 and self.angleBuf[2][1] and self.leftContractionCnt == 3:
            self.leftContractionCnt += 1 # left elbow -> 75도 ~ 60도 -> left contraction count ++ if count is 3

        if 105 < self.angleBuf[3][0] <= 120 and self.angleBuf[2][1] and not self.rightContractionCnt:
            self.rightContractionCnt += 1  # right elbow -> 120도 ~ 105도 -> right contraction count ++ if count is 0
        elif 90 < self.angleBuf[3][0] <= 105 and self.angleBuf[2][1] and self.rightContractionCnt == 1:
            self.rightContractionCnt += 1  # right elbow -> 105도 ~ 90도 -> right contraction count ++ if count is 1
        elif 75 < self.angleBuf[3][0] <= 90 and self.angleBuf[2][1] and self.rightContractionCnt == 2:
            self.rightContractionCnt += 1  # right elbow -> 90도 ~ 75도 -> right contraction count ++ if count is 2
        elif 60 <= self.angleBuf[3][0] <= 75 and self.angleBuf[2][1] and self.rightContractionCnt == 3:
            self.rightContractionCnt += 1  # right elbow -> 75도 ~ 60도 -> right contraction count ++ if count is 3

    def detectRelaxProc(self):
        if 60 <= self.angleBuf[2][0] <= 75 and self.angleBuf[3][1] and not self.leftRelaxCnt:
            self.leftRelaxCnt += 1  # left elbow -> 60도 ~ 75도 -> left relax count ++ if count is 0
        elif 75 <= self.angleBuf[2][0] <= 90 and self.angleBuf[3][1] and self.leftRelaxCnt == 1:
            self.leftRelaxCnt += 1  # left elbow -> 75도 ~ 90도 -> left relax count ++ if count is 1
        elif 90 <= self.angleBuf[2][0] <= 105 and self.angleBuf[3][1] and self.leftRelaxCnt == 2:
            self.leftRelaxCnt += 1  # left elbow -> 90도 ~ 105도 -> left relax count ++ if count is 2
        elif 105 <= self.angleBuf[2][0] <= 120 and self.angleBuf[3][1] and self.leftRelaxCnt == 3:
            self.leftRelaxCnt += 1  # left elbow -> 105도 ~ 120도 -> left relax count ++ if count is 3

        if 60 <= self.angleBuf[3][0] <= 75 and self.angleBuf[3][1] and not self.rightRelaxCnt:
            self.rightRelaxCnt += 1  # right elbow -> 60도 ~ 75도 -> right relax count ++ if count is 0
        elif 75 <= self.angleBuf[3][0] <= 90 and self.angleBuf[3][1] and self.rightRelaxCnt == 1:
            self.rightRelaxCnt += 1  # right elbow -> 75도 ~ 90도 -> right relax count ++ if count is 1
        elif 90 <= self.angleBuf[3][0] <= 105 and self.angleBuf[3][1] and self.rightRelaxCnt == 2:
            self.rightRelaxCnt += 1  # right elbow -> 90도 ~ 105도 -> right relax count ++ if count is 2
        elif 105 <= self.angleBuf[3][0] <= 120 and self.angleBuf[3][1] and self.rightRelaxCnt == 3:
            self.rightRelaxCnt += 1  # right elbow -> 105도 ~ 120도 -> right relax count ++ if count is 3

    def detectPtrnFromVideo(self):
        self.detectPtrnFromImage()

        # pose detection per each image : 각 부위 각도 정보로 자세 탐지
        self.detectAttentionProc()
        self.detectContractionProc()
        self.detectRelaxProc()

        # pose detection per images(video)
        # if left arm contraction steps is max --> "left arm contraction"!
        if self.leftContractionCnt >= contractionSteps:
            self.leftContractionCnt = 0
            #self.angleBuf = []
            self.leftContractionFlag = True
            # if left arm relax steps is max --> "left arm relax"!
        if self.leftRelaxCnt >= relaxSteps:
            self.leftRelaxCnt = 0
            #self.angleBuf = []
            self.leftRelaxFlag = True

        # if right arm contraction steps is max --> "right arm contraction"!
        if self.rightContractionCnt >= contractionSteps:
            self.rightContractionCnt = 0
            #self.angleBuf = []
            self.rightContractionFlag = True
        # if right arm contraction steps is max --> "right arm contraction"!
        if self.rightRelaxCnt >= relaxSteps:
            self.rightRelaxCnt = 0
            #self.angleBuf = []
            self.rightRelaxFlag = True

        # pattern detection
        # 1 -> attention
        # 2 -> left arm contraction and relax
        # 3 -> right arm contraction and relax
        # 0 -> nothing
        if self.leftAttentionFlag and self.rightAttentionFlag:
            self.leftContractionFlag = False
            self.leftRelaxFlag = False
            self.rightContractionFlag = False
            self.rightRelaxFlag = False
            return 1
        elif self.leftContractionFlag: #and \
              #not self.rightContractionFlag and not self.rightRelaxFlag:
            self.leftContractionFlag = False
            return 2
        elif self.leftRelaxFlag:
            self.leftRelaxFlag = False
            return -2
        elif self.rightContractionFlag:# and \
              #not self.leftContractionFlag and not self.leftRelaxFlag:
            self.rightContractionFlag = False
            return 3
        elif self.rightRelaxFlag:
            self.rightRelaxFlag = False
            return -3
        #else: return 0

    def recognizePtrn(self):
        ptrn = self.detectPtrnFromVideo()
        if ptrn == 1:
            print("Start")
        elif ptrn == 2:
            print("Turn Left : contraction")
        elif ptrn == -2:
            print("Turn Left : relax")
        elif ptrn == 3:
            print("Turn Right : contraction")
        elif ptrn == -3:
            print("Turn Right : relax")
        #else: print("Not Found")