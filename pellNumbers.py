def pelli(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return 2 * pelli(n - 1) + pelli(n - 2)

L = [0, 1]
def pelliDynamic(n):
    if n < len(L):
        return L[n]
    L.append(2 * pelliDynamic(n - 1) + pelliDynamic(n - 2))
    return L[n]

n = int(raw_input(": "))
print pelliSeq(n)
