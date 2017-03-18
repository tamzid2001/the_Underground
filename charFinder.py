a = raw_input("string, plz: ")
b = raw_input("char, plz: ")
count = 0
occ = True

for x in a:
    if b == x:
        print count
        occ = False
    else:
        count = count + 1

if occ:
    print "no occurences"
