'''
31.WAP to get output using UDF and lambda fun
input: lst=[1,2,3,4,5]
output:15
'''
'''
#My code
def fun(lst):

	return lst1
if __name__ == '__main__':
	lst=[1,2,3,4,5]
	res=fun(lst)
	print(res)
'''
#with lambda
lst=[1,2,3,4,5]
lst1=list(map(lambda i:sum(lst),lst))
print((lst1))

#SIr's code
#using UDF
def task(lst):
	return sum(lst)
if __name__ == '__main__':
	lst=[1,2,3,4,5]
	print(task(lst))

#using lambda method-1
res=lambda s:sum(s)
print(res([1,2,3,4,5]))

#using lambda method-2
lst=[1,2,3,4,5]
from functools import reduce
res=reduce(lambda x,y:x+y,lst)
print(res)