txtfile = raw_input("read: ")
txt = open(txtfile, 'r')

line = 0
word = 0
char = 0

for lines in txt:
    char += len(lines) - 1
    line += 1
    word += len(lines.split())

print "line:", line
print "word:", word
print "char:", char + 1
