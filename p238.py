import hashlib

filename = "apple.jpg"

with open(filename, "rb") as f: 
	file_data = f.read()
	image_hash = hashlib.sha3_256(file_data).hexdigest()
	print(image_hash)
