import PySimpleGUI as sg
from fenetres import interface2
from fenetres import interfaceeleve
from fenetres import interfacemoniteur


sg.theme('DarkGrey11')
layout3 =[[sg.T('entrez le mot de passe admin pour modifier')],[sg.T('entrez eleve1 pour acceder aux infos eleve')],[sg.T('entrez moniteur1 pour acceder aux infos moniteur')],
         [sg.Input(key='mdp', s=9 )],
         [sg.Button('entrer')]]

window = sg.Window('My window with tabs', layout3, default_element_size=(100,100))  

while True:    
    event, values = window.read()    
    print(event,values)
    if event == sg.WIN_CLOSED:
        break 
    if event == 'entrer': # on vérifie l'input pour determiner quelle interface ouvrir
        if values['mdp'] == '1234':
            window.close()
            interface2.interface2()
            break
    if values['mdp'] == 'eleve1' :
        window.close()
        interfaceeleve.interfaceeleve()
    if values['mdp'] == 'moniteur1' :
        window.close()
        interfacemoniteur.interfacemoniteur()
       
window.close()
