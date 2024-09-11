
def inventaire(chemin_fichier):
    with open(chemin_fichier) as f:
        print(f.readline())
    return f.readline


inventaire('DELAHOGUE_Fabien/DELAHOGUE_Fabien/Inventaire/article.txt')