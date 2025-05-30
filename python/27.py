#Q10:Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
st= 'Hello Mr. Rogers, how are you this fine Tuesday?'
count_up=0
count_down=0
for i in st:
	if i.isupper():
		count_up=count_up+1
	if i.islower():
		count_down=count_down+1
print(count_up)
print(count_down)
