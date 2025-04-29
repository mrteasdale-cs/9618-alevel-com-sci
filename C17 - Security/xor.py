def xorencrypt(text, key):
    encrypted = ""
    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted

def caesar(text, shift):
    encrypted = ""
    for i in range(len(text)):
        # simple encryption using caesar shift (get the ordinal of a letter, 
        # apply a shift, then modulo 26 for wrap around and add 65. Convert this back to 
        # char
        encrypted += chr((ord(text[i]) + shift - 65) % 26 + 65)
    return encrypted

# Example usage
plaintext = "Hello, World!"
key = "secretkey"

encrypted_text = xorencrypt(plaintext, key)
print("Encrypted:", encrypted_text)

# Decrypt by applying the same function with the same key
decrypted_text = xorencrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)

encrypted_text_caesar = caesar(plaintext, 4)
print("Encrypted using Caesar Cipher:", encrypted_text_caesar)