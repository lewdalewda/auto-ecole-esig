
from mysql.connector import connect 

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()


class eleve :
    def __init__(self,id,Nom,Prenom,age,hdc,hdf,boite):
        self.id=id
        self.Nom=Nom
        self.Prenom=Prenom
        self.age=age
        self.hdc=hdc
        self.hdf=hdf
        self.boite=boite
        
    def afficher(id):
        i= int(id)
        cursor.execute("SELECT * FROM eleve WHERE elv_id = %s", (i,))
        res = cursor.fetchall()
        
        return(res)
            
    
    
    def ajouter(self): ## 
        sql = "INSERT INTO eleve(elv_id, elv_nom, elv_prenom, elv_age, elv_heuresfts, elv_heuresrest, elv_boite) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.id, self.Nom, self.Prenom, self.age, self.hdc, self.hdf, self.boite))
        bdd.commit()
    
    def modifier(self): #works
        sql = """UPDATE eleve
        SET elv_nom = %s, 
        elv_prenom = %s, 
        elv_age = %s, 
        elv_heuresfts = %s, 
        elv_heuresrest = %s, 
        elv_boite = %s
        WHERE elv_id = %s"""
        cursor.execute(sql,(self.Nom, self.Prenom, self.age, self.hdc, self.hdf, self.boite,self.id))
        bdd.commit()
        
    def suprimer(id): #works
            i = int(id)  
            print(i)
            sql = "DELETE FROM eleve WHERE elv_id = %s"
            cursor.execute(sql,(i,))
            bdd.commit()
