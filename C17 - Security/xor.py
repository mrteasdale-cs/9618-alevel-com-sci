def encrypt(text, key):
    encrypted = ""
    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted

def caesar(text, shift):
    encrypted = ""
    for i in range(len(text)):
        encrypted += chr((ord(text[i]) + shift - 65) % 26 + 65)
    return encrypted

# Example usage
plaintext = "Hello, World!"
key = "secretkey"

encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

# Decrypt by applying the same function with the same key
decrypted_text = encrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)