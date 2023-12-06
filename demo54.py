#WAP to get the no. of reference pointing to the object
import sys
class demo:
	pass
if __name__ == '__main__':
	d1=demo()
	d2=d1
	print(f'Total number of ref are:{sys.getrefcount(d2)}')