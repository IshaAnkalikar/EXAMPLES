#Multiple inheritance
#example-1
class father:
	def order(self):
		print('Bring me some juice')
class mother:
	def order(self):
		print('Bring some vegetables')
class son(father,mother):
	def mywish(self):
		print('I wish to bring cake and ice-cream')
if __name__ == '__main__':
	s=son()
	s.mywish()
	s.order()