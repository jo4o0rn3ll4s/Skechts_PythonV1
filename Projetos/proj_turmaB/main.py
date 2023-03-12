import PySimpleGUI as sg
from funci import *
from login import login

menu_def = [['Registros', ['Cadastrar Alunos', 'Atualizar Informações de um Aluno', 'Excluir Aluno']],
            ['Pesquisas', ['Listar todos os alunos']],
            ['Sair', ['Sair']]]
# Define o layout da interface gráfica
def main():
    layout = [[sg.Menu(menu_def, pad=(200,1))]]

    # Cria a janela da interface gráfica
    window = sg.Window('Sistema de Gerenciamento de Alunos',layout, element_justification='c',finalize=True)
    window.maximize()

    # Loop principal do programa
    while True:
        event, values = window.read()

        if event in(sg.WIN_CLOSED,'Sair'):
            break
        elif event == 'Cadastrar Alunos':
            cadastrar_aluno()
        elif event == 'Atualizar Informações de um Aluno':
            atualizar_aluno()
        elif event == 'Excluir aluno':
            excluir_aluno()
        elif event == 'Listar todos os alunos':
            listar_alunos()
        else:
            sg.popup('Opção inválida. Tente novamente.')

    # Fecha a janela da interface gráfica
    window.close()

if login():
    main()
else:
    sg.popup('Erro!')