import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')

# STEP 1 define the layout
layout = [ 
            [sg.Push(), sg.Text('Índice de massa corpórea'), sg.Push()],
            [sg.Text('Massa:'), sg.Input(key='-MASS-', size=(35, 1))],
            [sg.Text('Altura:'), sg.Input(key='-HEIGHT-', size=(35, 1))],
            [sg.Push(), sg.Button('Calcular'), sg.Push()],
         ]

#STEP 2 - create the window
window = sg.Window('IMC', layout = layout, font='Monaco 18')

# STEP3 - the event loop
while True:
    event, value = window.read()   
    print(event, value)
    massa=float(value['-MASS-'])
    altura=float(value['-HEIGHT-'])
    imc = massa / (altura**2)
    sg.Popup(f'Seu IMC é {imc:.2f})', font='26')
    if event == 'QUIT' or event == sg.WIN_CLOSED:
      break
