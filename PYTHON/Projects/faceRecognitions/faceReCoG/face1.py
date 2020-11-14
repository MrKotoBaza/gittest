import face_recognition
import cv2
import os
import urllib.request
import numpy as np

faces_images=[]
for i in os.listdir(r'F:\SanDiskSecureAccess\PythonFiles\recognitions\faceReCoG\faces' ):
    faces_images.append(face_recognition.load_image_file(r'F:\SanDiskSecureAccess\PythonFiles\recognitions\faceReCoG\faces\' +i))
known_face_encodings=[]
for i in faces_images:
    known_face_encodings.append(face_recognition.face_encodings(i)[0])
known_face_names=[url]
for i in os.listdir('faces/'):
    i=i.split('.')[0]
    known_face_names.append(i)

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

req = urllib.request.urlopen('http://192.168.11.1:8080/snapshot?topic=/main_camera/image_raw')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
frame = cv2.imdecode(arr, -1)

