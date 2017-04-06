def fibi(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibi(n - 1) + fibi(n - 2)

n = int(raw_input(": "))
print fibi(n)
