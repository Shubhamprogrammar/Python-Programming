class Employee:
	no_of_leaves=24
	_protec=32
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
		return 
		
class player:
		no_of_games = 4
		def __init__(self, name, game):
			self.name= name
			self.game= game
		
		def printdetails(self):
			return f"The name is {self.name} and the game played by him is {self.game}"
			
class coolprogrammar(Employee, player):
		language ="C++"
		def printlanguage(self):
			return self.language		
			
Nisha = Employee("Nisha",45000,"Teacher")
sheeja = player("Sheeja", ["Cricket","Football","Kabaddi"])
print(sheeja.printdetails())
Nisha.change_leaves(30)
shaima = coolprogrammar("Shaima",80000,"CoolProgrammar")
print(shaima.printdetails())

shaima.printgood("sharma")
print(shaima.printlanguage())
print(shaima.no_of_leaves)
print(shaima._protec)
print(Employee._protec)