import PySimpleGUI as sg


def jalMain():
    """
    Função criadora de uma janela que contem 2 botões
    para chamar outras janelas, demonstrando então uma
    ideia de funcionamento de multiplas janelas no pySGui
    """
    
    # Seta o tema e o Layout da janela principal, depois 
    # cria o objeto 'janelaMain'
    sg.theme('DarkAmber')
    layMain = [[sg.Text('Texto'), sg.Input('Digite algo')],
               [sg.Button('JalA'), sg.Button('JalB')]]
    
    janelaMain = sg.Window('Janela Principal', layMain)

    # Realiza o loop infinito para ficar realizando a
    # leitura dos valores passados e dos eventos realizados
    while True:
        evento, valores = janelaMain.read()

        if evento == sg.WIN_CLOSED:
            break
        if evento == 'JalA':
            jalA()
        if evento == 'JalB':
            jalB()
    janelaMain.close()


def jalA():
    """
    Função criadora de uma janela nomeada 'janelaA' que
    tem como objetivo demonstrar o funcionamento de multiplas
    janelas graficas utilizando o pySGui
    """

    # Seta o tema e o Layout da janela A, depois cria o
    # objeto 'janelaA'
    sg.theme('DarkAmber')
    layA = [[sg.Text('Texto'), sg.Input('Digite algo')],
               [sg.Button('Janela_Main'), sg.Button('JalB')]]
    
    janelaA = sg.Window('Janela Principal', layA)

    # Realiza o loop infinito para ficar realizando a
    # leitura dos valores passados e dos eventos realizados
    while True:
        evento, valores = janelaA.read()

        if evento == sg.WIN_CLOSED:
            break
        if evento == 'Janela_Main':
            janelaA.close()
        if evento == 'JalB':
            janelaA.close()
            jalB()
    janelaA.close()


def jalB():
    """
    Função criadora de uma janela nomeada 'janelaB' que
    tem como objetivo demonstrar o funcionamento de multiplas
    janelas graficas utilizando o pySGui
    """

    # Seta o tema e o Layout da janela B, depois cria o
    # objeto 'janelaB'
    sg.theme('DarkAmber')
    layB = [[sg.Text('Texto'), sg.Input('Digite algo')],
               [sg.Button('JalA'), sg.Button('Janela_Main')]]
    
    janelaB = sg.Window('Janela Principal', layB)

    # Realiza o loop infinito para ficar realizando a
    # leitura dos valores passados e dos eventos realizados
    while True:
        evento, valores = janelaB.read()

        if evento == sg.WIN_CLOSED:
            break
        if evento == 'JalA':
            janelaB.close()
            jalA()
        if evento == 'Janela_Main':
            janelaB.close()
    janelaB.close()

jalMain()