a = raw_input("numbers, plz: ")
b = ' '
output = 0
count = 0

for x in a:
    if x == ',':
        count = count + 1
        output = output + float(b)
        b = ' '
    else:
        count = count + 1
        b = b + x

if count == len(a):
    output = output + float(b)

print output
