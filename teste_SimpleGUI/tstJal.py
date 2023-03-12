import PySimpleGUI as sg

sg.theme('DarkAmber')
menu_def = [['Janelas', ['Janela_Main', 'Janela_A', 'Janela_B']],
            ['Sair', ['Sair']]]

def login():   
    layout =[[sg.Text('login'), sg.InputText(key='login')],
             [sg.Text('Senha'), sg.InputText(key = 'senha')],
             [sg.Button('Sair'), sg.Button('Entrar')]]

    window = sg.Window ( 'CVTI SYSTEM 2023', layout)

    login = 'a'
    senha = '123'

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        if event == 'Entrar':
            if values['login'] == login and values['senha'] == senha:
                val = True
                window.close()
            else:
                val = False
                sg.popup('Login invalido', title='ERRO')

    window.close()
    return True if val else False

def main():
    layout_main = [[sg.Menu(menu_def, pad=(200, 1))],
                   [sg.Text('Janela Principal'), sg.Input('digite algo')],
                   [sg.Button('Janela_A'), sg.Button('Janela_B')]]

    janelaMain = sg.Window('teste', layout_main).finalize()
    janelaMain.maximize()

    while True:
        event = janelaMain.read()[0]
        if event == sg.WIN_CLOSED or event == 'Sair':  # if user closes window or clicks cancel
            break
        if event == 'Janela_A':
            jalA()
        if event == 'Janela_B':
            jalB()
    janelaMain.close()

def jalA():
    layout_A = [[sg.Text('Janela A')],
                [sg.Menu(menu_def, pad=(200, 1))],
                [sg.Button('Janela_Main'), sg.Button('Janela_B')]]

    janelaA = sg.Window('teste', layout_A, size=(300, 200))

    while True:
        event = janelaA.read()[0]
        if event == sg.WIN_CLOSED or event == 'Sair':  # if user closes window or clicks cancel
            break
        if event == 'Janela_Main':
            janelaA.close()
        if event == 'Janela_B':
            janelaA.close()
            jalB()

    janelaA.close()


def jalB():
    layout_B = [[sg.Menu(menu_def, pad=(200, 1))],
                [sg.Text('Janela B')],
                [sg.Button('Janela_Main'), sg.Button('Janela_A')]]

    janelaB = sg.Window('teste', layout_B, size=(300, 200))

    while True:
        event = janelaB.read()[0]
        if event == sg.WIN_CLOSED or event == 'Sair':  # if user closes window or clicks cancel
            break
        if event == 'Janela_Main':
            janelaB.close()
        if event == 'Janela_A':
            janelaB.close()
            jalA()
    janelaB.close()

if login():
    main()
