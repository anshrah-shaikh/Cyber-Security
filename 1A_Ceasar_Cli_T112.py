print("ANSHRAH SHAIKH \nT112 \nTYCS \nCYBER SECURITY PRACTICAL 1")
# Caesar Cipher - CLI Version

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== Caesar Cipher =====")

message = input("Enter Message: ")
shift = int(input("Enter Shift Value: "))

choice = input("Encrypt or Decrypt (E/D): ").upper()

if choice == "E":
    print("Encrypted Message:", encrypt(message, shift))
elif choice == "D":
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid Choice")
