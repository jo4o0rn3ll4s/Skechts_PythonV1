'''
Cria tela de cadastro de alunos
File name: Aluno.py
'''

import PySimpleGUI as sg

import sqlite3

#from Capfoto import captura

from Capfoto import captura_window


import os

#Cria a variavel com o caminho do bando de dados
pastadados = os.path.dirname(os.path.abspath(__file__))+'\Dados\\'
pastafotos = os.path.dirname(os.path.abspath(__file__))+'\FotosAluno\\'

sg.theme('Reddit') #Define as cores da tela

#Conecta oa Banco de Dados
conn = sqlite3.connect(pastadados+'Banco.db')
cursor = conn.cursor()


sg.theme('Reddit') #Define as cores da tela


def aluno_window():
    
    # Primeira janela com 2 colunas
    layout_frame1 = [[sg.Text("Matric: "), sg.Input(key = '-matric-', size = (8,1), enable_events=True),
                                        sg.Button('Buscar', size=(7, 1), font='Arial 12', disabled = True),
                      ],
                     [sg.Text ('Aluno: '),sg.Input(key = '-aluno-', size = (40,1))],
                    ]
    
    coluna_um = [[sg.Frame("Dados", layout_frame1, size=(280, 200))],
                ]

    layout_frame2 = [#[sg.Image(filename=pastafotos+'Fotovazia.png', key='-image-', subsample=2)]
                     [sg.Image(filename=pastafotos+'Fotovazia.png', key='-image-', pad = 5, expand_x = True)]
                    ]

    coluna_dois = [
                   [sg.Frame("Foto", layout_frame2, size=(150, 200))],
                   [sg.Button('Capturar Foto', key='-bfoto-')]
                  ]

    # ----- Full layout -----
    layout = [[sg.Column(coluna_um),
                 sg.VSeperator(),
                 sg.Column(coluna_dois),],
                 [sg.Text ('')], 
                 [sg.Text(' ')],
                 [sg.Text ('', size = (3,1)),
                  sg.Button('Incluir', size=(8, 1), font='Arial 12', disabled = True),
                  sg.Text ('', size = (0,1)),
                  sg.Button('Alterar', size=(8, 1), font='Arial 12', disabled = True),
                  sg.Text ('', size = (0,1)),
                  sg.Button('Voltar', size=(8, 1), font='Arial 12', disabled = False), # Cria o botão desabilitado
                  sg.Text ('', size = (0,1)),
                  sg.Button('Excluir', size=(8, 1), font='Arial 12', disabled = True),
                  sg.Text ('', size = (0,1)),
                  sg.Button('Sair', size=(8, 1), font='Arial 12')]
              
             ]
    

    window = sg.Window("Cadastro de Alunos", layout, modal=True, size = (600,400))
    choice = None
    while True:
        linha = 0
        eventos, valores = window.read()
        if eventos == "Sair" or eventos == sg.WIN_CLOSED:
            break

        if eventos == "Voltar":
            window['-matric-'].update('') # Limpa o campo
            window['-aluno-'].update('') # Limpa o campo
            window['Buscar'].update(disabled = True) # Coloca o botão desativado
            window['Incluir'].update(disabled = True) # Coloca o botão desativado
            window['Alterar'].update(disabled = True) # Coloca o botão desativado
            window['Excluir'].update(disabled = True) # Coloca o botão desativado
            window['-image-'].update(filename=pastafotos+'Fotovazia.png') # Coloca a FOTO vazia
            
        # inserindo dados na tabela
        if eventos == "Incluir":
            query = (f""" INSERT INTO Aluno (Matric, Nome) VALUES ('{valores['-matric-']}', '{valores['-aluno-']}') """)
            cursor.execute(str(query))
            window['-matric-'].update('') # Limpa o campo
            window['-aluno-'].update('') # Limpa o campo
            window['Incluir'].update(disabled = True) # Coloca o botão desativado

            # valida as alterações feitas
            conn.commit()

        # alterar dados na tabela
        if eventos == "Alterar":
            query = (f"""UPDATE Aluno SET Nome = '{valores['-aluno-']}' WHERE Matric = '{valores['-matric-']}' """)
            cursor.execute(str(query))
            window['-matric-'].update('') # Limpa o campo
            window['-aluno-'].update('') # Limpa o campo
            window['Buscar'].update(disabled = True) # Coloca o botão desativado
            window['Incluir'].update(disabled = True) # Coloca o botão desativado
            window['Alterar'].update(disabled = True) # Coloca o botão desativado
            window['Excluir'].update(disabled = True) # Coloca o botão desativado
            

            # valida as alterações feitas
            conn.commit()


        # excluir dados na tabela
        if eventos == "Excluir":
            query = (f"""DELETE FROM Aluno WHERE Matric = '{valores['-matric-']}' """)
            cursor.execute(str(query))
            window['-matric-'].update('') # Limpa o campo
            window['-aluno-'].update('') # Limpa o campo
            window['Buscar'].update(disabled = True) # Coloca o botão desativado
            window['Incluir'].update(disabled = True) # Coloca o botão desativado
            window['Alterar'].update(disabled = True) # Coloca o botão desativado
            window['Excluir'].update(disabled = True) # Coloca o botão desativado
            

            # valida as alterações feitas
            conn.commit()
            
            if os.path.isfile(pastafotos+valores['-matric-']+'.png'):
                os.remove(pastafotos+valores['-matric-']+'.png')
                window['-image-'].update(filename=pastafotos+'Fotovazia.png') # Coloca a FOTO vazia
            
        if eventos == "-bfoto-":
            window.close()
            captura_window()

        if eventos == "-matric-" and valores['-matric-'] != '':
            window['Buscar'].update(disabled = False) # Coloca o botão ativado

        # buscar dados na tabela
        if eventos == "Buscar":
            #procura usuario na tabela usuario
            query = (f"""SELECT * FROM Aluno WHERE Matric = '{valores['-matric-']}' """)
            cursor.execute(str(query))

            #verifica se o query retornou alguma linha
            if cursor.fetchone() != None:
                cursor.execute(str(query))
                linha = cursor.fetchone() ## Joga o resultado na variável linha

                if linha != 0:
                    # valida o nome e a senha
                    if valores['-matric-'] == linha[0]:
                        window['-aluno-'].update(linha[1]) # Coloca o valor no INPUT -aluno-

                        #pega a foto do aluno#
                        if os.path.isfile(pastafotos+valores['-matric-']+'.png'):
                            window['-image-'].update(filename=pastafotos+valores['-matric-']+'.png') # Coloca a FOTO do aluno
                        else:
                            window['-image-'].update(filename=pastafotos+'Fotovazia.png') # Coloca a FOTO vazia
                        
                        window['Alterar'].update(disabled = False) # Coloca o botão ativado

                        window['Incluir'].update(disabled = True) # Coloca o botão desativado
                        window['Excluir'].update(disabled = False) # Coloca o botão ativado

            else:
                window['-aluno-'].update('') # Limpa o campo
                window['-image-'].update(filename=pastafotos+'Fotovazia.png', subsample=2) # Coloca a FOTO vazia
                window['Incluir'].update(disabled = False) # Coloca o botão ativado
                window['Alterar'].update(disabled = True) # Coloca o botão desativado
                window['Excluir'].update(disabled = True) # Coloca o botão desativado
        
    window.close()
