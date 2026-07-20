print("ANSHRAH SHAIKH \nT112 \nTYCS \nCYBER SECURITY PRACTICAL 2")

import rsa

public_key, private_key = rsa.newkeys(512)

message = input("Enter message: ").encode()

encrypted = rsa.encrypt(message, public_key)
print("Encrypted:", encrypted)

decrypted = rsa.decrypt(encrypted, private_key).decode()
print("Decrypted:", decrypted)
