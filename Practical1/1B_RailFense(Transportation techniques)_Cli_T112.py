# Rail Fence Cipher (2 Rails)

def encrypt(text):
    rail1 = ""
    rail2 = ""

    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    return rail1 + rail2


def decrypt(cipher):
    mid = (len(cipher) + 1) // 2

    rail1 = cipher[:mid]
    rail2 = cipher[mid:]

    result = ""
    i = j = 0

    for k in range(len(cipher)):
        if k % 2 == 0:
            result += rail1[i]
            i += 1
        else:
            result += rail2[j]
            j += 1

    return result


print("===== Rail Fence Cipher =====")

message = input("Enter Message: ")

choice = input("Encrypt or Decrypt (E/D): ").upper()

if choice == "E":
    print("Encrypted:", encrypt(message))
elif choice == "D":
    print("Decrypted:", decrypt(message))
else:
    print("Invalid Choice")
