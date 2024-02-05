import numpy as np
import matplotlib.pyplot as plt

# Load data for the first plot
data1 = np.loadtxt("coordinate1.txt")

# Extract x and y values for the first plot
x1 = data1[:, 0]
y1 = data1[:, 1]

# Load data for the second plot
data2 = np.loadtxt("coordinate2.txt")

# Extract x and y values for the second plot
x2 = np.arange(0, 5)
y2 = data2

# Create subplots
plt.subplot(2, 1, 1)
plt.stem(x1, y1, basefmt='k-', linefmt='r-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of $x(n) = (0.25) 2^n$, $a= 0.25, r=2$')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(x2, y2, linefmt='r-', markerfmt='ro', basefmt='r-')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title(r'Stem Plot of $x(n) = 0.25^n + 0.5^n$, $a=0.25, b=0.5$')
plt.grid(True)

# Adjust layout for better appearance
plt.tight_layout()

# Display the combined plot
plt.show()

