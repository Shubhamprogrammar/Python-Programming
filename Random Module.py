import random

random_number = random.randint(1,100) #Returns a random number between the given range
print(random_number)
number = random.random()*100
print(number)
list = ["A","B","C","D","E","F","G","H","I","J","K","L"]
choice=random.choice(list) # Returns a random element from the sequence
print(choice)

x = random.getstate() # Returns the current internal state of the random number generator
print(x)

print(random.random())
state=random.getstate()
print(random.random())
random.setstate(state) # Restores the internal state of the random number generator
print(random.random())

print(random.randrange(2,1000)) #Returns a random number between the given range

mylist = ["apple", "mango", "cherry"] #Returns a list with a random selection from the sequence
print(random.choices(mylist,weights=[3,6,5] ,k=8))

random.shuffle(list) #Returns the sequence in a random order
print(list)

print(" ".join(random.sample(list,k=8)))
print("Shubham")