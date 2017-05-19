#PART 2
def hasUniqueValues(d):
    return len(set(d.values())) == len(d.values())

#PART 3
def addReverseDictionary(d):
    for key in d.keys():
        d[d[key]] = key

#PART 4
import random
import copy
pref = dict()
names = ['Sally', 'Ivory', 'Sam', 'Sue', 'Kim', 'Rob', 'Tom', 'Quin','Jose','Ying', 'Jill']
schools = ['Stuy', 'BronxSci', 'BklynTech'] 
for name in names:
   L = copy.copy(schools)
   random.shuffle(L)
   pref[name ] = L

#a.
for key in pref:
    print key, pref[key]

#b.
L = [ ]
for key in pref:
    L.append(pref[key][0])
m = max(set(L), key = L.count)
print ', '.join(set(filter(lambda x: L.count(x) == L.count(m), L)))

#c.
print "Stuy, count:", L.count('Stuy')

#d.
print "Jill, 2nd pref:", pref['Jill'][1]

#e.
x = min(set(L), key = L.count)
for key in pref:
    pref[key].remove(x)
print "new dict:", pref
