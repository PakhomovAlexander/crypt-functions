from DiffieHellman import get_gamma, get_ab, get_key
from CezarGamma import encode, decode
from Functions import pow_h, gcd, phi
import random as rnd

p = 54709
g = 23113 #из поля Zp
x = 1 #из {1, ..., P-1}

y = 25058 #g^x (mod p) pow_h(g,x,p)

while y != pow_h(g,x,p):
    x += 1

print(x)

a = 926 #g^k (mod p)
b = 16005 #Qy^k (mod p)


#Result
tmp = pow_h(a,x,p)

tmp1 = 1
while tmp1*tmp % p != 1:
    tmp1 += 1

Q = (b * tmp1) % p # b(a^x)^-1 (mod p)

text = 'ФСЙОЩГМПА'
decoded = decode(text, [3,2,4,4,7])

print (decoded) # СПЕКТАКЛЬ