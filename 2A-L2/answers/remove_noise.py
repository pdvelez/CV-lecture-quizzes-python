import cv2
import numpy as np


# Helper function
def imshow(title, image):
    # WARNING: Using np.clip to get results similar to the quiz.
    # This is NOT a good practice because you are discarding information that is
    # below 0 and above 255. Use normalization instead.

    image = np.clip(image, 0, 255).astype(np.uint8)
    cv2.imshow(title, image.astype(np.uint8))

# Apply a Gaussian filter to remove noise
img = cv2.imread('images/saturn.png', 0)
cv2.imshow('Img', img)

# Add some noise
noise_sigma = 25
w, h = img.shape
noise = np.random.randn(w, h) * noise_sigma
noisy_img = img + noise

imshow('Noisy Image', noisy_img)  # Customized imshow function to match the quiz

# Create a Gaussian filter
filter_size = 11
filter_sigma = 2

# OpenCV does not have a fspecial type of function. Instead we will cv2.getGaussianKernel
# to generate a Gaussian kernel.
filter_kernel = cv2.getGaussianKernel(filter_size, filter_sigma)

# This however generates a 1D kernel and we want a 2D that is of shape (filter_size, filter_size)
# To achieve this we multiply this array by its transpose
filter_kernel = filter_kernel * filter_kernel.T

# Apply it to remove noise
smoothed = cv2.filter2D(noisy_img, -1, filter_kernel)

imshow('Smoothed image', smoothed)  # Customized imshow function to match the quiz
cv2.waitKey(0)
