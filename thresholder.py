import cv2 as cv
import numpy as np
from PIL import Image
import os
for i in range(1,70):
    img = np.asarray(Image.open(f"-/-_{i}.jpeg"))
    _,img=cv.threshold(img,127,255,cv.THRESH_BINARY)
    cv.imwrite(f"-_{i}.jpeg",img)
