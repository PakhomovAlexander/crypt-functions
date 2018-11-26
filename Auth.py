from DiffieHellman import get_gamma, get_ab, get_key
from CezarGamma import encode, decode
from Functions import pow_h, gcd, phi

p = 33107
q = 16553
g = 2902
y = 9107
r = 32607

e1 = 15776
s1 = 9856

e2 = 490
s2 = 8108

e3 = 9987
s3 = 7309

e4 = 155
s4 = 1267

print(r == (g ** s1) * (y ** e1) % p)
print(r == (g ** s2) * (y ** e2) % p)
print(r == (g ** s3) * (y ** e3) % p)
print(r == (g ** s4) * (y ** e4) % p)
