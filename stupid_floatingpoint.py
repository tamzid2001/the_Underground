x = float(raw_input(": "))

bin_x = ''
while(x != 1):
    if x * 2 > 1:
        bin_x += '1'
        x = x * 2 - int(x * 2)
    else:
        bin_x += '0'
        x *= 2
bin_x = bin_x[:-1] + '1'

output = [ ]
for i in range(len(bin_x)):
    if bin_x[i] == '1':
        output.append('1/' + str(2 ** (i + 1)))

print output
