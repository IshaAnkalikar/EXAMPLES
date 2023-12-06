#Example-2 Operator overloading
class Book:
	def __init__(self,name,no_of_pages):
		self.name=name
		self.no_of_pages=no_of_pages
if __name__ == '__main__':
	b1=Book(name='fairytales',no_of_pages=60)
	b2=Book(name='tables',no_of_pages=20)
	print(f'The result is {b1+b2}')