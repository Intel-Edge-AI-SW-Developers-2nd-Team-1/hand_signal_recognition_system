
#사용전에 꼭 cv2, numpy, mediapipe 모듈을 설치하여야 구동이 됩니다.
import cv2
import numpy as np

#mediapipe 설치는 cmd 창에서 다음을 입력
#python -m pip install mediapipe
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#pose_landmarker_lite.task를 아래 링크에 들어가서 Models 부분에서 다운 받기
#https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
model_path = 'C:\pywork\pose_landmarker_lite.task'

def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image


# STEP 2: Create an PoseLandmarker object.
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    output_segmentation_masks=True)
detector = vision.PoseLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while True:
    
    # 카메라에서 프레임 읽기
    ret, frame = cap.read()
    
    # 프레임이 정상적으로 읽어졌는지 확인
    if not ret:
        break

    # STEP 3: Load the input image.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_frame = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    )
    
    # STEP 4: Detect pose landmarks from the input image.
    detection_result = detector.detect(image_frame)

    # STEP 5: Process the detection result. In this case, visualize it.
    annotated_image = draw_landmarks_on_image(image_frame.numpy_view(), detection_result)
    cv2.imshow("image", cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
    
    #카메라를 화면에 띄우기
    #cv2.imshow('frame', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 객체와 윈도우 창 닫기
cap.release()
cv2.destroyAllWindows()

#printf(detection_result)
