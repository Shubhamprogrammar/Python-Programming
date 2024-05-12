mark2 = 200
x = 0
try:
    x = mark2/0
    print("Division is ",x)
except (NameError):
    print("NameError Occured and handled")
except ZeroDivisionError as e:
    print(e)
except:
    print("Index Error")

finally:
    print("Marks: ",mark2)

try:
    total = mark1+mark2
    print("Total ",total)
except (NameError, ZeroDivisionError) as e:
    print(e)
finally:
    print("After try except, this block will execute")

# Raising the Exception
mbno = 254789563256
try:
    if len(str(mbno))>10:
        raise NameError("Number can't be greater than 10")
    print("Mobile number is correct")
except :
    print("An Exception raise")
finally:
    print("Welcome!!!")

x = 1
y = 100
assert y != 0, "Invalid operation"
print(x/y)

age = 10
assert age>18, ("You cannot enter as your age is less than 18")
print("Enter")