f = open("jungle.txt", 'r').read()
newtxt = open("madLibsJungle.txt", 'w')

animal = raw_input("animal: ")
food = raw_input("food: ")
city = raw_input("city: ")

coding = {"{animal}": "{0}", "{food}": "{1}", "{city}": "{2}"}

for k,v in coding.items():
    f.replace(k,v)

newtxt.write(f.format(animal = animal, food = food, city = city))

newtxt.close()
