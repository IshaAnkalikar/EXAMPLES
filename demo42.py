#Object orientation in python
#Example-1
class cricketer:
	def __init__(self,name,num,avg):
		self.name=name
		self.num=num
		self.avg=avg
	def display(self):
		print(f'name is {self.name}')
		print(f'num is {self.num}')
		print(f'avg is {self.avg}')
if __name__ == '__main__':
	c=cricketer('virat',18,102.4)
	c.display()