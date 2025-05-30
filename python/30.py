#Q13:Write a Python function to check whether a string is pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

str= "uick brown fox jumps over the lazy dog"
str1=str.lower()

op={}

for i in str1:
	if i.isalpha() and i not in op:
		op[i]=1
if len(op)!=26:
	print("Not a panagram!")
else:
	print("Panagram")
