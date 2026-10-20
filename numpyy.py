import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

# Display the original array
print("Original Array:")
print(numbers)

# Display the first element
print("First Element:", numbers[0])

# Display the last element
print("Last Element:", numbers[-1])

# Find the length of the array
print("Length of Array:", len(numbers))

# Calculate the sum of all elements
print("Sum of Elements:", np.sum(numbers))

# Calculate the mean (average)
print("Average:", np.mean(numbers))

# Find the maximum element
print("Maximum Element:", np.max(numbers))

# Find the minimum element
print("Minimum Element:", np.min(numbers))

# Multiply each element by 2
print("Array After Multiplication:", numbers * 2)

# Add 5 to each element
print("Array After Addition:", numbers + 5)

# Sort the array
print("Sorted Array:", np.sort(numbers))
