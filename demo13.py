'''
13. WAP to sum the first number with the second number and divide it by 2,
then sum the second number with the third number and divide it by 2
and so on...
input: [1,2,3,4,5,6,7]
output:[1.5,2.5,3.5,4.5,5.5,6.5]
'''
lst=[1,2,3,4,5,6,7]
print(lst)
x=0
lst1=[]
for i in range(0,len(lst)-1):
	x=(lst[i]+lst[i+1])/2
	lst1.append(x)
print(lst1)







