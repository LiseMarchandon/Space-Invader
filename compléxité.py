def Selection(liste,n):
    for i in range(0,n):
        petit = liste[i]
        j = i
        for k in range(i+1,n):
            if liste[k] < petit:
                j = k
                petit = liste[k]
        tmp = liste[j]
        liste[j] = liste[i]
        liste[i] = tmp

def Bulle(liste,n):
    for i in range()


tableau = [1,2,3,4,5,6,7]
print(Selection(tableau,7))

log (2n)
