'''
Cria tela principal do programa
File name: Principal.py
'''

import PySimpleGUI as sg

#from Principal2 import open_window
from Aluno import aluno_window

from Capfoto import captura_window

from Treino import getfotos

from ContaPessoas import conta_pessoas_window

from CapPessoa import captura_fotos

from Reconhece import reconhece_pessoas

sg.theme('Reddit') #Define as cores da tela

def main():
    
    # ------ Definição do Menu  ------ #
    menu_def = [#['&Cadastros', ['&Alunos', '&Professores', '&Funcionários', 'Fotos']],
                ['&Cadastros', ['&Alunos',  'Capturar Fotos', 'Conta Pessoas']],
                ['&Reconhecimento Facial', ['&Capturar', '&Treino', 'Reconhecer'], ],
                #['&Toolbar', ['---', 'Command &1', 'Command &2',
                #              '---', 'Command &3', 'Command &4']],
                ['S&air', ['S&air']]
               ]

    right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'Properties']]

    # ------ Definição do Layout  ------ #
    layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))] #coloca o Menu no Layout
             ]
    window = sg.Window("Controle de Entrada", layout).Finalize() # Precisa do Finaliza pra por a Tela em FullScreen
    window.Maximize() #Coloca a tela em FullScreen
    
    while True:
        eventos, valores = window.read()
        
        if eventos == "Sair" or eventos == sg.WIN_CLOSED:
            break

        if eventos == "Alunos":
            aluno_window()

        if eventos == "Capturar Fotos":
            captura_window()

        if eventos == "Conta Pessoas":
            conta_pessoas_window()

        if eventos == "Capturar":
            captura_fotos()
            
        if eventos == "Treino":
            getfotos()

        if eventos == "Reconhecer":
            reconhece_pessoas()                        
                    

        
    window.close()
if __name__ == "__main__":
    main()
  
