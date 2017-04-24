datatxt = open("data.csv", 'a')

name = raw_input("name: ")
age = raw_input("age: ")
namelist = name.split(' ')

datatxt.write(','.join(namelist[::-1]) + "," + age + '\n')

datatxt.close()
