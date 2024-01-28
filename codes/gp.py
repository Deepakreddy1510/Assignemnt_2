import numpy as np
import matplotlib.pyplot as plt

# Define the sequence parameters
a = 0.25
r = 2

# Generate values for n
n_values = np.arange(0, 10)

# Calculate x(n) values
x_values = a * np.power(r, n_values)

# Create a stem plot
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r-')

# Set labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title(r'Stem Plot of $x(n) =(0.25)2^n$')

# Display the plot
plt.show()


