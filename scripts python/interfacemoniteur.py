import PySimpleGUI as sg
import moniteur

liste=[]

def interfacemoniteur() : 
    
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
            elv= moniteur.moniteur.afficher(id1)
           
            texte_affichage = f"id: {elv[0][0]} | Nom: {elv[0][1]} | Prénom: {elv[0][2]} | Age: {elv[0][3]} | Heures libres: {elv[0][4]} | Heures casées: {elv[0][5]}"
            window.extend_layout(window["elv"], [[sg.T(texte_affichage)]])
            
