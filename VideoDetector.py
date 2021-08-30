import torch
import numpy as np
import cv2
import os


os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
model=torch.hub.load("ultralytics/yolov5",'custom',path="best3.pt",force_reload=True)
cap =cv2.VideoCapture("yourvideo.mp4")
while cap.isOpened():
    ret, frame = cap.read()

    # Make detections
    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


###################################### REAL TIME Detector ######################################################

# import torch
# import numpy as np
# import cv2
# import os
# from matplotlib import pyplot as plt
# import tkinter
# 
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# model=torch.hub.load("ultralytics/yolov5",'custom',path="best170).pt",force_reload=True)
# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
# 
#     # Make detections
#     results = model(frame)
# 
#     cv2.imshow('YOLO', np.squeeze(results.render()))
# 
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
