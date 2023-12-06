class Person:
	def __init__(self):
		self.name='isha'
		self.dob=self.Dob()
	def disp(self):
		print(f'The name is {self.name}')
		#person.Dob().disp_data()
		self.dob.disp_data()
	class Dob:
		def __init__(self):
			self.date=26
			self.month=9
			self.year=2003
		def disp_data(self):
			print(f'The date of birth is: {self.date}/{self.month}/{self.year}')
if __name__ == '__main__':
	ref=Person()
	ref.disp()
