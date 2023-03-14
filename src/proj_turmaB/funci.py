import json
import PySimpleGUI as sg

caminho = 'src/proj_turmaB/data.json'
alunos = json.load(open(caminho))
cursos = ['Programação', 'Excel', 'Web Design', 'Robótica']

sg.theme('DarkAmber')
menu_def = [['Registros', ['Cadastrar Alunos', 'Atualizar Informações de um Aluno', 'Excluir Aluno']],
            ['Pesquisas', ['Listar todos os alunos']],
            ['Sair', ['Sair']]]


#Funcao para ler os arquivos do Json
def carregar_alunos():
    try:
        with open(caminho, 'r') as openfile:
            alunos = json.load(openfile)
            if len(alunos) == 0:
                sg.popup("Nenhum aluno cadastrado!")
                return None
            return alunos
    except:
        sg.popup("Erro ao carregar os alunos.")
        return None


#Funcao para escrever os arquivos do Json        
def salvar_alunos(alunos):
     with open(caminho, "w") as outfile: 
                json.dump(alunos, outfile, indent='\t')


#Funcao para cadastro de aluno
def cadastrar_aluno():
    layout = [[sg.Menu(menu_def, pad=(200,1))],
              [sg.Text('Digite o nome do aluno: '),sg.InputText(key='nome')],
              [sg.Text('Digite o sobrenome do aluno: '), sg.InputText(key='sobrenome')],
              [sg.Text('Digite a idade do aluno: '), sg.InputText(key='idade')],
              [sg.Text('Digite o CPF do aluno:'),sg.InputText(key='cpf')],
              [sg.Text('Selecione o curso desejado: '),sg.Combo(values=cursos, key='curso')],
              [sg.Button('Cadastrar')]]
    window = sg.Window('Cadastro de Aluno', layout)
    
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        if event == 'Cadastrar':
            alunos.append({"nome": values['nome'], "sobrenome": values['sobrenome'], "idade": values['idade'], "cpf": values['cpf'], "curso": values['curso']})
            salvar_alunos(alunos)
            sg.popup('Aluno cadastrado com sucesso!')
    
    window.close()


#Funcao para atualizar dados do aluno
def atualizar_aluno():
    layout=[[sg.Menu(menu_def, pad=(200,1))],
            [sg.Text('Digite o nome completo do Aluno a ser atualizado: '), sg.InputText(key='nome_completo')],
            [sg.Button('Buscar e Atualizar', key='bt')]]
    window = sg.Window('Atualizar Cadastro',layout)
    #nome_completo = input("Digite o nome completo do aluno a ser excluido: ")

    while True:
        event, values = window.read(timeout=100)

        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        if event == 'bt':
            nome, sobrenome = str(values['nome_completo']).split(' ',1)
            subs(nome, sobrenome)
    window.close()
def subs(nome, sobrenome):#interage com atualizar_aluno
    layout = [[sg.Text('Digite a nova idade do aluno: '),sg.InputText(key='idade')],
              [sg.Text('Digite o novo cpf do aluno: '),sg.InputText(key='cpf')],
              [sg.Text('Selecione o novo curso do aluno:'),sg.OptionMenu(values=cursos, key='curso')],
              [sg.Button('Atualizar', key = 'atu')]]
    windown = sg.Window('',layout)
    
    while True:
        event,values = windown.read(timeout=100)
        if event == sg.WIN_CLOSED:
            break
        if event == 'atu':
            for aluno in alunos:
                if aluno['nome'].lower() == nome.lower() and aluno['sobrenome'].lower() == sobrenome.lower():
                    aluno['idade'] = values['idade'] if values['idade'] != '' else aluno['idade']
                    aluno['cpf'] = values['cpf'] if values['cpf'] != '' else aluno['cpf']
                    aluno['curso'] = values['curso'] if values['curso'] != '' else aluno['curso']
                    salvar_alunos(alunos)
                    sg.popup(f"Informacoes do aluno {nome} {sobrenome} atualizadas com sucesso!",auto_close = True, auto_close_duration = 3)
                    windown.close()
                    return
            sg.popup(f"Não foi encontrado nenhum aluno com o nome {nome} {sobrenome}.")
    windown.close()


#Funcao para excluir aluno
def excluir_aluno():
    layout=[[sg.Menu(menu_def, pad=(200,1))],
            [sg.Text('Digite o nome completo do Aluno a ser excluido: '), sg.InputText(key='nome_completo')],
            [sg.Button('Buscar e Excluir', key='bt')]]
    window = sg.Window('Excluir do cadastro',layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        if event == 'bt':
            nome_completo = values['nome_completo']
            nome, sobrenome = nome_completo.split(' ', 1)
            for aluno in alunos:
                if aluno['nome'].lower() == nome.lower() and aluno['sobrenome'].lower() == sobrenome.lower():
                    alunos.remove(aluno)
                    salvar_alunos(alunos)
                    sg.popup(f"Aluno {nome_completo} excluído com sucesso!")
                    return
            sg.popup(f"Não foi encontrado nenhum aluno com o nome {nome_completo}.")
    
    
    window.close()


#Funcao para listar apenas os alunos em determinado curso
def listar_alunos():


    #busca e cria uma lista formatada para o sg.table
    alunos = json.load(open(caminho, 'r'))
    cols = ['nome','sobrenome','idade','cpf','curso']
    lastvalue = None
    data = list()
    
    layout = [[sg.Menu(menu_def, pad=(200,1))],
              [sg.Text('Listagem de Alunos no curso:'),sg.OptionMenu(values=['Todos']+ [i for i in cursos],default_value='Todos', key='opc')],
              [sg.Table(values = data ,headings = cols,key='tb',expand_x=True,expand_y=True,justification='right')]]
    window = sg.Window('Lista de Alunos', layout)

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        
        if values['opc'] != lastvalue:
            lastvalue = values['opc']
            data = list()
            window['tb'].update(values = data)
            if lastvalue != 'Todos':
                j = 0
                while j < len(alunos):
                    i = 0
                    mid = list()
                    if alunos[j]['curso'] == values['opc']:
                        while i < len(cols):
                            mid.append(alunos[j][cols[i]])
                            i += 1
                        data.append(mid)
                    j += 1
                window['tb'].update(values = data)
            else:
                j = 0
                while j < len(alunos):
                    i = 0
                    mid = list()
                    while i < len(cols):
                        mid.append(alunos[j][cols[i]])
                        i += 1
                    data.append(mid)
                    j += 1
                window['tb'].update(values = data)
    window.close()


#Funcao para definir qual professor pertence a cada curso
def professor_do_curso(curso):
    if curso.lower() == "programacao":
        return "Joao"
    elif curso.lower() == "excel":
        return "Maria"
    elif curso.lower() == "web design":
        return "Sergio"
    elif curso.lower() == "robotica":
        return "Lucas"
    else:
        return "Professor desconhecido"


#Menu 
'''while True:
    alunos = carregar_alunos()
    print("Selecione uma opcao:")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar informacoes de um aluno")
    print("3 - Excluir aluno")
    print("4 - Listar todos os alunos")
    print("5 - Sair")
    opcao = int(input())

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        atualizar_aluno()
    elif opcao == 3:
        excluir_aluno()
    elif opcao == 4:
        listar_alunos()
    elif opcao == 5:
        break
    else:
        print("Opcao invalida. Tente novamente.")'''
