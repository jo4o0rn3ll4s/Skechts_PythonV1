import PySimpleGUI as sg

sg.theme('DarkAmber')

layout1 = [[sg.Text('Janela Principal')],
           [sg.Button('Janela A')],
           [sg.Button('Janela B')]]

layout2 = [[sg.Text('Janela A')],
           [sg.Button('Janela Principal')],
           [sg.Button('Janela B')]]

layout3 = [[sg.Text('Janela B')],
           [sg.Button('Janela Principal')],
           [sg.Button('Janela A')]]

lis_lay = [layout1,layout2,layout3]

est = int(0)
janela = sg.Window('Teste', lis_lay[est])

while True:
    
    event = janela.read()[0]
    if event == sg.WIN_CLOSED:
        break
    if event == 'Janela A':
        est = 1
        janela = sg.Window('Teste', lis_lay[est])
    if event == 'Janela B':
        est = 2
        janela = sg.Window('Teste', lis_lay[est])
    if event == 'Janela Principal':
        est = 0
        janela = sg.Window('Teste', lis_lay[est])

