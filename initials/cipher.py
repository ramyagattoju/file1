
def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + int(rot)) % 26
    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]

def encrypt(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated

def main():
    text = input("Type a message:")
    rot = input("Rotate by:")
    print(encrypt(text,rot))
if __name__ == "__main__":
    main()


