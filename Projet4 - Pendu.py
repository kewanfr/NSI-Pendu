
class Pendu:
    def __init__(self):
        self.mot_secret = input("Votre mot: ").upper()
        # print(self.mot_secret)
        self.compteur_erreurs = 0
        self.mot_devoile = ["_"] * len(self.mot_secret)
        self.affiche_mot()

    def affichage_dessin(self):
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

    def affiche_mot(self):
        for l in self.mot_devoile:
            print(l + " ", end="")
        print("\n")

    def verifie(self, lettre):
        if lettre in self.mot_devoile:
            return True
        return False

    def tour(self):
        lettre = input("Votre lettre: ").upper()
        if self.verifie(lettre):
            self.affiche_mot()
            self.compteur_erreurs += 1
            return print("Lettre déjà trouvée")
        if lettre in self.mot_secret:
            print("Oui")
            for i in range(len(self.mot_secret)):
                if self.mot_secret[i] == lettre:
                    self.mot_devoile[i] = lettre
        else:
            print("Non")
            self.compteur_erreurs += 1
        self.affiche_mot()


    def partie(self):
        continuer = True
        while self.compteur_erreurs < 9 and continuer:
            self.tour()
            self.affichage_dessin()
            if "_" not in self.mot_devoile:
                print("Gagné !")
                return
        if self.compteur_erreurs >= 9:
            print("Perdu !")
        
jeu = Pendu()
# jeu.partie()
# jeu.affichage_dessin()
# jeu.compteur_erreurs += 9
# jeu.affichage_dessin()
jeu.partie()
# jeu.tour()