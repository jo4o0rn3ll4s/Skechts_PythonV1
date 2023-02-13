import PySimpleGUI as sg


def main():
    sg.theme('DarkAmber')
    layout_main = [[sg.Text('Janela Principal')],
                   [sg.Button('Janela_A'), sg.Button('Janela_B')]]

    janelaMain = sg.Window('teste', layout_main)

    while True:
        event = janelaMain.read()[0]
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == 'Janela_A':
            #janelaMain.close()
            jalA()
        if event == 'Janela_B':
            #janelaMain.close()
            jalB()
    janelaMain.close()


def jalA():
    sg.theme('DarkAmber')
    layout_A = [[sg.Text('Janela A')],
                [sg.Button('Janela_Main'), sg.Button('Janela_B')]]

    janelaA = sg.Window('teste', layout_A)

    while True:
        event = janelaA.read()[0]
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == 'Janela_Main':
            janelaA.close()
            #main()
        if event == 'Janela_B':
            janelaA.close()
            jalB()
    janelaA.close()


def jalB():
    sg.theme('DarkAmber')
    layout_B = [[sg.Text('Janela B')],
                [sg.Button('Janela_Main'), sg.Button('Janela_A')]]

    janelaB = sg.Window('teste', layout_B)

    while True:
        event = janelaB.read()[0]
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == 'Janela_Main':
            janelaB.close()
            #main()
        if event == 'Janela_A':
            janelaB.close()
            jalA()
    janelaB.close()


main()
