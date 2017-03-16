a = int(raw_input("enter first number: "))
b = int(raw_input("enter second number: "))
isDivisor = lambda n,x: n % x == 0

for n in range(a,b):
    total = 0
    for x in range(1,n):
        if isDivisor(n,x):
            total += x
    if total == n:
        print n, "is a perfect number"
