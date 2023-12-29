class dad:
	football = 6
	__private="I love bappa"
	_protec=87
	def __init__(self,ano):
		self.no=ano
		self.football=2
	def isfoot(self):
		return f" {self.football} number of times football played is"
		
class son(dad):
	dance =1
	def __init__(self,adance):
		self.dance=adance
		self.dance=5
	def isdane(self):
		return f"yes i dance {self.dance} no. of times"
	
class grandson(son):
	def __init__(self,ano):
		self.no= ano
	dance = 2
	def isdance(self):
		return f"yes i dance awesome {self.dance} no. of times"
		
dada = dad(3)
papa = son(4)
beta = grandson(8)

print(beta.isdance())
print(beta.isfoot())
# print(papa.isfoot())
print(dada.isfoot())
print(beta.isdance())
print(beta._dad__private)
print(papa._dad__private)
print(beta._protec)