import matplotlib.pyplot as plt
import numpy as np

# Bar plot
def bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values = [3, 7, 2, 5]
    plt.bar(categories, values)
    plt.title("Bar Plot")
    plt.show()

# Scatter plot
def scatter_plot():
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Histogram
def histogram():
    data = np.random.randn(1000)
    plt.hist(data, bins=30)
    plt.title("Histogram")
    plt.show()

# Box plot
def box_plot():
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]
    plt.boxplot(data, vert=True)
    plt.title("Box Plot")
    plt.show()

bar_plot()
scatter_plot()
histogram()
box_plot()
