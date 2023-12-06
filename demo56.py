#HOW TO GET MRO PROGRAMMATICALLY
#Example for multiple inheritance
class father:
	def order(self):
		print('To bring some juice')
class mother:
	def order(self):
		print('To bring some vegetables')
class son(father,mother):
	def mywish(self):
		print('I wish to bring cake and ice-cream')
if __name__ == '__main__':
	s=son()
	s.mywish()
	s.order()
	#print(son.mro())
	print(son.__mro__)
