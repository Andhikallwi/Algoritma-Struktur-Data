from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil= [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if  n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n % 2) == 1:
                if(n % 3) != 0:
                    if(n % 5) != 0:
                        return True
                else:
                    return False