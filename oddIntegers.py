n = int(raw_input("positive int, plz: "))
isOdd = lambda n: n % 2 == 1

while(n >= 0):
    if isOdd(n):
        print n
        n = n - 2
    else:
        n = n - 1
