#To find given number is Strong number or not
#Strong number:A Strong number is a number where the sum of the factorials of its digits equals the number itself.
# //ex:145: find factorial with each digit 1!+4!+5!=145 we have to get same digit
"""num = int(input("Enter a number: "))
sum = 0    # sum is used to store the sum of the factorials of the digits.
temp = num #temp stores the original number for comparison later.

while num:
    i = 1
    fact = 1
    r = num % 10 # Extract the last digit         #r=145%10=5 r=4 fact=24 
    while i <= r:    # Calculate factorial of the digit       #1<=5
        fact = fact * i        #fact=1*1=1 fact=1*2=2, fact=2*3=6 fact=6*4=24, fact=24*5=120
        i += 1

    sum = sum + fact  # Add factorial to sum     #sum=0+120=120 //120+24=144  sum=144  sum=144+1=145
    num = num // 10   # Remove the last digit    #num=145/10=14 //14/10=1 num=1       num=144+1=145

if sum == temp:
    print(sum,"is a strong number")
else:
    print(sum,"is not a strong number")"""
    
# perfect number: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# 6=1+2+3 =6 6 devisors is 1+2+3
"""num = int(input("Enter a number: "))  #6
sum = 0
for i in range(1, num):  # num=6   1<6
    if num % i == 0:  # 6%1==0   6%1==0   6%2==0  6%3==0  6%4=
        sum += i  # sum=0+1=1     sum=1+2=3   sum=3+3=6                      3+4=7
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")"""

#print even nubers and odd numbers
"""for i in range(1, 11):  #1,2,3,4,5,6,,7,8,9,10
    if i % 2 == 0:     #1%2==1,  2%2==0
        print(i, "= even")    #2 =even
    else:
        print(i, "= odd")"""   #1 =odd"""

#print only even number  
"""for i in range(0, 11, 2):    #0+2=2, 2+2=4,
    if i % 2 == 0:
        print(i, "= even")
    else:
        print(i, "= odd")"""

#print 2nd table
"""n = int(input("Enter a number: "))     #2 * 1= 2*1=2,  2*2=4 2*3=6 2*4=8
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")"""
    
#Sum of natural numbers
"""n = int(input("Enter a number: "))   #5
sum = 0
for i in range(1, n+1):
    sum = sum + i       #0+1=1,   1+2=3, 3+3=6 6+4=10 10+5=15
print(sum)"""

#Sum of natural numbers using while loop
"""n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 1
print(sum)"""

#Find the given number is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     
