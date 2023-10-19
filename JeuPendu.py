import random
from unidecode import unidecode

class Pendu:
  def __init__(self):
    """
    Entrées: self
    Sorties: self, self.mot_secret, self.compteur_erreurs, self.mot_devoile
    Role: Initialise une instance du jeu Pendu
    """
    self.mot_secret = self.get_random_word().upper()
    # print(unidecode(self.mot_secret))
    # self.mot_secret = input("Votre mot: ").upper()
    self.compteur_erreurs = 0
    self.mot_devoile = ["_"] * len(self.mot_secret)
    self.affiche_mot()

  def get_random_word(self):
    return unidecode(random.choice(open('liste_francais.txt').readlines()))

  def affichage_dessin(self):
    """
    Entrées: self
    Sorties: 
    Rôle: Affiche le dessin du pendu en fonction du nombre d'erreurs
    """
    etapes = {
        0: "",
        1: "\n" * 8 + "------------------",
        2: "  |    \n" * 8 + "------------------",
        3: "  _______     \n" + "  |\n" * 8 + "------------------",
        4: "  _______     \n" + "  |/\n" + "  |\n" * 7 + "------------------", 
        5: "  _______     \n" + "  |/    |\n" + "  |     |\n" + "  |\n" * 6 + "------------------",
        6: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n" + "  |\n" * 5 + "------------------",
        7: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n"+ "  |    /|\    \n" + "  |\n" * 4 + "------------------",
        8: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n"+ "  |    /|\    \n" +  "  |     |\n" + "  |\n" * 3  + "------------------",
        9: "  _______     \n" + "  |/    |\n" + "  |     |\n"+ "  |     O    \n"+ "  |    /|\    \n" +  "  |     |\n" + "  |    / \    \n"  + "  |\n" * 2  + "------------------"
    }
    if 0 <= self.compteur_erreurs <= 9:
      print(etapes[self.compteur_erreurs])
    print("Erreurs: ", self.compteur_erreurs)

  def affiche_mot(self):
    """
    Entrées: self.mot_devoile
    Sorties: 
    Rôle: Affiche le mot dévoilé
    """
    for l in self.mot_devoile:
      print(l + " ", end="")
    print("\n")
    # for lettre in range(len(self.mot_devoile)):
    #   print(self.mot_devoile)

  def verifie(self, lettre):
    """
    Entrées: - self
              - lettre, la lettre à vérifier
    Sorties: Aucune
    Rôle: Vérifie si la lettre est dans le mot à trouver
      Si non, augmente le compteur d'erreurs
      Si oui, vérifie si la lettre a dèjà été dite: en redemande une
        Change le mot dévoilé en dévoilant la lettre trouvée
    """
    if lettre in self.mot_secret:
      pass
    else:
      self.compteur_erreurs += 1

  def tour(self):
    lettre = input("Choisir une lettre: ").upper()
    self.verifie(lettre)
    self.affichage_dessin()
    self.affiche_mot()

    return self.mot_devoile == self.mot_secret

    # self.affichage_dessin()

  def partie(self):
    pass
        
jeu = Pendu()
jeu.tour()
jeu.tour()
jeu.tour()
jeu.tour()
jeu.tour()
# print(jeu.get_random_word())