letters = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(text, key):
    enc_text = ''

    for char in text:
        if char.lower() in letters:
            index = (letters.index(char.lower()) + key) % 26
            new_char = letters[index]

            if char.isupper():
                new_char = new_char.upper()

            enc_text += new_char
        else:
            enc_text += char

    return enc_text


def decrypt(text, key):
    dec_text = ''

    for char in text:
        if char.lower() in letters:
            index = (letters.index(char.lower()) - key) % 26
            new_char = letters[index]

            if char.isupper():
                new_char = new_char.upper()

            dec_text += new_char
        else:
            dec_text += char

    return dec_text


print()
print('Welcome to the Caesar Cipher Program!')
print()

print('Do you want to encrypt or decrypt a message?')
print()

user_choice = input('Type "e" to encrypt, type "d" to decrypt:\n').lower()
print()

if user_choice == 'e' or user_choice == 'd':

    key = int(input('Enter the key (a number between 1 and 25):\n'))

    if key < 1 or key > 25:
        print('Invalid key. Please enter a number between 1 and 25.')

    else:
        text = input('Enter the message:\n')

        if user_choice == 'e':
            result = encrypt(text, key)
            print()
            print('Encrypted message:', result)

        else:
            result = decrypt(text, key)
            print()
            print('Decrypted message:', result)

else:
    print('Invalid choice. Please enter "e" or "d".')