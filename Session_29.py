#union
#We can create a union of 2 sets, which creates a new set containing unique elements found across both the sets
"""set1={1,2,3}
set2={2,3,4}
set3=set1.union(set2)
print(set3)"""

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
print(set3)

#intersection can also be performed by using '&' operator
set1 = {1,2,3}
set2 = {2,3,4}
set3=set1 & set2
print(set3)"""
#Both set1.intersection(set2) and set1 & set2 do exactly the same thing """
#Find Max and Min without using built-in functions
# The given set of numbers
"""nums = {12, 45, 23, 67, 34}
# To find the max and min without built-in functions,
# we first need to convert the set to a list to iterate over it.
numbers_list = list(nums)

print(numbers_list)"""


#Dictionories: Collection of key-value pairs
#How to we define dictionory

"""my_empty_dict={} #we have to define dictionory with {}   #alternative: my_empty_dict=dict()
print(f"dict:{my_empty_dict},type:{type(my_empty_dict)}")"""

#initilization: How we Define
"""dict1={"value1":1.6, "value2":10, "name":"Syed"}
dict2= dict(value1=1.6, value2=10, name="Syed")
print(dict1)
print(dict2)

print(f"equals: {dict1==dict2}")
print(f"lenght: {len(dict1)}")

print(f"keys: {dict1.keys()}")
print(f"values: {dict1.values()}")
print(f"items:{dict1.items()}")"""


#Setting the values
my_dict={}   #create a new dictionory
my_dict["key1"] = "value1"
my_dict["key2"] = 99
my_dict["key3"] = "Syed"
my_dict["key2"] = "Ravi" 

#print(my_dict)

#Accessing values:
"""print(f"value of key1: {my_dict['key1']}")
print(f"value of key2: {my_dict['key2']}")"""

#Access Key from value
# Create a dictionary with three key-value pairs
"""my_dict = {'name': 'Rizwan', 'age': 25, 'city': 'Khammam'}

# Store the value we want to search for in a variable
value_to_find = 'Khammam'
# Use a for loop to go through each key-value pair in the dictionary
for key, value in my_dict.items():
    # .items() returns both key and value together for each element in the dictionary
    # Check if the current value matches the value we are searching for
    if value == value_to_find:
        # If it matches, print the corresponding key
        print("Key:", key)"""

#Accessing a noneexistent key will raise "KeyError" (see dict.get(.).) for workaround):
#print(my_dict['key4'])

#Deleting a key-value pair: del dict[key]
"""my_dictn={"key1":"value1","key2":99, "keyx":"valuex"}
del my_dictn["keyx"]
print(my_dictn)"""

#Dictonary mutable
"""my_dict={"ham":"good", "carrot":"Semi good"}
my_other_dict=my_dict
#print(my_other_dict)

my_other_dict["carrot"] = "Super tasty"   #replace in semi good

my_other_dict["sausage"]="best ever"     #cretaing a new key

print(my_other_dict)"""
#print(my_dict)


#dict.get: Returns none if key is not in dict. However, you can also specify default return value which will be returned if key is not present in the dict.
"""my_dict={"a":1, "b":2, "c":3}
#value_of_d= my_dict.get("d")
value_of_d = my_dict.get("d", "my default value")
print(value_of_d)"""

# Create a dictionary using dict() constructor
# Keys = "food", "drink", "sport"
# Values = "ham", "beer", "football"
"""my_dict = dict(food="ham", drink="beer", sport="football")
# Print the dictionary before removing anything
print(f"dict before pops: {my_dict}")

# pop("drink") removes the key "drink" from the dictionary
# It also returns the value associated with "drink" → "beer"
food = my_dict.pop("drink")
print(f"food:{food}")  
# Output: food:beer
# Now the dictionary no longer has the "drink" key

print(my_dict)"""  
# Output: {'food': 'ham', 'sport': 'football'}

#dict.setdefault: its a one of the command
#Return the value of key defined as first parameter. if the key is not present in the dict, adds key with default value (second parameter)
"""my_dict={"a":1,"b":2,"c":3}
print(my_dict)

a=my_dict.setdefault("a","my default value")
d=my_dict.setdefault("d","my default value")
print(a)
print(d)"""


#dict.update: Merge two dicts  (its like append))
"""dict1={"a":1, "b":2,}
print(dict1)
dict2={"c":3}
dict1.update(dict2)
print(dict1)"""

#we can also give list values to key
"""good_dict={"mykey": ["python", "is","still", "cool"]}
print(good_dict)"""

#Count Word Occurrences in a Sentence using Dictionary"
# Define a string (sentence) in which we want to count word occurrences
sentence = "python is easy and python is powerful"
# Create an empty dictionary to store words as keys and their counts as values
word_count = {}
# Loop through each word in the sentence after splitting it by spaces
for word in sentence.split():  
    # sentence.split() → splits the sentence into ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']
    # For each word, get its current count from the dictionary
    # If the word is not found, default value 0 is returned
    # Then we add 1 to the count
    word_count[word] = word_count.get(word, 0) + 1  # word_count.get(word, 0) fetches the current count of 'word' from 'word_count'.

"""Step 1: Understanding word_count.get(word, 0)
.get(key, default_value) is a dictionary method
It tries to get the value for the given key (word)
If the key exists, it returns its current value
If the key doesn't exist, it returns the default_value (0 in this case)

Step 2: The Complete Process
Get current count: word_count.get(word, 0)
Add 1: + 1
Store back: word_count[word] = ...
Let's Trace Through the Example
Sentence: "python is easy and python is powerful"
Words: ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']

Iteration 1: word = "python"
word_count.get("python", 0) → "python" not in dictionary → returns 0

0 + 1 → 1

word_count["python"] = 1

Dictionary becomes: {"python": 1}

Iteration 2: word = "is"
word_count.get("is", 0) → "is" not in dictionary → returns 0
0 + 1 → 1
word_count["is"] = 1
Dictionary becomes: {"python": 1, "is": 1}

Iteration 3: word = "easy"
word_count.get("easy", 0) → "easy" not in dictionary → returns 0

0 + 1 → 1
word_count["easy"] = 1
Dictionary becomes: {"python": 1, "is": 1, "easy": 1}

Iteration 4: word = "and"
word_count.get("and", 0) → "and" not in dictionary → returns 0

0 + 1 → 1
word_count["and"] = 1
Dictionary becomes: {"python": 1, "is": 1, "easy": 1, "and": 1}

Iteration 5: word = "python" (second occurrence)
word_count.get("python", 0) → "python" exists with value 1 → returns 1

1 + 1 → 2
word_count["python"] = 2
Dictionary becomes: {"python": 2, "is": 1, "easy": 1, "and": 1}

Iteration 6: word = "is" (second occurrence)
word_count.get("is", 0) → "is" exists with value 1 → returns 1

1 + 1 → 2
word_count["is"] = 2
Dictionary becomes: {"python": 2, "is": 2, "easy": 1, "and": 1}

Iteration 7: word = "powerful"
word_count.get("powerful", 0) → "powerful" not in dictionary → returns 0

0 + 1 → 1
word_count["powerful"] = 1
Final dictionary: {"python": 2, "is": 2, "easy": 1, "and": 1, "powerful": 1}"""

# Finally, print the dictionary containing each word and its occurrence count
print("Word Count:", word_count)
#Output: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
