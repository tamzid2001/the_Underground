def collapseWord(word):
    output = ' '
    temp = word[0]
    
    for i in range(1, len(word)):
        if word[i] == temp[0]:
            temp += word[i]
        else:
            output += temp[0]
            temp = word[i]

    return output + temp[0]

a = raw_input("enter a string: ")

print collapseWord(a)
