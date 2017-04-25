wordx = raw_input("word: ")
txtfile = raw_input("read: ").lower()
txt = open(txtfile, 'r')

newtxt = map(lambda s: s.strip('!?.,;:'), txt.read().split())
output = 0

for word in newtxt:
    if word.lower() == wordx:
        output += 1

print output
