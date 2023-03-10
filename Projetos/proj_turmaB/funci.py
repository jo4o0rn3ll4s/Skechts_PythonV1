import json
import PySimpleGUI as sg

caminho = 'Projetos/proj_turmaB/data.json'
alunos = json.load(open(caminho))

sg.theme('DarkAmber')
menu_def = [['Registros', ['Cadastrar Alunos', 'Atualizar Informações de um Aluno', 'Excluir Aluno']],
            ['Pesquisas', ['Listar todos os alunos','Filtrar Alunos por curso']],
            ['Sair', ['Sair']]]


#Funcao para ler os arquivos do Json
def carregar_alunos():
    try:
        with open(caminho, 'r') as openfile:
            alunos = json.load(openfile)
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado!")
                return None
            return alunos
    except:
        print("Erro ao carregar os alunos.")
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
              [sg.Text('Selecione o curso desejado: '),sg.Combo(values=('Programacao', 'Excel', 'Web Design','Robotica'), key='curso')],
              [sg.Button('Cadastrar')]]
    window = sg.Window('Cadastro de Aluno', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
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
        event, values = window.read()
        nome, sobrenome = values['nome_completo'].split(' ', 1)
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        if event == 'bt':
            subs(nome, sobrenome)


    window.close()
def subs(nome, sobrenome):#interage com atualizar_aluno
    layout = [[sg.Text('Digite a nova idade do aluno: '),sg.InputText(key='idade')],
              [sg.Text('Digite o novo cpf do aluno: '),sg.InputText(key='cpf')],
              [sg.Text('Selecione o novo curso do aluno:'),sg.Combo(values=('Programacao', 'Excel', 'Web Design','Robotica'), key='curso')],
              [sg.Button('Atualizar', key = 'atu')]]
    windown = sg.Window('',layout)

    while True:
        event,values = windown.read()
        if event == 'atu':
            for aluno in alunos:
                if aluno['nome'].lower() == nome.lower() and aluno['sobrenome'].lower() == sobrenome.lower():
                    sg.popup(f"Atualizando informacoes do aluno {nome} {sobrenome}:")
                    aluno['idade'] = values['idade']
                    aluno['cpf'] = values['cpf']
                    aluno['curso'] = values['curso']
                    salvar_alunos(alunos)
                    sg.popup(f"Informacoes do aluno {nome} {sobrenome} atualizadas com sucesso!")
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


#Funcao para listar todos os alunos - ta quebrado, to com sono n sei o erro
def listar_alunos():
    
    alunos = carregar_alunos()
    cols = ['nome', 'sobrenome','idade','cpf','curso']
    #print(alunos[0]['nome'])
    data = list()
    i = 0
    while i < len(alunos):
        for j in cols:
            data.append(alunos[i][j])
        i+=1

    layout = [[sg.Menu(menu_def, pad=(200,1))],
              [sg.Text('Listagem de Alunos Cadastrados')],
              [sg.Table(values = data ,headings = cols,key='tb',expand_x=True,expand_y=True,justification='right')]]
    window = sg.Window('Lista de Alunos', layout)
    #carregar_alunos()
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
    window.close()
    return data

#Funcao para listar apenas os alunos em determinado curso
def filtrar_alunos_por_curso():
    curso = input("Digite o curso a ser filtrado (Programacao, Excel, Web Design ou Robotica): ")
    carregar_alunos()
    alunos_filtrados = [aluno for aluno in alunos if aluno['curso'].lower() == curso.lower()]
    if len(alunos_filtrados) == 0:
        print("Nao ha alunos cadastrados neste curso.")
    else:
        print(f"Alunos do curso de {curso}:")
        for aluno in alunos_filtrados:
            print(f"Nome: {aluno['nome']} {aluno['sobrenome']}, Idade: {aluno['idade']}, Cpf: {aluno['cpf']}, Professor: {professor_do_curso(aluno['curso'])}")


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
while True:
    alunos = carregar_alunos()
    print(len(alunos))
    print("Selecione uma opcao:")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar informacoes de um aluno")
    print("3 - Excluir aluno")
    print("4 - Listar todos os alunos")
    print("5 - Filtrar alunos por curso")
    print("6 - Sair")
    opcao = int(input())

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        atualizar_aluno()
    elif opcao == 3:
        excluir_aluno()
    elif opcao == 4:
        print(listar_alunos())
    elif opcao == 5:
        filtrar_alunos_por_curso()
    elif opcao == 6:
        break
    else:
        print("Opcao invalida. Tente novamente.")