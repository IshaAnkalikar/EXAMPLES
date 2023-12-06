'''
11.WAP to find the largest odd number in given list
input:lst=[0,9,2,4,5,6]
output:9
'''

#without LC
lst=[0,9,2,4,5,6]
print(lst)
lst1=[]
for i in lst:
	if i%2!=0:
		lst1.append(i)
print(max(lst1))

#with LC
lst=[0,9,2,4,5,6]
print(lst)
lst1=[i for i in lst if i%2!=0]
print(max(lst1))