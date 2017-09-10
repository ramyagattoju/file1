from helpers import alphabet_position,rotate_character
def encrypt(text, key):
    baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    keyList = []
    keyLength = 0
    while keyLength < len(text):
        for char in key:
            if keyLength < len(text):
                keyList.append(str(char))
                keyLength = keyLength + 1
    completeCipherText = []
    cipherCharIndexValue = 0
    keyIncrement = 0 

    for plaintextchar in text:
        ind_char = plaintextchar.lower()
        if ind_char in baseAlphabet:
            
            cipherCharIndexValue =int(alphabet_position(keyList[keyIncrement])) +int(alphabet_position(ind_char)) 
            while cipherCharIndexValue > 25:
                cipherCharIndexValue = cipherCharIndexValue - 26
            if plaintextchar.isupper():
                
                completeCipherText.append(baseAlphabet[cipherCharIndexValue].upper())
            else:       
                completeCipherText.append(baseAlphabet[cipherCharIndexValue])
            keyIncrement = keyIncrement + 1
        else:
            completeCipherText.append(ind_char)
 
    return ''.join(completeCipherText)

    

def main():
    text = input("Type a message:")
    rot = input("Rotate by:")
    print(encrypt(text,rot))

if __name__ == "__main__":
     main()

