'''Taking input from the user and display 
multiplication table for the same 
'''
class multable:
	def __init__(self,num):
		self.num=num
	def table(self):
		for i in range(1,11):
			print(f'The table of {self.num} is {num}x{i}={self.num*i}')
if __name__ == '__main__':
	num=int(input('enter a number:'))
	m=multable(num=num)
	m.table()
