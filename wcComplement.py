def wcComplement(dna):
    newDna = ''
    
    for b in dna:
        if b == 'A':
            newDna += 'T'
        elif b == 'T':
            newDna += 'A'
        elif b == 'G':
            newDna += 'C'
        elif b == 'C':
            newDna += 'G'

    output = ''

    for x in newDna:
        output = x + output

    return output

dna = raw_input("enter sequence: ")

print wcComplement(dna)
