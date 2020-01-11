import cv2

# Color planes

img = cv2.imread('images/fruit.png')
cv2.imshow("Fruit image", img)

print(img.shape)

# TODO: Select a color plane, display it, inspect values from a row

cv2.waitKey(0)
