##factorial.py

def fact_rec(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    if (n < 0):
        return 0
    return n * fact_rec(n - 1)

def fact_it(n):
    if (n < 0):
        return 0
    if (n == 0):
        return 1
