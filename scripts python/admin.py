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
            print(liste , "lol" )
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
                    eleve.eleve.afficher(liste[1])
                chx = int(liste[1]) #int(input("entrez id d'éléve"))
                
                for elv in lst:
                    if chx == elv.id:
                        
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
                              
                        
                        elif edi == 2:
                            a = int(liste[3]) #str(input("entrez le nouveau age "))
                            elv.age = a
                           
                            elv.modifier()
                            
                           
                        
                        elif edi == 3:
                            hc = int(liste[3]) #int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            elv.hdc = hc
                            elv.hdf = hf
                            
                            elv.modifier()
                            
                        
                        elif edi == 4:
                            b = int(liste[3]) #str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                elv.boite = 0
                            elif b == "A":
                                elv.boite = 1
                            else:
                                print("entrée non valide")
                            
                            elv.modifier()
                            
                        
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
                        moniteur.moniteur.afficher(liste[1])
                        edi = int(liste[2]) #int(input(""""que voulez vous modifier ?
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
                                                        

                        elif edi == 2:
                            a = int(liste[3]) #str(input("entrez le nouveau age "))
                            mon.age = a
                            mon.modifier()
                            

                        elif edi == 3:
                            hc = int(liste[3]) #int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            mon.hc = hc
                            mon.hl = hf
                            mon.modifier()
                                                       
                        
                        elif edi == 4:
                            break
    
            
            elif choix == 3:
                cursor.execute("SELECT * FROM voiture")
                res = cursor.fetchall()
                lst =[]
                
                for voi in res:
                    v = voiture.voiture(voi[0],voi[1],voi[2],voi[3],voi[4],voi[5],voi[6],voi[7])                   
                    lst.append(v)

                chx = int(liste[1]) #int(input("entrez id de voiture"))
                
                for car in lst:
                    if chx == car.id:
                        voiture.voiture.afficher(liste[1])
                        edi = int(liste[2]) #int(input(""""que voulez vous modifier ?
                                        #1)nom 
                                        #2)annee
                                        #3)capacité
                                        #4)kilometrage
                                        #5)hpw
                                        #6)lstd
                                        #7)boite
                                        #8)quiter """))
                        if edi == 1:
                            n = liste[3] #str(input("entrez le nouveau nom (en majuscule) "))
                            car.Nom = n
                            car.modifier()
                               
                        
                        elif edi == 2:
                            print("age")
                            a = int(liste[3]) #str(input("entrez l'année "))
                            car.annee = a
                            car.modifier()
                            
                        
                        elif edi == 3:
                            hc = int(liste[3]) #int(input("entrez la capacité "))
                            car.capa = hc
                            car.modifier()
                            
                        
                        elif edi == 4:
                            hc = int(liste[3]) #int(input("entrez le kilometrage "))
                            car.km = hc
                            car.modifier()
                            
                        
                        elif edi == 5:
                            hc = int(liste[3]) # int(input("entrez la puissance "))
                            car.hpw = hc
                            car.modifier()
                               
                        
                        elif edi == 6:
                            hc = int(liste[3]) #int(input("entrez le dernier conducteur "))
                            car.lstd = hc
                            car.modifier()
                            
               
                        elif edi == 7:
                            b = liste[3] #str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                car.boite = 0
                            elif b == "A":
                                car.boite = 1
                            else:
                                print("entrée non valide")
                            car.modifier()
                        
                        
                        elif edi == 8:
                            break
            
            elif choix ==4:
                cursor.execute("SELECT * FROM heure")
                res = cursor.fetchall()
                lst =[]
                
                for hr in res:
                    h = heures.heure(hr[0],hr[1],hr[2],hr[3],hr[4],hr[5],hr[6],hr[7],hr[8],hr[9],hr[10])
                    lst.append(h)
                                    
                chx = int(liste[1]) #int(input("entrez id d'heure "))
                
                for hr in lst:
                    if chx == hr.id:
                        
                        edi = int(liste[2]) #int(input(""""que voulez vous modifier ?
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
                            y = int(liste[3])#int(input("entrez l'année ")) ##ATTENTION A BIEN FAIRE MARCHER LES DATES !!!!
                            m = int(liste[4])#int(input("entrez le mois "))
                            d = int(liste[5])#int(input("entrez le jour "))
                            a = datetime.date(y,m,d)
                            hr.date = a
                            hr.modifier()
                            break
                        
                        if edi == 2:
                            n = int(liste[3])#int(input("entrez la nouvelle duree "))
                            hr.duree = n
                            hr.modifier()
                            
                        
                        if edi == 3:
                            n = int(liste[3]) #int(input("entrez l'id de l'eleve "))
                            hr.elv = n
                            hr.modifier()
                                
                        
                        if edi == 4:
                            n = int(liste[3]) #int(input("entrez l'id du prof "))
                            hr.prof = n
                            hr.modifier()
                            
                        
                        if edi == 5:
                            n = int(liste[3]) #int(input("entrez l'id de la voiture "))
                            hr.car = n
                            hr.modifier()
                            
                        
                            n = int(liste[3]) #int(input("entrez la distance "))
                            hr.km = n
                            hr.modifier()
                            
                        
                        if edi == 7:
                            print(liste,"hour")
                            h = int(liste[3]) #int(input("entrez l'heure de debut "))
                            m= int(liste[4]) #int(input("entrez les minutes de debut "))
                            a = datetime.datetime(hr.depart.year, hr.depart.month, hr.depart.day, h, m)
                            print(a.hour, a.minute)
                            hr.depart = a
                            hr.modifier()
                            
                        
                        if edi == 8:
                            h = int(liste[3])  #int(input("entrez l'heure de fin "))
                            m= int(liste[4]) #int(input("entrez les minutes de fin "))
                            a = datetime.datetime(hr.fin.year, hr.fin.month, hr.fin.day, h, m)
                            hr.fin = a
                            hr.modifier()
                            
                        
                        if edi == 9:
                            b = liste[3]  #str(input("boite manuelle (M) ou auto (A) "))
                            if b == "M":
                                hr.boite = 0
                            elif b == "A":
                                hr.boite = 1
                            else:
                                print("entrée non valide")
                            hr.modifier()
                            
                        
                        if edi == 10:
                            
                            b = liste[3] #str(input("heure complétée (Y) ou pas (N) "))
                            if b == "Y":
                                hr.passee = 1
                            elif b == "N":
                                hr.passee = 0
                            else:
                                print("entrée non valide")
                            hr.modifier()
                            
                        
                        elif edi == 11:
                            break
                        
                        break 
           
            
            
            
            elif choix == 5:
                bdd.close()
                break
            break


