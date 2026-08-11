alphabet = "abcdefghijklmnopqrstuvwxyz"
def encrypt(plain_text,shift):
    encrypted_text = ""
    for p in plain_text:
        pos = alphabet.index(p)
        new_pos = (pos + shift) % 26
        encrypted_text += alphabet[new_pos]
    return encrypted_text
def decrypt(encrypted_text,shift):
    decrypted_text = ""
    for p in encrypted_text:
        pos = alphabet.index(p)
        new_pos = (pos - shift) % 26
        decrypted_text += alphabet[new_pos]
    return decrypted_text
print("Welcome to the Caesar Cipher Program!")
choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
shift = int(input("Type the shift number:\n"))
if choice == "encode":
    text = input("Type your message:\n").lower()
    encrypted_text = encrypt(text,shift)
    print(f"The encoded text is {encrypted_text}")
elif choice == "decode":
    text = input("Type your message:\n").lower()
    decrypted_text = decrypt(text,shift)
    print(f"The decoded text is {decrypted_text}")
