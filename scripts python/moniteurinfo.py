from mysql.connector import connect 

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()

prenom = str(input("entrer votre prenom "))
nom  = str(input("entrer votre Nom ")) 

class moniteurinfo :
    def __init__(self,prenom,nom):
        self.prenom=prenom
        self.nom=nom
        
    def selectinfo(prenom,nom):
        cursor.execute("SELECT * FROM prof WHERE pro_nom = %s and pro_prenom = %s", (nom,prenom))
        resultat = cursor.fetchall()
        if len(resultat) == 0 :
            print("il n'existe pas")
        else : 
            for prof in resultat:
                id, nom, prenom, age, heurescas, heureslbr = prof
                print(id, nom, prenom, age, heurescas, heureslbr)
        
 
moniteurinfo.selectinfo(prenom,nom)
