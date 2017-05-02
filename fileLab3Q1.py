txtfile = raw_input("read: ")
txt = open(txtfile, 'r')

print list(set(map(int, txt.read().split(','))))
