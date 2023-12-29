thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets cannot have duplicate values
thisset = {"apple", "apple","banana", "cherry"}
print(thisset) # duplicate values will be ignored

print(len(thisset))
print(type(thisset))

sett = set((1,4,5,7,"shaan",8))
print(sett)
for i in sett:
    print(i)
sett.add(12)
print(sett)
sett.remove(8)
print(sett)
thisset.update(sett) # You can even add list into a set
print(thisset)

thisset.discard(100)
print(thisset)

x = sett.pop(1)
print(x)
print(sett)

thisset.clear()
print(thisset)

# Practice
# Q.1. Prepare a generalized set by taking user input
# Q.2. Write a program to find the maximum and minimum element in the set
# Q.3. Write a program to reverse the set
# Q.4. Create a list and then two setA and setB and then find happiness, setA contain all the element which you like and setB contain all the element which you dislike so if elements occur in setB then happiness-1 and if elements occur in setA then happiness+1(increment). Calculate total happiness
