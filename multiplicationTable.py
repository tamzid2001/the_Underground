output = ' '

for row in range(1,11):
    for col in range(1,11):
        output += '  ' * (4 - (len(str(row * col)))) + str(row * col)
    print output
    output = ' '
