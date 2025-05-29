import hashlib

def convert(file_name):
	with open(file_name,"rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hashlib.sha256().update(chunk)
	return hashlib.sha256().hexdigest()
if __name__ == "__main__":
	file_name=input("Enter file:")
	print("The converted file is:",convert(file_name))
