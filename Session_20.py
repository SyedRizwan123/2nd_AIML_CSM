# Simple Triangle Pattern
"""rows = 6  # Sets the total number of rows for the triangle pattern.
for i in range(1, rows):  # Loop from 1 to rows-1 (i = 1 to 5)
    spaces = rows - i - 1         # Calculate number of spaces before the stars for current row
    stars = 2 * i - 1             # Calculate number of stars for current row (odd numbers: 1, 3, 5, ...)
    print(" " * spaces + "*" * stars)"""  # Print spaces followed by stars on the same line
        # " " * spaces: adds leading spaces to center the triangle
        # "*" * stars: prints the required number of stars for the row"""
    
#Inverted Pyramid
"""n = 5   # Assign the number of rows for the triangle. Here, n = 5.
# Loop starts from n down to 1 with step -1.
# So, i will take values: 5, 4, 3, 2, 1
for i in range(n, 0, -1):
    # The + operator joins spaces and stars in one string for each row.
    print(" " * (n-i) + "* " * i)"""


#Diamond Pattern
"""n = 5  # Number of rows for the upper half of the diamond
# Upper half of the diamond (including the middle row)
for i in range(1, n+1):  # Loop from 1 to n (1 to 5)
    print(" "*(n-i) + "* " * i)  
        # " "*(n-i): Prints spaces to center the stars
        # "* " * i: Prints i stars with a space after each
    # Lower half of the diamond (excluding the middle row)
for i in range(n-1, 0, -1):  # Loop from n-1 down to 1 (4 to 1)
    print(" "*(n-i) + "* " * i)"""
    # " "*(n-i): Prints spaces to center the stars
    # "* " * i: Prints i stars with

#hollow square pattern pattern
# Outer loop: Controls the rows, running from i = 1 to 5 (range stops before 6)
for i in range(1, 6):
    
    # Inner loop: Controls the columns within each row, running from j = 1 to 5
    for j in range(1, 6):
        #We want stars only on the boundary of the rectangle."
                # Check if the current position lies on any of the four borders:
                # - i == 1: Top row
                # - i == 5: Bottom row
                # - j == 1: Leftmost column
                # - j == 5: Rightmost column
                if i == 1 or j == 1 or i == 5 or j == 5:
                    # Print an asterisk followed by a space, keeping the cursor on the same line
                    print("*", end=" ")
                else:
                    # For interior cells, print two spaces to keep alignment without a border
                    print(" ", end=" ")
                    
            # After finishing all columns for row 'i', print an empty line to move to the next row
    print()

            