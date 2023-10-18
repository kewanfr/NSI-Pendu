
class Pendu:
    def __init__(self):
        # self.mot_secret = input("Votre mot: ")
        self.compteur_erreurs = 0
        self.mot_devoile = ''

    def affichage_dessin(self):
        etapes = {
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

    def affiche2(self):
        pass

    def verifie(self):
        pass

    def tour(self):
        pass

    def partie(self):
        pass
        
jeu = Pendu()
# jeu.partie()
jeu.affichage_dessin()