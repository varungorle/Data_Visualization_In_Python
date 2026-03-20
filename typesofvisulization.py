import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
sns.set(style="whitegrid")
# Sample dataset
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
# 1. Line Plot
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
# 2. Bar Chart
plt.figure()
plt.bar(["A", "B", "C", "D"], [5, 7, 3, 4])
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
# 3. Histogram
plt.figure()
hist_data = np.random.randn(1000)
plt.hist(hist_data, bins=30, alpha=0.7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
# 4. Scatter Plot
plt.figure()
plt.scatter(x, y, s=100, alpha=0.6)
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
# 5. Pie Chart
plt.figure()
sizes = [30, 20, 25, 25]
labels = ["A", "B", "C", "D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
# 6. Box Plot
plt.figure()
box_data = np.random.randn(100)
plt.boxplot(box_data)
plt.title("Box Plot")
# 7. Heatmap (Seaborn)
plt.figure()
matrix = np.random.rand(6, 6)
sns.heatmap(matrix, annot=True, cmap="coolwarm")
plt.title("Heatmap")
# 8. Stacked Area Chart
plt.figure()
days = np.arange(1, 6)
sales_A = [3, 4, 2, 5, 6]
sales_B = [1, 2, 3, 4, 2]
plt.stackplot(days, sales_A, sales_B, labels=["Product A", "Product B"])
plt.legend()
plt.title("Stacked Area Chart")
plt.xlabel("Days")
plt.ylabel("Sales")
# 9. Violin Plot
plt.figure()
tips = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot")
# 10. Pair Plot
sns.pairplot(tips, hue="sex")
plt.suptitle("Pair Plot", y=1.02)
# 11. Bubble Chart
plt.figure()
bx = np.random.rand(20)
by = np.random.rand(20)
sizes = np.random.randint(50, 500, size=20)
plt.scatter(bx, by, s=sizes, alpha=0.5)
plt.title("Bubble Chart")
plt.xlabel("X")
plt.ylabel("Y")
# 12. 3D Scatter Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x3 = np.random.rand(50)
y3 = np.random.rand(50)
z3 = np.random.rand(50)
ax.scatter(x3, y3, z3)
ax.set_title("3D Scatter Plot")
plt.show()