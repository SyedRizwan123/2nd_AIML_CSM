#while loop: The while loop is used to execute a block of code as long as the given condition is True
#it repeats the block code until the condition becomes false 
"""number = 1   #2, 3, #4
while number <= 3:   #1<=3, 2<=3, 3<=3, 4<=3
    print(number)   #1, 2, 3
    number+=1"""   #number=number+1==>1+1=2, 2+1=3, 3+1=4

"""x=10
while x>0:  #10>0, 9>0
   print(x)   #10,9
   x-=1"""    #x=9, 8

#nested loop
"""for i in range(1, 4):        # Outer loop → rows
    for j in range(1, 4):       # Inner loop → columns
        print(i * j, end="  ")
    print()"""


#Loop control statement: python provides some special statements to control the flow of loops.
#Break statement: Terminates the loop completely
"""for i in range(5):
    if i==3:  #i=0==3, i=1==3, i=2==3, 3==3
        break
    print(i)"""   #0,1,2

#continue: Skips the current iteration and continue with the next value
"""for i in range(5):
    if i==3:  #i=0==3, i=1==3, i=2==3, 3==3
        continue
    print(i)"""  #0,1,2,4

#count of number digits
"""num = int(input("Enter a number: "))  #1234
count = 0  #4
while num != 0:         #1234 !=0, 123!=0,12!=0  0!=0
    num = num // 10     #1234//10=123, 123//10=12,12//10=1
    count+=1   #0+1=1+1=2+1=3+1
print(count)"""

#Find the ASCII value of a given character
"""ch = input("Enter a character: ")   #a #a-97 to z-122,  A-65 to Z-90
ascii_value = ord(ch)    #ord() function is used to find the ASCII value of the character.
print(f"\nThe ASCII value of {ch} is {ascii_value}")"""

#Find the given charecter is Alphabet or not
