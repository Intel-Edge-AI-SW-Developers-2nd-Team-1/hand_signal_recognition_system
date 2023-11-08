# Pattern Recognition

## Process
0. It is called at the middle of Pose Estimation Process

1. Input : The nodes' position info(x, y, z) from Pose Estimation Process

2. Calculate angles between certain nodes' position info
    - By the second cosin rule : When known the three lengths of a triangle

    - By the inverse cosin func : Convert value(-1 ~ 1) to angle

3. Determine Patterns from certain nodes' combination

4. So It can be Pattern Recognition of "Hand Signal"

5. Output : The Pattern Number

6. Back to the Pose Estimation Process

## Instance
- Global
    - contractionSteps : Steps that distinguish how much is arm contracted.

    - relaxSteps :  Steps that distinguish how much is arm relaxed.

    - limitInterval : The interval time that measured between the init of class and frame-detected moment. when this expired, re-start detection.
- Self 
    - angleBuf : A buffer that have angles of each node. 

    - leftContractionCnt, rightContractionCnt : A count shows how much contracted.

    - leftRelaxCnt, rightRelaxCnt : A count shows how much relaxed.

    - leftContractionFlag, rightContractionFlag, leftRelaxFlag, rightRelaxFlag : If count is same or upper than each "steps", each flag is on and init to 0.

    - startTime : It is measured as init the class. 
    
    - currTime : It is measured as requested to detect each frame.

    - startFlag : When the start motion(pattern number 0) detected, flag is on.

## Method
- \_\_init__() : Init the instances.

- setPosition(x, y, z) : Receive position infos sent by the parent Process.

- getLen(p1, p2) : Get length between two positions.

- getAngleWithLen(a, b, c) : Get angles of each node using length.

- getAngleAndDirOfNode(nodeNum) : Return list that has angles and directions of each node.

- isHandCrossed() : Detemine that the hands-crossed motion(pattern number 5).

- detectPtrnFromImage() : Detect pattern info from frame(image) and call getAngleAndDirOfNode().

- detectAttentionProc() : Detemine that it is attention motion(start motion : patern number 0).

- detectLeftElbowContractionProc(), detectRightElbowContractionProc() : Detemine contraction motion detected.

- detectLeftElbowRelaxProc(), detectRightElbowRelaxProc() : Detemine relax motion detected.

- detectHurrahPoseProc() : Detemine the hurrah(so called "manse-" in korean) motion(pattern number 4) detected.

- detectPtrnFromVideo() : Detect a frame from video for limitInterval(millisecond) and when the time expired, start flag is on again. Get pattern that this frames mean with some flags.

- recognizePtrn() : Return determined pattern number refered from explanition.


## Module
```python
import math
import time
```
    

## Reference
- [the second cosin rule](https://www.bing.com/ck/a?!&&p=969d904b994dd289JmltdHM9MTY5OTMxNTIwMCZpZ3VpZD0xYjNhMjczOS0zODQ2LTY3ZjMtMjU3NS0zNDQyMzk1MzY2NGMmaW5zaWQ9NTM5OQ&ptn=3&hsh=3&fclid=1b3a2739-3846-67f3-2575-34423953664c&psq=cos+second+rule&u=a1aHR0cHM6Ly9icmlsbGlhbnQub3JnL3dpa2kvY29zaW5lLXJ1bGUv&ntb=1)