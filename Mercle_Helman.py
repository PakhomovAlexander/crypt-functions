from DiffieHellman import get_gamma, get_ab, get_key
from CezarGamma import encode, decode
from Functions import pow_h

# Для шифрования используется системма дифихелмна, сообщеня на русском языке.
# A = 000001 ,..., Я = 1000000
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

w = [1, 2, 4, 9, 18, 35]
q = 80
r = 29

x = [55, 97, 21, 79, 100, 155]

def merkle_hellman(q, r, w, x):
    w = w[::-1]
    n = len(w)

    r1 = 1
    while r1 * r % q != 1:
        r1 = r1 + 1

    i = 0
    s = []
    while i < n:
        s = s + [x[i] * r1 % q]
        i = i + 1

    result = ""
    i = 0
    while i < n:
        val = 0
        j = 0
        while j < n:
            if s[i] >= w[j]:
                val = val + 2 ** j
                s[i] = s[i] - w[j]
            j = j + 1

        i = i + 1
        result = result + alphabet[val-1]

    return result


print (merkle_hellman(q, r, w, x))