import PySimpleGUI as sg

sg.theme('DarkAmber')

def login():
    layout = [[sg.Text('login'), sg.InputText(key='login')],
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
                sg.popup('Acesso Confirmado', auto_close=True, auto_close_duration=3)
                val = True
            else:
                val = False
                print(login, senha, values['login'],values['senha'])
                print('errado')

    window.close()
    return True if val else False