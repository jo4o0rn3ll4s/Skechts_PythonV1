import PySimpleGUI as sg

from service.database import aluno_service
from utils import categories_dict_to_string


class AlunoFormScreen:
    def __init__(self) -> None:
        self.layout = [[sg.Text('Nome', size=(15, 1)), sg.InputText(key='nome')],
                       [sg.Text('Renach', size=(15, 1)),
                        sg.InputText(key='renach')],
                       [sg.Text('Categorias', size=(15, 1)),
                        sg.Checkbox('A', key='A'), sg.Checkbox('B', key='B'), sg.Checkbox(
                            'C', key='C'), sg.Checkbox('D', key='D'), sg.Checkbox('E', key='E')
                        ],
                       [sg.Text('Total de Parcelas', size=(15, 1)),
                        sg.InputText(key='total')],
                       [sg.Button('Cadastrar'), sg.Button('Cancelar')]]

        self.window = sg.Window('Cadastrar Aluno', self.layout)

    def close(self) -> None:
        self.window.close()

    def valid(self, name, renach, categories, total_instalment):
        if name is None or renach is None or total_instalment is None or categories is None:
            return False

        if name == "" or renach == "" or total_instalment == "":
            return False

        if len(name) < 3:
            return False

        if len(renach) != 11:
            return False

        if not categories['A'] and not categories['B'] and not categories['C'] and not categories['D'] and not categories['E']:
            return False

        if int(total_instalment) < 1:
            return False

        return True

    def show(self) -> None:
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.close()  # Fecha a janela e encerra o programa
                break  # Sai do loop

            elif event == 'Cadastrar':
                categories = dict(
                    A=values['A'], B=values['B'], C=values['C'], D=values['D'], E=values['E']
                )
                if self.valid(values['nome'], values['renach'], categories, values['total']):

                    aluno_service.insert(
                        values['nome'], values['renach'], categories, values['total']
                    )
                    print("Aluno cadastrado com sucesso!")
                    self.close()
                else:
                    sg.popup('Dados inválidos. Tente novamente.',
                             auto_close=True, auto_close_duration=3)
