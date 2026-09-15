# Program to calculate the Area of a Circle

"""What is the Problem?
The task is to calculate the area of a circle when the radius is given by the user."""

"""Understanding the Problem in Simple Words
==> A circle is a round shape (like a coin or plate).
==> The radius is the distance from the center to the boundary.
==> Using the radius, we calculate how much space is inside the circle (area).

Steps to Solve the Problem
==> Take input from the user (radius).
==> Use the formula → Area = π × r × r
==> Calculate the result.
==> Display the output."""

# Define a constant value for PI
PI = 3.1415

# Take input from the user (radius of the circle)
# input() takes value as string, so we convert it to float
radius = float(input("Enter radius of circle: "))

# Calculate the area using formula: PI * r * r
area = PI * radius * radius

# Display the result
print("Area of circle:", area)