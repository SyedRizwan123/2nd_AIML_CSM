#Palidrome : A palindrome is a word, number, or sequence of characters that reads the same forward and backward ex:121
"""num=121     #12, 1
temp=num   #121
rev=0   #12
while num!=0: #121!=0, 12!=0, 1!=0
    rem=num%10   #1, 2, 1
    rev=rev*10+rem  #0*10+1=1, 1*10+2=12, 120+1=121
    num=num//10  #12, 1, #0
print("The rev value is", rev)
if temp==rev:    #121==121:
    print(f"{rev} is palindrome")
else:
    print(f"{rev} is not palindrome")"""
    
#Armstrong number:An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits. Specifically, 
#for a three-digit number like 153:

"""num=153     #153, 15, 1, 0
temp=num   #153
Arm=0   #153
while num!=0: #153!=0, 15!=0, 1!=0, 0!=0
    rem=num%10   #3, 5, 1
    Arm=Arm+rem*rem*rem  #0+27, 27+125=152, 152+1=153
    num=num//10  #15
print("The Arm value is", Arm)
if temp==Arm:    #153==153:
    print(f"{Arm} number is Armstrong ")
else:
    print(f"{Arm} number is not Armstrong")"""
    
#153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725
"""num = int(input("Enter any value: "))
temp = num
Arm = 0
count = 0

# Count number of digits
n = num
while n != 0:
    count += 1  # Increment count for each digit found in the number 
    n //= 10

# Compute sum of digits raised to count (power)
n = num   # Reset n to original number
while n != 0:
    rem = n % 10
    Arm= Arm + rem ** count   # use count as exponent
    n //= 10

print(f"The sum of digits^{count} = {Arm}")

if temp == Arm:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number")"""


#Find the factorial number of given value
# To find factorial value
"""n = int(input("Enter any value: "))
fact = 1
i = 1
while i <= n:        # 1<=5  2<=5 3<=5  4<=5 5<=5  6<=5
    fact = fact * i          #1*1=1 fact=1 fact=1*2=2 fact=2*3=6  fact=6*4=24   fact=24*5=120
    i = i + 1
print(f"Factorial value is {fact}")"""

#To find given number is Strong number or not
#Strong number:A Strong number is a number where the sum of the factorials of its digits equals the number itself.
# //ex:145: find factorial with each digit 1!+4!+5!=145 we have to get same digit


    