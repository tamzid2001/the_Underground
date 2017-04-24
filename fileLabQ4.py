datatxt = open("data.csv", 'r')
max_age = None
eldest = None

for line in datatxt:
    if int(line.split(',')[-1]) > max_age:
        eldest = ' '.join((line.split(',')[:2])[::-1])
        max_age = int(line.split(',')[-1])

print "eldest:", eldest
