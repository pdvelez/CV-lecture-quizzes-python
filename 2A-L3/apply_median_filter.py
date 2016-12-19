import cv2
import numpy as np


# Helper function
def imnoise(img_in, method, dens):

    if method == 'salt & pepper':
        img_out = np.copy(img_in)
        w, h = img_in.shape
        x = np.random.rand(w, h)
        ids = x < dens / 2.
        img_out[ids] = 0
        ids = dens / 2. <= x
        ids &= x < dens
        img_out[ids] = 255

        return img_out

    else:
        print "Method {} not yet implemented.".format(method)
        exit()

# Apply a median filter

# Read an image
img = cv2.imread('images/moon.png', 0)
cv2.imshow('Image', img)

# TODO: Add salt & pepper noise

# TODO: Apply a median filter. Use cv2.medianBlur
