import numpy as np
import cv2 #opencv-python
from mtcnn.mtcnn import MTCNN

def faceDetection():
  """
  Распознавание изображения в реальном времени. Сама получает доступ к камере, 
  ничего передавать в аргументы не нужно
  """
  detector = MTCNN()
  video_capture = cv2.VideoCapture(0)

  while True:
      ret, frame = video_capture.read()
      frame = cv2.flip(frame, 1)
      image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      result = detector.detect_faces(image)

      try:
        bounding_box = result[0]['box']
        keypoints = result[0]['keypoints']
      except IndexError:
        continue

      cv2.rectangle(frame,
        (bounding_box[0], bounding_box[1]),
        (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
        (0,155,255),
        2)
        
      cv2.circle(frame,(keypoints['left_eye']), 3, (0,155,255), 2)
      cv2.circle(frame,(keypoints['right_eye']), 2, (0,155,255), 2)
      cv2.circle(frame,(keypoints['nose']), 3, (0,155,255), 2)
      cv2.circle(frame,(keypoints['mouth_left']), 3, (0,155,255), 2)
      cv2.circle(frame,(keypoints['mouth_right']), 3, (0,155,255), 2)

      cv2.line(frame,(keypoints['left_eye']),keypoints['right_eye'], (0,0,255), 1)
      cv2.line(frame,(keypoints['left_eye']),keypoints['nose'], (0,255,0), 2)
      cv2.line(frame,(keypoints['right_eye']),keypoints['nose'], (255,0,0), 2)
  
      dX = keypoints['right_eye'][0] - keypoints['left_eye'][0]
      dY = keypoints['right_eye'][1] - keypoints['left_eye'][1]
      dist_norm = np.sqrt((dX ** 2) + (dY ** 2))
  
      dX = keypoints['left_eye'][0] - keypoints['nose'][0]
      dY = keypoints['left_eye'][1] - keypoints['nose'][1]
      dist_left = np.sqrt((dX ** 2) + (dY ** 2))

      dX = keypoints['right_eye'][0] - keypoints['nose'][0]
      dY = keypoints['right_eye'][1] - keypoints['nose'][1]
      dist_right = np.sqrt((dX ** 2) + (dY ** 2))

      input_left = dist_left/dist_norm
      input_right = dist_right/dist_norm

      #cv2.putText(frame, str(input_left), (50,50), 
      #            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), lineType=cv2.LINE_AA) 
      #cv2.putText(frame, str(input_right), (50,100), 
      #            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), lineType=cv2.LINE_AA)
  
      cv2.imshow('Video', frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
  video_capture.release()
  cv2.destroyAllWindows()