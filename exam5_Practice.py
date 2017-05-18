def hasUniqueValues(d):
    return len(set(d.values())) == len(d.values())

def addReverseDictionary(d):
    d2 = dict()
    for key in d:
        d2[d[key]] = key
    d.update(d2)

import random
import copy
pref = {}
names = ['Sally', 'Ivory', 'Sam', 'Sue', 'Kim', 'Rob', 'Tom', 'Quin','Jose','Ying', 'Jill']
schools = ['Stuy', 'BronxSci', 'BklynTech'] 
for name in names:
   L = copy.copy(schools)
   random.shuffle(L)
   pref[name ] = L

for key in pref:
    print key
    for school in pref[key]:
        print school

L = [ ]
for key in pref:
    L.append(pref[key][0])
print max(set(L), key = L.count)

print L.count('Stuy')

print pref['Jill'][1]

for key in pref:
    pref[key].remove(min(set(L), key = L.count))
print pref
