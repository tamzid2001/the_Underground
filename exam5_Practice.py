def hasUniqueValues(d):
    return len(set(d.values())) == len(d.values())

def addReverseDictionary(d):
    d2 = dict()
    for key in d:
        d2[d[key]] = key
    d.update(d2)

import random
import copy
pref = dict()
names = ['Sally', 'Ivory', 'Sam', 'Sue', 'Kim', 'Rob', 'Tom', 'Quin','Jose','Ying', 'Jill']
schools = ['Stuy', 'BronxSci', 'BklynTech'] 
for name in names:
   L = copy.copy(schools)
   random.shuffle(L)
   pref[name ] = L

for key in pref:
    print "Name:", key
    for school in pref[key]:
        print school

L = [ ]
for key in pref:
    L.append(pref[key][0])
print "most preferred school:", max(set(L), key = L.count)

print "Stuy, count:", L.count('Stuy')

print "Jill, 2nd pref:", pref['Jill'][1]

for key in pref:
    pref[key].remove(min(set(L), key = L.count))
print "new dict:", pref
