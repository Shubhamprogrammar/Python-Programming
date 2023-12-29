# List Comprehension

ls=[]
for i in range(100):
	if i%3==0:
		ls.append(i)
		
print(ls)

lst=[i for i in range(100) if i%3==0]
print(lst)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Set Comprehension

dresses={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
print(dresses)
print(type(dresses))

# Dictionary comprehension

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]    
myDict = { k:v for (k,v) in zip(keys, values)}  
print (myDict)

dict={i:f"item {i}" for i in range(100) if i%10==0}
dict2={vatue:keys for keys,vatue in dict.items()}
print(dict)
print(dict2)

# Practice
# Q.1. Given a list of numbers, remove all odd numbers from the list using list comprehension
# Q.2. Find all of the numbers from 1–1000 that have a 6 in them
# Q.3. Count the number of spaces in a string (take input for string)
# Q.4. Find all of the words in string that has less than 5 digits