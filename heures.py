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
        self.depaft=depart 
        self.fin=fin
        self.boite=boite
        self.passee=passee
    
    def ajouter(self):
        sql = "INSERT INTO heures(hr_id, hr_date, hr_duree, hr_elv, hr_prof, hr_car, hr_km, hr_depart, hr_fin, hr_boite, hr_passee) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.id, self.date, self.duree, self.elv, self.prof, self.car, self.km, self.depart, self.fin, self.boite, self.passee))
        bdd.commit()
        
    def modifier(self):
        sql = """UPDATE heures 
        SET hr_id= %s,
        hr_date= %s, 
        hr_duree = %s, 
        hr_elv = %s, 
        hr_prof = %s, 
        hr_car = %s,
        hr_km = %s,
        hr_depart = %s,
        hr_fin = %s,
        hr_boite = %s,
        hr_passee = %S,
        WHERE hr_id = %s"""
        cursor.execute(sql,(self.id, self.date, self.duree, self.elv, self.prof, self.car, self.km, self.depart, self.fin, self.boite, self.passee))
        bdd.commit()
        
    def supprimer(self):
        