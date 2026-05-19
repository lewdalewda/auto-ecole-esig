from mysql.connector import connect 

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()


class voiture :
    def __init__(self,id,Nom,annee,capa,km,hpw,lstd,boite):
        self.id=id
        self.Nom=Nom
        self.annee=annee
        self.capa=capa
        self.km=km
        self.hpw=hpw
        self.lstd=lstd
        self.boite=boite
        
    def afficher(self):
        i= int(id)
        cursor.execute("SELECT * FROM voiture WHERE elv_id = %s", (i,))
        res = cursor.fetchall()
        
        return(res)
      
    
    def ajouter(self): ##work
        sql = "INSERT INTO voiture(car_id, car_nom, car_annee, car_capa, car_km, car_hpw, car_lstd, car_boite) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.id, self.Nom, self.annee, self.capa, self.km, self.hpw, self.lstd, self.boite))
        bdd.commit()
    
    def modifier(self): ##work
        sql = """UPDATE voiture 
        SET car_nom = %s, 
        car_annee = %s, 
        car_capa = %s, 
        car_km = %s, 
        car_hpw = %s,
        car_lstd = %s,
        car_boite = %s
        WHERE car_id = %s"""
        cursor.execute(sql,(self.Nom, self.annee, self.capa, self.km, self.hpw, self.lstd, self.boite,self.id))
        bdd.commit()
        
    def suprimer(id): ##work
         
        i = int(id)  
        print(i)
        sql = "DELETE FROM voiture WHERE car_id = %s"
        cursor.execute(sql,(i,))
        bdd.commit()
                
##p = voiture(40, "Peugeot 108", 2016, 500, 300000, 100, 0, 0)
##p.ajouter()
##p.lstd = 2
##p.annee = 2012
##p.modifier()
##bdd.close()
