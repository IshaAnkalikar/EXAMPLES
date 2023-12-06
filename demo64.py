#GC Example-5 [Destructor]
class Demo:
	def __init__(self):
		print('constructor gets executed')
		print('initialize the obj')
	def __del__(self):
		print('destructor gets executed')
		print('fulfilling the last wish of the obj')
if __name__ == '__main__':
	print('prog execution starts')
	print('main method executes')
	d1=Demo()
	d1=None
	print('prog execution ends')