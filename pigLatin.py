vowels = "aeiou"

def findIndex(word):
    for i in range(0,len(word)):
        if word[i] in vowels:
            return i

def pigify(word):
    if word[0] in vowels:
        return word + "way"
    else:
        return word[findIndex(word):] + word[:findIndex(word)] + "ay"

def pigLatin(text):
    return ' '.join(map(pigify, text.split()))

text = raw_input("enter a string: ")
print pigLatin(text)
