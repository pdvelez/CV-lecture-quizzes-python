import cv2

def downsample(img):
	#TODO: img_d = ? (pick alternate rows, cols: 1, 3, 5, ...)
	pass


def blur_downsample(img):
	#TODO img_bd = ? (blur by 5x5 gaussian, then downsample)
	pass


img = cv2.imread('images/frizzy.png')
cv2.imshow("original_image", img)
print(img.shape)

#downsample image
img_d = downsample(img)
img_d = downsample(img_d)
img_d = downsample(img_d)
print(img_d.shape)

#blur and downsample
img_bd = blur_downsample(img)
img_bd = blur_downsample(img_bd)
img_bd = blur_downsample(img_bd)
print(img_bd.shape)

cv2.imshow("downsampled_image", cv2.resize(img_d, (img.shape[1], img.shape[0])))
cv2.imshow("blur_downsampled_image", cv2.resize(img_bd, (img.shape[1], img.shape[0])))
cv2.waitKey(0)


