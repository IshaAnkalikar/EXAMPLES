'''
30. WAP to get required output:
input:lst=[1,2,3,4,5]
output:[1,4,9,16,25]
'''

#with UDF
def fun(lst):
	lst1=[]
	for i in lst:
		lst1.append(i*i)
	return lst1
if __name__ == '__main__':
	lst=[1,2,3,4,5]
	res=fun(lst)
	print(res)

#using lambda fun #method-1
lst=[1,2,3,4,5]
lst1=list(map(lambda i:i*i,lst))
print(lst1)

#method-2
def fun(lst):
	return list(map(lambda i:i**2))
if __name__ == '__main__':
	lst=[1,2,3,4,5]
	res=fun(lst)
	print(res)
