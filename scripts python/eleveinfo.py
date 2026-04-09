from mysql.connector import connect 

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()

prenom = str(input("entrer votre prenom "))
nom  = str(input("entrer votre Nom ")) 

class eleveinfo :
    def __init__(self,prenom,nom):
        self.prenom=prenom
        self.nom=nom
        
    def selectinfo(prenom,nom):
        cursor.execute("SELECT * FROM eleve WHERE elv_nom = %s and elv_prenom = %s", (nom,prenom))
        resultat = cursor.fetchall()
        if len(resultat) == 0 :
            print("il n'existe pas")
        else : 
            for eleve in  resultat:
                id, nom, prenom, age, heuresfts, heuresrest, boite = eleve 
                print(id, nom, prenom, age, heuresfts, heuresrest, boite)
        
 
eleveinfo.selectinfo(prenom,nom)
