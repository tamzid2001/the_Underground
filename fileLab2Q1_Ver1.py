txtfile = raw_input("read: ")
txt = open(txtfile, 'r')

longestword = ''

def new_longestword(word):
    global longestword
    if len(word) > len(longestword):
        longestword = word

for line in txt:
    map(new_longestword, line.split())

print longestword
