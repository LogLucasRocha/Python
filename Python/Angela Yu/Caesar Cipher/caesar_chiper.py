import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text, shift, direction):
    cipher_text = ""
    for letter in text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = (position + shift) % 26
            code = "encode"
        elif direction == "decode":
            new_position = (position - shift) % 26
            code = "decode"
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The {code}d text is {cipher_text}")
    return input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") == "yes"

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26: 
        shift = shift % 26

    should_continue = caesar(text, shift, direction)

print("Goodbye")

