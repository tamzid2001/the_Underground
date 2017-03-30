letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = raw_input("plaintext: ")
cipher = raw_input("cipher: ").upper()
shift = 0

if cipher == "CAESAR":
    shift = 3
elif cipher == "ROT13":
    shift = 13

def find(char, word):
    for i in range(0,len(word)):
        if letters[i] == char:
            return i

def encryptOne(char):
    return letters[(find(char,letters) + shift) % 26]

def encryptWord(plaintext,shift):
    output = ''
    for char in plaintext:
        output += encryptOne(char)
    return output

print encryptWord(plaintext.upper(),shift)
