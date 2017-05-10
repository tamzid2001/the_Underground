L = ['a', 'c', 'd', 'c', 'b']
#[4, 3, 5, 4, 3, 5, 5]

def orderedList(L):
    return sorted(set(L))[::-1]

print orderedList(L)
