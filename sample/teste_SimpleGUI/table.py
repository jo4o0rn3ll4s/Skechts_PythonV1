import PySimpleGUI as sg
import json

sg.theme('DarkAmber')

data = list()
dt = json.load(open('Projetos/proj_turmaB/data.json'))
for i in dt:
    data.append(i)

cols = ['nome','sobrenome','idade','cpf','curso']

layout = [[sg.Text('Teste duplo')],
          [sg.Table(values = data, headings= cols)]]
janela = sg.Window('Teste', layout)

while True:
    events, values = janela.read()

    if events == sg.WIN_CLOSED:
        break

janela.close()