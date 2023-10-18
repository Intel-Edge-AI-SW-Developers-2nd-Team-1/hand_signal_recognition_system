# Google Mediapipe를 이용한 Pose Estimantion Landmark 추출 코드 설명

## 개요
Google이 제공하는 다양한 모듈 중 단일 카메라를 이용하여 다양한 물체 또는 사물을 파악하고 좌표를 제공하는 Mediapipe를 이용한다. 
Mediapipe가 제공하는 모듈 중에 사람을 탐지하여 사람의 Pose를 Estimation하는 모듈을 사용하여 사람의 자세를 추출한다. 
추출한 좌표는 추출 대상을 기준으로 33개의 지점에 대해 표준화하여 저장한다.(사진1 참조) 
해당 코드는 추출한 좌표 중 수신호 판독에 필요한 일부를 시각화 및 엑셀 파일로 저장한다. 
(어떤 부분이 추출되고 시각화되는지는 사진2 참조)

## 사진1
그림
그림
0 - nose,
1 - left eye (inner),
2 - left eye,
3 - left eye (outer),
4 - right eye (inner),
5 - right eye,
6 - right eye (outer),
7 - left ear,
8 - right ear,
9 - mouth (left),
10 - mouth (right),
11 - left shoulder,
12 - right shoulder,
13 - left elbow,
14 - right elbow,
15 - left wrist,
16 - right wrist,
17 - left pinky,
18 - right pinky,
19 - left index,
20 - right index,
21 - left thumb,
22 - right thumb,
23 - left hip,
24 - right hip,
25 - left knee,
26 - right knee,
27 - left ankle,
28 - right ankle,
29 - left heel,
30 - right heel,
31 - left foot index,
32 - right foot index,


## 사진2
사진2


