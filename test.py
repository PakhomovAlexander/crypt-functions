from DiffieHellman import get_gamma, get_ab, get_key
from CezarGamma import encode, decode
from Functions import pow_h, gcd, phi

# def get_b1(m1, m2, p):
#     b1 = 1
#     while m2 != pow_h(m1, b1, p):
#         b1 += 1
#
#     return b1
#
# p = 49559
# m1 = 11039
# m2 = 31214
# m3 = 14790
#
# b1 = get_b1(m1, m2, p)
# phi_p = 49558
# print(b1)
# assert m2 == pow_h(m1, b1, p)
# m = pow_h(m3, b1, p)
# print(m)

def last_primitiv(p):
    for j in range(1, p):
        flag = True
        for m in range(1, p - 1):
            if (j ** m) % p == 1:
                flag = False
                break
        if flag:
            print(j)
            return j
    return 0


p = 97
last = last_primitiv(p)
print("last =", last)



