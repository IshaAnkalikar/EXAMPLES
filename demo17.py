'''
17.WAP to get the required result with and without List Comprehension(LC)
input:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
output: ['*', 2, '*', 4, '*', 6, '*', 8, '*', 10]
'''



#without LC
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
lst1=[]
for i in lst:
	if i%2!=0:
		lst1.append('*')
	else:
		lst1.append(i)
print(lst1)

#with LC
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
lst2=[i if i%2==0 else '*' for i in lst ]
print(lst2)
