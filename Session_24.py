#find longest word
"""text='python programming is easy'
longest=''   #longest='python', longest='programming'
for word in text.split():    #['python', 'programming','is','easy']
    if len(word) > len(longest):   #11>6, 2>11, 4>11
        longest=word
print('Longest word:',longest)"""

#Reverse words in a string
"""text='Hello World Python'
words=text.split()  #['Hello', 'World', 'Python']
#the split() method in Python is used to split a string into a list of substrings based on a specified delimiter. By default, it splits the string at whitespace characters (spaces, tabs, newlines). In this case, the string 'Hello World Python' is split into a list of words: ['Hello', 'World', 'Python'].
result=' '.join(reversed(words))  #['Python', 'Worls', 'Hello']
#.join() method in Python is used to concatenate a list or iterable of strings into a single string, with a specified separator between each element. In this case, we are using a space (' ') as the separator to join the reversed list of words back into a single string.
#reversed() function in Python is used to reverse the order of elements in an iterable (like a list, tuple, or string). In this case, it reverses the order of the words in the list created by text.split().
#so finally the result will be "Python World Hello"
print(result)"""  #Python Worls Hello

listpeople = ["tom","harry","jane","liz"]
"""print(type(listpeople))
print(listpeople)"""
listflowers = ["rose","lily","tulip","jasmine"]
listpets = ["cat","turtle","goat","dog"]
listnumfriends = [21,33,10,51]

#List of heterogenious items are not incorrect, just atypical
"""listAtypical = [1,'cat',0x43,567.55]       #0x45 UTF-8 ENCODING FOR 69
print(listAtypical)"""

#concatenate lists
"""listCon= listpeople + listflowers
print("listcon->", listCon)
print(len(listCon))"""

#refer to item in list with index
"""print("listpeople[2]->", listpeople[2])
print("listpeople[-3]->", listpeople[-3])"""

#slice list with [startindex:endindex]

listpeople = ["tom","harry","jane","liz"]
"""print("listpeople[2:]->", listpeople[2:])
print("listpeople[2:]->", listpeople[1:4])"""

#unlike strings, Lists are mutable
#assign to an index, we can update a value
"""listpets = ["cat","turtle","goat","dog"]
print(listpets)
listpets[0]='t-rex'
print(listpets)"""

#Assign to a slice
"""listpets[0:2] =['python','elephant']
print(listpets)"""

#delete a slice
"""listpets[2:4]=[]
print(listpets)"""

#append new items to list
"""listpets.append('fox')
print(listpets)"""

#clear a list by assignment to an empty list
"""listpets[:]=[]
print(listpets)"""

#nested list
"""nestedlist=[listpeople,listflowers]
print(nestedlist)

print("nestedlist[0]:",nestedlist[0])
print("nestedlist[1]:",nestedlist[1])

print(nestedlist[0][1])"""

#lists with integers
list1=[100,200,300]
list2=[5,15,25]
list3=[10,50,50,20,0,10,50]
print(list1)
print(list2)
print(list3)


list1.append(-400)   #Add an item to the end of the list. equalent to list
print("list1 Append:",list1)

list2.extend(list1)  #Extend the list2 by appending all the time in list1.
print("list2extend:", list2)

list2.remove(-400)  #Remove the first item from list2 whose value is -400.
print("list2 Remove Element:",list2)
"""list2.remove(100)  #Remove the first item from list2 whose value is -400.
print("list2 Remove Element:",list2)"""

"""del list2[3]       #Remove the item at index[6]
print("delete list2[3]:", list2)

list2.pop()       #Remove and returns the last item in the list
print("list2 pop():", list2)

pop=list2.pop()       #Remove and returns the last item in the list
print("list2 pop():", pop)

list3=[10,50,50,20,0,10,50]
print("Index of an element:", list3.index(20)) #Returns the index in list3 of element position

print(list3.count(50))   #count the number of times 50 appears in list3

list3.reverse()    #Reverse the items of list3 in place
print("list3 Reverse:", list3)

list3.sort()      #Sort the items of list3 in place
print("list3 sorted:",list3)

list3.clear()      #Remove all items from the list
print("list3 clear:",list3)

del list3        #Delete the list
print("delete list3:")
#print(list3)


list4=[10,50,50,20,0,10,50]
for num in list4:
    print(num)"""
    
#Find the largest and smallest element in a list
"""numbers = [12, 45, 67, 2, 89, 34]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))"""

#Find the largest and smallest element in a list without using built-in functions
"""numbers = [12, 45, 67, 2, 89, 34]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:   #12>12, 45>12
        largest = num
    elif num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)"""

#Reverse a list without using built-in reverse()
"""numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed:", reversed_list)"""

#Find the sum and average of list elements
"""numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("Sum:", total)
average = total / len(numbers)
print("Average:", average)"""

#Remove duplicates from a list

"""numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Unique elements:", unique)"""


#Find the second largest number in a list
# List of numbers
"""numbers = [12, 45, 67, 89, 34]
# Sort the list in ascending order (smallest → largest)
numbers.sort()   # After sorting: [12, 34, 45, 67, 89]
# Print the second largest element
print("Second Largest:", numbers[-2])"""


##Find the second largest number in a list without using the sort()
numbers = [10, 50, 40, 50, 50,34]
for index, num in enumerate(numbers):
    if num==50:
        print(index)