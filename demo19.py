'''
19. WAP to calculate the sum of the lowest negative number in the given list:
input: lst=[-14,15,-10,-11,-12,-13,16,17,18,20]
logic: [(-14)+(-13)=-27]
output:-27
'''
#using built in function
lst=[-14,15,-10,-11,-12,-13,16,17,18,20]
print(lst)
lst1=[]
lst1.append(min(lst))
lst.remove(min(lst))
lst1.append(min(lst))
print(sum(lst1))

#without using built-in fun
lst=[-14,15,-10,-11,-12,-13,16,17,18,20]
print(lst)
lst1=[]
for i in lst:
	if i<0:
		lst1.append(i)
lst2=sorted(lst1)
print(lst2[0]+lst2[1])