#constructor overloading
#Example-1
class Employee:
	def __init__(self,name):
		self.name=name
		print(f'The name is {self.name}')
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print(f'The name is {self.name} and age is {self.age}')
	def __init__(self,name,age,eid):
		self.name=name
		self.age=age
		self.eid=eid
		print(f'The name is {self.name} and age is {self.age} and id is {self.eid}')
if __name__ == '__main__':
	e=Employee('sachin',42,10)