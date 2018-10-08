# A и B шифруют сообщения без передачи ключа каждая бука шифрутся ее номером в Алфавите + 9
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
P = 62_923_926_601
b = 678_433

m1 = 2_146_916_375
m3 = 34_979_060_413


def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module

    return r

def get_x(a, b, m):
    (x0, y0, d) = bezout(b, m)


def bezout(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)


# def extd_evklid(a, b, c):
#     r1 = a
#     r2 = b
#     x1 = 1
#     x2 = 0
#     r = r1−(q∗r2)
#     while r != 0:
#         q = r1 // r2
#         r = r1−(q∗r2)
#         r1 = r2
#         r2 = r
#         x = x1−(q∗x2)
#         x1 = x2
#         x2 = x
#
#     return  (r1, x1)

def gcd(a, b):
    while b:
        a, b=b, a%b
    return a

def phi(a):
    b=a-1
    c=0
    while b:
        if not gcd(a,b)-1:
            c+=1
        b-=1
    return c

def decode_text(m):
    decoded = str(m)
    first = ""
    second = ""
    word = []

    for ch in decoded:
        ind = decoded.index(ch)
        if ind % 2 == 0:
            first = ch
        else:
            second = ch
            pos = int(first + second) - 10
            word.append(alphabet[pos])

    return word


# b1 = get_beta(b, P - 1)
b1 = 48820618897

# m2 = (m1 ** b1) % P


m2 = 40880130890

# print(m2)

m4 = pow_h(m3, b1, P)
# m4 = 48820618897

# print(m4)
print(decode_text(m4))
# print(pow_h(b, phi(P-1), P - 1))