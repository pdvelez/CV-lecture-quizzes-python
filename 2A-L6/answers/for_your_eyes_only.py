import cv2
import numpy as np


# For Your Eyes Only
frizzy = cv2.imread('../images/frizzy.png', 0)
froomer = cv2.imread('../images/froomer.png', 0)
cv2.imshow('Frizzy', frizzy)
cv2.imshow('Froomer', froomer)

# Find edges in frizzy and froomer images
frizzy_edge = cv2.Canny(frizzy, 20, 100)
froomer_edge = cv2.Canny(froomer, 20, 100)
cv2.imshow('Frizzy Edge', frizzy_edge)
cv2.imshow('Froomer Edge', froomer_edge)

# Display common edge pixels
common = frizzy_edge * froomer_edge
cv2.imshow('Common', common.astype(np.float))
cv2.waitKey(0)
