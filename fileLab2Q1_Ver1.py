txtfile = raw_input("read: ")
txt = open(txtfile, 'r')

longestword = ''
newtxt = map(lambda s: s.strip('!?.,;:'), txt.read().split())

def new_longestword(word):
    global longestword
    if len(word) > len(longestword):
        longestword = word

map(new_longestword, newtxt)

print longestword
