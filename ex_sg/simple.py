import PySimpleGUI as sg

# Define o tema da janela como 'DarkAmber'
sg.theme('DarkAmber')

# Cria a ideia de design da interface
layout = [  [sg.Text('Um texto qualquer')],
            [sg.Text('Digite o primeiro valor'), sg.InputText()],
            [sg.Text('Digite o segundo valor'), sg.InputText()],
            [sg.Button('Soma'), sg.Button('Subtrai')] ]

# Cria o objeto 'janela' com a propriedade .Window
janela = sg.Window('Titulo', layout)

# Introduz um loop infinito para realizar a leitura da interface
# até que a mesma seja encerrada
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Soma':
        va_soma = int(values[0]) + int(values[1])
        sg.popup(f'O valor da soma foi {va_soma}',grab_anywhere=True)
    

# Encerramento da janela
janela.close()
