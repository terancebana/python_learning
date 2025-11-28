import string

alphabet = list(string.ascii_lowercase)

def encode(message, rotation):
    message = list(message.lower())
    encoded_message = ""

    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            encoded_message += alphabet[(position + rotation) % 26]
        else:
            encoded_message += char

    return encoded_message

def decode(message, rotation):
    message = list(message.lower())
    decoded_message = ""

    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            decoded_message += alphabet[(position - rotation) % 26]
        else:
            decoded_message += char

    return decoded_message


banner = r"""
  ___   _   ___ ___  _   ___     ___ ___ ___ _  _ ___ ___ 
 / __| /_\ | __/ __|/_\ | _ \   / __|_ _| _ \ || | __| _ \
| (__ / _ \| _|\__ / _ \|   /  | (__ | ||  _/ __ | _||   /
 \___/_/ \_\___|___/_/ \_\_|_\  \___|___|_| |_||_|___|_|_\
"""

print(banner)


option = input("Type 'encode' or 'decode' to choose action: ").lower()
message = input("Input the message: ")
rotation = int(input("Enter the rotation value "))

if option == "encode":
    print(f"result: {encode(message=message, rotation=rotation)}")
elif option == "decode":
    print(f"result: {decode(message=message, rotation=rotation)}")
else:
    print("Invalid!")


while True:
    pass
