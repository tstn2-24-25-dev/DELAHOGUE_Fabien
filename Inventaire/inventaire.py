
def lire_data(chemin_fichier):
    with open(chemin_fichier) as f:

        nb_article = f.readline().strip()
        liste_article = f.readlines()
        liste_complete = [nb_article]
        for line in liste_article :
            art = line.strip()
            liste_complete.append(art)
        return (liste_complete)




def affichage(liste_classee):
    for tup in liste_classee:
        print(tup)


def inventaire(chemin_fichier):
    liste_classee = lire_data(chemin_fichier)
    print(liste_classee)
    affichage(liste_classee)


print(inventaire('Inventaire/article.txt'))