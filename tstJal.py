import PySimpleGUI as sg

def main():
    sg.theme('DarkAmber')
    layout_main = [[sg.Text('Janela Principal')],
                   [sg.Button('Janela_A'),sg.Button('Janela_B')],
                   '''[sg.Button('Janela_C'),sg.Button('Janela_D')]''']
    
    janelaMain = sg.Window('teste', layout_main)

    while True:
        event = janelaMain.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
        if event == 'Janela_A':
           jalA()
        if event == 'Janela_B':
           jalB()
def jalA():
    sg.theme('DarkAmber')
    layout_main = [[sg.Text('Janela Principal')],
                   [sg.Button('Janela_A'),sg.Button('Janela_B')],
                   '''[sg.Button('Janela_C'),sg.Button('Janela_D')]''']
    
    janelaMain = sg.Window('teste', layout_main)

    while True:
        event = janelaMain.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
        if event == 'Janela_A':
           jalA()
        if event == 'Janela_B':
           jalB()