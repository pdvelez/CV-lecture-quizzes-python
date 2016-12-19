import cv2
import numpy as np
import scipy.signal as sp


def normalize(img_in):
    img_out = np.zeros(img_in.shape)
    cv2.normalize(img_in, img_out, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    return img_out


# Gradient Direction
def select_gdir(gmag, gdir, mag_min, angle_low, angle_high):
    # TODO: Find and return pixels that fall within the desired mag, angle range
    result = gmag >= mag_min
    result &= gdir >= angle_low
    result &= gdir <= angle_high
    return result.astype(np.float)  # Converts bool array to float [0., 1.]

# Load and convert image to double type, range [0, 1] for convenience
img = cv2.imread('images/octagon.png', 0) / 255.
cv2.imshow('Image', img)  # assumes [0, 1] range for double images

# Compute x, y gradients
gx = cv2.Sobel(img, -1, dx=1, dy=0)
gy = cv2.Sobel(img, -1, dx=0, dy=1)
cv2.imshow('Gx', gx)
cv2.imshow('Gy', gy)

gmag = np.sqrt(gx**2 + gy**2)

# The minus sign here is used based on how imgradient is implemented in octave
# See https://sourceforge.net/p/octave/image/ci/default/tree/inst/imgradient.m#l61
gdir = np.arctan2(-gy, gx) * 180 / np.pi
cv2.imshow('Gmag', normalize(gmag / (4 * np.sqrt(2))).astype(np.uint8))
cv2.imshow('Gdir', normalize(gdir).astype(np.uint8))

# Find pixels with desired gradient direction
my_grad = select_gdir(gmag, gdir, 1, 30, 60)
cv2.imshow('My Grad', my_grad)
cv2.waitKey(0)
