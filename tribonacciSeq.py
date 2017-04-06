def tribi(n):
    if n < 4:
        return 1
    return tribi(n - 3) + tribi(n - 2) + tribi(n - 1)

n = int(raw_input(": "))
print tribi(n)
