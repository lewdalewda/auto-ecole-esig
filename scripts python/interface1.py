import PySimpleGUI as sg
import interface2
import interfaceeleve
import interfacemoniteur

layout3 =[[sg.T('entrez le mot de passe')],
         [sg.Input(key='mdp')],
         [sg.Button('entrer')]]

window = sg.Window('My window with tabs', layout3, default_element_size=(100,100))  

while True:    
    event, values = window.read()    
    print(event,values)
    if event == sg.WIN_CLOSED:
        break 
    if event == 'entrer':
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