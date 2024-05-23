# Method Overriding
class Car:
  def move(self):
    print("Drive!")
    

class Boat(Car):
  def move(self):
    print("Sail!")

car1 = Car()       
boat1 = Boat()  

car1.move()
boat1.move()

class Parent(): 	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 	
	def show(self): 		
		# Calling the parent's class method 
		super().show() 
		print("Inside Child") 
		
# Driver's code 
obj = Child() 
obj.show() 


# Method Overloading
def product(a, b):
    p = a * b
    print(p)

def product(a, b, c):
    p = a * b*c
    print(p)
 
# product(4, 5)
product(4, 5, 5)

class Employee:
	def __init__(self, aname, asalary, arole,no):
		self.name=aname
		self.salary=asalary
		self.role=arole
		self.no=no
	
	def printdetails(self):
		return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
		
	def __add__(self,others):
		return self.salary + others.salary
		
	def __repr__(self):
#		return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
		return f"Employee ( '{self.name}', {self.salary}, '{self.role}' )"
		
	def __str__(self):
		return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
		
	def __mul__(self,other):
		return other.salary * self.salary
		
	def __sub__(self,other):
		return self.salary - other.salary,self.no- other.no
Shubham = Employee("Shubham",56789,"Coder",50)
shaan = Employee("Shaan",70000,"Programmar",30)
print(Shubham + shaan)
print(Shubham * shaan)
print(shaan - Shubham)
print(Shubham)

# Practice
# Q.1. Write a program for the real life example of polymorphism