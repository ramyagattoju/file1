from helpers import alphabet_position,rotate_character
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


