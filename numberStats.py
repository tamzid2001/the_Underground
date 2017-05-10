import orderedList
f = map(int, open("numbers.txt", 'r').read().split())

print "max:", max(f)
print "min:", min(f)
print "average:", sum(f) / float(len(f))

#assuming No Modes means 2+ different #s of equal freq
freq = map(lambda x: f.count(x), f)
modes = orderedList.orderedList(filter(lambda x: f.count(x) == max(freq), f))
modes = modes[0] if modes[0] == modes[-1] else "No Modes"
print "mode:", modes
