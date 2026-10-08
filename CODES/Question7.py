import numpy as np

data = np.array([12, 25, np.nan, 18, 30, np.nan, 22, 15, 28, np.nan])

print("Original array:")
print(data)

nan_values = np.isnan(data)

print("\nNaN positions:")
print(nan_values)

mean = np.nanmean(data)
median = np.nanmedian(data)
std = np.nanstd(data)
minimum = np.nanmin(data)
maximum = np.nanmax(data)

print("\nNaN-aware statistics:")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
print("Minimum:", minimum)
print("Maximum:", maximum)

data[np.isnan(data)] = mean

print("\nArray after replacing NaNs with mean:")
print(data)

# Verify no NaN values remain
print("\nAre there any NaN values remaining?")
print(np.isnan(data).any())