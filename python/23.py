#Q6:Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
trial=st.split(" ")
op=[w[0] for w in trial]
print(op)
