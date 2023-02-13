import PySimpleGUI as sg


def main():
    sg.theme('DarkAmber')
    layout_main = [[sg.Text('Janela Principal')],
                   [sg.Button('Janela_A'), sg.Button('Janela_B')],
                   '''[sg.Button('Janela_C'),sg.Button('Janela_D')]''']

    janelaMain = sg.Window('teste', layout_main)

    while True:
        event = janelaMain.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == 'Janela_A':
            jalA()
        if event == 'Janela_B':
            jalB()
    janelaMain.close()


def jalA():
    sg.theme('DarkAmber')
    layout_A = [[sg.Text('Janela A')],
                [sg.Button('Janela_Main'), sg.Button('Janela_B')],
                '''[sg.Button('Janela_C'),sg.Button('Janela_D')]''']

    janelaA = sg.Window('teste', layout_A)

    while True:
        event = janelaA.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == 'Janela_Main':
            main()
        if event == 'Janela_B':
            jalB()
    janelaA.close()


def jalB():
    sg.theme('DarkAmber')
    layout_B = [[sg.Text('Janela B')],
                [sg.Button('Janela_Main'), sg.Button('Janela_A')],
                '''[sg.Button('Janela_C'),sg.Button('Janela_D')]''']

    janelaB = sg.Window('teste', layout_B)

    while True:
        event = janelaB.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == 'Janela_Main':
            main()
        if event == 'Janela_A':
            jalA()
    janelaB.close()


main()
