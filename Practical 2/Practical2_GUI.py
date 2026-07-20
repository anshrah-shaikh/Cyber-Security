print("ANSHRAH SHAIKH \nT112 \nTYCS \nCYBER SECURITY PRACTICAL 2")

import tkinter as tk
import rsa

public_key, private_key = rsa.newkeys(512)

def encrypt():
    global cipher
    cipher = rsa.encrypt(entry.get().encode(), public_key)
    output.config(text="Encrypted:\n" + str(cipher))

def decrypt():
    text = rsa.decrypt(cipher, private_key).decode()
    output.config(text="Decrypted: " + text)

root = tk.Tk()
root.title("RSA")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Encrypt", command=encrypt).pack()
tk.Button(root, text="Decrypt", command=decrypt).pack()

output = tk.Label(root)
output.pack()

root.mainloop()
