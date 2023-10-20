import random
from os import path
# import subprocess
# import sys
# subprocess.call([sys.executable, '-m', 'pip', 'install', "unidecode"])
# from unidecode import unidecode


class Pendu:
  def __init__(self):
    """
    Entrées: - self
    Sorties: 
    Role: Initialise une instance du jeu Pendu
    """
    print("------------- Pendu -------------\n")

    self.mot_secret = self.get_mot() # Récupère le mot secret en majuscule (aléatoire ou demandé à l'utilisateur)
    self.tableau_mot = len(self.mot_secret) * ['_']

    self.compteur_erreurs = 0
    self.mot_devoile = ["_"] * len(self.mot_secret) # Créé le tableau du mot dévoilé
    self.affiche_mot()

  def unidecode(self, input_str):
    """
    Entrées: - self
             - input_str, le texte à décoder
    Sorties: le str décodé
    Rôle: Retire les caractères spéciaux d'une chaine de caractères
    """
    normalMap = {'À': 'A', 'Á': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
             'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'ª': 'A',
             'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
             'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
             'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
             'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
             'Ò': 'O', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
             'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'º': 'O',
             'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U',
             'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
             'Ñ': 'N', 'ñ': 'n',
             'Ç': 'C', 'ç': 'c',
             '§': 'S',  '³': '3', '²': '2', '¹': '1'}
    normalize = str.maketrans(normalMap)
    return input_str.translate(normalize)
    # return unidecode(input_str)

  def get_mot(self):
    """
    Entrées: self
    Sorties: 
    Rôle: Renvoie un mot aléatoire ou un mot demandé à l'utilisateur, en majuscule
    """
    choix_mot = input("Voulez vous choisir votre mot (Y/N): ").upper()
    if choix_mot == "Y":
      return self.unidecode(input("Choisir un mot: ").upper())
    if(path.exists("liste_francais.txt")): # On vérifie si le dictionnaire français est présent
      print("Mot choisi aléatoirement:")
      motrandom = self.unidecode(random.choice(open('liste_francais.txt').readlines()).upper()) # On récupère un mot aléatoire et on lui retire ses accents
      return motrandom[:-1] # On retire le dernier caractère, car cela génère une erreur avec le len
    return self.unidecode(input("Choisir un mot: ").upper()) # Si le dictionnaire n'est pas présent, on demande à l'utilisateur de choisir un mot et on le mets en majuscule

  def affichage_dessin(self):
    """
    Entrées: self
    Sorties: 
    Rôle: Affiche le dessin du pendu en fonction du nombre d'erreurs
    """
    etapes = {
        1: "\n" * 8 + "------------------",
        2: "  |    \n" * 8 + "------------------",
        3: "  _______     \n" + "  |\n" * 8 + "------------------",
        4: "  _______     \n" + "  |/\n" + "  |\n" * 7 + "------------------", 
        5: "  _______     \n" + "  |/    |\n" + "  |     |\n" * 6 + "------------------",
        6: "  _______     \n" + "  |/    |\n" + "  |     |\n" + "  |\n" * 6 + "------------------",
        7: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n" + "  |\n" * 5 + "------------------",
        8: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n"+ "  |    /|\    \n" + "  |\n" * 4 + "------------------",
        9: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n"+ "  |    /|\    \n" +  "  |     |\n" + "  |\n" * 3  + "------------------",
        10: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n"+ "  |    /|\    \n" +  "  |     |\n" + "  |    / \    \n"  + "  |\n" * 2  + "------------------"
    }
    if 1 <= self.compteur_erreurs <= 10:
      print(etapes[self.compteur_erreurs])
    print("Erreurs: ", self.compteur_erreurs)
    

  def affiche_mot(self):
    """
    Entrées: self
    Sorties: 
    Rôle: Affiche le mot dévoilé
    """
    for l in self.mot_devoile:
      print(l + " ", end="") # On affiche chaque lettre suivie d'un espace et on ne saute pas de ligne dans le print avec end=""
    print("\n")

  def verifie(self, lettre):
    """
    Entrées: - self
             - lettre, la lettre à vérifier
    Sorties: 
    Rôle: Vérifie si la lettre est dans le mot à trouver
      Si non, augmente le compteur d'erreurs
      Si oui, vérifie si la lettre a dèjà été dite: en redemande une
        Change le mot dévoilé en dévoilant la lettre trouvée
    """
    if lettre not in jeu.mot_secret.upper():
        jeu.compteur_erreurs += 1
        self.affichage_dessin()
        print("Cette lettre n'est pas dans le mot mystère!")
    else:
        while lettre in jeu.mot_devoile:
            print("Vous avez déjà rentré cette lettre!")
            lettre = input("Entrez une nouvelle lettre! ").upper()
        for nb_lettre in range(len(jeu.mot_secret)):
            # jeu.mot_devoile = ''
            if jeu.mot_secret[nb_lettre] == lettre:
                jeu.mot_devoile[nb_lettre] = lettre
            # for nb_lettre in range(len(jeu.mot_secret)):
            #     jeu.mot_devoile += jeu.tableau_mot[nb_lettre]

  def tour(self):
    lettre = self.unidecode(input("\nChoisir une lettre: ")).upper() # Demande une lettre à l'utilisateur et la mets en majuscule
    self.verifie(lettre) # Vérifie que la lettre est présente dans le mot ou n'a pas déjà été trouvée, augmente le compteur d'erreurs, sinon dévoile la lettre trouvée dans le mot
    self.affiche_mot()

    return self.mot_devoile == [i for i in self.mot_secret] # Si le mot a été trouvé

  def partie(self):
    """
    Entrée :
    Sortie :
    Rôle : Fait tourner la fonction self.tour tant que le compteur d'erreur est inférieur
    à 9, rafraîchit la page et affiche à la fin si l'utilisateur a gagné ou perdu.
    """
    aGagne = False
    while self.compteur_erreurs < 10 and aGagne == False: # compteur_erreurs doit rester
                                                          # inférieur à 10 et aGagne doit
                                                          # rester faux car la partie
                                                          # n'est pas terminée
      aGagne = self.tour() # exécute tour et conserve le booléen dans aGagne

    if aGagne == True: # on regarde la valueur finale entre True et False
      print("Bravo, vous avez gagné !") # si c'est True c'est que l'utilisateur a trouvé la
                                    # réponse
    else:
      print("Vous avez perdu !") # sinon l'utilisateur a perdu.
      print("Le mot était:", self.mot_secret)
        
jeu = Pendu()
jeu.partie()