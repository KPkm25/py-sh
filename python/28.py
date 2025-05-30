#Q11:Write a Python function that takes a list and returns a new list with unique elements of the first list.

sample= [1,1,1,1,2,2,3,3,3,3,4,5]

#Unique List : [1, 2, 3, 4, 5]
op=set([])
for i in sample:
	op.add(i)
print(op)
