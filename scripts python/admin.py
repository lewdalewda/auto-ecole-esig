import heures
import eleve
import voiture
import moniteur
from mysql.connector import connect 

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()

class admin:
    def __init__(self):
        self.prop=1
        
    def edit():
        while True:
            choix = int(input("""menu modifications,choisisez ce que vous voulez modifier :
                  1) élèves
                  2) moniteurs
                  3) voitures
                  4) heures
                  5) quitter le menu
                  entrez votre choix """))
            if choix == 1: ## modification données eleve
                cursor.execute("SELECT * FROM eleve")
                res = cursor.fetchall()
                lst =[]
                
                for etu in res:
                    e = eleve.eleve(etu[0],etu[1],etu[2],etu[3],etu[4],etu[5],etu[6])
                    lst.append(e)
                print(lst)
                chx = int(input("entrez id d'éléve"))
                
                for elv in lst:
                    if chx == elv.id:
                        elv.afficher()
                        edi = int(input(""""que voulez vous modifier ?
                                        1)nom et prenom
                                        2)age
                                        3)heures faites/a faire
                                        4)boite manuelle/automatique
                                        5)quiter """))
                        if edi == 1:
                            n = str(input("entrez le nouveau nom (en majuscule) "))
                            p = str(input("entrez le nouveau prenom "))
                            elv.Nom = n
                            elv.Prenom = p
                            elv.modifier()
                            
                        elif edi == 2:
                            a = str(input("entrez le nouveau age "))
                            elv.age = a
                            elv.modifier()
                        
                        elif edi == 3:
                            hc = int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            elv.hdc = hc
                            elv.hdf = hf
                            elv.modifier()
                        
                        elif edi == 4:
                            b = str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                elv.boite = 0
                            elif b == "A":
                                elv.boite = 1
                            else:
                                print("entrée non valide")
                            elv.modifier()
                        
                        elif edi == 5:
                            break
                        
                            
    
            elif choix == 2: ## modification données profs
                cursor.execute("SELECT * FROM prof")
                res = cursor.fetchall()
                lst =[]
                
                for pro in res:
                    p = moniteur.moniteur(pro[0],pro[1],pro[2],pro[3],pro[4],pro[5])
                    lst.append(p)
                print(lst)
                chx = int(input("entrez id de prof "))
                
                for mon in lst:
                    if chx == mon.id:
                        mon.afficher()
                        edi = int(input(""""que voulez vous modifier ?
                                        1)nom et prenom
                                        2)age
                                        3)heures faites/a faire
                                        4)quiter """))
                        
                        if edi == 1:
                            n = str(input("entrez le nouveau nom (en majuscule) "))
                            p = str(input("entrez le nouveau prenom "))
                            mon.Nom = n
                            mon.Prenom = p
                            mon.modifier()
                            
                        elif edi == 2:
                            a = str(input("entrez le nouveau age "))
                            mon.age = a
                            mon.modifier()
                        
                        elif edi == 3:
                            hc = int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            mon.hc = hc
                            mon.hl = hf
                            mon.modifier()
                        
                        elif edi == 4:
                            break
            
            
            elif choix == 3:
                cursor.execute("SELECT * FROM voiture")
                res = cursor.fetchall()
                lst =[]
                
                for voi in res:
                    v = eleve.eleve(voi[0],voi[1],voi[2],voi[3],voi[4],voi[5],voi[6],voi[7])
                    lst.append(v)
                print(lst)
                chx = int(input("entrez id de voiture"))
                
                for elv in lst:
                    if chx == elv.id:
                        elv.afficher()
                        edi = int(input(""""que voulez vous modifier ?
                                        1)nom 
                                        2)annee
                                        3)capacité
                                        4)kilometrage
                                        5)hpw
                                        6)lstd
                                        7)boite
                                        5)quiter """))
                        if edi == 1:
                            n = str(input("entrez le nouveau nom (en majuscule) "))
                            p = str(input("entrez le nouveau prenom "))
                            elv.Nom = n
                            elv.Prenom = p
                            elv.modifier()
                            
                        elif edi == 2:
                            a = str(input("entrez le nouveau age "))
                            elv.age = a
                            elv.modifier()
                        
                        elif edi == 3:
                            hc = int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            elv.hdc = hc
                            elv.hdf = hf
                            elv.modifier()
                        
                        elif edi == 4:
                            b = str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                elv.boite = 0
                            elif b == "A":
                                elv.boite = 1
                            else:
                                print("entrée non valide")
                            elv.modifier()
                        
                        elif edi == 5:
                            break
            
            elif choix ==4:
                print("zut")
            
            
            elif choix == 5:
                break
        
admin.edit()
