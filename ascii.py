import base64, pyfiglet
# note: this code only works if you have pyfiglet
def base64_encode(s):
    """Encode a string to Base 64."""
    return base64.b64encode(s.encode()).decode()

def base64_decode(s):
    """Decode a Base 64 string."""
    return base64.b64decode(s).decode()

def base32_encode(s):
    """Encode a string to Base 32."""
    return base64.b32encode(s.encode()).decode()

def base32_decode(s):
    """Decode a Base 32 string."""
    return base64.b32decode(s).decode()

def scramble(s):
    """Scramble the string by swapping adjacent characters."""
    scrambled = ''.join(s[i+1] + s[i] if i + 1 < len(s) else s[i] for i in range(0, len(s), 2))
    return scrambled

def unscramble(s):
    """Unscramble the string by swapping adjacent characters back."""
    unscrambled = ''.join(s[i+1] + s[i] if i + 1 < len(s) else s[i] for i in range(0, len(s), 2))
    return unscrambled

def encode_string(s):
    """Encode a string using the advanced method."""
    # Step 1: Base64 Encode
    base64_encoded = base64_encode(s)
    # Step 2: Scramble
    scrambled = scramble(base64_encoded)
    # Step 3: Base32 Encode
    base32_encoded = base32_encode(scrambled)
    # Step 4: Reverse
    final_encoded = base32_encoded[::-1]
    return final_encoded

def decode_string(s):
    """Decode a string using the advanced method."""
    # Step 4: Reverse
    reversed_s = s[::-1]
    # Step 3: Base32 Decode
    base32_decoded = base32_decode(reversed_s)
    # Step 2: Unscramble
    unscrambled = unscramble(base32_decoded)
    # Step 1: Base64 Decode
    final_decoded = base64_decode(unscrambled)
    return final_decoded

def main():
    password = "sigma" # choose the password here.
    attempts = 0
    max_attempts = 3
    banner = pyfiglet.figlet_format("ASCII Scrambler")
    print(banner)
    print("(Legacy: version 1.2)")
    while attempts < max_attempts:
        user_password = input("Enter password: ")
        if user_password == password:
            while True:
                action = input("Do you want to encode, decode, or exit? ").strip().lower()
                if action == "encode":
                    text = input("Enter the text you want to encode: ").strip()
                    encoded_text = encode_string(text)
                    print(f"Encoded: {encoded_text}")
                elif action == "decode":
                    text = input("Enter the text you want to decode: ").strip()
                    decoded_text = decode_string(text)
                    print(f"Decoded: {decoded_text}")
                elif action == "exit":
                    print("Exiting BASE/ASCII Scrambler Legacy...")
                    return
                else:
                    print("Invalid option. Please choose 'encode', 'decode', or 'exit'.")
        else:
            print("Incorrect password. Try again.")
            attempts += 1
    print("Too many incorrect attempts. Exiting.")

if __name__ == "__main__":
    main()
