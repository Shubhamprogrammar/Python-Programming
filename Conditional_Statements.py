a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 10
if a>0:
  print("It is positive integer")
elif a<0:
  print("It is negative integer")
else:
  print("Zero")

print("A") if a > b else print("B")

angle1 = int(input("Enter Angle1:  "))
angle2 = int(input("Enter Angle2:  "))
angle3 = int(input("Enter Angle3:  "))
if angle1+angle2+angle3==180 and angle1!=0 and angle2!=0 and angle3!=0:
    if angle1==90 or angle2==90 or angle3==90:
        print("It is right angle triangle")
    elif angle1>90 or angle2>90 or angle3>90:
        print("It is obtuse angle triangle")
    else:
        print("It is acute angle triangle")
else:
         print("It is not a triangle") 


# Practice
# Q.1. Create a calculator by taking input and operation(+,-,*,/) from user 
# Q.2. Write a program to determine the number is odd or even
# Q.3. Write a program to determine which number is maximum by taking three input from user
# Q.4. Write a program to take input as string if the length of the string is greater 20 then print "hello" otherwise "world"