#What is enumerate() in Python?
#Simple definition:
"""enumerate() is a Python built-in function that gives us both the index (position) 
and the value of each item while looping through a sequence."""
#Normally, if you loop through a list:
"""students = ["Rahul", "Anil", "Priya"]
for student in students:
    print(student)"""
    
"""But what if we also want the position/index?
0 → Rahul
1 → Anil
2 → Priya

That's where enumerate() is useful."""

"""Imagine you are a teacher and you have students standing in a line:
Position       Student

   0           Rahul
   1           Anil
   2           Priya
   3           John

"Rahul is at position 0."

"Anil is at position 1."

"Priya is at position 2." """


# ---------------------------------------------------------
# EXAMPLE: enumerate()
# ---------------------------------------------------------
# We create a list called "students".
#
# This list contains 3 student names.
#
# Python automatically gives every item an index (position):
#
# Index 0 → Rahul
# Index 1 → Anil
# Index 2 → Priya
"""students = ["Rahul", "Anil", "Priya"]
for index, student in enumerate(students):
    print(index, student)"""
    
# ---------------------------------------------------------
# FIND THE INDEX POSITIONS OF NUMBER 50
# ---------------------------------------------------------
"""numbers = [10, 50, 40, 50, 50, 34]
for index, num in enumerate(numbers):
    if num == 50:
        print(f"Number 50 found at index position: {index}")"""
        
#Check if a list is a palindrome
"""list1 = [1, 2, 3, 2, 1]
if list1 == list1[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")"""


#Find the common elements between two lists
"""list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []

for x in list1:             # check each element in list1
    if x in list2:          # if element is also in list2
        common.append(x)    # add to common list

print("Common Elements:", common)"""


#Find all even numbers from a list
"""numbers = [10, 15, 20, 25, 30]
evennumbers=[]
for num in numbers:
    if num % 2 == 0:
        evennumbers.append(num)
print("Even numbers", evennumbers)"""



#print vowels from a list of cities
"""cities = ["hyderabad", "mumbai", "Banglore", "Kolkata", "chennai"]
vowels = "aeiouAEIOU"   # include uppercase vowels also
for city in cities:
    print("City:", city)
    for ch in city:
        if ch in vowels:          # if character is a vowel
            print(ch, end=" ")    # print vowel
    print()"""
    
# Missing number

"""numbers = [1, 2, 3, 5, 6]
# This list contains numbers from 1 to 6,
# but number 4 is missing.
n = 6
# 'n' represents the largest number in the expected sequence.
# Since we expect numbers from 1 to 6, n = 6.
missing = n * (n + 1) // 2 - sum(numbers)
# First calculate the sum of ALL numbers from 1 to n.
#
# Formula:
# n * (n + 1) // 2
#
# For n = 6:
# 6 * (6 + 1) // 2
# 6 * 7 // 2
# 6* 3.5
# 21
#
# So, the expected sum is 21.
#
#
# Now calculate the sum of the numbers actually present:
#
# sum(numbers)
# = 1 + 2 + 3 + 5 + 6
# = 17
#
#
# Therefore:
#
# missing = 21 - 17
# missing = 4
print(f"missing number is {missing}")"""


#List comprehension = create a new list by looping over an existing sequence, optionally applying a condition.
"""Basic syntax
[expression for item in iterable]

For example:

[x * 2 for x in numbers]"""

#Suppose we want to create a list of squares:
"""numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num * num)
print(squares)"""

#We took every number from the list, multiplied it by itself, and stored the result in a new list."""
#The same program can be written as:
"""numbers=[1,2,3,4,5]
print([x ** 2 for x in numbers])"""

# Create a list containing numbers from 1 to 5
"""numbers = [1, 2, 3, 4, 5]
# Create a new list called 'squares'
# For every 'num' in the numbers list,
# calculate num * num and put the result into squares.
squares = [num * num for num in numbers]
print(squares)"""


#Example:2 imagine you have 5 students:
#Rahul,Anil,Priya,John,Sara
#You want to create a new list containing the length of each student's name.

#Normally:
"""names = ["Rahul", "Anil", "Priya", "John", "Sara"]
lengths = []
for name in names:
    lengths.append(len(name))

print(lengths)"""


#With list comprehension:
# Create a list containing student names
"""names = ["Rahul", "Anil", "Priya", "John", "Sara"]
# Create a new list called 'lengths'
#
# for name in names:
#     Take one student name at a time from the 'names' list.
#
# len(name):
#     Find the number of characters in that student's name.
#
# The calculated length is automatically added
# to the new 'lengths' list.
lengths = [len(name) for name in names]

# Print the final list containing the length of each name
print(lengths)"""

#List Comprehension with if
#Suppose we want only even numbers.

#Normal approach:
"""numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)"""

#Using list comprehension:
#Syntax:
    #[expression for item in iterable if condition]
# Create a list containing numbers from 1 to 6
"""numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
# Print the final list containing only even numbers
print(even_numbers)"""

#What is happening inside the loop?
#The main line is:
    #even_numbers = [num for num in numbers if num % 2 == 0]


#Read it like normal English:
""" "Take each number from numbers, and put it into the new list only 
if the number is even." """

"""Same program using a normal for loop

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)
Output:
[2, 4, 6]

List comprehension does the same thing:

even_numbers = [num for num in numbers if num % 2 == 0]

explanation

"The for loop checks every number. The if condition acts like a filter. Only numbers that pass the filter are added to the new list." """

# Move all zeros to the end of the list

numbers = [0, 1, 0, 3, 12, 0, 5]





