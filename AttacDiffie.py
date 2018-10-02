from DiffieHellman import get_gamma, get_ab, get_key
from CezarGamma import encode, decode

# Алиса и боб обмениваются секретными сообщениямичерез гаммирование, для аормирования гаммы они применяэт Алгоритм Диффа Хелмана со следующими параметрами 
m = 41903
q = 10109
x = 11108
y = 35218

a1 = 29026
b1 = 33872

# Алиса назначила Бобу встречу в городе 
city = "ННЛЛЧСШФВ"

city1 = "ФОУВЙЬШУ"

# --------------------------------------------------

x1 = q ** a1 % m
y1 = q ** b1 % m

(a, b) = get_ab(m, q, x, y)

key_A = get_key(m, a, y1)
key_B = get_key(m, b, x1)

g_a = get_gamma(key_A)
g_b = get_gamma(key_B)

decoded_city_A = decode(city, g_a)
print(decoded_city_A)

decoded_city_B = decode(city1, g_b)
print(decoded_city_B)
