from itertools import combinations_with_replacement
def gen (n):
    lst = []
    while n >= 1:
        comb = combinations_with_replacement(['A', 'T', 'G', 'C'], n)
        n -= 1
        for i in list(comb):
            lst.append(i)
    print(*lst)
gen(2)
