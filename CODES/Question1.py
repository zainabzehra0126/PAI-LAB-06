import numpy as np

marks = np.array([
    [100, 65, 82, 55, 70],
    [45, 52, 48, 60, 50],
    [90, 88, 92, 85, 95],
    [62, 100, 58, 64, 68],
    [35, 40, 45, 38, 42],
    [75, 80, 100, 78, 85],
    [55, 60, 50, 48, 52],
    [88, 76, 90, 90, 82],
    [49, 51, 99, 55, 48],
    [68, 72, 55, 79, 75]
])

student_totals = np.sum(marks, axis=1)

student_averages = np.mean(marks, axis=1)

subject_averages = np.mean(marks, axis=0)

highest_student = np.argmax(student_averages) + 1

passed_count = np.sum(student_averages >= 50)

result = np.where(student_averages >= 50, "Pass", "Fail")

print("Student Totals:", student_totals)
print("Student Averages:", student_averages)
print("Subject Averages:", subject_averages)
print("Student with Highest Average:", highest_student)
print("Number of Students with Average >= 50:", passed_count)
print("Result:", result)