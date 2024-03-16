#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
print(student_grades)
bins = list(range(30, 111, 10))
plt.hist(student_grades, bins, edgecolor='black')
plt.xlim(30, 110)
# plt.ylim(0, 30)
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Project A")
plt.show()
