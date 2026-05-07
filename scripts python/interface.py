import PySimpleGUI as sg    

liste=[]

def ouvrir1():
    tab1_layout =  [[sg.T('This is inside tab 1')]]    
    
    tab2_layout = [[sg.T('choisir que faire')],    
                   [sg.Button('modifier élèves'), sg.Button('modifier moniteur'), sg.Button('modifier voiture'), sg.Button('modifier heures')],
                   [sg.T('')]]    
    
    tab3_layout =  [[sg.Image(filename = "911.gif")]]   
    
    layout2 = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('élèves', tab2_layout, key="elv"), sg.Tab('Nos Voitures', tab3_layout)]], tooltip='TIP2')],    
              [sg.Button('Read')]]    
    
    
    window = sg.Window('My window with tabs', layout2, default_element_size=(100,100))    
    
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
            window.extend_layout(window["elv"], [[sg.Button("manuelle1"),sg.Button("automatique1")]])
        if event=="manuelle1":
            liste.append("M")
        if event=="automatique1":
            liste.append("A")
            
            
            
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
            
            
        
        if event == "modifier voiture" :
            liste.append(3)
            window.extend_layout(window["elv"], [[sg.Button("nom3"),sg.Button("annee"),sg.Button("capacité"),sg.Button("kilometrage"),sg.Button("hpw"),sg.Button("lstd"),sg.Button("boite voiture")]]) 
        if event == "nom3" :
            liste.append(1)
            window.extend_layout(window["elv"], [[sg.Input("entrer nom",key='nom4'),sg.Button("approuver10")]])
        if event=="approuver10":
            nom4 = values['nom4']
            liste.append(nom4)
        if event=="annee" :
            liste.append(2)
            window.extend_layout(window["elv"], [[sg.Input("entrer annee",key='annee1'),sg.Button("approuver11")]])
        if event=="approuver11":
            annee1 = values['annee1']
            liste.append(annee1)
        if event == "capacité" :
             liste.append(3)
             window.extend_layout(window["elv"], [[sg.Input("entrer la capacité",key='capacité1'),sg.Button("approuver15")]])
        if event=="approuver15":
             capacité1=values['capacité1']
             liste.append(capacité1)
        if event == "kilometrage" :
            liste.append(4)
            window.extend_layout(window["elv"], [[sg.Input("entrer kilometrage",key='klm'),sg.Button("approuver12")]])
        if event=="approuver12":
            klm1=values['klm']
            liste.append(klm1)      
        if event == "hpw" :
            liste.append(5)
            window.extend_layout(window["elv"], [[sg.Input("entrer puissance",key='hpw1'),sg.Button("approuver13")]])
        if event=="approuver13":
            hpw1=values['hpw1']
            liste.append(hpw1)
        if event == "lstd" :
            liste.append(6)
            window.extend_layout(window["elv"], [[sg.Input("entrer id dernier conducteur",key='lstd2'),sg.Button("approuver14")]])
        if event=="approuver14":
            lstd1=values['lstd2']
            liste.append(lstd1)
        if event == "boite voiture" :
            liste.append(7)
            window.extend_layout(window["elv"], [[sg.Button("manuelle2"),sg.Button("automatique2")]])
        if event=="manuelle2":
            liste.append("M")
        if event=="automatique2":
            liste.append("A")
            
        
        
        if event == "modifier heures" :
            liste.append(4)
            window.extend_layout(window["elv"], [[sg.Button("date"),sg.Button("duree"),sg.Button("eleve"),sg.Button("prof"),sg.Button("voiture"),sg.Button("distance"),sg.Button("depart"),sg.Button("fin"),sg.Button("boite1"),sg.Button("faite")]]) 
        if event == "date" :
            liste.append(1)
            window.extend_layout(window["elv"], [[sg.Input("entrer date",key='date1'),sg.Button("approuver17")]])
        if event=="approuver17":
            date1 = values['date1']
            liste.append(date1)
            
            
        if event=="duree" :
            liste.append(2)
            window.extend_layout(window["elv"], [[sg.Input("entrer duree",key='duree1'),sg.Button("approuver18")]])
        if event=="approuver18":
            duree1 = values['duree1']
            liste.append(duree1)
            
            
        if event == "eleve" :
            liste.append(3)
            window.extend_layout(window["elv"], [[sg.Input("entrer eleve id",key='eleve1'),sg.Button("approuver19")]])
        if event=="approuver19":
            eleve1=values['eleve1']
            liste.append(eleve1)   
            
            
        if event == "prof" :
            liste.append(4)
            window.extend_layout(window["elv"], [[sg.Input("entrer prof id",key='prof1'),sg.Button("approuver20")]])
        if event=="approuver20":
            prof1=values['prof1']
            liste.append(prof1)
            
            
        if event == "voiture" :
            liste.append(5)
            window.extend_layout(window["elv"], [[sg.Input("entrer voiture id",key='voiture1'),sg.Button("approuver21")]])
        if event=="approuver21":
            voiture1=values['voiture1']
            liste.append(voiture1)
            
            
        if event == "distance" :
            liste.append(6)
            window.extend_layout(window["elv"], [[sg.Input("entrer la distance",key='distance1'),sg.Button("approuver22")]])
        if event=="approuver22":
            distance1=values['distance1']
            liste.append(distance1)
            
            
        if event == "depart" :
            liste.append(7)
            window.extend_layout(window["elv"], [[sg.Input("entrer le depart",key='depart1'),sg.Button("approuver23")]])
        if event=="approuver23":
            depart1=values['depart1']
            liste.append(depart1)
            
            
        if event == "fin" :
            liste.append(8)
            window.extend_layout(window["elv"], [[sg.Input("entrer la fin",key='fin1'),sg.Button("approuver24")]])
        if event=="approuver24":
            fin1=values['fin1']
            liste.append(fin1) 
        
        
        if event == "boite1" :
            liste.append(9)
            window.extend_layout(window["elv"], [[sg.Button("manuelle3"),sg.Button("automatique3")]])
        if event=="manuelle3":
            liste.append("M")
        if event=="automatique3":
            liste.append("A")
            
            
        if event == "faite" :
            liste.append(10)
            window.extend_layout(window["elv"], [[sg.Button("oui"),sg.Button("non")]])
        if event=="oui":
            liste.append("Y")
        if event=="non":
            liste.append("N")
    
       
        print(liste)
        
    window.close()