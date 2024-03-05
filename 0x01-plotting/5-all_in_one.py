#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 12))

y0 = np.arange(0, 11) ** 3
plt.subplot(321)
plt.plot(y0)

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180
plt.subplot(322)
plt.scatter(x1, y1, c='c',label="Data Points")
plt.xlabel("Height in Inches")
plt.ylabel("Weight in Pounds")


x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)
plt.subplot(323)
plt.plot(x2, y2, label='Exponential Function')
plt.yscale('log')
plt.xlim(1, 28650)
plt.title("Exponential Decay of C-14")
plt.xlabel("Time(years)")
plt.ylabel("Fraction Remaining")

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)
plt.subplot(324)
plt.plot(x3, y31, linestyle='dashed', color='red')
plt.plot(x3, y32, linestyle='solid', color='green')
plt.xlabel("Time(years)")
plt.ylabel('Fraction Remaining')
plt.title("Exponential Decay of Radioactive Elements")
plt.xlim(0, 20000)
plt.ylim(0, 1)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
bins = list(range(30, 111, 10))
plt.subplot(325)
plt.hist(student_grades, bins, edgecolor='black')
plt.xlim(30, 110)
plt.ylim(0, 30)
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Project A")

plt.tight_layout()
plt.show()