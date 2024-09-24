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
    i = 0
    m = 0
    while (i <= len(tab)-2):
        if tab[i] > tab[i+1]:
            m = tab[i+1]
            tab[i+1] = tab[i]
            tab[i] = m

        if(tab[i-1] > tab[1]):
            m = tab[i]
            tab[i] = tab[i-1]
            tab[i-1] = m
            i = i+1

        else:
            i+= 1

    return(tab)



    # m = 0
    # for i in range(len(tab)-1):
    #     if tab[i] > tab[i+1]:
    #         m = tab[i+1]
    #         tab[i+1] = tab[i]
    #         tab[i] = m
            
    # return (tab)

print(triSelection(tab))