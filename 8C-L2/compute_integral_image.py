import cv2
import numpy as np

def compute_integral(img):
	#TODO: Compute I such that I(y,x) = sum of img(1,1) to img(y,x)
	pass

img = cv2.imread('images/dolphin.png', 0)
cv2.imshow("original_image", img)
print(img.shape)

#compute integral
img = np.float64(img)
I = compute_integral(img)
cv2.imshow("integral_image", (I/I.max()))

x1=150; y1=100
x2=350; y2=200

print("Sum: ", np.sum(img[y1:y2+1, x1:x2+1]))
print(I[y2, x2] - I[y1 - 1, x2] - I[y2, x1 - 1] + I[y1 - 1, x1 - 1])

cv2.waitKey(0)