f = open("data.txt", 'r').read()
newtxt = open("analysis.txt", 'w')

L1 = f.split()
L2 = list(set(L1))

for x in L2:
    newtxt.write(x + ',' + str(L1.count(x)) + '\n')

newtxt.close()
