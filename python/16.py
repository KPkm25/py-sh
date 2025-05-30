data= {
	"a":{
		"b":{
			"c":42
}
},
	"x":{
		"y":{
			"z":"Hello"
}
}
}


def get_value(data,path):
	keys=path.split("/")
	value=data
	for key in keys:
		value=value[key]
	print(value)

get_value(data,"a/b/c")
get_value(data,"x/y/z")
