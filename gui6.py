# cannon simulator
#player can enter (with SLIDERS) angle and velocity
#and must try to hit a given target

import PySimpleGUI as sg      

sg.ChangeLookAndFeel('GreenTan') 

layout = [ 
         [sg.Text('Raphaelas cannon simulator!', size=(30, 1), justification='center', font=("Helvetica", 35), relief=sg.RELIEF_RIDGE)],    
         [sg.Text("Triff ein Ziel, das 100 m entfernt ist", key="Entfernung")],
         [sg.Text("Winkel:"),          sg.Slider(key="Winkel", range=(1, 90), orientation='h', size=(34, 20), default_value=85)], 
         [sg.Text("Geschwindigkeit:"), sg.Slider(key="Geschwindigkeit",range=(1, 400), orientation='h', size=(34, 20), default_value=85)],  
         [sg.Text("Ergebnis", key="Ergebnis")],
         [sg.Button("Schuss"), sg.Button("Cancel")]
        ]
 
window = sg.Window('Everything bagel', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == "Schuss":
        print(values)
