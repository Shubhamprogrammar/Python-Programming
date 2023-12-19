# For loop

# Print the number if it is divisible by 3 and 5
lower = 1
upper = 50
for i in range(lower, upper+1):
   if((i%3==0) & (i%5==0)):
      print(i,end=" ")

# Print the table of 4
n=4
for i in range(1,11):
    print(n,"x",i,"=",n*i)

# Iteration on list
list = ["Shubham","Radhe",42,"Krsna",95,10,38]
for item in list:
    if  str(item).isnumeric() and item>30:
        print(item)

for i in list:
    print(i)

# Pattern Printing
for i in range(0, 5):
    for j in range(0, i+1):
        print("*",end="")
    print("\r")

# While loop

# Print the number from 1 to 10   
a=1
while a<11:
    print(a)
    a =a + 1

# Print the number if it is divisble by 3 and 5
x = 1
while x<=30:
    if x%3==0 and x%5==0:
        print(x)
    x= x+1

# Print the odd numbers
a = 1
while a < 100:
    print(a)    
    a = a + 2

# Practice
# Q.1. Write a program to take input from user and provide square of the number by iterations till that number
# Q.2. Write a program to print the list of integers from 1 to n as a string, without spaces.(n is input given by the user)
# Q.3. Write a program to create a table of number 12 using while loop
# Q.4. Write a program to create a reverse loop using for and while loop.
# Q.5. Write a program to print the following pattern using for loop
    # 1
    # 11
    # 111
    # 1111
