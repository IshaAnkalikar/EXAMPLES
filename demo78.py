#constructor overriding 
#Examole-1
class parent:
	def __init__(self):
		print('Parent class constructor')
class child(parent):
	'''	def __init(self):
		print('child class constructor')'''
if __name__ == '__main__':
	c=child()

