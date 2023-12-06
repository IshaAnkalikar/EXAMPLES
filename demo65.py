#GC Example-6 [Destructor]
import time
class Cricketer:
	def __init__(self):
		print('constructor gets executed ')
		print('initialize the obj')
	def __del__(self):
		print('destructor gets executed')
		print('fulfilling the last wish of the obj')
		print('delete the obj')
if __name__ == '__main__':
	print('prog execution starts')
	print('main method gets executed')
	lst=[Cricketer(),Cricketer(),Cricketer()]
	del lst
	time.sleep(15)
	print('prog execution ends')