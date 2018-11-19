from DiffieHellman import get_gamma, get_ab, get_key
from CezarGamma import encode, decode
from Functions import pow_h, gcd, phi

# f_p1p2 = p1p2 * (1 - 1/p1) * (1 - 1/p2)

# А и Б обменимаются сообщениями используя гаммирование, для формарования гаммы они применяют алгоритм RSA,

rB = 71361259
b = 74671
m1 = 3942877

text = "ДМТЭЕСХ"


beta = 2
# fi = phi(rB) //todo: написать реализацию phi быструю!!!
fi = 71344240
print(fi)

# while beta * b % fi != 1:
#     beta += 1
#
# print(beta)

beta = 33289711

m2 = pow_h(m1, beta, rB)
print(m2)

print(decode(text, [3,7,7,9,5,0,3,1]))
#БЕЛФАСТ