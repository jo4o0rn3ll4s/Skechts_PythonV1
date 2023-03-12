import PySimpleGUI as sg

# Layout da janela principal
layout = [
    [sg.Menu([['Menu', ['Tela 1', 'Tela 2', 'Tela 3']]])],
    [sg.Column([[] for _ in range(3)], element_justification='c', expand_x=True, expand_y=True)]
]

# Cria a janela principal
window = sg.Window('Janela Principal', layout, element_justification='c',finalize=True)
window.maximize()

# Loop principal
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Tela 1':
        # Layout da Tela 1
        layout_tela1 = [
            [sg.Text('Tela 1')],
            [sg.Button('Fechar')]
        ]
        # Cria a janela da Tela 1
        window_tela1 = sg.Window('Tela 1', layout_tela1, size=(400, 300), element_justification='c')
        # Loop da Tela 1
        while True:
            event_tela1, values_tela1 = window_tela1.read()
            if event_tela1 == sg.WIN_CLOSED or event_tela1 == 'Fechar':
                window_tela1.close()
                break
    elif event == 'Tela 2':
        # Layout da Tela 2
        layout_tela2 = [
            [sg.Text('Tela 2')],
            [sg.Button('Fechar')]
        ]
        # Cria a janela da Tela 2
        window_tela2 = sg.Window('Tela 2', layout_tela2, size=(400, 300), element_justification='c')
        # Loop da Tela 2
        while True:
            event_tela2, values_tela2 = window_tela2.read()
            if event_tela2 == sg.WIN_CLOSED or event_tela2 == 'Fechar':
                window_tela2.close()
                break
    elif event == 'Tela 3':
        # Layout da Tela 3
        layout_tela3 = [
            [sg.Text('Tela 3')],
            [sg.Button('Fechar')]
        ]
        # Cria a janela da Tela 3
        window_tela3 = sg.Window('Tela 3', layout_tela3, size=(400, 300), element_justification='c')
        # Loop da Tela 3
        while True:
            event_tela3, values_tela3 = window_tela3.read()
            if event_tela3 == sg.WIN_CLOSED or event_tela3 == 'Fechar':
                window_tela3.close()
                break

# Fecha a janela principal
window.close()
