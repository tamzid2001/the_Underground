import math
n = int(raw_input(": "))
pi = math.pi

for i in range(n):
    print format(pi, '.{}f'.format(i))
