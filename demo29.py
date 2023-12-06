'''
WAP to get the required output
input:lst=[1,2,3,4,5,6,7,8,9,10]
output:[2, 4, 6, 8, 10]
'''



'''
#with using UDF
def even(lst):
		lst1=[]
		for i in lst:
			if i%2==0:
				lst1.append(i)
		print(lst1)

if __name__ == '__main__':
	lst=[1,2,3,4,5,6,7,8,9,10]
	res=even(lst)
	print(res)
'''
#using lambda fun
#my code
def fun(lst):
	return lambda lst:lst[1::2]
if __name__ == '__main__':
	lst=[1,2,3,4,5,6,7,8,9,10]
	res=fun(lst)
	print(res)

	#sirs code
lst=[1,2,3,4,5,6,7,8,9,10]
lst1=[]

