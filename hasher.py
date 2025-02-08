import hashlib, os

# The password you want to prehash
print(os.urandom(16))
password = input("Enter password to hash: ")

# Create a hash object
hash_object = hashlib.sha256(password.encode())

# Get the hexadecimal representation of the hash
prehashed_password = hash_object.hexdigest()

# Output the prehashed password
print(prehashed_password)
