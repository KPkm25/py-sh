def convert_fn(data,data2):
	temp=data.copy()
	for key,value in data2.items():
		if key in temp:
			if isinstance(temp[key],list) and isinstance(value,list):
				temp[key]+=value
			elif isinstance(temp[key],(int,float)) and isinstance(value, (int,float)):
				temp[key]+=value
			else:
				temp[key]=value
		else:
			temp[key]=value
	return temp
data={'x':[10,20],'y':25,'z':"trial"}
data2={'x':[50],'y':45,'z':"overwrite"}

op=convert_fn(data,data2)
print(op)
