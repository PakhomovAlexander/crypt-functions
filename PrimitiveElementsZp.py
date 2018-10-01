p = 37
i = 0

for j in range(1, 37):
    flag = True
    for m in range(1, 36):
        if (j ** m) % 37 == 1:
            flag = False
            break
    if flag:
        print(j)
        i += 1

print("count =", i)
