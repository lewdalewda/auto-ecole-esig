import PySimpleGUI as sg
import modifier
import ajouter
import supprimer
sg.theme('DarkGrey11')
def interface2() :
    
    layout1 =[[sg.T('Que voulez vous faire')],
             [sg.Button('ajouter'), sg.Button('modifier'), sg.Button('supprimer')]]
    
    window = sg.Window('My window with tabs', layout1, default_element_size=(100,100))  
    
    while True:    
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

