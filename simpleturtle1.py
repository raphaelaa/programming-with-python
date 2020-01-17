import PySimpleGUI as sg
import turtle

layout = [[sg.Text("Mein Wurfsimulator")],
          [sg.Text("Weite:"),sg. Input(key="fv",default_text=20,),
          sg.Text("Grad:"), sg.Input(key="rv", default_text=15)],
          [ sg.Text ("pencolor"), sg.Input(key="cv", default_text="#ff0000"),
          sg.Text("Dicke:"), sg.Input(key="sv", default_text=1)],
          [sg.Canvas ( size=(800, 500), key= "sandbox")],
          [sg.Button ("vorwärts"), sg.Button("links"), sg.Button("rechts"), sg.Button("clear"), sg.Button("home"), sg.Button("penup"), sg.Button("pendown")]]

window=sg.Window("My window", layout, finalize=True)
canvas= window["sandbox"]. TKCanvas

rosi= turtle.RawTurtle(canvas)
rosi.pencolor("#ff0000")  #red
rosi.shape("turtle")
rosi_speed= 20
rosi_dreh=15
while True:   #event loop
    event, values= window.read()
    if event is None:
        break
    #---input---
        
    #---buttons---
    if event=="pendown":
        rosi.pendown()
    if event=="penup":
        rosi.penup()
    if event== "home":
        rosi.home()
    if event== "clear":
        rosi.clear()
    if event == "vorwärts":
        #raw=values["cv"]
        try:
            rosi.pensize(values["sv"])
        except:
            rosi.pensize(1)
        rc = values["cv"]
        try:
            rosi.pencolor(rc)
        except:
            rosi.pencolor("#ff0000")
        raw=values["fv"]
        try:
            raw=int(raw)
        except:
            raw=20
        rosi.forward(raw)
    
        
    elif event=="links":
        raw=values["rv"]
        try:
            raw=int(raw)
        except:
            raw=20
        rosi.left(raw)
        
    elif event=="rechts":
        raw=values["rv"]
        try:
            raw=int(raw)
        except:
            raw=20
        rosi.right(raw)
        
window.close()
