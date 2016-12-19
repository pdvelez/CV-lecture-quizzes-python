import cv2
import numpy as np
import scipy.signal as sp


# Find template 2D
def find_template_2D(template, img):
    c = sp.correlate2d(img, template, mode='same')

    # These y, x coordinates represent the peak. This point needs to be
    # translated to be the top-left corner as the quiz suggests
    y, x = np.unravel_index(np.argmax(c), c.shape)
    return y - template.shape[0] // 2, x - template.shape[1] // 2

tablet = cv2.imread('images/tablet.png', 0)
cv2.imshow('Tablet', tablet)

glyph = tablet[74:165, 149:184]
cv2.imshow('Glyph', glyph)

tablet_2 = 1. * tablet - np.mean(tablet)
glyph_2 = 1. * glyph - np.mean(glyph)

y, x = find_template_2D(glyph_2, tablet_2)
print "Y: {}, X: {}".format(y, x)

# The code below is not part of the quiz but helps to verify the results are
# what we are looking for.
tablet = cv2.cvtColor(tablet, code=cv2.COLOR_GRAY2BGR)
cv2.rectangle(tablet, (x, y), (x + glyph.shape[1], y + glyph.shape[0]),
              (0, 0, 255), thickness=2)
cv2.imshow('Rectangle', tablet)
cv2.waitKey(0)
