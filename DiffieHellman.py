m = 41903
q = 10109
x = 38421
y = 14092
# k - ?
txt = "ВСУПНХЧХУАУСПЗ"


def get_key(m, b, x):
    return (x ** b) % m


def get_b(q, m, y):
    qq = q
    b = 1
    while y != qq % m:
        b += 1
        qq *= q

    return b

def get_ab(m,q,x,y):
    return (get_b(q, m, x), get_b(q, m, y))

def get_gamma(key):
    arr = []
    for i in str(key):
        arr.append(int(i))
    
    return arr


#print(get_b(q, m, y))

#print(get_gamma(m, 17809, x))


