txtfile = raw_input("read: ")
txt = open(txtfile, 'r')

total_length = 0
word_count = 0

for line in txt:
    for word in line.split():
        total_length += len(word)
    word_count += len(line.split())

print total_length / word_count
