import PySimpleGUI as sg

sg.theme('DarkAmber')
menu_def = [['Janelas', ['Janela_A', 'Janela_B']],
            ['Sair', ['Sair']]]


def main():
    layout_main = [[sg.Menu(menu_def, pad=(200, 1))],
                   [sg.Text('Janela Principal'), sg.Input('digite algo')]]
    janelaMain = sg.Window('teste', layout_main)

    while True:
        event = janelaMain.read()[0]
        if event == sg.WIN_CLOSED or event == 'Sair':  # if user closes window or clicks cancel
            break
        if event == 'Janela_A':
            sg.popup('Evento Disparado -> Janela_A', title='TESTE DIZ')
        if event == 'Janela_B':
            sg.popup('Evento Disparado -> Janela_B', title='TESTE DIZ')
    janelaMain.close()

main()