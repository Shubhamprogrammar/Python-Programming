class Employee:
	no_of_leaves=24
	def __init__(self, aname, asalary, arole):
		self.name=aname
		self.salary=asalary
		self.role=arole
		
	def printdetails(self):
		return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
	
class hod(Employee):
		no_of_holiday = 58
		def __init__(self,aname,asalary, arole, language):
			super().__init__(aname,asalary,arole)
			self.language=language
		@classmethod	
		def change_holiday(cls, leaves):
			cls.no_of_holiday = leaves
		def hoddetails(self):
			return f"The HOD name is {self.name}. The salary is {self.salary}. The role is {self.role} and the language is {self.language}"
		
Nisha = Employee("Nisha",45000,"Teacher")
Sheeja = hod("Sheeja",60000, "HOD",['Python','Java','Ruby','Django'])
Nisha.no_of_leaves=30
print(Sheeja.hoddetails())
Sheeja.change_holiday(90)
print(Sheeja.no_of_leaves)
print(Sheeja.printdetails())
