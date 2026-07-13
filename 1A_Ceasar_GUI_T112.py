from tkinter import *

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char)-65+shift)%26+65)
            else:
                result += chr((ord(char)-97+shift)%26+97)
        else:
            result += char

    return result

def encrypt_message():
    msg = entry.get()
    shift = int(shift_entry.get())
    result_label.config(text="Encrypted: " + encrypt(msg, shift))

def decrypt_message():
    msg = entry.get()
    shift = int(shift_entry.get())
    result_label.config(text="Decrypted: " + encrypt(msg, -shift))

root = Tk()
root.title("Caesar Cipher")

Label(root, text="Enter Message").pack()

entry = Entry(root, width=40)
entry.pack()

Label(root, text="Shift Value").pack()

shift_entry = Entry(root)
shift_entry.pack()

Button(root, text="Encrypt", command=encrypt_message).pack(pady=5)

Button(root, text="Decrypt", command=decrypt_message).pack(pady=5)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
