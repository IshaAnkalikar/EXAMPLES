'''
12. WAP to add all the elements to the list of
 integers except the number at index
 input:[1,2,3]
 explanation:[1+2+3-1,1+2+3-2,1+2+3-3]
 output:[5,4,3]
'''

#without LC
#METHOD-1
lst=[1,2,3]
print(lst)
x=0
lst1=[]
for i in lst:
	x=x+i
for i in lst:
	lst1.append(x-i)
print(lst1)


#METHOD-2
lst=[1,2,3]
print(lst)
x=sum(lst)
lst1=[]
for i in lst:
	lst1.append(x-i)
print(lst1)

#with LC
lst=[1,2,3]
print(lst)
lst1=[sum(lst)-i for i in lst]
print(lst1)