#Multi-level inheritance
#Example-1
class grandfather:
	def past(self):
		print('My grandfather was working hard..')
class father(grandfather):
	def present(self):
		print('Father has taken all the property from grand father')
class grandson(father):
	def future(self):
		print('I will enjoy my father and grandfathers property')
if __name__ == '__main__':
	ref=grandson()
	ref.past()
	ref.present()
	ref.future()