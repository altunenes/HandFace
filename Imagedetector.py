import torch
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt



os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

xmodel=torch.hub.load("ultralytics/yolov5",'custom',path="best3.pt",force_reload=True)
path = (r'C:\Users\emportent\Desktop\ImageJ') # your input folder
files = os.listdir(path)

img=os.path.join(path,"test","21hand.jpg")    #input folder from the path (test), and, source image

result=xmodel(img)
result.print()

plt.imshow(np.squeeze(result.render()))

plt.savefig("best3/21hand.png")                 #saving image to "best3" folder 
