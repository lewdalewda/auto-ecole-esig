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
        
    def ajouter(self):
        sql = "INSERT INTO eleve(elv_id, elv_nom, elv_prenom, elv_age, elv_heuresfts, elv_heuresrest, elv_boite) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.id, self.Nom, self.Prenom, self.age, self.hdc, self.hdf, self.boite))
        bdd.commit()
    
    def modifier(self):
        sql = """UPDATE eleve
        SET elv_id = %s, 
        elv_nom = %s, 
        elv_prenom = %s, 
        elv_age = %s, 
        elv_heuresfts = %s, 
        elv_heuresrest = %s, 
        elv_boite = %s,
        WHERE elv_id = %s"""
        cursor.execute(sql,(self.id, self.Nom, self.Prenom, self.age, self.hdc, self.hdf, self.boite,self.id))
        bdd.commit()
        
    def suprimer():
        
        while True:
            choix = int(input("choisisez id 1 ou nom 2 "))
            
            if choix == 1:
               
                i = int(input("entrer id à supprimer"))
                
            
            elif choix == 2:
                
                n = str(input("entre le nom (nom en Majuscule) "))
                p = str(input("entre le nom (nom en Majuscule) "))
                
                cursor.execute("select elv_id from eleve where elv_nom = %s and elv_prenom = %s ", (n,p))
                res = cursor.fetchall()
                i = res[0]
                
                
                
            print(i)
            sql = "DELETE FROM eleve WHERE elv_id = %s"
            cursor.execute(sql,(i))
            bdd.commit()
            break        
    
eleve.suprimer()

