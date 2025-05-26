k = [2,3,5]
for n in range(2,1000):
        if n in k :
                print(n)
        elif(n % 2) == 1:
            if(n % 3) != 0:
                if(n % 5) != 0:
                        print(n)
