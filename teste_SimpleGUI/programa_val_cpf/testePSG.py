import PySimpleGUI as sg
#import valcpf as cc
import funciCPF as cc

sg.theme('Reddit')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Digite seu CPF para consulta :'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('VALIDADOR DE CPF', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        if cc.vericpf(int(values[0])):
            sg.popup('CPF Valido', title='VALIDADOR DE CPF DIZ')
        else:
            sg.popup('CPF Invalido', title='VALIDADOR DE CPF DIZ')

window.close()