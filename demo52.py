class parent:
	def wish(self):
		print('my kid should become engg')
class child(parent):
	def wish(self):
		print('I wish to become an actor')
		super(child,self).wish()
if __name__ == '__main__':
	c=child()
	c.wish()
