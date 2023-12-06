class Satyug:
	def __init__(self):
		self.name='god'
		self.t=self.Tretayug()
	def disp_data(self):
		print(f'The name is {self.name}')
		Satyug.Tretayug().Dwaparyug().disp_data()
		Satyug.Tretayug.Dwaparyug.Kaliyug().danger()

	class Tretayug:
		def __init_(self):
			self.d=self.Dwaparyug()
		def disp_data(self):
			print(' Tretayug-> Ramayana ')
			Tretayug.Dwaparyug().disp_data()
			Tretayug.Dwaparyug.Kaliyug().danger()

		class Dwaparyug:
			def __init__(self):
				self.k=self.Kaliyug()
			def disp_data(self):
				print('Dwaparyug->Mahabharata')

			class Kaliyug:
				def danger(self):
					print('In Kaliyug we see a combination of Good and Evil in one single creature.')
if __name__ == '__main__':
	ref=Satyug()
	ref.disp_data()
