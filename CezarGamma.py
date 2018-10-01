# gamma = [3, 28, 1, 23, 8, 15, 19]
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def shift(char, g):
    return alphabet[(alphabet.index(char) + g) % len(alphabet)]


def decode(text, gamma):
    res = ""
    index = 0

    for c in text:
        res += shift(c, -gamma[index % len(gamma)])
        index += 1

    return res


def encode(text, gamma):
    res = ""
    index = 0

    for c in text:
        res += shift(c, gamma[index % len(gamma)])
        index += 1

    return res


print(decode("ВСУПНХЧХУАУСПЗ", [1, 9, 5, 7, 0]))
