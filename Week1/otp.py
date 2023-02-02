default_message = 'attack at dawn'
# default_cipher_text = 0x09e1c5f70a65ac519458e7e53f36
default_cipher_text = 0x6c73d5240a948c86981bc294814d
default_new_message = 'attack at dusk'

def key_getter(message, cipher_text):
    hex_message = message.encode().hex()
    return hex(int(hex_message, 16) ^  cipher_text)

def encrypt(message, key):
    hex_message = message.encode().hex()
    return hex(int(hex_message, 16) ^  key)

def main():
    message = input("Enter the message: ")
    if message == '':
        message = default_message
    cipher_text = input("Enter the cipher text: ")
    if cipher_text == '':
        cipher_text = default_cipher_text
    new_message = input("Enter the new message: ")
    if new_message == '':
        new_message = default_new_message

    key = key_getter(message, cipher_text)
    print("The key is: ", key)
    print("The new cipher text is: ", encrypt(new_message, int(key, 16)))

if __name__ == "__main__":
    main()