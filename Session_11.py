# Program to calculate the Area of a Rectangle
"""Problem Explanation: Area of a Rectangle
What is the Problem?
we need to calculate the area of a rectangle using:
Length
Breadth (Width)

Mathematical Concept

A=l×b

A → Area of rectangle
l → Length
b → Breadth

Simple Understanding
A rectangle is a four-sided shape (like a book or table).
To find its area:
Multiply length × breadth

Steps to Solve
Take length and breadth as input from user
Apply formula → length × breadth
Display the result  """

# Take input from the user
# Convert input values into integers
"""length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

# Calculate area using formula: length * breadth
area = length * breadth

# Display the result
print("Area of Rectangle:", area)"""

# Program to calculate Total and Average of 3 subjects
# Take input from the user
# Convert input values into float (marks can be decimal)
"""english = float(input("Enter English marks: "))
hindi = float(input("Enter Hindi marks: "))
maths = float(input("Enter Maths marks: "))

# Calculate total marks
total = english + hindi + maths

# Calculate average marks
average = total / 3        # formula to calculate average = total number of subjects / number of subjects

print(total)
print(average)"""


"""What is the Problem?
we need to calculate an employee’s Gross Salary (GS) based on:
Basic Salary (BS)

# Allowances:
HRA (House Rent Allowance) = 80% of BS
TA (Travel Allowance) = 40% of BS
DA (Dearness Allowance) = 30% of BS

# Mathematical Concept
HRA = 0.8 × Basic Salary
TA = 0.4 × Basic Salary
DA = 0.3 × Basic Salary

Gross Salary = BS + HRA + TA + DA

# Simple Understanding
Basic salary is the main salary
Additional benefits (HRA, TA, DA) are calculated as percentages
Add all → get Gross Salary"""

# Take basic salary input from user
"""basic_salary = int(input("Enter basic salary: "))   #30000

# Calculate allowances based on percentage
hra = basic_salary * 0.8   # 80% of basic salary  #24000
ta = basic_salary * 0.4    # 40% of basic salary  #12000
da = basic_salary * 0.3    # 30% of basic salary  #9000

# Calculate gross salary
gross_salary = basic_salary + hra + ta + da #75000

# Display results
print("\nHRA (80%) =", hra)
print("TA (40%) =", ta)
print("DA (30%) =", da)
print("\nGross Salary =", gross_salary)"""

"""Problem Explanation: Simple Interest
What is the Problem?

You need to calculate Simple Interest (SI) based on:

Principal Amount (P)
Time (T) in years
Rate of Interest (R) in percentage

# Mathematical Concept
SI= P×T×R / 100

P → Principal (amount)
T → Time (years)
R → Rate (%)

# Simple Understanding
You invest some money (principal)
Bank gives interest based on:
time
rate
Formula calculates how much extra money you earn

# Steps to Solve
Take amount, time, rate as input
Apply formula → (P × T × R) / 100
Display the result"""

# Program to calculate Simple Interest

# Take input from user
# Convert values into integers
"""amount = int(input("Enter principal amount: "))
time = int(input("Enter time (in years): "))
rate = int(input("Enter rate of interest (%): "))

# Calculate simple interest using formula
simple_interest = (amount * time * rate) / 100

# Display result
print("\nRate of Interest =", rate, "%")
print("Simple Interest =", simple_interest)"""

# Program to swap two numbers using a third variable
# Take input from user
"""a = int(input("Enter value of a: "))  #10
b = int(input("Enter value of b: "))  #20

# Display values before swapping
print("\nBefore swapping a =", a, "b =", b)

# Swapping logic using third variable
temp = a   # store value of a in temp   #10
a = b      # assign value of b to a   #20
b = temp   # assign value of temp (old a) to b  #10
# Display values after swapping
print("After swapping a =", a, "b =", b)"""

# Program to swap two numbers without using a third variable
# Take input from user
"""a = int(input("Enter value of a: "))   #10
b = int(input("Enter value of b: "))   #20

a=a+b  # Step 1: a now holds the sum of a and b  #10+20=30
b=a-b  # Step 2: b now holds the original value of a  #30-20=10
a=a-b  # Step 3: a now holds the original value of b  #30-10=20

#a, b = b, a  # Swapping using tuple unpacking

# Display values after swapping
print("\nAfter swapping a =", a, "b =", b)"""


# Program to calculate sum of N natural numbers
"""Problem Explanation: Sum of N Natural Numbers
What is the Problem?
we need to calculate the sum of first N natural numbers.

Natural numbers → 1, 2, 3, 4, ... , N
Example: If N = 5 → Sum = 1 + 2 + 3 + 4 + 5 = 15

#Mathematical Concept
S=n(n+1)/2
S → Sum of numbers
n → Number of terms

#Simple Understanding
--> Instead of adding numbers one by one
--> We use a direct formula to save time

#Steps to Solve
--> Take n value from user
--> Apply formula → n × (n + 1) / 2
--> Display the result"""

# Take input from user
"""n = int(input("Enter n value: "))

# Calculate sum using formula
sum_n = (n * (n + 1)) // 2   # // for integer result
#n=5 then sum_n = (5 * (5 + 1)) // 2 = (5 * 6) // 2 = 30 // 2 = 15

# Display result
print("Sum of", n, "natural numbers is =", sum_n)"""

# Program to calculate sum of squares of N natural numbers
""" Problem Explanation: Sum of Squares of N Natural Numbers
# What is the Problem?
we need to calculate the sum of squares of first N natural numbers.

Example:
If N = 3
Sum = 1² + 2² + 3² = 1 + 4 + 9 = 14

Mathematical Concept

S=n(n+1)(2n+1)/6

--> S → Sum of squares
--> n → Number of terms

# Simple Understanding
--> Instead of calculating:1² + 2² + 3² + ... + n²
--> We use a direct formula to save time

#Steps to Solve
--> Take n value from user
--> Apply formula → n(n+1)(2n+1)/6
--> Display the result """

# Take input from user
"""n = int(input("Enter n value: "))  #3
# Calculate result using formula
result = (n * (n + 1) * (2 * n + 1)) // 6   # // gives integer result
# If n=3 then result = (3 * (3 + 1) * (2 * 3 + 1)) // 6
# = (3 * 4 * 7) // 6
# Display result
print("Sum of squares of", n, "is =", result)"""


# Program to calculate Volume of a Cylinder














