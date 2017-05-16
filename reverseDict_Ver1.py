def reverseDict_Ver1(d):
    output = {}
    for key in d:
        output[d[key]] = key
    return output

phonebook = {'Jane': '718-4211'}
phonebook['Albert'] = '343-2342'
phonebook['Sara'] = '231-8976'

reversePhonebook = reverseDict(phonebook)
print phonebook
print reversePhonebook
