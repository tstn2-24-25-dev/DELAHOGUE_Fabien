import io


def associer_valeur(ligne):

    d_lettre_valeur = {}
    liste_score = ligne.split(" ")
    for i in range (0,len(liste_score)-1,2):
        d_lettre_valeur[liste_score[i]]=int(liste_score[i+1])
    return d_lettre_valeur



def calcul_score(mot, valeurs_lettres):
    score = 0
    for i in mot:
        try :
            score += valeurs_lettres[i]
        except:
            score+=0
    return score

def readData(chemin, mode):
    # create a multi-line string and pass it into StringIO
    return io.StringIO('''p 7 r 8 f 7 i 2 m 1 e 3 u 2 s 9 c 3 
primeur
semeur
escrime
frimeur
ruer''')

"""
1: lecture des données
"""
def lire_data(chemin_fichier):
    with readData(None, 'r') as infile:
        ligne_valeurs = infile.readline().strip()
        lettres_valeurs = associer_valeur(ligne_valeurs)

        liste_mots_scores = [] # liste
        for line in infile:
            mot = line.strip() # 1.2
            score = calcul_score(mot, lettres_valeurs) # 2
            t_mot_score = (mot, score) # Création tuple
            liste_mots_scores.append(t_mot_score)
        return liste_mots_scores


"""
3 tri des données
"""
def tri(liste_mots_scores):
    liste_mots_scores.sort(key=lambda a: a[1])
    return liste_mots_scores



"""
4 affichage
"""
def affichage(liste_classee):
    for tup in liste_classee:
        print(tup[0])

"""
Partie principale (0 - scrabble)
"""
def scrabble(chemin_fichier):
    liste_classee = tri(lire_data(chemin_fichier)) # 3
    print(liste_classee)
    affichage(liste_classee) # 4


scrabble('data.txt')