import PySimpleGUI as sg
from bases import logopy,check,cancel,gifpy

sg.theme('Reddit')
confBot = (sg.theme_background_color(),sg.theme_background_color(),sg.theme_border_width(0))
# Cria a ideia de design da interface
layout = [  [sg.Text('Um texto qualquer')],
            [sg.Text('Digite algo qualquer ->'), sg.InputText()],
            [sg.Button('',image_data=check,key='Ok',button_color=confBot), sg.Button('',image_data=cancel,key='Cancel',button_color=confBot)]]

# Cria o objeto 'janela' com a propriedade .Window
janela = sg.Window('Titulo', layout, icon=logopy)

# Introduz um loop infinito para realizar a leitura da interface
# até que a mesma seja encerrada
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        print('Você digitou:', values[0])

# Encerramento da janela
janela.close()
