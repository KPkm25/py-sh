st = 'Print only the words that start with s in this sentence'

trial=st.split(" ")
for t in trial:
	if t[0]=="s" and len(t)>1:
		print(t)
