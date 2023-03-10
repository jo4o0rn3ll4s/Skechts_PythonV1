
import json as js
import pandas as pd

ende = 'proj_turmaD/db'
db_csv = pd.read_csv(ende +'.csv')
db_json = js.load(open(ende +'.json'))

'''
print(db_csv)
print('\n\n')
print(db_json)
'''

cod=list()

#print pesquisado pela cat
cont = 0
for i in db_json['cat']:
    print(cont, i)
    cont += 1
esc = int(input('Selecione o curso a pesquisar: '))

for i in range(len(db_json['cat'])):
    if esc == i:
        pesq = db_json['cat'][i]

for i in range(len(db_csv['nome'])):
    if db_csv['cat'][i] == pesq:
        cod.append(i)

for j in cod:
    for i in range(len(db_json['col'])):
        inter = db_csv[db_json['col'][i]][j]
        print(f'{inter:<10}',end=' ')
    print()
