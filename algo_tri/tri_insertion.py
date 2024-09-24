tab = [4,8,2,10,1,9,7,6,3,5]

def triInsertion(tab):
    for i in range(1, len(tab)):
        m = tab[i]
        j = i - 1

        while j >= 0 and tab[j] > m:
            tab[j + 1] = tab[j]  
            j -= 1

        tab[j + 1] = m
    return tab 
print(triInsertion(tab))