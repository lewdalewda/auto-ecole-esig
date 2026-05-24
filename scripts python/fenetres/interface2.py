import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ## méthode permettant d'acceder au fichier placés dans les different dossiers du projet 
import PySimpleGUI as sg
from mthds import modifier
from mthds import ajouter
from mthds import supprimer


sg.theme('DarkGrey11')


def interface2() :
    
    layout1 =[[sg.T('Que voulez vous faire')],
             [sg.Button('ajouter'), sg.Button('modifier'), sg.Button('supprimer')]]
    
    window = sg.Window('My window with tabs', layout1, default_element_size=(100,100))  
    
    while True: ## ici on choisit quelle fonction du dossier mthds on veut utiliser   
        event, values = window.read()    
        print(event,values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'ajouter':
            ajouter.ajouter()
        if event == 'modifier':
            modifier.modifier()
        if event == 'supprimer':
            supprimer.supprimer()   
    window.close()

