# PRODIGY_CS_01


Caesar Cipher Encryption & Decryption 🔐

A simple Python script to encrypt and decrypt messages using the Caesar Cipher algorithm.

📌 Overview

The Caesar Cipher is one of the oldest encryption techniques, where each letter in the plaintext is shifted by a fixed number of places in the alphabet. This program allows users to:

✅ Encrypt a message by shifting letters forward.

✅ Decrypt a message by shifting letters backward.



📂 Project Structure

📦 Caesar-Cipher
 
 ┣ 📜 caesar_cipher.py  # The main Python script
 
 ┣ 📜 README.md          # Project documentation

 ┗ 📷 Screenshot.png     # Output example



🛠️ Features

✔️ Encrypts and decrypts messages using a shift value.

✔️ Supports both uppercase and lowercase letters.

✔️ Preserves non-alphabetical characters (spaces, numbers, punctuation).

✔️ User-friendly input prompts.


💻 Installation & Usage

1️⃣ Clone the Repository

git clone https://github.com/YOUR-USERNAME/Caesar-Cipher.git

cd Caesar-Cipher

2️⃣ Run the Python Script

python caesar_cipher.py

3️⃣ Input Example

Enter a message: good morning

Enter a shift value: 4

Type 'e' for encryption or 'd' for decryption: e

Encrypted text: kssh qsvmrk

Enter a message: kssh qsvmrk

Enter a shift value: 4

Type 'e' for encryption or 'd' for decryption: d

Decrypted text: good morning


📜 Code Explanation

def caesar_cipher(text, shift, encrypt=True):
   
    result = ""
    
    if not encrypt:
        
        shift = -shift  # Reverse shift for decryption
    
    for char in text:
        
        if char.isalpha():
           
            base = 'A' if char.isupper() else 'a'
            
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        
        else:
            
            result += char  # Keep spaces and symbols unchanged
    
    return result


📷 Screenshot of Output

![Screenshot 2025-03-24 002827](https://github.com/user-attachments/assets/ac6f45e8-5400-413e-b1ae-483b16e0c9e3)


⚡ Improvements & Future Enhancements

🔹 Add support for negative shifts.

🔹 Improve UI with a GUI-based version (Tkinter).

🔹 Implement brute-force decryption (when shift value is unknown).


🛠️ Requirements

📌 Python 3.x installed.
📌 Works on Windows, Linux, macOS.

