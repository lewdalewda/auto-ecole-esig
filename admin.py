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
            if choix == 1:
                cursor.execute("SELECT * FROM eleve")
                res = cursor.fetchall()
                lst =[]
                
                for etu in res:
                    print(etu)
                    e = eleve.eleve(etu[0],etu[1],etu[2],etu[3],etu[4],etu[5],etu[6])
                    lst.append(e)
                print(lst)
                chx = int(input("entrez id d'éléve"))
                
                for elv in lst:
                    if chx == elv.id:
                        elv.afficher()
            
            
            elif choix == 2:
                print("zut")
            
            
            elif choix == 3:
                print("zut")
            
            
            elif choix ==4:
                print("zut")
            
            
            elif choix == 5:
                break
        
admin.edit()