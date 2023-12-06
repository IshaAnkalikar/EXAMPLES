#Example for composition / Strong relation / has -a
class Salary:
	def __init__(self,pay,bonus):
		self.pay=pay
		self.bonus=bonus
	def annual_salary(self):
		return (self.pay*12)+self.bonus
class employee:
	def __init__(self,name,age,pay,bonus):
		self.name=name
		self.age=age
		self.obj=Salary(pay,bonus)
	def total_salary(self):
		return (self.obj.annual_salary())
if __name__ == '__main__':
	e=employee('sachin',22,30000,3000)
	print(e.total_salary())
	