import hashlib

def encrypt_pws(pwd):
	return hashlib.sha256(pwd.encode()).hexdigest()
def check_pwd(og,new):
	new_e=encrypt_pws(new)
	if(og==new_e):
		print("Password match successful!")
	else:
		print("Password authentication failed")

if __name__ == "__main__":
	password=input("Please enter a password:")
	og_encrypt=encrypt_pws(password)
	match=input("Enter pwd to match:")
	check_pwd(og_encrypt,match)
