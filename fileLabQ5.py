datatxt = open("data.csv", 'r')
max_age = None
eldest = []

for line in datatxt:
    if int(line.split(',')[-1]) == max_age:
        eldest.append(' '.join((line.split(',')[:2])[::-1]))
    elif int(line.split(',')[-1]) > max_age:
        eldest = []
        eldest.append(' '.join((line.split(',')[:2])[::-1]))
        max_age = int(line.split(',')[-1])

print "eldest:", ', '.join(eldest)
