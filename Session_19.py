"""Fibonacci series is a sequence of numbers in which each number is obtained by adding the previous two numbers."""
#The standard Fibonacci sequence starts with: 0, 1
#Suppose I ask you to write a Python program that prints the first 10 Fibonacci numbers. How can we do it?
# Prompt the user to input the number of terms they want in the Fibonacci series
"""n = int(input("Enter the number of terms: "))  #10

# Initialize the first two numbers of the Fibonacci series
first = 0 #1, 1, 2, 3, 5, 8, 13,21
second = 1 #1, 2, 3, 5, 8, 13, 21,34

# Print the first two numbers of the Fibonacci series
print("Fibonacci Series:", first, ",", second, end=", ")
# Loop to generate and print the remaining terms of the Fibonacci series
for i in range(2, n):    #10
    # Calculate the next term in the Fibonacci series
    next_term = first + second    #0+1=1, 1+1=2 1+2=3,2+3=5, 3+5=8, 5+8=13
    #8+13=21, 13+21=34
    # Print the next term of the Fibonacci series
    print(next_term, end=", ")
    
    # Update the values of 'first' and 'second' for the next iteration
    first = second    #1``  1,2, 3,5,8,13,21
    second = next_term  #1, 2,3,5,8,13,21,34
# Print a newline character to end the output
print()""" 


#Pattern programs
"""for r in range(5):       #rows 
    for c in range(4):
        print("*", end=" ")
    print() """  
    
#Left Triangle Star Pattern
"""for i in range(1, 7):
    for j in range(1, 7):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print() """

"""n = 5
for i in range(1, n+1):
    print("* " * i)"""

#Inverted Left Triangle Pattern
"""n = 5   # Step 1: Assign the value 5 to variable 'n'. 
        # This means the pattern will have 5 rows.
# Step 2: Loop starts from 'n' down to 1, with step -1 (decreasing order).
for i in range(n, 0, -1):  
    # When n=5 → i takes values: 5, 4, 3, 2, 1
    
    # Step 3: For each row, print '* ' repeated 'i' times.
    print("* " * i)"""


#Right Triangle of Stars
"""n = 6   # Step 1: Assign 5 to variable 'n'. 
        # This means the triangle will have 5 rows.
# Step 2: Loop from 1 to n (inclusive).
for i in range(1, n+1):    
    # When n=5 → i takes values: 1, 2, 3, 4, 5
    # Step 3: "  " * (n-i) → adds spaces before stars to shift them to the right
    # Step 4: "* " * i → prints stars, count increases with each row    
    print("  " * (n-i) + "* " * i)"""


for i in range(4,0,-1):
    for j in range(1,5):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
