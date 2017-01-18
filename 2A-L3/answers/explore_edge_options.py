import cv2

# Explore edge options

# Load an image
img = cv2.imread('../images/fall-leaves.png')
cv2.imshow('Image', img)

# Create a Gaussian Filter
filter_size = 11
filter_sigma = 2
filter_kernel = cv2.getGaussianKernel(filter_size, filter_sigma)
filter_kernel = filter_kernel * filter_kernel.T

# Apply the kernel using different edge parameters. The ones below mimic what
# Matlab does. OpenCV has even more options, you should read the cv2.filter2D
# documentation for more
edge_params = {"replicate": cv2.BORDER_CONSTANT, "symmetric": cv2.BORDER_REFLECT,
               "circular": cv2.BORDER_WRAP}

method = "symmetric"
if method == "circular":
    # cv2.copyMakeBorder does not support cv2.BORDER_WRAP. Instead we create a new image
    # with borders that mirror the edges adding a number of pixels around it equal to
    # filter_size. Then we proceed to filter the image with the Gaussian Kernel.
    # Finally, we crop the blurred image back to the original size removing the added
    # border.

    temp_img = cv2.copyMakeBorder(img, filter_size, filter_size, filter_size, filter_size,
                                  edge_params[method])
    smoothed = cv2.filter2D(temp_img, -1, filter_kernel)
    smoothed = smoothed[filter_size:-filter_size,
                        filter_size:-filter_size]

else:
    smoothed = cv2.filter2D(img, -1, filter_kernel, borderType=edge_params[method])

cv2.imshow('Smoothed', smoothed)
cv2.waitKey(0)
