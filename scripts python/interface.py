import PySimpleGUI as sg    

liste=[]

tab1_layout =  [[sg.T('This is inside tab 1')]]    

tab2_layout = [[sg.T('choisir que faire')],    
               [sg.Button('modifier élèves'), sg.Button('modifier moniteur'), sg.Button('modifier voiture'), sg.Button('modifier heures')],
               [sg.T('')]]    

tab3_layout =  [[sg.Image(filename = "911.gif")]]   

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('élèves', tab2_layout, key="elv"), sg.Tab('Nos Voitures', tab3_layout)]], tooltip='TIP2')],    
          [sg.Button('Read')]]    


window = sg.Window('My window with tabs', layout, default_element_size=(100,100))    

modifeleve = False
while True:    
    event, values = window.read()    
    print(event,values)
    if event == sg.WIN_CLOSED:
        break
    if event == "modifier élèves" :
        liste.append(1)
        window.extend_layout(window["elv"], [[sg.Input("entrer id",key='id'),sg.Button("approuver")]])
    if event == "approuver":
        if modifeleve == False :
            id1 = values['id']
            liste.append(id1)
            window.extend_layout(window["elv"], [[sg.Button("nom/prenom"),sg.Button("age eleve "),sg.Button("heure faite eleve"),sg.Button("boite")]])
            modifeleve = True 
    if event == "nom/prenom" :
        liste.append(1)
        window.extend_layout(window["elv"], [[sg.Input("entrer nom",key='nom')],[sg.Input("entrer prenom",key='prenom'),sg.Button("approuver2")]])
    if event=="approuver2":
        nom = values['nom']
        prenom = values['prenom']
        liste.append(nom)
        liste.append(prenom)
    if event=="age eleve " :
        liste.append(2)
        window.extend_layout(window["elv"], [[sg.Input("entrer age",key='age1'),sg.Button("approuver3")]])
    if event=="approuver3":
        age1 = values['age1']
        liste.append(age1)
    if event == "heure faite eleve" :
        liste.append(3)
        window.extend_layout(window["elv"], [[sg.Input("entrer heure faite",key='hf'),sg.Button("approuver4")]])
    if event=="approuver4":
        hf=values['hf']
        liste.append(hf)      
    if event == "boite" :
        liste.append(4)
        window.extend_layout(window["elv"], [[sg.Input("entrer boite",key='boite1'),sg.Button("approuver5")]])
    if event=="approuver5":
        boite1 = values['boite1']
        liste.append(boite1)
    
    
    if event == "modifier moniteur" :
        liste.append(2)
        window.extend_layout(window["elv"], [[sg.Input("entrer id",key='id2'),sg.Button("approuver6")]])
    if event == "approuver6":
        if modifeleve == False :
            id2 = values['id2']
            liste.append(id2)
            window.extend_layout(window["elv"], [[sg.Button("nom//prenom"),sg.Button("age moniteur"),sg.Button("heure faite moniteur")]])
            modifeleve = True 
    if event == "nom//prenom" :
        liste.append(1)
        window.extend_layout(window["elv"], [[sg.Input("entrer nom",key='nom2')],[sg.Input("entrer prenom",key='prenom2'),sg.Button("approuver7")]])
    if event=="approuver7":
        nom2 = values['nom2']
        prenom2 = values['prenom2']
        liste.append(nom2)
        liste.append(prenom2)
    if event=="age moniteur" :
        liste.append(2)
        window.extend_layout(window["elv"], [[sg.Input("entrer age",key='age2'),sg.Button("approuver8")]])
    if event=="approuver8":
        age2 = values['age2']
        liste.append(age2)
    if event == "heure faite moniteur" :
        liste.append(3)
        window.extend_layout(window["elv"], [[sg.Input("entrer heure faite",key='hf2'),sg.Button("approuver9")]])
    if event=="approuver9":
        hf2=values['hf2']
        liste.append(hf2) 
    print(liste)
        