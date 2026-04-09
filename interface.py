import PySimpleGUI as sg    

tab1_layout =  [[sg.T('This is inside tab 1')]]    

tab2_layout = [[sg.T('This is inside tab 2')],    
               [sg.In(key='in')]]    

tab3_layout =  [[sg.Image(filename = "911.gif"), sg.Image(filename = "944.gif"), sg.Image(filename = "mazda.gif")]]   

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('élèves', tab2_layout), sg.Tab('Nos Voitures', tab3_layout)]], tooltip='TIP2')],    
          [sg.Button('Read')]]    


window = sg.Window('My window with tabs', layout, default_element_size=(100,100))    

while True:    
    event, values = window.read()    
    print(event,values)    
    if event == sg.WIN_CLOSED:
        break
