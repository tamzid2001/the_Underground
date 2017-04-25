txtfile = raw_input("read: ")
txt = open(txtfile, 'r')

def greater_word(word1, word2):
    if len(word1) > len(word2):
        return word1
    else:
        return word2

print reduce(greater_word, txt.read().split())
