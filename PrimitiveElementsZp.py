def count_primitives(p, i):
    for j in range(1, p):
        flag = True
        for m in range(1, p - 1):
            if (j ** m) % p == 1:
                flag = False
                break
        if flag:
            print(j)
            i += 1
    return i


p = 97
i = 0
count = count_primitives(p, i)
print("count =", count)
