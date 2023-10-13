alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !?.,"

def substitution_cipher_encrypt(text, key):
    encrypted_text = ""

    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_text += key[char_index]
        else:
            encrypted_text += char

    return encrypted_text

def substitution_cipher_decrypt(encrypted_text, key):
    decrypted_text = ""

    for char in encrypted_text:
        if char in key:
            char_index = key.index(char)
            decrypted_text += alphabet[char_index]
        else:
            decrypted_text += char

    return decrypted_text


text = str(input('Enter text to encrypt: '))

key = "2SZXvdO!qPoF7Jc3fgYl1KIX9Hi ?w6pCmeNkLzURj8nAtQG4h.yMs5xb0DTBEJarV,QuW"


encrypted_text = substitution_cipher_encrypt(text, key)
print(f'Encrypted: {encrypted_text}')

to_decrypt = str(input('Type y if want to see decrypt the message: '))

if to_decrypt == 'y':
    print(f'Decrypted text: {substitution_cipher_decrypt(encrypted_text, key)}')
else:
    print("Thank you for using Encryption System.")
