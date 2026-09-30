# This program prints a right-angled pattern of numbers.
"""for i in range(1, 6):     # This is the outer loop. It will run 5 times, with 'i' taking values from 1 to 5.
                        # This loop controls the number of rows to be printed.
    for j in range(1, i + 1):  # This is the inner loop. It depends on the value of 'i' from the outer loop.
                                # For each row 'i', it will run 'i' times, with 'j' taking values from 1 up to 'i'.
                                # This loop is responsible for printing the numbers in each row.
        print(j, end=" ")    # This prints the current value of 'j' followed by a space instead of a new line.
                                # This keeps the numbers for a single row on the same line.
    
    print()"""                 # This prints a new line character after the inner loop completes.
                                # It moves the cursor to the next line, so the numbers for the next row
                                # will be printed on a new line."""


#Number Triangle Pattern Program" (also called Floyd’s Triangle in mathematics).
"""n = 5          # Step 1: Set the number of rows for the pattern (triangle will have 5 rows).
num = 1        # Step 2: Initialize 'num' with 1. 
            # This variable will be printed and incremented each time.
# Step 3: Outer loop → controls the number of rows (from 1 to n).
for i in range(1, n+1):  
    # When n=5 → i takes values 1, 2, 3, 4, 5
    # Step 4: Inner loop → runs 'i' times in each row
    # For row 1 → loop runs 1 time
    # For row 2 → loop runs 2 times
    # For row 3 → loop runs 3 times, etc.
    for j in range(i):    #0,  0,1, 0,1,2, 0,1,2,3, 0,1,2,3,4
         # Step 5: Print the current value of 'num'
        # 'end=" "' means: stay on the same line and put a space after printing
        print(num, end=" ")   
        
        # Step 6: Increase 'num' by 1 for the next print
        num += 1
    print()"""
    
# This program prints a right-angled pattern of letters.
"""for i in range(1, 6):       # This is the outer loop. It will iterate 5 times, with 'i' taking values from 1 to 5.
                            # This loop controls the number of rows to be printed.
    ch = 'A'                # Inside the outer loop, we initialize a variable 'ch' to the character 'A'
                                # at the beginning of each new row. This ensures that every row starts with 'A'.
    for j in range(1, i + 1):  # This is the inner loop. It depends on the current value of 'i'.
                                # For each row 'i', it will run 'i' times, with 'j' from 1 up to 'i'.
                                # This loop is responsible for printing the characters in each row.
        print(ch, end=' ')  # This prints the current character 'ch' followed by a space.
                                    # The 'end=' argument prevents a new line, keeping the characters on the same line.
        ch = chr(ord(ch) + 1)  # This is the key line for character manipulation.
                                    # 1. 'ord(ch)' gets the ASCII (or Unicode) value of the current character 'ch'.
                                    # 2. We add 1 to this value to get the next character's ASCII value.
                                    # 3. 'chr()' converts this new ASCII value back into a character.
                                    # This effectively moves to the next letter of the alphabet (A -> B, B -> C, etc.).
        
    print()                 # After the inner loop finishes (i.e., a row is complete), this prints a new line.
                                    # This moves the cursor to the next line for the next row of the pattern."""
        
        
# Alphabet Triangle Pattern Program
"""ch = ord('A')  # Initialize 'ch' with the ASCII value of 'A'
for i in range(1, 6):         # Outer loop for rows (1 to 5)
    for j in range(1, i+1):   # Inner loop for columns in each row
        print(chr(ch), end=' ')  # Print the character
        ch += 1                  # Move to next character (ASCII value)
    print() """                    # New line after each row


"""print("'Hello python'")
print("\"Syed\"")
print("sayyad"*2)"""
#here i given multiple print statements then i want to print in signle line we have to use "end='..'"
"""print("we'll first learn how to print.",end=" ")# end=' ' is used to specify what should be printed at the end of the output. By default, it is a newline character (\n), which means that each print statement will be printed on a new line. However, by setting end=' ', we are telling Python to print a space instead of a newline at the end of the output, allowing us to print multiple statements on the same line.
print("Then we'll learn how to comment code.")"""

#string formating:In Python, string formatting is the process of creating a formatted string by embedding variables or values within a text string. This allows you to create dynamic strings that incorporate variable values, making your code more readable and flexible.
#using '%' operator: This operator uses the % operator to insert values into a string.
name = "Syed"
age = 25
formatted_string = "My name is %s and I am %d years old." % (name, age)    #My name is Syed and i am 25 years old
print(formatted_string)
