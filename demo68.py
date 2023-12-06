#Example for multi-level inner classses
#inner class Example-3
class Human:
	def __init__(self):
		self.name='Manoj'
		self.h=self.Head()
	def disp_data(self):
		print(f'The name is {self.name}')
		Human.Head().mouth()
		Human.Head.Brain().think()
	class Head:
		def __init__(self):
			self.b=self.Brain()
		def mouth(self):
			print('mouth is used for talking')
		class Brain:
			def think(self):
				print('Brain is used to think')
if __name__ == '__main__':
	ref=Human()
	ref.disp_data()
