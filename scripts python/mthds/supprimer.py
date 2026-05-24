import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ## méthode permettant d'acceder au fichier placés dans les different dossiers du projet t
import PySimpleGUI as sg    
from items import eleve
from items import voiture
from items import moniteur
from items import heures


liste=[]
sg.theme('DarkGrey11')


def supprimer(): #supprimer est plus simpliste que les autres méthodes car on utilise la fonction supprimer communes a chaque classe items
    
    tab2_layout = [[sg.T('choisir que faire')],    
                   [sg.Button('supprimer élèves'), sg.Button('supprimer moniteur'), sg.Button('supprimer voiture'), sg.Button('supprimer heures')],
                   [sg.T('')]]      
    
    layout2 = [[sg.TabGroup([[sg.Tab('supprimer', tab2_layout, key="elv")]], tooltip='TIP2')],    
              [sg.Button('quitter')]]
    
    
    window = sg.Window('My window with tabs', layout2, default_element_size=(100,100))    
    

    while True:    
        event, values = window.read()    
        print(event,values)
        if event == sg.WIN_CLOSED:
            break
        if event == "quitter":
            window.close()
        if event == "supprimer élèves" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id1')],[sg.Button("approuver1")]])
        if event=="approuver1":
             id1 = values['id1']
             eleve.eleve.suprimer(int(id1))
             
        if event == "supprimer moniteur" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id2')],[sg.Button("approuver2")]])
        if event=="approuver2":
             id2 = values['id2']
             moniteur.moniteur.suprimer(int(id2))
            
        if event == "supprimer voiture" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id3')],[sg.Button("approuver3")]])
        if event=="approuver3":
             id3 = values['id3']
             voiture.voiture.suprimer(int(id3))

        if event == "supprimer heures" :
            window.extend_layout(window["elv"], [[sg.Input("ID",key='id4')],[sg.Button("approuver4")]])
        if event=="approuver4":
             id4 = values['id4']
             
             heures.heure.supprimer(int(id4))
