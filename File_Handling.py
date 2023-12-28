#File Io Basic

"""
"r" - Open file for reading - default
"w" - Open file for writing
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - Text mode - default
"b" - Binary mode
"+" - Read and Write
"""

"""
f = ("Harry.txt", "rt")
content = f.read()
print(content)

content = f.read(3)
print(content)
f.close()

print(f.readline())
print(f.readline())

print(f.readlines()) #To print everything on one line
"""

f = open("Shubham.txt","w")#To write
f.write("Shubham is good person\n")
f.close()

f = open("Shubham.txt","a")#To append
i = f.write("Shubham is fine")
print(i)
f.close()

#Handle read and write both
f = ("Shubham.txt", "r+")
print(f.read())
f.write("Thank You")

f = open("Harry.txt")
print(f.tell())
print(f.readline())
f.seek(10)#You can bring pointer/handler to that point
print(f.tell())#It tells where the pointer is at this point after reading the character or if you have used seek() it will read from that point
print(f.readline())
print(f.tell())
f.close()

with open("Shubham.txt","rt") as f:#This is the same as open and close & it is another alternative
    a = f.read(4)
    print(a)

# Practice
# Q.1. Write a program to create a file into another foler by specifying path and write "I love my country" int the file.
# Q.2. Write a program to read the file which is created in above question 
# Q.3. Write a program to append the data into the file and then print the content by changing the pointer again and again