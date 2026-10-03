# Program to reverse a string
"""input_string = "Python"
reversed_string = input_string[::-1]   # Using slicing to reverse the string
print("Reversed string:", reversed_string)"""

#loop through string ,Program to reverse a string
"""input_string = "Python"  # Input string to be reversed
reversed_string = ""  # Initialize an empty string to store the reversed string
# Loop through each character of the input string
# The loop iterates from the first character to the last
for char in input_string:
    # Concatenate the current character 'char' to the beginning of 'reversed_string'
    # This effectively adds characters in reverse order
    # For "Python":
    # 1. char = 'P', reversed_string = "P"
    # 2. char = 'y', reversed_string = "yP"
    # 3. char = 't', reversed_string = "tyP"
    # 4. char = 'h', reversed_string = "htyP"
    # 5. char = 'o', reversed_string = "ohtyP"
    # 6. char = 'n', reversed_string = "nohtyP"
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)"""   # Print the final reversed string


# Program to check if a string is a palindrome
"""input_string = "madam"
if input_string == input_string[::-1]:  # Compare the string with its reverse
    print("Palindrome")
else:
    print("Not a palindrome")"""
    
# Program to check if a string is a palindrome through loop
"""input_string = "python"
is_palindrome = True
# Initialize two pointers, one at the start and one at the end of the string
start_index = 0
end_index = len(input_string) - 1   #4
# Loop as long as the start pointer is less than the end pointer
while start_index < end_index: #The condition is 0 < 4, which is True. The loop starts. 
    # Compare the characters at the two pointers
        if input_string[start_index] != input_string[end_index]:  #This line becomes if input_string[0] != input_string[4]:. m!=m
            #The condition 'm' != 'm' is False. The code inside the if block is skipped.
            
            # If they don't match, it's not a palindrome
            is_palindrome = False
            break  # Exit the loop immediately
    
    # Move the pointers towards the center
        start_index += 1      #start_index becomes 0 + 1 = 1.
        end_index -= 1        #end_index becomes 4 - 1 = 3.
    #The loop condition is checked again: 1 < 3, which is True.
    #The condition is 2 < 2, which is False. The loop t
# Print the result based on the final value of the flag
if is_palindrome:         #if is_palindrome: The condition is if True:, which is True.
    print("Palindrome")
else:
    print("Not a palindrome")"""


# Program to find the first non-repeating character in a string 
"""input_string = "aabbcde"
for char in input_string:
    if input_string.count(char) == 1:
        print("First non-repeating character:", char)
        break"""
        
#How to print the second non repeating character in a string
"""input_string = "aabbcde"
non_repeating_chars = []  # Initialize an empty list to store non-repeating characters
for char in input_string:
    if input_string.count(char) == 1:  # Check if the character appears only once in the string
        non_repeating_chars.append(char)  # Add the non-repeating character to the list
    
if len(non_repeating_chars) >= 2:
    # Check if there are at least two non-repeating characters
    We want the second non-repeating character.
       The first non-repeating character is at index 0.
       The second non-repeating character is at index 1.
       To safely access index [1], we must have at least 2 elements in the list.
    print("Second non-repeating character:", non_repeating_chars[1])  # Print the second non-repeating character
else:
    print("There is no second non-repeating character.")"""


