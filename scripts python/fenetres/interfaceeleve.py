import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ## méthode permettant d'acceder au fichier placés dans les different dossiers du projet 
import PySimpleGUI as sg
from items import eleve

liste=[]
sg.theme('DarkGrey11')


def interfaceeleve() : ## comme interfacemoniteur.py on recupere un id et on afficher les infor correspondantes avec la méthode afficher d'eleve.py
    
    layout3 =[[sg.T('entrez identifiant', key='elv')],
             [sg.Input(key='mdp')],
             [sg.Button('entrer')]]
    
    window = sg.Window('My window with tabs', layout3, default_element_size=(100,100))  
    
    while True:    
        event, values = window.read()    
        print(event,values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'entrer': # on afficher les informations de maniere présentable avec un systeme pour afficher le type de boite (manuel ou auto) plutot que 0 ou 1
            id1=values['mdp']
            elv= eleve.eleve.afficher(id1)
            boite = elv[0][6]
            
            if boite == 0:
                txt = "manuel"
                
            elif boite == 1:
                txt = "auto"
                
            texte_affichage = f"id: {elv[0][0]} | Nom: {elv[0][1]} | Prénom: {elv[0][2]} | Age: {elv[0][3]} | Heures faites: {elv[0][4]} | Heures à faire: {elv[0][5]} | Boite: {txt}"
            window.extend_layout(window["elv"], [[sg.T(texte_affichage)]])
            
            
