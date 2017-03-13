n = int(raw_input("positive int, plz: "))
d = n
count = 0

while(d > 1):
    if n % d == 0:
        print d, "is a divisor of", n
        d = d - 1
        count = count + 1
    else:
        d = d - 1

print "1 is a divisor of", n

if count == 1:
    print n, "is a prime number"
