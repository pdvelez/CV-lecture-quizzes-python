import numpy as np
import matplotlib.pyplot as plt
import cv2

currDir='../2A-L1'
imgsDir=currDir+'/images'

plt.clf()
img=cv2.imread(imgsDir+'/fruit.png', 1)
cv2.imshow('img',img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
