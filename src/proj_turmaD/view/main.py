import PySimpleGUI as sg
from . import AlunoListScreen
from . import AlunoFormScreen

menu_def = [['Arquivo', ['Abrir', 'Salvar', '---', 'Sair']]]


class MainScreen:
    def __init__(self) -> None:
        self.layout = [
            [sg.Menu(menu_def, pad=(200, 1))],
            [
                sg.Text('Sistema de Gerenciamento de Alunos',
                        size=(30, 1),
                        font=('Helvetica', 25),
                        justification='center')
            ],
            [sg.Button('Cadastrar Alunos',
                       size=(30, 2),
                       font=('Helvetica', 15))
             ],
            [sg.Button("Lista de Alunos",
                       size=(30, 2),
                       font=("Helvetica", 15))
             ],


        ]

        self.window = sg.Window('Sistema de Gerenciamento de Alunos', self.layout,
                                element_justification='c', finalize=True, size=(800, 600))
        self.window.maximize()

    def close(self) -> None:
        self.window.close()
        exit()

    def show(self) -> None:
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, 'Sair'):
                self.close()  # Fecha a janela e encerra o programa

            elif event == 'Cadastrar Alunos':
                aluno = AlunoFormScreen()
                aluno.show()

            elif event == 'Lista de Alunos':
                alunos = AlunoListScreen()
                alunos.show()

            elif event == 'Atualizar Informações de um Aluno':
                print("Atualizar Informações de um Aluno")
            elif event == 'Excluir aluno':
                print("Excluir aluno")
            elif event == 'Listar todos os alunos':
                print("Listar todos os alunos")
            else:
                sg.popup('Opção inválida. Tente novamente.')
