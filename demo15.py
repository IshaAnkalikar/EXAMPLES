'''
15. WAP to get cumulative sum of the given elements in the list
input:lst=[1,2,3,4]
explanation:[1,1+2,3+3,6+4]
output:[1, 3, 6, 10]

'''

#without LC METHOD-1
lst=[1,2,3,4]
x=1
lst1=[]
for i in lst:
	if x>=1:
		x=x+i 
		lst1.append(x-1)
	print(lst1)


#METHOD-2
lst=[1,2,3,4]
print(lst)
lst1=[]
data=0
for i in lst:
	data=data+i
	lst1.append(data)
print(lst1)



#using LC
lst=[1,2,3,4]
print(lst)
lst2=[sum(lst[0:i]) for i in lst] 
print(lst2)

	


	



