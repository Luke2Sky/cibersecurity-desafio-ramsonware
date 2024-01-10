import os
import pyaes

# Open encrypted file

file_name = 'test.txt.ransomware'
with open(file_name, 'rb') as file:
    file_data = file.read()

# Cryptographic key

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

# Remove encrypted file

os.remove(file_name)

# create decrypted file

new_file_name = file_name.replace('.ransomware', '')
with open(new_file_name, 'wb') as new_file:
    new_file.write(decrypted_data)

