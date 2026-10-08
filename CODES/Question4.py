import numpy as np

readings = np.array([
    [45, 52, 60, 48],
    [50, 55, 65, 51],
    [47, 58, 62, 49],
    [53, 60, 70, 55],
    [49, 54, 68, 52],
    [56, 62, 75, 58],
    [52, 59, 72, 54],
    [60, 65, 80, 61]
])

sensor_mean = np.mean(readings, axis=0)
sensor_min = np.min(readings, axis=0)
sensor_max = np.max(readings, axis=0)
sensor_std = np.std(readings, axis=0)

highest_sensor = np.argmax(sensor_mean) + 1

threshold = 65

above_threshold = readings > threshold

print("Sensor Readings:")
print(readings)

print("\nSensor Mean:")
print(sensor_mean)

print("\nSensor Minimum:")
print(sensor_min)

print("\nSensor Maximum:")
print(sensor_max)

print("\nSensor Standard Deviation:")
print(sensor_std)

print("\nSensor with Highest Average Reading:", highest_sensor)

print("\nReadings Above Threshold:")
print(above_threshold)