# List and it's operations

Numbers = [27,14,56,9,100,47,52,18,37]
Numbers.append(34)
Numbers.extend([10,20])
Numbers.insert(2,736)
Numbers.remove(9)
Numbers.pop()
print(Numbers.index(100))
#Numbers.sort()
#Numbers.reverse()
Numbers[1] = 97
print(Numbers)
print(Numbers[1:4])
print(Numbers[::2])
print(len(Numbers))
print(max(Numbers))
print(min(Numbers))
for i in Numbers:
    print(i)

# Tuple and it's operations

# Mutable-Can Change
# Immutable-Cannot Change
# Tuple is immutable(means once it is declared it cannot be change)
tp = (2,65,98) #Parenthesis
print(tp)
print(len(tp))

# To declare tuple with only one item add "," at last, otherwise python will not recognise it as a tuple
tp1 = (1,)
print(type(tp1))
tup = (4,3,9,8,"Shaan","Radhe")
for i in tup:
    if str(i).isnumeric():
        print(i)

# Practice
# Q.1. Write a program to create a cumulative frequency and add it into the list
# Q.2. Write a generalised program to get the input from the user and add it into the list
# Q.3. Write a program to reverse the list
# Q.4. Write a program to print the list in reverse without reversing the list
