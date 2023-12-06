#WAP to count the number of objects in the class
class count:
	no_of_obj=0
	def __init__(self):
		count.no_of_obj=count.no_of_obj+1
		print(f'The no. of obj are: {count.no_of_obj}')
if __name__ == '__main__':
	c1=count()
	c2=count()