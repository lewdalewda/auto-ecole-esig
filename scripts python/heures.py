from mysql.connector import connect 

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()

class heure : 
    def __init__(self,id,date,duree,elv,prof,car,km,depart,fin,boite,passee):
        self.id=id
        self.date=date
        self.duree=duree
        self.elv=elv
        self.prof=prof
        self.car=car
        self.km=km
        self.depart=depart 
        self.fin=fin
        self.boite=boite
        self.passee=passee
    
    
    def afficher(self):
        print(self.id, self.date, self.duree, self.elv, self.prof, self.car, self.km, self.depart, self.fin, self.boite, self.passee)
    
    def ajouter(self): ##work
        sql = "INSERT INTO heure(hr_id, hr_date, hr_duree, hr_elv, hr_prof, hr_car, hr_km, hr_depart, hr_fin, hr_boite, hr_passee) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.id, self.date, self.duree, self.elv, self.prof, self.car, self.km, self.depart, self.fin, self.boite, self.passee))
        bdd.commit()
        
    def modifier(self): ##work
        sql = """UPDATE heure
        SET hr_date= %s, 
        hr_duree = %s, 
        hr_elv = %s, 
        hr_prof = %s, 
        hr_car = %s,
        hr_km = %s,
        hr_depart = %s,
        hr_fin = %s,
        hr_boite = %s,
        hr_passee = %s
        WHERE hr_id = %s"""
        cursor.execute(sql,(self.date, self.duree, self.elv, self.prof, self.car, self.km, self.depart, self.fin, self.boite, self.passee, self.id))
        bdd.commit()
        
    def supprimer(): ##work
           
        while True:
            choix = int(input("choisisez id 1 ou nom 2 "))
             
            if choix == 1:
                
                i = int(input("entrer id à supprimer"))
                 
             
            elif choix == 2:
                 
                d = str(input("entre la date (annee-mois-jour) "))
                 
                cursor.execute("select hr_id from heure where hr_date = %s ", (d,))
                res = cursor.fetchall()
                i = res[0][0]
                
                 
                 
                 
            print(i)
            sql = "DELETE FROM heure WHERE hr_id = %s"
            cursor.execute(sql,(i,))
            bdd.commit()
            break
        

h = heure(5,"2026-06-12", 2, 4, 1, 4, 50, "2026-06-12 09:00:00", "2026-06-12 11:00:00", 0, 0)
##h.ajouter()
h.date = "2026-07-12"
h.modifier()
##bdd.close()
