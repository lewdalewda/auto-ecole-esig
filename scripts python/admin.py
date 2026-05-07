import heures
import eleve
import voiture
import moniteur
from mysql.connector import connect 
import datetime

bdd = connect(host="localhost", user="root", password="root", database="Auto")

cursor = bdd.cursor()

class admin:
    def __init__(self):
        self.prop=1
        
    def edit(liste):
        while True:
            choix = liste[0] ##int(input("""menu modifications,choisisez ce que vous voulez modifier :
                  #1) élèves
                  #2) moniteurs
                  #3) voitures
                  #4) heures
                  #5) quitter le menu
                  #entrez votre choix """))
            if choix == 1: ## modification données eleve
                cursor.execute("SELECT * FROM eleve")
                res = cursor.fetchall()
                lst =[]
                
                for etu in res:
                    e = eleve.eleve(etu[0],etu[1],etu[2],etu[3],etu[4],etu[5],etu[6])
                    lst.append(e)
                print(lst)
                chx = liste[1] #int(input("entrez id d'éléve"))
                
                for elv in lst:
                    if chx == elv.id:
                        elv.afficher()
                        edi = liste[2] #int(input(""""que voulez vous modifier ?
                                        #1)nom et prenom
                                        #2)age
                                        #3)heures faites/a faire
                                        #4)boite manuelle/automatique
                                        #5)quiter """))
                        if edi == 1:
                            n = liste[3] #str(input("entrez le nouveau nom (en majuscule) "))
                            p = liste[4] #str(input("entrez le nouveau prenom "))
                            elv.Nom = n
                            elv.Prenom = p
                            elv.modifier()
                            break    
                        
                        elif edi == 2:
                            a = liste[3] #str(input("entrez le nouveau age "))
                            elv.age = a
                            elv.modifier()
                            print("j'arrete ")
                            break
                        
                        elif edi == 3:
                            hc = liste[3] #int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            elv.hdc = hc
                            elv.hdf = hf
                            elv.modifier()
                            break
                        
                        elif edi == 4:
                            b = liste[3] #str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                elv.boite = 0
                            elif b == "A":
                                elv.boite = 1
                            else:
                                print("entrée non valide")
                            elv.modifier()
                            break
                        
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
                chx = liste[1]#int(input("entrez id de prof "))
                
                for mon in lst:
                    if chx == mon.id:
                        mon.afficher()
                        edi = liste[2] #int(input(""""que voulez vous modifier ?
                                       # 1)nom et prenom
                                       # 2)age
                                       # 3)heures faites/a faire
                                       # 4)quiter """))
                        
                        if edi == 1:
                            n = liste[3] #str(input("entrez le nouveau nom (en majuscule) "))
                            p = liste[4] #str(input("entrez le nouveau prenom "))
                            mon.Nom = n
                            mon.Prenom = p
                            mon.modifier()
                            break                            

                        elif edi == 2:
                            a = liste[3] #str(input("entrez le nouveau age "))
                            mon.age = a
                            mon.modifier()
                            break

                        elif edi == 3:
                            hc = liste[3] #int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            mon.hc = hc
                            mon.hl = hf
                            mon.modifier()
                            break                            
                        
                        elif edi == 4:
                            break
            
            
            elif choix == 3:
                cursor.execute("SELECT * FROM voiture")
                res = cursor.fetchall()
                lst =[]
                
                for voi in res:
                    v = voiture.voiture(voi[0],voi[1],voi[2],voi[3],voi[4],voi[5],voi[6],voi[7])
                    print(v.id)
                    lst.append(v)
                print(lst)
                chx = liste[1] #int(input("entrez id de voiture"))
                
                for car in lst:
                    if chx == car.id:
                        car.afficher()
                        edi = liste[2] #int(input(""""que voulez vous modifier ?
                                        #1)nom 
                                        #2)annee
                                        #3)capacité
                                        #4)kilometrage
                                        #5)hpw
                                        #6)lstd
                                        #7)boite
                                        #8)quiter """))
                        if edi == 1:
                            n = str(input("entrez le nouveau nom (en majuscule) "))
                            car.Nom = n
                            car.modifier()
                            break    
                        
                        elif edi == 2:
                            a = str(input("entrez l'année "))
                            car.age = a
                            car.modifier()
                            break
                        
                        elif edi == 3:
                            hc = int(input("entrez la capacité "))
                            car.capa = hc
                            car.modifier()
                            break
                        
                        elif edi == 4:
                            hc = int(input("entrez le kilometrage "))
                            car.km = hc
                            car.modifier()
                            break
                        
                        elif edi == 5:
                            hc = int(input("entrez la puissance "))
                            car.hpw = hc
                            car.modifier()
                            break    
                        
                        elif edi == 6:
                            hc = int(input("entrez le dernier conducteur "))
                            car.lstd = hc
                            car.modifier()
                            break
               
                        elif edi == 7:
                            b = str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                car.boite = 0
                            elif b == "A":
                                car.boite = 1
                            else:
                                print("entrée non valide")
                            car.modifier()
                            break
                        
                        elif edi == 8:
                            break
            
            elif choix ==4:
                cursor.execute("SELECT * FROM heure")
                res = cursor.fetchall()
                lst =[]
                
                for hr in res:
                    h = heures.heure(hr[0],hr[1],hr[2],hr[3],hr[4],hr[5],hr[6],hr[7],hr[8],hr[9],hr[10])
                    lst.append(h)
                    print(type(h.date))
                print(lst)
                chx = liste[1] #int(input("entrez id d'heure "))
                
                for hr in lst:
                    if chx == hr.id:
                        hr.afficher()
                        edi = liste[2] #int(input(""""que voulez vous modifier ?
                                        #1)date 
                                        #2)duree
                                        #3)eleve
                                        #4)prof
                                        #5)voiture
                                        #6)distance
                                        #7)depart
                                        #8)fin
                                        #9)boite
                                        #10)faite
                                        #11) """))
                        if edi == 1:
                            y = liste[3]#int(input("entrez l'année ")) ##ATTENTION A BIEN FAIRE MARCHER LES DATES !!!!
                            m = liste[4]#int(input("entrez le mois "))
                            d = liste[5]#int(input("entrez le jour "))
                            a = datetime.date(y,m,d)
                            hr.date = a
                            hr.modifier()
                            break
                        
                        if edi == 2:
                            n = liste[3] #int(input("entrez la nouvelle duree "))
                            hr.duree = n
                            hr.modifier()
                            break
                        
                        if edi == 3:
                            n = liste[3] #int(input("entrez l'id de l'eleve "))
                            hr.elv = n
                            hr.modifier()
                            break     
                        
                        if edi == 4:
                            n = liste[3] #int(input("entrez l'id du prof "))
                            hr.prof = n
                            hr.modifier()
                            break
                        
                        if edi == 5:
                            n = liste[3] #int(input("entrez l'id de la voiture "))
                            hr.car = n
                            hr.modifier()
                            break
                        
                        if edi == 6:
                            n = liste[3] #int(input("entrez la distance "))
                            hr.km = n
                            hr.modifier()
                            break
                        
                        if edi == 7:
                            h = liste[3] #int(input("entrez l'heure de debut "))
                            m= liste[4] #int(input("entrez les minutes de debut "))
                            a = datetime.datetime(hr.depart.year, hr.depart.month, hr.depart.day, h, m)
                            hr.depart = a
                            hr.modifier()
                            break
                        
                        if edi == 8:
                            h = liste[3] #int(input("entrez l'heure de fin "))
                            m= liste[4] #int(input("entrez les minutes de fin "))
                            a = datetime.datetime(hr.fin.year, hr.fin.month, hr.fin.day, h, m)
                            hr.fin = a
                            hr.modifier()
                            break
                        
                        if edi == 9:
                            b = liste[3] #str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                hr.boite = 0
                            elif b == "A":
                                hr.boite = 1
                            else:
                                print("entrée non valide")
                            hr.modifier()
                            break
                        
                        if edi == 10:
                            b = liste[3] #str(input("heure complétée (Y) ou pas (N) "))
                            if b == "Y":
                                hr.passee = 0
                            elif b == "N":
                                hr.passee = 1
                            else:
                                print("entrée non valide")
                            hr.modifier()
                            break
                        
                        elif edi == 11:
                            break
                        
                        break 
           
            
            
            
            elif choix == 5:
                bdd.close()
                break
            break

admin.edit([1,1,1,"MEKHAZNi","Yasmina"])
admin.edit([4,2,1,2026,6,12])

