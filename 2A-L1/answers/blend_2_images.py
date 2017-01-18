import os
import cv2
import numpy as np


# Blend two images
def blend(a, b, alpha):
    """ Blends to images using a weight factor.
    Args:
        a (numpy.array): Image A.
        b (numpy.array): Image B.
        alpha (float): Weight factor.

    Returns:
        numpy.array: Blended Image.
    """
    return alpha * a + (1. - alpha) * b

if os.name == "nt":  # Simple hack for windows users
    dolphin = cv2.imread(os.path.join("..\images", "dolphin.png"))
    bicycle = cv2.imread(os.path.join("..\images", "bicycle.png"))
else:
    dolphin = cv2.imread(os.path.join("images", "dolphin.png"))
    bicycle = cv2.imread(os.path.join("images", "bicycle.png"))

result = blend(dolphin, bicycle, 0.75)
cv2.imshow('Result', result.astype(np.uint8))
cv2.waitKey(0)
