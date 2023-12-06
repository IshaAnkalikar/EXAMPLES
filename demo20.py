'''
20. Write a program to pair up consecutive elements of a given list lst:
input: lst=[1,2,3,4,5,6]
output: [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
'''




lst=[1,2,3,4,5,6]
print(lst)
lst1=[]
lst1.extend((lst[:2],lst[1:3],lst[2:4],lst[3:5],lst[4:6]))
print(lst1)