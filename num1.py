import numpy as np

# Create a NumPy array of student marks
marks = np.array([85, 90, 78, 92, 88, 76, 95])

# Display the student marks
print("Student Marks:")
print(marks)

# Display the number of students
print("Number of Students:", len(marks))

# Calculate the total marks
total = np.sum(marks)
print("Total Marks:", total)

# Calculate the average marks
average = np.mean(marks)
print("Average Marks:", average)

# Find the highest marks
highest = np.max(marks)
print("Highest Marks:", highest)

# Find the lowest marks
lowest = np.min(marks)
print("Lowest Marks:", lowest)

# Sort marks in ascending order
sorted_marks = np.sort(marks)
print("Marks in Ascending Order:", sorted_marks)

# Sort marks in descending order
descending_marks = np.sort(marks)[::-1]
print("Marks in Descending Order:", descending_marks)

# Add 5 bonus marks to every student
bonus_marks = marks + 5
print("Marks After Bonus:", bonus_marks)

# Count students who scored 90 or above
count = np.sum(marks >= 90)
print("Students Scoring 90 or Above:", count)
