txt = open("gpa.txt", 'r')

def num(x):
    if 'A' in x: return 4
    if 'B' in x: return 3
    if 'C' in x: return 2
    if 'D' in x: return 1
    else: return 0

for line in txt:
    L = line.split(',')
    name = ' '.join((L[:2])[::-1])
    gpa = round(sum(map(num, L[2:])) / float(len(L[2:])), 2)
    print name + ',', gpa, ('*' if gpa > 3.75 else '')
