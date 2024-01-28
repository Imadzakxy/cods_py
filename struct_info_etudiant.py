#!/usr/bin/python3
##############
def informations():
    class etudiant:
        def __init__(self, nom, p_nom, sec,grp, matr):
            self.nom = nom
            self.p_nom = p_nom
            self.sec = sec
            self.grp=grp
            self.matr = matr

    liste_etudiants = []

    while True:
        n = input("Entrer le nombre d'étudiants : ")
        try:
            n = int(n)
            if n > 0:
                break
            else:
                print("Le nombre d'étudiants doit être supérieur à 0.")
        except ValueError:
            print("Nombre incorrect !")

    for i in range(n):
        print(f"\nÉtudiant numéro {i+1}:")
        nom = input("Nom : ")
        p_nom = input("Prénom : ")
        
        while True:
            sec = input("Section : ")
            if sec.lower()=="a" or sec.lower()=="b" or sec.lower()=="c":
                break
            else:
                print("section introuvable!")
                
        while True:
            grp=input("groupe : ")
            try:
                grp=int(grp)
                if grp>0 and grp<=4:
                    break
                else:
                    print("groupe incorrect !")    
            except:
                print("groupe incorrect !")
                
        while True:
            matr = input("Matricule : ")
            try:
                matr = int(matr)
                if matr > 0:
                    break
                else:
                    print("Matricule incorrect !")
            except:
                print("Matricule incorrect !")

        etudiants = etudiant(nom, p_nom, sec,grp,matr)
        liste_etudiants.append(etudiants)
        
    for i,etudiants in enumerate(liste_etudiants):
        print("-------------------------------------------")
        print(f"***Informations pour l'étudiant numéro {i+1}***")
        print(f"\t\tNom : {etudiants.nom}")
        print(f"\t\tPrénom : {etudiants.p_nom}")
        print(f"\t\tSection : {etudiants.sec}")
        print(f"\t\tgroupe:{etudiants.grp}")
        print(f"\t\tMatricule : {etudiants.matr}")
##########
informations()
############