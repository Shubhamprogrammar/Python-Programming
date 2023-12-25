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