# String Compression : String compression means reducing the size of a string by representing repeated characters in a shorter format.
# ---------------------------------------------------------
# STRING COMPRESSION
# Input  : aaabbbcccaaa
# Output : a3b3c3a3
# ---------------------------------------------------------
# This is our original string.
#
# We have:
#
# a a a b b b c c c a a a
#
# We want to convert it into:
#
# a3 b3 c3 a3
#
# Because:
# aaa → a3
# bbb → b3
# ccc → c3
# aaa → a3
#
"""input_string = input("Enter a string to compress: ")

# We create an empty string.
#
# Purpose:
# We will slowly build our final compressed string.
#
# At the beginning, we don't have anything.
#
# compressed_string = ""
#
# Later:
# compressed_string = "a3"
# compressed_string = "a3b3"
# compressed_string = "a3b3c3"
#
compressed_string = ""

# We need to count how many times the SAME character
# appears continuously.
#
# The first character is:
#
# input_string[0] = "a"
#
# We already have ONE "a".
#
# Therefore:
#
# count = 1
#
count = 1
# ---------------------------------------------------------
# NOW WE START THE LOOP
# ---------------------------------------------------------


# len(input_string) gives the total number of characters.
#
# "aaabbbcccaaa"
# has 12 characters.
#
# Therefore:
#
# len(input_string) = 12
#
# range(1, 12) gives:
#
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#
# Why start from 1?
#
# Because we want to compare the CURRENT character
# with the PREVIOUS character.
#
# For example:
#
# current character  → input_string[1]
# previous character → input_string[0]
#
# If we started from 0, there would be no previous
# character at index -1 that we want to use here.
#
for i in range(1, len(input_string)):
    # -----------------------------------------------------
        # CURRENT CHARACTER VS PREVIOUS CHARACTER
        # -----------------------------------------------------
    
    
        # input_string[i]
        #
        # means:
        # "Give me the character at the CURRENT index."
        #
        # input_string[i - 1]
        #
        # means:
        # "Give me the character immediately BEFORE it."
        #
        #
        # Example when i = 1:
        #
        # input_string[1]     → "a"   current
        # input_string[1 - 1] → "a"   previous
        #
        # So we compare:
        #
        # "a" == "a"
        #
        if input_string[i] == input_string[i - 1]:
            # -------------------------------------------------
                    # SAME CHARACTER
                    # -------------------------------------------------
            
            
                    # If the current character and previous character
                    # are the SAME, it means the current group continues.
                    #
                    # Therefore, increase count by 1.
                    #
                    # Example:
                    #
                    # First "a":
                    # count = 1
                    #
                    # Second "a":
                    # count = 2
                    #
                    # Third "a":
                    # count = 3
                    #
            count += 1
        else:
                # -------------------------------------------------
                # CHARACTER HAS CHANGED
                # -------------------------------------------------
        
        
                # If we reach here, the current character is
                # DIFFERENT from the previous character.
                #
                # Example:
                #
                # Current character = "b"
                # Previous character = "a"
                #
                # "b" != "a"
                #
                # This tells us:
                #
                # "The group of a's has finished."
                #
                # We counted:
                #
                # a a a
                #
                # Therefore:
                #
                # a occurred 3 times.
                #
                #
                # input_string[i - 1]
                #
                # gives the PREVIOUS character.
                #
                # Why previous character?
                #
                # Because the previous character is the character
                # whose counting has just finished.
                #
                # str(count)
                #
                # converts the number 3 into the string "3".
                #
                # So:
                #
                # "a" + "3"
                #
                # becomes:
                #
                # "a3"
                #
            compressed_string += input_string[i - 1] + str(count)
        
            # -------------------------------------------------
                    # RESET COUNT
                    # -------------------------------------------------
            
            
                    # A new character has started.
                    #
                    # For example:
                    #
                    # We finished:
                    #
                    # aaa
                    #
                    # Now we reached:
                    #
                    # b
                    #
                    # We have already seen ONE "b".
                    #
                    # Therefore we reset count to 1.
                    #
            count = 1
# ---------------------------------------------------------
# AFTER THE LOOP
# ---------------------------------------------------------


# There is an important problem.
#
# The loop saves a group ONLY when it finds a DIFFERENT
# character.
#
# Consider the last group:
#
# aaa
#
# There is NO character after these a's.
#
# Therefore, the loop never gets a chance to say:
#
# "The character changed!"
#
# So the last "aaa" is still not added to our result.
#
# We must add it manually after the loop.
#
#
# input_string[-1]
#
# means:
# "Give me the LAST character."
#
# In our string:
#
# input_string[-1] = "a"
#
#
# count is currently:
#
# count = 3
#
# because the last group contains:
#
# a a a
#
# Therefore:
#
# input_string[-1] + str(count)
#
# becomes:
#
# "a" + "3"
#
# = "a3"
#
compressed_string += input_string[-1] + str(count)


# Finally, print the compressed string.
#
# At this point:
#
# compressed_string = "a3b3c3a3"
#
print("Compressed string:", compressed_string) """

#Count vowels and consonants
"""input_string = "Hello, World!"
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for char in input_string:
    if char in vowels:
        vowel_count+=1
    else:
        consonant_count+=1
print("number of vowels=",vowel_count)
print("number of consonants=",consonant_count)"""       
    
"""input_string = "Hello, World!"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in input_string: #H,e,l,l,o,,, ,W,o,r,l,d,!
    if char.isalpha():    #Check if the character is an alphabet letter
        if char in vowels: #Check if the character is a vowel 
                    #H in vowels? False, e in vowels? True
            vowel_count += 1   #Increment the vowel count
                
        else: #If the character is not a vowel, it must be a consonant H in vowels? False
            consonant_count += 1   #Increment the consonant count
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)"""

#Program to check if two strings are anagrams
"""An anagram is a word  formed by rearranging the letters of another word  using all the original letters exactly once. 
For example, listen" and "silent" are anagrams because both use the same letters in a different order."""
"""str1 = "listen"
str2 = "silent"
print((sorted(str1)))
print((sorted(str2)))
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")"""
    
# Program to remove all duplicate characters from a string
# Input string with duplicate characters
"""input_string = "programming"

# Initialize an empty string to store the result without duplicates
# This will be used to build the final string
result_string = ""
# Loop through each character of the input string
# For each character, we check if it's already in our result string
for char in input_string:
    # If the character is not already in result_string, we add it
    if char not in result_string:
        result_string += char  # Concatenate the character to result_string
# Print the final string with all duplicates removed
print("Original string:", input_string)
print("String after removing duplicates:", result_string)"""
        

#Program to print decending order
text="python"
# Assuming 'chars' is a list of characters, for example: chars = ['p', 'y', 't', 'h', 'o', 'n']
chars=list(text)
# Get the total number of elements in the list and store it in the variable 'n'.
n = len(chars)

# This is the outer loop. It controls the number of passes through the list.
# After each pass, one more element will be in its correct sorted position.
# It runs 'n' times to ensure every element is checked.
for i in range(n):
    # This is the inner loop. It performs the actual comparisons and swaps.
        # It iterates from the first element up to the last unsorted element.
        # The 'n-i-1' is an optimization: after 'i' passes, the last 'i' elements are already sorted,
        # so we don't need to compare them again.
    for j in range(0, n-i-1):
         # Compare the current element with the next one.
        # For descending order, we check if the current element is LESS THAN the next one.
        # If it is, they are in the wrong order and need to be swapped.
        if chars[j] < chars[j+1]:
            # This is the swap. It swaps the positions of the two elements
                        # using a concise Python feature called tuple unpacking.
                        # The larger element "bubbles up" towards the beginning of the list.
            chars[j], chars[j+1] = chars[j+1], chars[j]
# After the loops are finished, the list 'chars' is sorted in descending order.
# The "".join(chars) method concatenates all characters in the list into a single string.
# Finally, print() displays the sorted string to the console.
# For example, if chars was ['p', 'y', 't', 'h', 'o', 'n'], it will print "ytponh".
print("".join(chars))
            









    
    
    