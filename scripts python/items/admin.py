from items import heures
from items import eleve
from items import voiture
from items import moniteur
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
            choix = liste[0] ##le systeme d'édit fonctionne comme un "arbre a choix" chaque étape propose plusieurs choix ainsi la liste donnée quand on "invoque" la fonction sert de "chemin" ou [0] donne la catégorie de données modifiée (elv, prof, ect), [1] donne quel type de données on modifie (nom, age, ect) et les emplacements suivants contiennent les nouvelles informations 
            if choix == 1: ## modification données eleve
                cursor.execute("SELECT * FROM eleve")
                res = cursor.fetchall()
                lst =[]
                
                for etu in res:
                    e = eleve.eleve(etu[0],etu[1],etu[2],etu[3],etu[4],etu[5],etu[6])
                    lst.append(e)  
                chx = int(liste[1]) #id de l'eleve à modifier
                
                for elv in lst:
                    if chx == elv.id:
                        edi = liste[2] #choix de la donnée à modifier
                        if edi == 1: #modifier nom et prenom
                            n = liste[3] 
                            p = liste[4] 
                            elv.Nom = n
                            elv.Prenom = p
                            elv.modifier()
                            
                        elif edi == 2: #modifier age
                            a = int(liste[3]) #str(input("entrez le nouveau age "))
                            elv.age = a
                            elv.modifier()
                            
                        elif edi == 3: #modifier heures faites et heures à faire
                            hc = int(liste[3]) 
                            hf = 30 - hc
                            elv.hdc = hc
                            elv.hdf = hf
                            elv.modifier()
                        
                        elif edi == 4: #modifier type de boite
                            b = (liste[3])
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
                chx = int(liste[1]) ##id du moniteur à modifier
                
                for mon in lst:
                    if chx == mon.id:
                        edi = int(liste[2]) #choix de la donnée à modifier
                        
                        if edi == 1: #modifier nom et prenom
                            n = liste[3] 
                            p = liste[4] 
                            mon.Nom = n
                            mon.Prenom = p
                            mon.modifier()                              

                        elif edi == 2: #modifier age
                            a = int(liste[3]) #str(input("entrez le nouveau age "))
                            mon.age = a
                            mon.modifier()
                        
                        elif edi == 3: #modifier heures cassées et heures à faire
                            hc = int(liste[3]) #int(input("entrez le nombe d'heures faites "))
                            hf = 30 - hc
                            mon.hc = hc
                            mon.hl = hf
                            mon.modifier()
                                                       
                        elif edi == 4:
                            break
    
            
            elif choix == 3: ## modification données voiture
                cursor.execute("SELECT * FROM voiture")
                res = cursor.fetchall()
                lst =[]
                
                for voi in res:
                    v = voiture.voiture(voi[0],voi[1],voi[2],voi[3],voi[4],voi[5],voi[6],voi[7])                   
                    lst.append(v)

                chx = int(liste[1]) #id de la voiture à modifier
                
                for car in lst:
                    if chx == car.id:
                       
                        edi = int(liste[2]) #choix de la donnée à modifier
                        if edi == 1:
                            n = liste[3] #modifier nom
                            car.Nom = n
                            car.modifier()
                               
                        elif edi == 2:
                            print("age")
                            a = int(liste[3]) #modifier l'annee
                            car.annee = a
                            car.modifier()
                            
                        
                        elif edi == 3:
                            hc = int(liste[3]) #modifier la capacité
                            car.capa = hc
                            car.modifier()
                            
                        
                        elif edi == 4:
                            hc = int(liste[3]) #modifier le nombre de km
                            car.km = hc
                            car.modifier()
                            
                        
                        elif edi == 5:
                            hc = int(liste[3]) #mofier la puissance
                            car.hpw = hc
                            car.modifier()
                               
                        
                        elif edi == 6:
                            hc = int(liste[3]) #modifier le dernier conducteur
                            car.lstd = hc
                            car.modifier()
                            
               
                        elif edi == 7:
                            b = liste[3] #mofier le type de boite
                            if b == "M":
                                car.boite = 0
                            elif b == "A":
                                car.boite = 1
                            else:
                                print("entrée non valide")
                            car.modifier()
                        
                        elif edi == 8:
                            break
            
            elif choix ==4: ## modification données heures
                cursor.execute("SELECT * FROM heures")
                res = cursor.fetchall()
                lst =[]
                
                for hr in res:
                    h = heures.heure(hr[0],hr[1],hr[2],hr[3],hr[4],hr[5],hr[6],hr[7],hr[8],hr[9],hr[10])
                    lst.append(h)
                                    
                chx = int(liste[1]) #id de l'heure à modifier
                
                for hr in lst:
                    if chx == hr.id:
                        
                        edi = int(liste[2]) #choix de la donnée à modifier
                        if edi == 1: #modifier la date
                            y = int(liste[3])
                            m = int(liste[4])
                            d = int(liste[5])
                            a = datetime.date(y,m,d)
                            hr.date = a
                            hr.modifier()
                            break
                        
                        if edi == 2: #modifier la duree
                            n = int(liste[3])#int(input("entrez la nouvelle duree "))
                            hr.duree = n
                            hr.modifier()
                            
                        
                        if edi == 3: #modifier l'id de l'eleve
                            n = int(liste[3]) 
                            hr.elv = n
                            hr.modifier()
                                
                        
                        if edi == 4: #modifier l'id du prof
                            n = int(liste[3]) 
                            hr.prof = n
                            hr.modifier()
                            
                        
                        if edi == 5: #modifier l'id de la voiture
                            n = int(liste[3]) 
                            hr.car = n
                            hr.modifier()
                            
                        if edi == 6: #modifier le nombre de km
                            n = int(liste[3]) 
                            hr.km = n
                            hr.modifier()
                            
                        
                        if edi == 7: #modifier l'heure de debut
                            print(liste,"hour")
                            h = int(liste[3])
                            m= int(liste[4]) 
                            a = datetime.datetime(hr.depart.year, hr.depart.month, hr.depart.day, h, m) #on reutilise la date de départ pour ne modifier que l'heure et les minutes
                            print(a.hour, a.minute)
                            hr.depart = a
                            hr.modifier()
                            
                        
                        if edi == 8: #modifier l'heure de fin
                            h = int(liste[3])  
                            m= int(liste[4]) 
                            a = datetime.datetime(hr.fin.year, hr.fin.month, hr.fin.day, h, m)
                            hr.fin = a
                            hr.modifier()
                            
                        
                        if edi == 9: #modifier le type de boite
                            b = liste[3]  
                            if b == "M":
                                hr.boite = 0
                            elif b == "A":
                                hr.boite = 1
                            else:
                                print("entrée non valide")
                            hr.modifier()
                            
                        if edi == 10: #modifier si l'heure est passée ou non
                            b = liste[3] 
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

