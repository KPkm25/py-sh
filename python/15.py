import re
import json
input_file="sample.log"
output_file="op.json"
errors=[]
pattern=r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\sERROR\s(.*)"

with open(input_file,"r") as f:
	for line in f:
		match=re.search(pattern,line)
		print(match)
		if match:
			timestamp,message=match.groups()
			errors.append({"timestamp":timestamp,"Error":message})
with open(output_file,"w") as op:
	json.dump(errors,op,indent=4)
