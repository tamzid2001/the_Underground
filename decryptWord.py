letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = raw_input("ciphertext: ")
decipher = raw_input("decipher: ").upper()

if decipher == "CAESAR":
    shift = -3
elif decipher == "ROT13":
    shift = -13
else:
    print "invalid input"
    shift = 0

def find(char, word):
    for i in range(0,len(word)):
        if letters[i] == char:
            return i

def encryptOne(char):
    return letters[find(char,letters) + shift]

def encryptWord(cipher,shift):
    output = ''
    for char in cipher:
        output += encryptOne(char)
    return output

print encryptWord(cipher.upper(),shift)
