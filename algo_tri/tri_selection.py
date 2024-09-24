tab = [15,32,10,5,14]
j = 0

def indiceMin (tab,j):
    i = 0
    for i in range (len(tab)):
        if tab[j] > tab[i] :
            j = i  
    
    return (tab[j],j)


print("élément et indice min :", indiceMin(tab,j))


def triSelection(tab):
    
    for i in range(len(tab)):
       m = i
       
       for j in range(i+1, len(tab)):
           
           if tab[m] > tab[j]:
               m = j
                
       v = tab[i]
       tab[i] = tab[m]
       tab[m] = v

    return tab



print(tri_selection(tab))