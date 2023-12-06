'''
16. WAP to print the even numbers which is greater than 4 using for loop
input:lst=[1,2,3,4,5,6,7,8,9,10]
output:[6, 8, 10]
'''

#without LC
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
lst1=[]
for i in lst:
	if i>4:
		if i%2==0:
			lst1.append(i)
print(lst1)


#with LC
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
lst2=[i for  i in lst if i>4 if i%2==0 ]
print(lst2)
