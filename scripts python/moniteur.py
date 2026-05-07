from mysql.connector import connect 

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()


class moniteur :
    def __init__(self,id,Nom,Prenom,age,hc,hl):
        self.id=id
        self.Nom=Nom
        self.Prenom=Prenom
        self.age=age
        self.hc=hc
        self.hl=hl
        
    def afficher(self):
        print(self.id, self.Nom, self.Prenom, self.age, self.hc, self.hl)
      
    
    
    def ajouter(self): #works
        sql = "INSERT INTO prof(pro_id, pro_nom, pro_prenom, pro_age, pro_heurescas, pro_heureslbr) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.id, self.Nom, self.Prenom, self.age, self.hc, self.hl))
        bdd.commit()
    
    def modifier(self): #works
        sql = """UPDATE prof
        SET pro_nom = %s,
        pro_prenom = %s,
        pro_age = %s,
        pro_heurescas = %s,
        pro_heureslbr = %s
        WHERE pro_id = %s """
        cursor.execute(sql,(self.Nom, self.Prenom, self.age, self.hc, self.hl, self.id))
        bdd.commit()
        
    def suprimer(): #works
         
        i = int(id)  
        print(i)
        sql = "DELETE FROM prof WHERE pro_id = %s"
        cursor.execute(sql,(i,))
        bdd.commit()

#p = moniteur(3,"GERAUT","Athalia",20,20,10)
##p.ajouter()
#p.age = 25
#p.modifier()
##moniteur.suprimer()
##bdd.close()
