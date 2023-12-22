#user defined function

# Function to print the statement
def func1():
    print("You are in the function")
func1()

# Function along with docstring
def function2(a,b):
    """This is a function which will calculate average of two numbers and it is docstring"""
    average=(a+b)/2
    print(average)
function2(10,20)
print(function2.__doc__)

# Function by taking input from the user
a=float(input("Enter your Number1\n"))
b=float(input("Enter your Number2\n"))
def func2(a,b):
    add=a+b
    return(add)
v=func2(a,b) #If you want to store function in variable you have to first give return
print(v)

# Fibonacci sequence using recursion
def fib(n):
   if n <= 1:
       return n
   else:
       return (fib(n-1) + fib(n-2))
n = 10
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fib(i))

# Same fibonacci series using iteration
def fib_it(n):
    a = 0
    b = 1   
    print(a,b,end=" ")
    while(n-2):
        c=a+b
        a,b = b,c
        print(c,end=" ")
        n=n-1
n=int(input("Enter the number of terms in the sequence: "))
fib_it(n)

# Practice
# Q.1. Create a function to print the table of 5 by passing a parameter into the function
# Q.2. Write a program to create a function which takes two paramter as firstname and lastname and print the following statements. "Hello firstname lastname! You just delved into python."
# Q.3. Write a program to create function to return the sum of the arguments(arguments=5 which should be taken from the user)
# Q.4. Write a program to create function to get the factorial using iterative method
# Q.5. Same Q.4. using recursive method