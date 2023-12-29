class Employee:
	no_of_leaves=24
	def __init__(self, aname, asalary, arole):
		self.name=aname
		self.salary=asalary
		self.role=arole

	
	def printdetails(self):
		return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
	
	@classmethod	
	def change_leaves(cls, newleaves):
		cls.no_of_leaves = newleaves
	
	@staticmethod
	def printgood(str):
		print(str," is good boy") 
		
Nisha = Employee("Nisha",45000,"Teacher")
Shreya = Employee("shreya",45000,"Teacher")
Sakshi = Employee("Sakshi", 30000, "Teacher")
Employee.change_leaves(48)
print(Shreya.no_of_leaves)
Nisha.change_leaves(30)
print(Nisha.no_of_leaves)
print(Shreya.no_of_leaves)
print(Nisha.printdetails())
print(Sakshi.printdetails())
Sakshi.printgood("Shubham")

# Practice
# Q.1. Create class named "Shape" and create all the types of three methods and then access it.
# Q.2. Create class and then create object according to user requirement