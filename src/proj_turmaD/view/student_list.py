import PySimpleGUI as sg
from service.database import aluno_service
from utils import categories_dict_to_string


class AlunoListScreen:
    def __init__(self) -> None:
        self.topRow = ["Nome", "Renach", "Categoria",
                       "Total de Parcelas", "Parcelas Pagas", "Status"]
        all_alunos = aluno_service.read()
        self.row = []
        for aluno in all_alunos:
            self.row.append(
                [
                    aluno["name"],
                    aluno["renach"],
                    categories_dict_to_string(aluno["categories"]),
                    aluno["total_instalment"],
                    aluno["paid_instalment"],
                    aluno["status"]
                ]
            )

        tbl1 = sg.Table(
            values=self.row,
            headings=self.topRow,
            auto_size_columns=True,
            justification='left',
            key='-TABLE-',
            enable_events=True,
            expand_x=True,
            expand_y=True,
        )
        self.layout = [[tbl1], [sg.Button('Voltar')]]
        self.window = sg.Window(
            'Lista de Alunos', self.layout, size=(800, 600), resizable=True)

    def close(self) -> None:
        self.window.close()

    def show(self) -> None:
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Voltar':
                self.close()
                break
            elif "+CLICKED+" in event:
                print(values['-TABLE-'][0])
