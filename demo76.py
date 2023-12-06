'''WAP to display the details of the employee
as well as use opeartor overloading to calculate the salary
hike of employee'''
class employee:
	def __init__(self,name,eid,salary):
		self.name=name
		self.eid=eid
		self.salary=salary
	def disp(self):
		print(f'The name is {self.name}')
		print(f'The eid is {self.eid}')
		print(f'The salary is {self.salary}')
class Hr:
	def hike(self,data):
		return data.salary+5000
if __name__ == '__main__':
	e=employee(name='sachin',eid=10,salary=45000)
	h=Hr()
	totalsalary=h.hike(e)
	e.disp()
	print(f'The salary after hike is {totalsalary}')

