'''
14.WAP to print the square numbers with the help of list using for loop
input: lst=[10,2.5,'abc',20,2+3j,True,30]
output: [100,400,900]
'''

#without LC
lst=[10,2.5,'abc',20,2+3j,True,30]
print(lst)
lst1=[]
for i in lst:
	if type(i)==int:
		lst1.append(i*i)
print(lst1)


#with LC
lst=[10,2.5,'abc',20,2+3j,True,30]
print(lst)
lst1=[i*i for i in lst if type(i)==int]
print(lst1)


