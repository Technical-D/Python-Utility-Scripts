from arts import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart = True

print(logo)

def encrypt(plain_text, shift_amount):
    encrypted_text = ''
    for letter in plain_text:
        if letter in alphabet:

            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > len(alphabet) - 1:
                new_position -= len(alphabet)
            encrypted_text+=alphabet[new_position]
        else:
            encrypted_text+=letter
    print(f"Here's the encoded result: {encrypted_text}")

def decrypt(cipher_text, shift_amount):
    decrypted_text = ''
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            if new_position < 0:
                new_position = len(alphabet) + new_position

            decrypted_text += alphabet[new_position]
        else:
            decrypted_text+=text

    print(f"Here's the decoded result: {decrypted_text}")
    

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text, shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == 'no':
        restart = False

print("Sayonara")