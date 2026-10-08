import numpy as np

image = np.array([
    [12, 85, 143, 201, 56, 174, 233, 91],
    [67, 190, 34, 122, 245, 78, 156, 210],
    [230, 45, 99, 187, 63, 151, 219, 28],
    [110, 172, 240, 54, 136, 88, 199, 75],
    [39, 221, 118, 164, 250, 102, 47, 183],
    [154, 72, 205, 31, 129, 238, 84, 116],
    [193, 26, 147, 229, 58, 175, 97, 212],
    [81, 246, 43, 135, 188, 69, 157, 105]
])

minimum = np.min(image)

maximum = np.max(image)

mean = np.mean(image)

threshold = 150

mask = image > threshold

thresholded_image = np.where(image > threshold, 255, 0)

print("Image:")
print(image)

print("\nMinimum Intensity:", minimum)
print("Maximum Intensity:", maximum)
print("Mean Intensity:", mean)

print("\nBinary Mask:")
print(mask)

print("\nThresholded Image:")
print(thresholded_image)