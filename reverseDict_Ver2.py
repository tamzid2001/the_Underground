def reverseDict_Ver2(d):
    d2 = dict(d)
    for key in d2:
        d[d[key]] = key
        d.pop(key)

phonebook = {'Jane': '718-4211'}
phonebook['Albert'] = '343-2342'
phonebook['Sara'] = '231-8976'

reverseDict_Ver2(phonebook)
print phonebook
