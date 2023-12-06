#Example for Aggregation / Weak relation /is-a
class salary:
	def __init__(self,pay,bonus):
		self.pay=pay
		self.bonus=bonus
	def annual_salary(self):
		return (self.pay*12)+self.bonus
class employee:
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.obj=salary 
	def total_salary(self):
		return (self.obj.annual_salary())
if __name__ == '__main__':
	s=salary(pay=30000,bonus=3000)
	e=employee(name='sachin',age=24,salary=s)
	print(e.total_salary())