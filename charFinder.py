a = raw_input("string, plz: ")
b = raw_input("char, plz: ")
count = 0
occ = False

for x in a:
    if b == x:
        print count
        occ = True
    else:
        count = count + 1

if not(occ):
    print "no occurences"
