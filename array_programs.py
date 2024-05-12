# Python Array Programs

from collections import deque,defaultdict

l1=[1,3,5,7,9,2,4,6,8,10,2,10,5,8,1,3]

# 1) Python Program to copy all elements of one array into another array

l2=l1
print(l2)

# 2) Python Program to print the duplicate elements of an array

def printDuplicates(arr):
    map=defaultdict()
    for x in arr:
        if x not in map:
            map[x]=1 
        else:
            map[x]=map[x]+1 
    print("Duplicates Elements are :- ",end=" ")
    for index,key in enumerate(map):
        if map[key]>1:
            print(key,end=" ")

printDuplicates(l1)

# 3) Python Program to print the elements of an array

print()
print(l1)

# 4) Python Program to print the elements of an array in reverse order

def printInReverseOrder(arr):
    print("Elements in reverse order :- ",end=' ')
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end=" ")
        
printInReverseOrder(l1)   
print()

# 5) Python Program to print the elements of an array present on even position

def printElementsAtEvenPosition(arr):
    print("Elements at even position :- ",end=' ')
    for i in range(0,len(arr)):
        if i%2==0:
            print(arr[i],end=" ")

printElementsAtEvenPosition(l1)

# 6) Python Program to print the elements of an array present on odd position

def printElementsAtOddPosition(arr):
    print("Elements at odd position :- ",end=' ')
    for i in range(0,len(arr)):
        if i%2!=0:
            print(arr[i],end=" ")
print()
printElementsAtOddPosition(l1)

# 7) Python Program to print the largest element in an array

l1.sort()

print("Largest element in the array :- ",l1[-1])

# 8) Python Program to print the smallest element in an array

print("Smallest element in the array :- ",l1[0])

# 9) Python Program to print the number of elements present in an array

print("Length of array :- ",len(l1))

# 10) Python Program to print the sum of all the items of the array

def printSumOfAllElements(arr):
    sum=0
    for x in arr:
        sum+=x 
    print("Sum of all elements in the array is ;- ",sum)

printSumOfAllElements(l1)

# 11) Python Program to sort the elements of an array in ascending order

print(l1)
l1.sort()
print(l1)

# 12) Python Program to sort the elements of an array in descending order

print(l1)
l1.sort(reverse=True)
print(l1)

# 13) Python Program to Find 3rd Largest Number in an array

l1.sort()
print(l1)

print("3rd Largest element in the array :- ",l1[-3])

# 14) Python Program to Find 2nd Largest Number in an array

print("2nd Largest element in the array :- ",l1[-2])

# 15) Python Program to Find Largest Number in an array

print("1st Largest element in the array :- ",l1[-1])

# 16) Python to Program Find 2nd Smallest Number in an array

print("2nd Smallest element in the array :- ",l1[1])

# 17) Python Program to Find Smallest Number in an array

print("1st Smallest element in the array :- ",l1[0])

# 18) Python Program to Remove Duplicate Element in an array

def removeDuplicates(arr):
    result=[]
    map=defaultdict()
    for x in arr:
        if x not in map:
            map[x]=1 
        else:
            map[x]=map[x]+1 
    for index,key in enumerate(map):
        if map[key]>1:
            continue
        else:
            result.append(key)
    return result

# print(l1)
# l1=removeDuplicates(l1)
# print(l1)

# 19) Python Program to Print Odd and Even Numbers from an array

def printOddEvenNumbersInAarray(arr):
    print("Even Elements are :- ",end=" ")
    for x in arr:
        if x%2==0:
            print(x,end=' ')
    print()
    print("Odd Elements are :- ",end=" ")
    for x in arr:
        if x%2!=0:
            print(x,end=' ')
            
printOddEvenNumbersInAarray(l1)

# 20) How to Sort an Array in Python 

print("Before Sorting :- ")
print(l1)
l1.sort()
print('After Sorting :-')
print(l1)
            
# 21) General Program for operations        
n = int(input())
l = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "insert":
        l.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == "remove":
        l.remove(int(cmd[1]))
    elif cmd[0] == "print":
        print(l)
    elif cmd[0] == "append":
        l.append(int(cmd[1]))
    elif cmd[0] == "sort":
        l.sort()
    elif cmd[0] == "pop":
        l.pop()
    else:
        l.reverse()
                