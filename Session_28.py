"""a,b,c=10,7,8
print(c)"""


#tuple packing and unpacking
#tuple packing and unpacking is a way to assign multiple values to multiple variables in a single statement
#tuple packing
"""tuple7= 1,2,3   #(1,2,3)
print("tuple7:", tuple7, len(tuple7))"""

#tuple unpacking
"""tuple7= (1,2,3)
x,y,z=tuple7
print("tuple unpacking:", x,y,z)"""

#we can convert list in tuples
"""tuple6=tuple([1,2,3])
print(type(tuple6))
print("tuple6:", tuple6, len(tuple6))"""

# Define the two tuples
"""t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenate the two tuples using the '+' operator
concatenated_tuple = t1 + t2

# Print the original tuples and the result
print(f"Original tuple t1: {t1}")
print(f"Original tuple t2: {t2}")
print(f"The concatenated tuple is: {concatenated_tuple}")"""


#Repeating Elements: Given colors = ("red", "blue"),repeat it 3 times using *.
# Define the original tuple with colors
"""colors = ("red ", " blue")
# Repeat the tuple 3 times using the * operator.
# The result is a new tuple with the original elements repeated in sequence.
#repeated_colors = colors * 3
repeated_element = colors[0] * 3
# Print the original and the new, repeated tuple to show the result.
print(f"Original tuple: {colors}")
#print(f"Repeated tuple: {repeated_colors}")
print(f"Repeated element: {repeated_element}")"""


# Define the tuple of numbers
"""nums = (1, 2, 3, 2, 4, 2, 5)
# Find the index of the first occurrence of 3 using the .index() method
# This method returns the index of the first matching item.
index_of_3 = nums.index(3)
# Count how many times 2 occurs using the .count() method
# This method returns the total number of occurrences of an item in the tuple.
count_of_2 = nums.count(2)
# Print the results
print(f"The index of the first occurrence of 3 is: {index_of_3}")
print(f"The number of times 2 occurs is: {count_of_2}")"""

# Define the nested tuple
"""nested = (1, (2, 3), (4, (5, 6)))
print(len(nested))  # Output: 3
# Access and print the number 3
# The first index, 1, selects the inner tuple (2, 3).
# The second index, 1, selects the element 3 from that inner tuple.
print("Accessing 3:", nested[1][1])
# Access and print the number 6
# The first index, 2, selects the inner tuple (4, (5, 6)).
# The second index, 1, selects the nested tuple (5, 6).
# The third index, 1, selects the element 6 from that deepest tuple.
print("Accessing 6:", nested[2][1][1])"""


#Check Membership
"""animals = ("dog", "cat", "lion", "tiger")
# Check if "cat" exists in the tuple and store the boolean result in the variable 'is_cat_present'
is_cat_present = "cat" in animals
# Check if "elephant" exists in the tuple and store the boolean result in the variable 'is_elephant_present'
is_elephant_present = "elephant" not in animals
# Print the result for "cat"
print(f"Is 'cat' present in the tuple? {is_cat_present}")
# Print the result for "elephant"
print(f"Is 'elephant' present in the tuple? {is_elephant_present}")"""

#Tuple of Tuples Given students = (("Alice", 20), ("Bob", 22), ("Charlie", 19)), print all student names and ages.
#output: Alice is 20 years old, Bob is 22 years old, Charlie is 19 years old.
# Define the tuple of tuples containing student names and ages
"""students = (("Alice", 20), ("Bob", 22), ("Charlie", 19))
# Iterate through each student tuple in the students tuple
for student in students:
    # Unpack the student tuple into name and age variables
    #name, age = student   # Unpacking the tuple into two variables name and age, output: Alice 20 
    # Print the formatted string with the student's name and age
    #print(f"{name} is {age} years old")
    
    # Alternatively, you can access the elements directly without unpacking
    #print(f"{student[0]} is {student[1]} years old")  """ 

#Reversing a Tuple: Given nums = (10, 20, 30, 40, 50), reverse the tuple.
"""nums = (10, 20, 30, 40, 50)
# The [::-1] slicing syntax creates a reversed copy of the tuple.
reversed_nums = nums[::-1]

# Print the original and the reversed tuples to show the change.
print(f"Original tuple: {nums}")
print(f"Reversed tuple: {reversed_nums}")"""

#set:set is a data structure a set is a collection of unique items, with the structural implementation of the set not allowing duplicate values a set is defined by curly braces{}
"""set1={1,2,3}
print(set1)"""

#Add an element
"""we can add an element to an existing set by using the add function . The resulting set will ensure uniquness of the added value within the set. 
An add operation modifies the original set """
"""set1={1,2,3}
set1.add(4)
set1.add(2)
print(set1)"""

#Find element:
"""We can search a set to see if a specified element is present within the set.
This can be done using the in 'keyword'""" 
"""set1={1,2,3}
contains2 = 2 in set1
contains4 = 4 in set1
print("contain2:", contains2)
print("contain4:", contains4)"""

#Remove an element
"""We can remove an element from a set by using the remove function.
A remove operation modifies the original set""" 
"""set1={1,2,3}
set1.remove(2)
print(set1)"""

"""We cannot attempt to remove an nonexistent element from the set. The operation will
return in 'keyerror' if the specified element to be removed is not found within the set"""
"""set1 = {1,2,3}
set1.remove(4)
print(set1)"""

"""To prevent an accidental 'KeyError', we can always check to see if the element is present within the 
set or not before attempting a delete operation"""
#if condition
"""set1={1,2,3}
if 4 in set1:
    set1.remove(4)
print(set1)"""

#pop element
"""We can pop out a randomm element from the set. This is usually done when to iterate over
the set to fully consume it. What we mean by consume is, we don't want the value we popped to be present within the set;
and we will continue to do so unit the set is empty"""

my_set = {5,2,1,4,3}
popped_element = my_set.pop()
print(popped_element)
print(my_set)