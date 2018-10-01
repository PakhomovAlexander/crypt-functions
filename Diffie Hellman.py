m = 41903
q = 10109
x = 38421
y = 14092
# k - ?
txt = "ВСУПНХЧХУАУСПЗ"


def get_gamma(m, b, x):
    return (x ** b) % m


def get_b(q, m, y):
    qq = q
    b = 1
    while y != qq % m:
        b += 1
        qq *= q
    return b


print(get_b(q, m, y))


print(get_gamma(m, 17809, x))


