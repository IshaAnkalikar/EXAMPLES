'''TASK YET TO COMPLETE
WAP to get the required output
input: [(2,5),(1,2),(4,4),(2,3),(2,1)]
output:[(2,1),(1,2),(2,3),(4,4),(2,5)]
'''


lst1= [(2,5),(1,2),(4,4),(2,3),(2,1)]
print(lst1)
lst2=[]
lst3=[]
lst4=[]
lst5=[]
lst6=[]

lst2.extend(lst1[:-2:-1])
lst3.extend(lst1[1::2])
lst4.extend(lst1[-3::3])
lst5.extend(lst1[0])
'''print(lst2)
print(lst3)
print(lst4)
print(lst5)'''
lst6.append(lst2)
lst6.append(lst3)
lst6.append(lst4)
lst6.append(lst5)
print(lst6)


