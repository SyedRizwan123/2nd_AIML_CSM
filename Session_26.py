"""numbers=[0,1,0,3,12,0,5]
list=[]
for num in numbers:
    if num>0:
        list.append(num)
for num in numbers:
    if num==0:
        list.append(num)
print(list)"""


"""numbers = [0, 1, 0, 3, 12, 0, 5]
result = []
for num in numbers:
    if num != 0:
            # Check whether the current number is NOT equal to 0.
            #
            # If num is 0 → condition is False → don't add it.
            # If num is not 0 → condition is True → add it.
    
        result.append(num)
result += [0] * numbers.count(0)
print(result) """   

"""numbers = [0, 1, 0, 3, 12, 0, 5]
result = [num for num in numbers if num != 0]
result += [0] * numbers.count(0)
print(result)"""

#Built-in Python Sorting
#sort()
#sorts the original list (modifies it).
#does not return any value (returns none)
#used only with lists
#syntax: list.sort()
"""nums=[5,2,8,1]
nums.sort(reverse=True)
print(nums)"""

#sorted
#Returns a new sorted list
#does not modify the orginal list
#can be used with any iterable(list,tuple,string, etc..)
#syntx:sorted(iterable)

"""nums=[5,2,8,1]
new_num=sorted(nums)
print("newlist",new_num)
print(nums)"""

"""nums=[5,2,8,1]
new_num=sorted(nums, reverse=True)
print("newlist",new_num)
print(nums)"""


#Searching
"""Linear Search: Works on unsorted lists. Check each element one by one."""
#EX: nums = [10,20,30,40]     Search 30 → found at index 2
#We check each element one by one until we find the target.
# This is an example list of numbers that we will search through.
"""nums = [40, 50, 30, 10, 20]
# Prompt the user to enter a number and store it as the 'target'.
# The input() function reads text, and int() converts that text into an integer.
target = int(input("Enter element to search: "))   #30

# Initialize a 'flag' variable named 'found' to -1.
# We use -1 because it's not a valid list index. If this value never changes,
# it means we didn't find the target in our list.
found = -1
# Start a 'for' loop to iterate through the list.
# 'len(nums)' gets the length of the list (which is 5).
# 'range(len(nums))' creates a sequence of numbers from 0 to 4 (0, 1, 2, 3, 4).
# The variable 'i' will hold the current index during each iteration.
for i in range(len(nums)):
     # Inside the loop, check if the element at the current index 'i' (nums[i])
    # is equal to the 'target' value the user entered.
    if nums[i] == target:
        # If the element is found, update the 'found' variable to the current index 'i'.
            found = i
        
            # 'break' immediately exits the loop. This is an optimization because
            # once we've found the element, there's no need to check the rest of the list.
            break
# After the loop finishes, check the value of the 'found' variable.
# If 'found' is not equal to -1, it means the target was found and the
# 'found' variable was updated with a valid index inside the loop.
if found != -1:
    # If the element was found, print a message showing the index where it was located.
    print("Element found at index:", found)
# If the condition 'found != -1' is false, this 'else' block will run.
else:

    # This means the loop finished without finding the target, so 'found' is still -1.
    # Print a message indicating that the element was not in the list.
    print("Element not found")"""
        
#Binary Search: Works only on sorted lists. Divide list into halves repeatedly until element is found.
#nums = [10,20,30,40,50] Search 40 → found at index 3
# This is an example SORTED list. Binary search only works on sorted data.
nums = [10, 20, 30, 40, 50]

# Prompt the user to enter a number to search for and store it in the 'target' variable.
# The input() function reads text, and int() converts that text into an integer.
target = int(input("Enter element to search: "))  #40
# Initialize a pointer 'low' to the first index of the list (0).
low = 0
# Initialize a pointer 'high' to the last index of the list (len(nums)-1, which is 4 here).
high = len(nums) - 1
# Initialize a 'flag' variable to -1. We use -1 because it's not a valid index.
# If this value doesn't change, it means the element was not found.
found = -1
# Start the main loop. The search continues as long as our search space is valid (low <= high).
# If 'low' ever becomes greater than 'high', it means the element is not in the list.
while low <= high:
    # Calculate the middle index of the current search space.
    # We use '//' for integer division to ensure 'mid' is a whole number.
    mid = (low + high) // 2  #calculates the middle index: mid = (0 + 4) // 2 = 2.
    #It checks the element at nums[2], which is 30.
    # Check if the element at the middle index is our target.
    if nums[mid] == target:  #The condition nums[mid] == target (30 == 40) is false.
            
        # If it is, we've found it! Store the index in the 'found' variable.
        found = mid
        # Exit the loop immediately since there's no need to search further.
        break
        # If the middle element is LESS THAN the target...
    elif nums[mid] < target:   #The condition nums[mid] < target (30 < 40) is true. 
            
        #The low pointer is updated to mid + 1. So, low becomes 2 + 1 = 3.
        low = mid + 1
        #The search space is now the right half of the list: [40, 50]. low = 3 ,high = 4
        # Otherwise, the middle element must be GREATER THAN the target.
    else:
            # ...it means the target must be in the LEFT half of the current search space.
            # So, we discard the right half by moving our 'high' pointer to the left of 'mid'.
        high = mid - 1
# After the loop finishes, check if the 'found' variable was ever updated.
if found != -1:
    # If 'found' is not -1, the element was found. Print its index.
    print("Element found at index:", found)
else:
    # If 'found' is still -1, the loop completed without finding the element.
    print("Element not found")
