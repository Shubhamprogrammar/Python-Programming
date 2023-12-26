d1 = {}
print(type(d1))
d2 = {"Shubham":"Burger","Harry":"Rasgulla","Aman":"Chapati", "Jitendra":{"B":"Maggie","L":"Chinese","D":"Biryani"}}
d2["Ankit"] = "Junk Food"
d2[360] = "Kabab"
del d2[360]
d2.update({"Leena":"Makhana"})
print(d2)
print(d2["Jitendra"])
d2.pop("Aman")
print(d2)
print(d2.get("Harry"))
print(d2.keys())
print(d2.items())

print("The Keys")
for i in d2.keys():
    print(i)

print("The Values")
for i in d2.values():
    print(i,end=" ")

list1 = [["Shubham",3],["Shaan",2],["Shaanma",4],["Shubbu",650]]
print(list1)
dict1 = dict(list1)
print(dict1)
for item,chocolate in list1:
    print(item, "and chocolate is ", chocolate)

# Practice
# Q.1. Write a program to sum all the values of dictionary
# Q.2. Write a program to remove a key from a dictionary if it is present by taking a user input
# Q.3. Create a generalised program for dictionary
# Q.4. Create dictinary and take user input as key and then provide the value to the user