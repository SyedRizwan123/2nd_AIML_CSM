#set:set is a data structure a set is a collection of unique items, with the structural implementation of the set not allowing duplicate values a set is defined by curly braces{}
#set1={1,2,3}
#print(type(set1))
#print(set1)

#tuple=(1,1,2,3)
#print(tuple)

#Add an element
"""we can add an element to an existing set by using the add function . The resulting set will ensure uniquness of the added value within the set. 
An add operation modifies the original set """
"""set1={1,2,3}
set1.add(4)
set1.add(2)

print(set1)"""

#Find element:
"""We can search a set to see if a specified element is present within the set.
This can be done using the "in" 'keyword'""" 
"""set1={1,2,3}
contains2 = 2 in set1
contains4 = 4 in set1

print(contains2)
print(contains4)"""

#Remove an element
"""We can remove an element from a set by using the remove function.
A remove operation modifies the original set"""
"""set1={1,2,3}
set1.remove(2)
print(set1)
"""

"""We cannot attempt to remove an nonexistent element from the set. The operation will
return in 'keyerror' if the specified element to be removed is not found within the set"""
"""set1 = {1,2,3}
set1.remove(4)
print(set1)"""

"""To prevent an accidental 'KeyError', we can always check to see if the element is present within the 
set or not before attempting a delete operation"""
#if condition
"""set1={1,2,3,4}
if 4 in set1:
    set1.remove(4)
    
print(set1)"""

#pop element
#We can pop out a randomm element from the set.
"""my_set = {20,40,10,50,60}
popped_element = my_set.pop()
print(popped_element)
print(my_set)"""

# A pop operation will result in a 'KeyError' if invoked on an empty set
"""set1 = {1}
print(set1.pop())
set1.pop()"""

#union
#We can create a union of 2 sets, which creates a new set containing unique elements found across both the sets
"""set1={1,2,3}
set2={2,3,4}
set3=set1.union(set2)
print(set3)"""

#A union can also be performed using pipe operator
"""set1 = {1,2,3}
set2 = {2,3,4}
set3=set1 | set2
print(set3)"""


#intersection
"""One can performm an intersection operation on sets. This results in a set that contains elements
which are present in both sets. Let us take the same example as before, but this time we will do an intersection operation"""
"""set1={1,2,3}
set2={2,3,4}
set3= set1.intersection(set2)
print(set3)"""


#intersection can also be performed by using '&' operator
"""set1 = {1,2,3}
set2 = {2,3,4}
set3=set1 & set2
print(set3)"""
#Both set1.intersection(set2) and set1 & set2 do exactly the same thing """

#Dictionory: Collection of key-value pairs
#How to we define dictionory
"""my_empty_dict={} #we have to define dictionory with {}   #alternative: my_empty_dict=dict()
print(f"dict:{my_empty_dict},type:{type(my_empty_dict)}")"""

dict1={"value1":1.6, "value2":10, "name":"Syed"}
dict2= dict(value1=1.6, value2=10, name="Syed")

#print(dict1)
#print(dict2)

#print(f"equals: {dict1==dict2}")
#print(f"lenght: {len(dict1)}")

#dict.keys(), dict.values(), dict.items()
"""print(f"keys: {dict1.keys()}")
print(f"values:{dict1.values()}")
print(f"items:{dict1.items()}")"""


#setting values and Accessing values
#Setting the values
"""my_dict={}   #create a new dictionory
my_dict["key1"] = "value1"
my_dict["key2"] = 99
my_dict["key3"] = "Syed"   
my_dict["key2"]=101   #overriding existing value
#Accessing values:
print(f"value of key2: {my_dict['key2']}")"""

#Access Key from value
my_dict = {'name': 'Rizwan', 'age': 25, 'city': 'Khammam'}

# Store the value we want to search for in a variable
value_to_find = 'Khammam'
# Use a for loop to go through each key-value pair in the dictionary
for key, value in my_dict.items():
    # .items() returns both key and value together for each element in the dictionary

    # Check if the current value matches the value we are searching for
    if value == value_to_find:
        # If it matches, print the corresponding key
        print("Key:", key)