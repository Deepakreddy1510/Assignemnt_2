import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data_ab = np.loadtxt('data_ab.txt')

# Generate values for n
n_values = np.arange(0, 5)

# Create a stem plot with red color
plt.stem(n_values, data_ab, linefmt='r-', markerfmt='ro', basefmt='r-')

# Set labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title(r'Stem Plot of $x(n) = 0.25^n + 0.5^n$, $a=0.25, b=0.5$')
plt.grid(True)

# Display the plot
plt.show()

