#Example-2 
#Method overriding 
class parent:
	def __init__(self):
		print('parent class constructor')
class child(parent):
	def __init__(self):
		super().__init__()
		print('child class constructor')
if __name__ == '__main__':
	c=child()