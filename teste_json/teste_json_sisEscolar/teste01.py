import json

file = json.load(open('teste_json/teste_json_sisEscolar/teste01.json','r'))
ata = ['nomes',['RG','CPF','CEP'],'turmas']
aluno = 0

for i in range(len(file['alunos'])):
    if i == 1:
        for j in range(3):
            print(file['alunos'][ata[i]][ata[i][j]][aluno])
    else:
        print(file['alunos'][ata[i]][aluno])
    

'''
print(file['alunos']['nomes'][1])
print(file['alunos']['documentos']['rg'][1])
print(file['alunos']['documentos']['cpf'][1])
print(file['alunos']['documentos']['cep'][1])
print(file['alunos']['turmas'][1])
'''