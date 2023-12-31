# Project : 수신호 기반 로봇 제어

![back](https://github.com/simpleis6est/How-to-using-Git-Github/assets/143490860/c2fc94b1-f2c7-4c10-baca-38c213f443d4)

![back(com)](https://github.com/simpleis6est/How-to-using-Git-Github/assets/143490860/26f9212e-f54b-4a87-a935-1590331f6bca)

robot control system based on hand signal(ex. airport) recognition

수신호 중인 대상을 카메라로 촬영하여 Pose estimaion 후 분석하여 현재 어떤 수신호인지 판별
판별한 수신호를 기준으로 원하는 제어에 해당하는 메세지를 터틀봇 ROS에 전송하여 터틀봇이 목적하는 행동을 수행
1. Tuttle Bot에 카메라를 장착하여 라즈베리로 촬영 후 Server로 촬영 영상을 전송(박재병, 한정재 담당)
2. 전송 받은 사진을 OpenCV와 Mediapipe를 이용해 관절부를 탐색(안석현 담당)
3. 탐색한 관절부의 이동을 알고리즘을 통해 분석 후 결과를 Tuttle Bot 라즈베리로 전송(김영대 담당)
4. 전송 받은 결과를 ROS에 보내어 결과에 맞는 제어를 수행(권춘구, 안현홍 담당)
<div align=center>   
   <img src = "https://github.com/Intel-Edge-AI-SW-Developers-2nd-Team-1/HandSignalRecognitionSystem/assets/45201672/3a1a08d7-071d-41fd-b6f4-3df8b84cc534">


![구현계획](https://github.com/roby238/HandSignalRecognitionSystem/assets/45201672/92f572c1-8c2a-49c8-aa6e-84dce05db09b)
![개발일정](https://github.com/roby238/HandSignalRecognitionSystem/assets/45201672/43e9513a-cd21-45bc-ad1d-f8113b26d0a9)
![부품 리스트](https://github.com/roby238/HandSignalRecognitionSystem/assets/45201672/6808d626-fdd9-4c2f-98ae-a0d81eab4035)
</div>

## contributors

**yeongdaekim(roby238)**
- Project Leader
- Git Manager
- Pattern Recognition Algorithm
- Create Deliverables for Develop

**User3198352(User3198352)**
- Project Communication
- System Integration
- Image Processing for Pose Estimaion
- Create Deliverables for Develop

**Daniel(kcg0118)**
- Client Action
- Create Deliverables for Communication
  
**simpleis6est(simpleis6est)**
- Client Rx
- Create Deliverables for Develop

**Park JaeByeong(pjb8051)**
- Hardware
- Create Deliverables for Develop 
  
**jungjaeJJ(jungjaeJJ)**
- Server Tx
- Create Deliverables for Develop 

## How to manage
1. manager가 PR을 확인하고 merge
2. 문제가 있다면 code에 대한 comment나 issue를 통해 feedback을 거쳐 해결

## How to PR
1. fork 원본 저장소(this repository)
2. commit 규칙에 맞게 code 업로드하기
- Visual Studio 환경에서는 Git 계정 로그인, repository 복제 후 code staging하여 commit
- Pycharm 환경에서는 Git 계정 로그인, repository 연결 후 code select하여 commit
4. 원본 저장소(this repository)로 PR(Pull Request)

## PR 규칙
- 작업 기간, 작업명, 본인 이름 포함하여 PR
  ```
  23/10/12 ~ 23/10/13 영상신호전처리_수정2 김영대
  ```

## commit 규칙
- commit message: code 제목
  ```
  git commit -m "system_server.c"
  ```
