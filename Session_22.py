#Using '.format().: This  .format() method use to format strings. It allows for more flexibility in terms of the order of variables and additional formatting options.
"""name = "Rahul"
age=25
print("my name is {} and i am {} years old".format(name,age))

#Using f-strings (Formatted String Literals):  f-strings are a concise and readable way to format strings. They allow you to embed expressions directly within string literals by using curly braces {}
name = "Zareena"
age = 22
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)"""


"""decimal_number = 10
binary_value =bin(decimal_number) [2:]
print(binary_value)"""

#String Operations:                   Apple   A P P L E
#string can be concatenated using + 

"""f_str="Abc"
l_str="def"
number=10
#print(f_str+l_str)  #Output: Abcdef
print(f_str+number)"""

# string can be counted from the left using +ve indices, starting with 0
word = "python"
"""print(word[0])
print(word[1])
print(word[2])
print(word[3])        
print(word[4])
print(word[5])"""

#string can be counted fromm the right using -ve indices,starting with -1
"""print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])"""


#Access Charecter from the given string through loop
"""for ch in word:    #ch='p'  #ch='y'  #ch='t'  #ch='h'  #ch='o'  #ch='n'
    print(ch)"""
    
#print(len(word))

"""for i in range(len(word)-1,-1,-1):
    print(word[i])"""

#slicing
# - string can be sliced with [startIndex:endIndex]
# - startIndex is included and endIndex is excluded
# - startIndex must be < endIndex, else empty string is returned
# - if a slice index is out of range, python will go as far as it can

"""word="python"
print(word[0:3])
print(word[0:10])
print(word[-3:-1])

#print(word[-3:-6])
#print(word[6:3])
print(word[:2])
print(word[4:])"""


"""word="pyhton"
word[0] = 'e'
print(word)"""

#if you need different string, you should just create a new one

#pjython
word="pyhton"
"""newword= 'J' + word[0:]
print(newword)"""


"""newword1=word[0] + word[5]
print(newword1)"""

"""print(len('python'))
print('python'.find('t')) #find index of substring in string
print('python'.startswith('p'))  # check string starts with substring
print('python'.endswith('n'))    # check string ends with substring

print('PYTHON'.lower())
print('python'.upper())

print('a'.isalpha())  #True
print('abc123'.isalnum())  #True
print('12345'.isdigit())  #True #check if all characters in the string are digits
print('syed'.capitalize())  #Syed
print('  python  '.strip())  #python

print("syed rizwan".title())   #Syed Rizwan If you want each word’s first letter capitalized, use .title():

print('python is very easy'.split())  #the split() method in Python is used to split a string into a list of substrings based on a specified delimiter. By default, it splits the string at whitespace characters (spaces, tabs, newlines). In this case, the string 'python is very easy' is split into a list of words: ['python', 'is', 'very', 'easy'].
print("Syed".count('S'))

#.join() method in Python is used to concatenate a list or iterable of strings into a single string, with a specified separator between each element.
words = ["Python", "is", "fun"]
print(words)

sentence = " ".join(words)   # join with a space
print(sentence)"""


#print vowels in a given string
input_string = "Hello World!"
vowels = "aeiouAEIOU"
vowel_count = 0
vowel_list = []
for char in input_string:      #char="H", char='e
    if char in vowels:
        
        vowel_count += 1
        vowel_list.append(char)
print(f"Number of vowels in the given string: {vowel_count}")
print("Vowels in the given string:", vowel_list)
