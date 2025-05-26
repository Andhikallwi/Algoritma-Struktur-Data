def faktorisasi(n):
    list = []
    loop = 2
    while loop <= n :
        if (n % loop) == 0 :
            n /= loop
            list.append(loop)
        else:
            loop+=1
    return list
print(list)
