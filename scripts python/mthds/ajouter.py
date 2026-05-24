import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ## méthode permettant d'acceder au fichier placés dans les different dossiers du projet 
import PySimpleGUI as sg    
import datetime
from items import eleve
from items import voiture
from items import moniteur
from items import heures


liste=[]
sg.theme('DarkGrey11')


def ajouter():      
    
    tab2_layout = [[sg.T('choisir que faire')],    
                   [sg.Button('ajouter élèves'), sg.Button('ajouter moniteur'), sg.Button('ajouter voiture'), sg.Button('ajouter heures')],
                   [sg.T('')]]      
    
    layout2 = [[sg.TabGroup([[sg.Tab('ajouter', tab2_layout, key="elv")]], tooltip='TIP2')],    
              [sg.Button('quitter')]]
    
    
    window = sg.Window('My window with tabs', layout2, default_element_size=(100,100))    
    

    while True: #pour choisir quelle type d'ajout on veut faire (élève, moniteur, voiture ou heures) et ensuite on remplit les champs pour ajouter l'item voulu   
        event, values = window.read()    
        print(event,values)
        if event == sg.WIN_CLOSED:
            break
        if event == "quitter":
            window.close()
        if event == "ajouter élèves" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id1')], [sg.Input("nom",key='nom')],[sg.Input("prenom",key='prenom')],[sg.Input("age eleve",key='age1')],[sg.Input("heure faite eleve",key='hf')],[sg.Button("approuver")],[sg.Button("manuelle1"),sg.Button("automatique1")]])
        if event=="approuver":
            id1 = values['id1']
            liste.append(id1)
            nom = values['nom']
            prenom = values['prenom']
            liste.append(nom)
            liste.append(prenom)  
            age1 = values['age1']
            liste.append(age1)     
            hf=values['hf']
            liste.append(hf)      
        if event=="manuelle1": #pour confirmer l'ajout de l'élève on doit appuyer soit sur manu ou auto pour que les données soient traitées et ajoutées à la base de données
            liste.append(0)
            p = eleve.eleve(int(liste[0]),liste[1],liste[2],int(liste[3]),int(liste[4]),30-int(liste[4]),int(liste[5]))
            print("1 ok")
            p.ajouter()
        if event=="automatique1":
            liste.append(1)
            p = eleve.eleve(int(liste[0]),liste[1],liste[2],int(liste[3]),int(liste[4]),30-int(liste[4]),int(liste[5]))
            print("1 ok")
            p.ajouter()
        
            
            
        if event == "ajouter moniteur" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id2')],[sg.Input("nom",key='nom2')],[sg.Input("prenom",key='prenom2')],[sg.Input("age moniteur",key='age2')],[sg.Input("heure faite moniteur",key='hf2')],[sg.Button("approuver2")]])
        if event == "approuver2":
            id2 = values['id2']
            liste.append(id2)
            nom2 = values['nom2']
            prenom2 = values['prenom2']
            liste.append(nom2)
            liste.append(prenom2)
            age2 = values['age2']
            liste.append(age2)
            hf2=values['hf2']
            liste.append(hf2) 
            m = moniteur.moniteur(int(liste[0]),liste[1],liste[2],int(liste[3]),0,int(liste[4]))
            m.ajouter()
            
        
        if event == "ajouter voiture" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id3')],[sg.Input("nom3",key='nom4')],[sg.Input("annee",key='annee1')],[sg.Input("capacité",key='capacité1')],[sg.Input("kilometrage",key='klm')],[sg.Input("hpw",key='hpw1')],[sg.Input("lstd",key='lstd2')],[sg.Button("approuver3")],[sg.Button("manuelle2"),sg.Button("automatique2")]]) 
        if event=="approuver3":
            id3 = values['id3']
            liste.append(id3)
            nom4 = values['nom4']
            liste.append(nom4)
            annee1 = values['annee1']
            liste.append(annee1)
            capacité1=values['capacité1']
            liste.append(capacité1)
            klm1=values['klm']
            liste.append(klm1)      
            hpw1=values['hpw1']
            liste.append(hpw1)
            lstd1=values['lstd2']
            liste.append(lstd1)
        if event=="manuelle2":
            liste.append(0)
            v = voiture.voiture(int(liste[0]),liste[1],int(liste[2]),int(liste[3]),int(liste[4]),int(liste[5]),int(liste[6]),int(liste[7]))
            v.ajouter()
        if event=="automatique2":
            liste.append(1)
            v = voiture.voiture(int(liste[0]),liste[1],int(liste[2]),int(liste[3]),int(liste[4]),int(liste[5]),int(liste[6]),int(liste[7]))
            v.ajouter()
            
        
        
        if event == "ajouter heures" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id4')],[sg.Input("date/annee",key='date/annee', s=10),sg.Input("date/mois",key='date/mois', s=10), sg.Input("date/jour",key='date/jour',s=10)],[sg.Input("duree",key='duree1')],[sg.Input("eleve",key='eleve1')],[sg.Input("prof",key='prof1')],[sg.Input("voiture",key='voiture1')],[sg.Input("distance",key='distance1')],[sg.Input("depart/heure",key='depart1', s=10),sg.Input("depart/minute",key='depart2', s= 10)],[sg.Input("fin/heure",key='fin1', s= 10),sg.Input("fin/min",key='fin2', s= 10)],[sg.Input("faite")],[sg.Button("approuver4")],[sg.Button("manuelle3"),sg.Button("automatique3")]]) 
        if event=="approuver4":
            id4 = values['id4']
            liste.append(id4)
            annee1 = int(values['date/annee'])
            mois1 = int(values['date/mois'])
            jour1 = int(values['date/jour'])
            d = datetime.datetime(annee1, mois1, jour1)
            liste.append(d)
            
            duree1 = values['duree1']
            liste.append(duree1)
            eleve1=values['eleve1']
            liste.append(eleve1)   
            prof1=values['prof1']
            liste.append(prof1)
            voiture1=values['voiture1']
            liste.append(voiture1)
            distance1=values['distance1']
            liste.append(distance1)
            
            depart1= int(values['depart1'])
            depart2= int(values['depart2'])
            d = datetime.datetime(annee1, mois1, jour1, depart1, depart2)
            liste.append(d)
            
            fin1= int(values['fin1'])
            fin2=int(values['fin2'])
            d2 = datetime.datetime(annee1, mois1, jour1, fin1, fin2)
            liste.append(d2)
            liste.append(0)
        if event=="manuelle3":
            liste.append(0)
            v = heures.heure(int(liste[0]),liste[1],int(liste[2]),int(liste[3]),int(liste[4]),int(liste[5]),int(liste[6]),liste[7], liste[8], liste[9], liste[10])
            v.ajouter()
        if event=="automatique3":
            liste.append(1)
            v = heures.heure(int(liste[0]),liste[1],int(liste[2]),int(liste[3]),int(liste[4]),int(liste[5]),int(liste[6]),liste[7], liste[8], liste[9], liste[10])
            v.ajouter()
            
        print(liste)
            
    window.close()
