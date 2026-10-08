import numpy as np

features = np.array([
    [25, 120, 3.2, 45],
    [30, 135, 4.1, 50],
    [22, 110, 2.8, 42],
    [35, 150, 5.0, 60],
    [28, 125, 3.7, 48],
    [40, 165, 5.5, 65],
    [32, 140, 4.5, 55],
    [27, 118, 3.0, 47],
    [45, 180, 6.2, 72],
    [38, 155, 5.1, 63]
], dtype=float)

mean = np.mean(features, axis=0)

std = np.std(features, axis=0)

standardized = (features - mean) / std

new_mean = np.mean(standardized, axis=0)

new_std = np.std(standardized, axis=0)

print("Original Feature Matrix:")
print(features)

print("\nFeature Means:")
print(mean)

print("\nFeature Standard Deviations:")
print(std)

print("\nStandardized Matrix:")
print(standardized)

print("\nNew Means:")
print(new_mean)

print("\nNew Standard Deviations:")
print(new_std)