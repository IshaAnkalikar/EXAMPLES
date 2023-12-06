#Method overriding in python
#Example-1
class parent:
	def House(self):
		print('Fathers house')
	def bike(self):
		print('Father has active honda')
class child(parent):
	'''
	#inherited method
	def House(self):
		print('Fathers house')
		'''
	#overrided method
	def bike(self):
		print('I want KTM bike')
if __name__ == '__main__':
	c=child()
	c.bike()
	c.House()