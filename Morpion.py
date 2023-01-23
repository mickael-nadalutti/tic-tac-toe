"""
       0     1     2
    ┏━━━━━┳━━━━━┳━━━━━┓
 0  ┃  _  ┃  _  ┃  _  ┃
    ┣━━━━━╋━━━━━╋━━━━━┫
 1  ┃  _  ┃  _  ┃  _  ┃
    ┣━━━━━╋━━━━━╋━━━━━┫
 2  ┃  _  ┃  _  ┃  _  ┃
    ┗━━━━━┻━━━━━┻━━━━━┛
"""
import random
import time

def afficherGrille():
    """None -> None
        Affiche la grille de jeu"""
    print("       0     1     2\n"
          "    ┏━━━━━┳━━━━━┳━━━━━┓\n"
          " 0  ┃  "+grille[0][0]+"  ┃  "+grille[0][1]+"  ┃  "+grille[0][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 1  ┃  "+grille[1][0]+"  ┃  "+grille[1][1]+"  ┃  "+grille[1][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 2  ┃  "+grille[2][0]+"  ┃  "+grille[2][1]+"  ┃  "+grille[2][2]+"  ┃\n"
          "    ┗━━━━━┻━━━━━┻━━━━━┛\n")

def placerSymbole(ligne, col, symbole):
    """int x int x str -> None
       Place le symbole dans la case dite"""
    grille[ligne][col] = symbole
    lstCasesLibres.remove((ligne,col))

def ifCaseLibre(ligne, col):
    """int x int -> Bool
       Vérifie si la case est libre"""
    if(grille[ligne][col]) == "_":
        return True
    return False

def afficherSeparateur():
    """None -> None
       Affiche une ligne de séparation"""
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def verifVictoire(symbole):
    """str -> Bool
       Renvoie True si trois symboles sont alignés"""

    for i in grille: # Cas où une ligne est alignée
        if i == [symbole for _ in range(3)]:
            return True

    for i in range(3): # Cas où une colonne est alignée
        lst = []
        for k in grille:
            lst.append(k[i])
        if lst == [symbole for _ in range(3)]:
            return True

    # Cas où une des deux diagonale est alignée
    if grille[0][0] == grille [1][1] == grille[2][2] == symbole\
            or grille[2][0] == grille[1][1] == grille[0][2] == symbole:
        return True
    return False

Rejouer = "O"
Joueur1 = {"prenom" : "", "symbole" : "X"}
Joueur2 = {"prenom" : "", "symbole" : "O"}

afficherSeparateur()
print("Bienvenue dans le jeu du morpion !\n"
      "Règles du jeu :\n"
      "Pour gagner, il faut que vous aligner trois de vos symboles :\n"
      "  - Sur une même ligne\n"
      "  - Sur une même colonne\n"
      "  - Sur une même diagonale\n")
afficherSeparateur()

while Rejouer == "O":
    grille = [["_" for _ in range(3)] for _ in range(3)]
    lstCasesLibres = [(x,y) for x in range(3) for y in range(3)]
    Joueur1['prenom'] = input("Entrez le prénom du joueur 1 : ")
    Joueur2['prenom'] = input("Entrez le prénom du joueur 2 : ")
    afficherSeparateur()
    print(Joueur1['prenom'],"tu joueras les X")
    print(Joueur2['prenom'],"tu joueras les O")
    print("Un tirage au sort va désigner le premier joueur...")
    JoueurActuel = random.choice([Joueur1, Joueur2])
    time.sleep(2)
    afficherSeparateur()
    while True:
        print(JoueurActuel['prenom']," à ton tour !")
        afficherGrille()
        while True :
            while True :
                ligne = int(input("Quelle ligne souhaites-tu jouer ? "))
                if ligne not in [0, 1, 2]:
                    print("/!\ Cette ligne n'existe pas !")
                else:
                    break
            while True :
                col = int(input("Quelle colonne souhaites-tu jouer ? "))
                if col not in [0,1,2]:
                    print("/!\ Cette colonne n'existe pas !")
                else :
                    break
            if ifCaseLibre(ligne, col):
                break
            else :
                 print("/!\ Cette case est déjà remplie !")

        placerSymbole(ligne, col, JoueurActuel['symbole'])
        afficherSeparateur()
        if verifVictoire(JoueurActuel['symbole']):
            afficherGrille()
            print("Bravo ", JoueurActuel['prenom'], " ! Tu as gagné !")
            break

        if len(lstCasesLibres) == 0:
            afficherGrille()
            print("Égalité ! Toutes les cases ont été remplies !")
            break

        if JoueurActuel == Joueur1:
            JoueurActuel = Joueur2
        else:
            JoueurActuel = Joueur1

    Rejouer = "X"
    while Rejouer not in ["O", "N"]:
        afficherSeparateur()
        Rejouer = input("Souhaitez-vous rejouer ? [O/N] ")

    if Rejouer == "N":
        break

afficherSeparateur()
print("Merci d'avoir joué !")
afficherSeparateur()