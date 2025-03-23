def caesar_cipher(text,shift,encrypt=True):
    result = ""
    if not encrypt:
        shift=-shift
    for char in text:
        if char.isalpha():
            base= 'A' if char.isupper() else 'a'
            result+=chr((ord(char) - ord(base) + shift) %26 + ord(base))
        else:
            result+=char
    return result
#user input
message= input("Enter a message:")
shift= int(input("Enter a shift value:"))
mode= input("Type 'e' for encryption or 'd' for decryption:").lower()

#encrypt or decrypt
if mode == 'e':
    print("Encrypted text:", caesar_cipher(message,shift))
elif mode == 'd':
    print("Decrypted text:",caesar_cipher(message,shift,encrypt=False))
else:
    print("Invalid choice!!")
    
