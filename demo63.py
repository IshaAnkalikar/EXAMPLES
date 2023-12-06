# GC Example-4 [Destructor]
class Demo:
	def __init__(self):
		print('constructor gets executed')
		print('Initialize the obj')
	def __del__(self):
		print('Destructor gets executed')
		print('fulfilling the last wish of the obj')
		print('delete the obj')
if __name__ == '__main__':
	print('prog execution starts')
	print('main method executes')
	d1=Demo()
	print('prog execution ends')
	