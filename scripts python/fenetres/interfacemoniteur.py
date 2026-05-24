import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ## méthode permettant d'acceder au fichier placés dans les different dossiers du projet 
import PySimpleGUI as sg
from items import moniteur


liste=[]
sg.theme('DarkGrey11')


def interfacemoniteur() : ## comme interfaceeleve.py on recupere un id et on afficher les infos correspondantes avec la méthode afficher de moniteur.py
    
    layout3 =[[sg.T('entrez identifiant', key='elv')],
             [sg.Input(key='mdp')],
             [sg.Button('entrer')]]
    
    window = sg.Window('My window with tabs', layout3, default_element_size=(100,100))  
    
    while True:    
        event, values = window.read()    
        print(event,values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'quitter':
            window.close()
        if event == 'entrer':
            id1=values['mdp']
            mon= moniteur.moniteur.afficher(id1)
           
            texte_affichage = f"id: {mon[0][0]} | Nom: {mon[0][1]} | Prénom: {mon[0][2]} | Age: {mon[0][3]} | Heures libres: {mon[0][4]} | Heures casées: {mon[0][5]}"
            window.extend_layout(window["elv"], [[sg.T(texte_affichage)]])
            
