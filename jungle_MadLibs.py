f = open("jungle.txt", 'r').read()
newtxt = open("madLibsJungle.txt", 'w')

animal = raw_input("animal: ")
food = raw_input("food: ")
city = raw_input("city: ")

newtxt.write(f.format(animal = animal, food = food, city = city))
newtxt.close()
