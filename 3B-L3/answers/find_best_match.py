import cv2
import numpy as np


# Find best match
def find_best_match(patch, strip):
    # TODO: Find patch in strip and return column index (x value) of topleft corner

    # We will use SSD to find out the best match

    best_id = 0
    min_diff = np.infty

    for i in range(int(strip.shape[1] - patch.shape[1])):
        temp = strip[:, i: i + patch.shape[1]]
        ssd = np.sum((temp - patch) ** 2)
        if ssd < min_diff:
            min_diff = ssd
            best_id = i

    return best_id

# Test code:

# Load images
left = cv2.imread('../images/flowers-left.png')
right = cv2.imread('../images/flowers-right.png')
cv2.imshow('Left', left)
cv2.imshow('Right', right)

# Convert to grayscale, double, [0, 1] range for easier computation
left_gray = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY) / 255.
right_gray = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY) / 255.

# Define image patch location (topleft [row col]) and size
patch_loc = [94, 119]  # Adapted index values to approximate the difference with the original images shapes
patch_size = [100, 100]

# Extract patch (from left image)
patch_left = left_gray[patch_loc[0]:patch_loc[0] + patch_size[0],
                       patch_loc[1]:patch_loc[1] + patch_size[1]]
cv2.imshow('Patch', patch_left)

# Extract strip (from right image)
strip_right = right_gray[patch_loc[0]: patch_loc[0] + patch_size[0], :]
cv2.imshow('Strip', strip_right)

# Now look for the patch in the strip and report the best position (column index of topleft corner)
best_x = find_best_match(patch_left, strip_right)
print( best_x)

patch_right = right_gray[patch_loc[0]: patch_loc[0] + patch_size[0],
                         best_x: best_x + patch_size[1]]

# Because we had to adjust the index numbers for this quiz, we will
# plot a rectangle where the best match is in the right image. This
# will help us verify if what we did was correct.
cv2.rectangle(right, (best_x, patch_loc[0]),
              (best_x + patch_size[0], patch_loc[0] + patch_size[0]),
              (0, 0, 255),
              2)
cv2.imshow("Match", right)
cv2.waitKey(0)
