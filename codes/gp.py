import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt("sequence_data.txt")

# Extract x and y values
x = data[:, 0]
y = data[:, 1]

# Plot the stem graph
plt.stem(x, y, basefmt='k-', linefmt='r-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of $x(n) = (0.25) 2^n$')
plt.grid(True)
plt.show()

