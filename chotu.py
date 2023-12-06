#simple interest
class SI:
	def __init__(self,p,t,r):
		self.p=p
		self.t=t
		self.r=r
		res={self.p}*{self.t}*{self.r}/{100}
	def disp(self):
		print(f'The Simple Interest is {res}')
if __name__ == '__main__':
	PA=int(input('enter principle amount:'))
	time=int(input('enter the time:'))
	ROI=int(input('enter the rate of interest:'))
	s=SI(PA,time,ROI)
	s.disp()
