import hashlib

# Step 1: Prehash the password "sigma" and store the result as bytes
prehashed_password_hex = "38de90475bb334fb3dea5d54f250500aba60fe2c6158115d342b06bcb46e39bf"
prehashed_password_bytes = bytes.fromhex(prehashed_password_hex)

# Step 2: Define a constant to be concatenated
constant = "static_constant"

def hash_with_constant(prehashed_password, constant):
    """Combine the prehashed password with a constant and hash the result."""
    combined = prehashed_password + constant.encode('utf-8')
    hashed = hashlib.sha256(combined).digest()
    return hashed

def verify_password(stored_password, input_password, constant):
    """Verify a stored password against an input password combined with a constant."""
    # Prehash the user input password first
    user_prehashed_password = hashlib.sha256(input_password.encode('utf-8')).digest()
    combined = user_prehashed_password + constant.encode('utf-8')
    hashed_input_password = hashlib.sha256(combined).digest()
    return hashed_input_password == stored_password

def main():
    stored_password = hash_with_constant(prehashed_password_bytes, constant)
    print(f"Stored Password (hashed): {stored_password}")

    while True:
        user_password = input("Enter password: ")
        
        # Prehash the user-entered password before combining with constant
        user_password_bytes = hashlib.sha256(user_password.encode('utf-8')).digest()
        combined_user_password = user_password_bytes + constant.encode('utf-8')
        hashed_user_password = hashlib.sha256(combined_user_password).digest()

        print(f"Entered Password: {user_password}")
        print(f"Prehashed User Password: {user_password_bytes}")
        print(f"Combined with Constant: {combined_user_password}")
        print(f"Hashed Entered Password: {hashed_user_password}")

        is_verified = verify_password(stored_password, user_password, constant)
        print(f"Verification: {is_verified}")

        if is_verified:
            print("Password correct! The entered password is:", user_password)
            break
        else:
            print("Incorrect password. Try again.")

if __name__ == "__main__":
    main()
