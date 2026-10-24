#What are Functions ?
"""1. A function is a block of code that performs a specific task
   2. it helps in reusing code and makes your program more organized
   3. we can call a function multiple times
   4. functions can take input(arguments) and can return a value
   5. A function in Python is a block of reusable code that performs a specific task.
   6. Instead of writing the same code again and again, you can put it inside a function and call it whenever needed.
"""

# Key Points:
"""
1. Reusable code block
2. take inputs (arguments)
3. Return value (optional)
4. Reduce code duplication
5. Improve code readability
6. has its own scope(local variable)
"""

#creating function
"""def function_name():
    #function body
    return"""

#Calling a function
"""
1. After defining a function we call it using its name 
2. Arguments are passed inside parenthese

result=function_name(10,20)
print(result)"""

"""def my_name():
    print("Hello Python")

my_name()
my_name()"""

"""def add():
    x=10
    y=20
    print(x+y)
add()"""

#Function with Arguments
"""
1. Arguments are the value we pass to a function.
2. They can be positional or Keyword arguments.
"""

"""def add(a,b):
    print(a+b)
#add(5,6)   #positional Arguments
add(b=6,a=7)"""  #Keyword Arguments

"""def my_fun2(name):
    print("Hello",name)

my_fun2("Ravi")
my_fun2("Ram")
my_fun2("Alice")
my_fun2([1,2,3])
my_fun2((1,2,3))"""

#in order
"""def print_coordinate(y=8, x=5):
    print('Coordinates  (',x,',',y,')')
    
print_coordinate(10,7)"""

#Function with Return value
"""
1. The return statement send a value back to the caller
2. if no return is used the function return None by default
"""
"""def square(n):
    return n*n
print(square(5))"""

"""def isEven(x):
    print("checking whether number is even or not")
    if x%2==0:     #4%2==0
        return True
    else:
        return False
print(isEven(4))"""

"""def addition(a,b):
    return a+b   #2+3=5

result = addition(2,3)
print(result)"""

#Returning multiple values:unlike several other languages python allows you to return multiple values
"""def squareandcube(x):
    return x*x, x*x*x
print(squareandcube(3))

x2,x3=squareandcube(3)         #this is packing and unpacking concepts
print("Suare", x2)
print("Cube", x3)"""

#we can also achieve the same thing by returning a dict
"""def squarandcube(x):
    return{'x2':x*x, 'x3':x*x*x}
ret = squarandcube(3)
print('3 square is:',ret['x2'])
print('3 cube is:',ret['x3'])"""


#functions are objects
"""def squareandcube(x):
    return x*x,x*x*x
my_fun = squareandcube       #Here my fun is Object and squareand cube is function, if we give squareandcube(3) my_fun will change as variable
print(my_fun(3))"""

# Create an empty dictionary to store all users
users = {}   #Key:Value {Syed123@gmail.com:Syed@123}

# 1. SIGN UP MODULE
def signup():
    print("\n--- SIGN UP ---")
    username = input("Enter new username: ")    #SyedRizwan123@gmail.com
    # Check if username already exists
    if username in users:
        print(" Username already exists! Try another one.")
    else:
        password = input("Enter new password: ")   #Syed@123
        users[username]=password
        print("Account created successfully!")

#2. LOGIN MODULE
def login():
    print("\n--- LOGIN ---")
    username = input("Enter username: ")     #Syed123@gmail.com
    password = input("Enter password: ")     #Syed@1234
    name=input("Enter your name")
    # Check if username exists and password matches
    if username in users and users[username] == password:
        print(" Login Successful! Welcome, ", name)
    else:
        print(" Invalid username or password!")
#3. MAIN MENU
def main():
    while True: # This creates an infinite loop that will keep showing the menu until the user chooses to exit.
        print("\n===== MENU =====")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
    
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            signup()
            print(users)
        elif choice == '2':
            login()
        elif choice == '3':
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice, please try again.")
# Run the program
main()