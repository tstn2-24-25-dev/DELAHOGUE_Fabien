tab = [4,8,2,10,1,9,7,6,3,5]

def triRapide(tab):
    j = len(tab)
    for i in range(len(tab)-1):
        m = tab[i+1]
        tab[i+1] = tab[j]
        tab[j] = m
        triRapide(tab)
        i = i+1
        j = j-1
    return(tab)
print(triRapide(tab))
