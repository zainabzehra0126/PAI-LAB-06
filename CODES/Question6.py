import numpy as np

rng1 = np.random.default_rng(42)
data1 = rng1.normal(50, 10, 1000)

mean1 = np.mean(data1)
median1 = np.median(data1)
std1 = np.std(data1)
min1 = np.min(data1)
max1 = np.max(data1)

inside1 = np.sum((data1 >= mean1 - std1) & (data1 <= mean1 + std1))
percentage1 = (inside1 / 1000) * 100

print("Experiment 1")
print("Mean:", mean1)
print("Median:", median1)
print("Standard Deviation:", std1)
print("Minimum:", min1)
print("Maximum:", max1)
print("Percentage inside 1 standard deviation:", percentage1, "%")


# Second experiment with a different seed
rng2 = np.random.default_rng(100)
data2 = rng2.normal(50, 10, 1000)

mean2 = np.mean(data2)
median2 = np.median(data2)
std2 = np.std(data2)
min2 = np.min(data2)
max2 = np.max(data2)

inside2 = np.sum((data2 >= mean2 - std2) & (data2 <= mean2 + std2))
percentage2 = (inside2 / 1000) * 100

print("\nExperiment 2")
print("Mean:", mean2)
print("Median:", median2)
print("Standard Deviation:", std2)
print("Minimum:", min2)
print("Maximum:", max2)
print("Percentage inside 1 standard deviation:", percentage2, "%")


print("\nComparison")
print("Mean difference:", abs(mean1 - mean2))
print("Standard deviation difference:", abs(std1 - std2))
print("Percentage difference:", abs(percentage1 - percentage2), "%")