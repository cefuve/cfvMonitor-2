# by cefuve electronics
# Github: https://www.github.com/cefuve
# Webpage: https://www.cefuve.com

import serial, sys, time
import PySimpleGUI as sg
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
puertos = []
conectado = False
Arduino = None

#Get port devices
for p in ports:
    puertos.append(p.device)

#Configure app windows
sg.theme('DarkAmber')

col_1 = [[sg.Text("PIN", size=(3,1))],
         [sg.Text("D13")],
         [sg.Text("D12")],
         [sg.Text("D11")],
         [sg.Text("D10")],
         [sg.Text(" D9")],
         [sg.Text(" D8")]]

dir_1 = [[sg.Text("DIR", size=(3,1))],
         [sg.Text(" in ",key='d13')],
         [sg.Text(" in ",key='d12')],
         [sg.Text(" in ",key='d11')],
         [sg.Text(" in ",key='d10')],
         [sg.Text(" in ",key='d9')],
         [sg.Text(" in ",key='d8')]]

state_1 = [[sg.Text("ST", size=(2,1))],
          [sg.Text("[  ]",key='p13')],
          [sg.Text("[  ]",key='p12')],
          [sg.Text("[  ]",key='p11')],
          [sg.Text("[  ]",key='p10')],
          [sg.Text("[  ]",key='p9')],
          [sg.Text("[  ]",key='p8')]]

col_2 = [[sg.Text("PIN", size=(3,1))],
         [sg.Text(" D7 ")],
         [sg.Text(" D6")],
         [sg.Text(" D5")],
         [sg.Text(" D4")],
         [sg.Text(" D3")],
         [sg.Text(" D2")],
         [sg.Text(" RX")],
         [sg.Text(" TX")]]

dir_2 = [[sg.Text("DIR", size=(3,1))],
         [sg.Text(" in ",key='d7')],
         [sg.Text(" in ",key='d6')],
         [sg.Text(" in ",key='d5')],
         [sg.Text(" in ",key='d4')],
         [sg.Text(" in ",key='d3')],
         [sg.Text(" in ",key='d2')],
         [sg.Text(" in ",key='d1')],
         [sg.Text("out",key='d0')]]

state_2 = [[sg.Text("ST", size=(2,1))],
           [sg.Text("[  ]",key='p7')],
           [sg.Text("[  ]",key='p6')],
           [sg.Text("[  ]",key='p5')],
           [sg.Text("[  ]",key='p4')],
           [sg.Text("[  ]",key='p3')],
           [sg.Text("[  ]",key='p2')],
           [sg.Text("[  ]",key='p1')],
           [sg.Text("[  ]",key='p0')]]

portd = [[sg.Text("PORTD", size=(6,1))],[sg.Text("     D.5")],[sg.Text("     D.4")],[sg.Text("     D.3")],[sg.Text("     D.2")],[sg.Text("     D.1")],[sg.Text("     D.0")]]
portb = [[sg.Text("PORTB", size=(6,1))],[sg.Text("     B.7")],[sg.Text("     B.6")],[sg.Text("     B.5")],[sg.Text("     B.4")],[sg.Text("     B.3")],[sg.Text("     B.2")],[sg.Text("     B.1")],[sg.Text("     B.0")]]

layout = [[sg.Text("Select Port:"), sg.Combo(puertos, enable_events=True, key='combo', size=(6,1)), sg.Button("Open")],
          [sg.Text("")],
          [sg.Frame(layout=portd, title='', pad=(0,0)), sg.Frame(layout=col_1, title='', pad=(0,0)), sg.Frame(layout=dir_1, title='', pad=(0,0)), sg.Frame(layout=state_1, title='', pad=(0,0))],
          [sg.Frame(layout=portb, title='', pad=(0,0)), sg.Frame(layout=col_2, title='', pad=(0,0)), sg.Frame(layout=dir_2, title='', pad=(0,0)), sg.Frame(layout=state_2, title='', pad=(0,0))],
          [sg.Text("")],
          [sg.Button("Exit", size=(10,1)), sg.Button("?")]]

center = [[sg.Column(layout, element_justification='center')]]

window = sg.Window("cfvMonitor v2.0", center)
 
#Function that create about window
def open_about():
    layout = [[sg.Text('::[ Information ]::..')],
              [sg.Text('PORT is microcontroller register for pin manipulation.')],
              [sg.Text('BIT is microcontroller port register address.')],
              [sg.Text('PIN is Arduino number id for port\'s bit.')],
              [sg.Text('DIR is port\'s pin direction (INPUT or OUTPUT).')],
              [sg.Text('ST is port\'s pin state (HIGH or LOW).')],
              [sg.Text('')],
              [sg.Text('::[ Credits ]::..')],
              [sg.Text('by cefuve electronics')],
              [sg.Text('www.cefuve.com')],
              [sg.Text('2021')],]

    return sg.Window('About...', layout)


#Infinite loop
while True:
    event, values = window.read(timeout=0)

    #Get info from serial and trim
    if conectado == True:
        received = ascii(Arduino.readline())
        data = received[2:-5]
        #print(data)
        if data[0] == 'P':
            for i in range(14):
                if data[i+1] == '1':
                    window['p'+str(i)].update('[■]')
                else:
                    window['p'+str(i)].update('[  ]')
        
        if data[0] == 'D':
            for i in range(2,14):
                if data[i+1] == '1':
                    window['d'+str(i)].update('out ')
                else:
                    window['d'+str(i)].update(' in ')

    #Connecting to selected port
    if event == "Open" and values['combo'] != "":
        try:
            serial.Serial.close()
        except:
            pass
        port = values['combo']
        Arduino = serial.Serial(port, 115200, timeout=1.0)
        data = ascii(Arduino.readline())
        Arduino.close()
        if len(data) > 5:
            conectado = True
            Arduino = serial.Serial(port, 115200)
            sg.popup_auto_close('Connected.', auto_close_duration=1.5)
        else:
            Arduino.close()
            conectado = False
            sg.Popup('No cfvMonitor configured...', keep_on_top=True)

    #Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    #About button
    if event == "?":
        about = open_about()
        event2, values2 = about.read(timeout=0)

#Finalize app
window.close()
    