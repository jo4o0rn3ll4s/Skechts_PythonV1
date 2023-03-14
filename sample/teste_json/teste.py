import json

with open('teste_json/teste.json', 'r') as trans:
    teste = json.load(trans)

print(teste)

nome = input('Digite um nome: ')
idade = input('Digite sua idade')

teste = (dict(nome = nome, idade= idade))

with open('teste_json/teste.json', 'w') as trans:
    json.dump(teste, trans, indent='\t')

with open('teste_json/teste.json', 'r') as trans:
    teste = json.load(trans)

print(teste)