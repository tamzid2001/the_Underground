wordx = raw_input("word: ")
txtfile = raw_input("read: ")
txt = open(txtfile, 'r')

output = 0

for line in txt:
    for word in line.split():
        if wordx == word:
            output += 1

print output
