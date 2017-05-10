L = ['arg', 'arg', 'arg']
#['a', 'b', 'c']

newL = []

def numbered(L):
    for i in range(len(L)):
        newL.append(L[i] + str(i))
    return newL

print numbered(L)
