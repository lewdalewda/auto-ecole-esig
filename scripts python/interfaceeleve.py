import PySimpleGUI as sg
import eleve

liste=[]

def interfaceeleve() : 
    
    layout3 =[[sg.T('entrez identifiant', key='elv')],
             [sg.Input(key='mdp')],
             [sg.Button('entrer')]]
    
    window = sg.Window('My window with tabs', layout3, default_element_size=(100,100))  
    
    while True:    
        event, values = window.read()    
        print(event,values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'entrer':
            id1=values['mdp']
            elv= eleve.eleve.afficher(id1)
            boite = elv[0][6]
            
            if boite == 0:
                txt = "manuel"
                
            elif boite == 1:
                txt = "auto"
                
            texte_affichage = f"id: {elv[0][0]} | Nom: {elv[0][1]} | Prénom: {elv[0][2]} | Age: {elv[0][3]} | Heures faites: {elv[0][4]} | Heures à faire: {elv[0][5]} | Boite: {txt}"
            window.extend_layout(window["elv"], [[sg.T(texte_affichage)]])
            
            
