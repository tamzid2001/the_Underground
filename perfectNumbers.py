n = int(raw_input("enter a number: "))
isDivisor = lambda n,x: n % x == 0
total = 1

for x in range(2,n):
    if isDivisor(n,x):
        total += x

if total == n:
    print n, "is a perfect number"
else:
    print n, "is not a perfect number"
