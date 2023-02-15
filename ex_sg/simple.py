import PySimpleGUI as sg

# Define o tema da janela como 'DarkAmber'
sg.theme('DarkAmber')

# Cria a ideia de design da interface
layout = [  [sg.Text('Um texto qualquer')],
            [sg.Text('Digite algo qualquer ->'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Cria o objeto 'janela' com a propriedade .Window
janela = sg.Window('Titulo', layout)

# Introduz um loop infinito para realizar a leitura da interface
# até que a mesma seja encerrada
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('Você digitou:', values[0])

# Encerramento da janela
janela.close()
