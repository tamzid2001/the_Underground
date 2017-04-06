def islucky(n):
    return not("13" in str(n))

def findluckynumbers(a, b):
    return filter(islucky, range(a, b))

n = int(raw_input(": "))
print islucky(n)

#a = int(raw_input("0: "))
#b = int(raw_input("1: "))
#print findluckynumbers(a, b)
