#Find the given number is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     
"""n=int(input("Enter a number"))   #3
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("its a prime number")
else:
    print("Not a prime number")"""

#Find the next prime number
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     

# 1. Takes an input string from the user, casts it into an integer, and stores it in 'prime'.
#    Purpose: Holds the number to be evaluated.
"""prime = int(input("Enter the number: "))

# 2. Initializes a counter to track how many divisors divide 'prime' evenly.
#    Purpose: Serves as the factor counter for the initial input.
count = 0

# 3. Loops through all integers starting from 1 up to 'prime' inclusive.
#    Purpose: Evaluates every potential factor of the given number.
for i in range(1, prime + 1):

    # 4. Modulo operator (%) calculates the remainder when 'prime' is divided by 'i'.
    #    Purpose: If remainder is 0, 'i' is an exact divisor/factor of 'prime'.
    if prime % i == 0:

        # 5. Increments 'count' by 1 whenever a divisor is found.
        #    Purpose: Tallies total number of factors.
        count += 1

# 6. Checks if the total number of positive divisors is exactly 2 (meaning only 1 and itself).
#    Purpose: Enforces the mathematical definition of a prime number.
if count == 2:

    # 7. Displays a message confirming the entered number is prime.
    #    Purpose: Outputs positive result to user and ends the program.
    print(prime, "is a prime number")

# 8. Executes if 'count != 2' (meaning the number is composite, 1, or <= 0).
# Purpose: Handles non-prime inputs and triggers the search for the next prime.
else:

    # 9. Increments 'prime' by 1 to skip testing the input number again.
    # Purpose: Sets up the first candidate number to inspect.
    prime += 1

    # 10. Starts an infinite loop that continues until a prime number is encountered.
    # Purpose: Drives the search upward indefinitely until a valid prime is found.
    while True:

        # 11. Resets the divisor tally to 0 for the candidate in this iteration.
        #     Purpose: Prevents counts from previous candidate numbers from carrying over.
        count = 0

        # 12. Loops through every number from 1 up to the current candidate 'prime' inclusive.
        #     Purpose: Checks factors for the current candidate.
        for i in range(1, prime + 1):

            # 13. Checks whether 'i' divides the candidate number evenly.
            #     Purpose: Identifies divisors of the candidate.
            if prime % i == 0:

                # 14. Adds 1 to the factor tally.
                #     Purpose: Accumulates factor count for this candidate.
                count += 1

        # 15. Tests whether the current candidate has exactly 2 divisors.
        #     Purpose: Determines if the candidate meets the prime condition.
        if count == 2:

            # 16. Prints the first prime number found that is greater than the input.
            #     Purpose: Informs the user of the next prime number.
            print("The next prime number is:", prime)

            # 17. Terminates the 'while True' loop immediately.
            #     Purpose: Halts the program so it stops searching after finding the first match.
            break

        # 18. Advances to the next integer if the current candidate was not prime.
        #     Purpose: Moves the search to the next candidate integer.
        prime += 1"""

#print even nubers and odd numbers count
"""even_count=0
odd_count=0
for i in range(1, 11):  #1,2,3,4,5,6,,7,8,9,10
    if i % 2 == 0:     #1%2==1,  2%2==0
        even_count+=1
    else:
        odd_count+=1
print(f"Even number count is = {even_count} and odd number count is = {odd_count}")"""

#print armstrong numbers
# 1. Iterate through numbers starting from 1 up to 1999 (stops before 2000).
#    If used: 'i' takes each number in that range one by one.
for i in range(1, 2000):

    # 2. Store the current number 'i' in variable 'num'.
    #    If used: Gives us a working copy of 'i' to dismantle digit-by-digit later.
    num = i

    # 3. Create another copy of the number in 'temp'.
    #    If used: Preserves the original value for final comparison, since 'num' becomes 0.
    temp = num

    # 4. Initialize the accumulator for the Armstrong sum to 0.
    #    If used: Holds the running total of (digit ** count) for each digit.
    arm = 0

    # 5. Create a third copy of the number in 'n'.
    #    If used: Gives a disposable variable dedicated solely to counting digits.
    n = num

    # 6. Initialize the digit counter to 0.
    #    If used: Will hold the total number of digits (the power 'n' in the definition).
    count = 0

    # 7. Loop until 'n' becomes 0 by peeling off one digit per cycle.
    #    If used: Determines how many digits the number has.
    while n != 0:

        # 8. Integer division by 10 discards the last digit (e.g., 153 // 10 -> 15).
        #    If used: Reduces 'n' toward 0 without floating-point errors.
        n = n // 10

        # 9. Increment the digit count by 1 for each discarded digit.
        #    If used: After this loop terminates, 'count' contains the exact number of digits.
        count += 1

    # 10. Loop until 'num' becomes 0 to extract and process each digit.
    #     If used: Calculates the sum of each digit raised to 'count'.
    while num != 0:

        # 11. Modulo 10 extracts the last digit of 'num' (e.g., 153 % 10 -> 3).
        #     If used: Isolates the current least-significant digit into 'rem'.
        rem = num % 10

        # 12. Raise the digit to the power of 'count' and add to 'arm' (e.g., 3 ** 3 = 27).
        #     If used: Builds the cumulative Armstrong sum.
        arm = arm + rem**count

        # 13. Drop the last digit of 'num' using integer division (e.g., 153 // 10 -> 15).
        #     If used: Moves to the next digit to the left until all digits are processed.
        num = num // 10

    # 14. Check if the computed sum ('arm') matches the original number ('temp').
    #     If used: Evaluates the mathematical definition of an Armstrong number.
    if temp == arm:

        # 15. Print the number followed by "is Armstrong".
        #     If used: Outputs the result to the console when a match is found.
        print(temp, "is Armstrong")
        
# perfect number: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# print the next perfect number
