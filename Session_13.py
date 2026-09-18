#Bodmas
"""BODMAS Rule

The BODMAS rule is a sequence that tells us the correct order of operations when solving mathematical expressions.

BODMAS stands for:

B → Brackets (solve inside brackets first)

O → Orders (powers, roots, exponents, square roots, etc.)

D → Division (÷)

M → Multiplication (×)

A → Addition (+)

S → Subtraction (−)"""

"""result = 10+(3*-8)/4      #-24/4=-6+10=4
print(result)"""

"""result2 = (8+4)*3/2  #12* 1.5
print(result2)"""

"""result3=16/4+2**3-6  #8 +4=12-6=6
print(result3)"""

#for loop: The for loop is used to iterate over a sequence (list,tuple,string,range,etc) or other iterable objects.
# it runs a specific number of times.
#Syntax: for variable in sequence:
                #code to be executed        
"""for number in range(0,11):
    print(number)"""

# for loop is used to repeat a block of code
#range(0, 10, 3) generates numbers:
# Start = 0
# Stop = 10 (10 is not included)
# Step = 3 (increase by 3 each time)

"""for number in range(0, 10, 3):
    # print() displays the current value of number
    print(number)"""
    
# Program to print numbers in reverse order
# range(5, -1, -1):
# Start = 5
# Stop = -1 (excluded)
# Step = -1 (decrease by 1)

"""for i in range(5,0,-1):
    print(i)"""

