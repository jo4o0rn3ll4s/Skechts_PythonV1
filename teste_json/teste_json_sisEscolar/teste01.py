import json

file = json.load(open('teste_json/teste_json_sisEscolar/teste01.json','r'))
ata = ('nomes','documentos','turmas')

for i in range(len(file['alunos'])):
    print(file['alunos'][ata[i]])
'''
print(file['alunos']['nomes'][1])
print(file['alunos']['documentos']['rg'][1])
print(file['alunos']['documentos']['cpf'][1])
print(file['alunos']['documentos']['cep'][1])
print(file['alunos']['turmas'][1])
'''