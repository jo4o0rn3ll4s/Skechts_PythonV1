import pandas as pd

turma = 1 #1 ou 2
df = pd.read_csv('teste_pandas/teste_pd - Página'+str(turma)+'.csv')

cols = ('Nomes','RG','CPF','CEP','Curso')
opc = ['programacao','excel','manutencao','informatica']
tab = 28
cod = list()
pesq = int

print(df)

'''
#print em toda tabela
for i in cols:
    print(f'{i:<{tab}}',end=' ')
print('')
for j in range(len(df['Nomes'])):
    for i in range(len(cols)):
        print(f'{df[cols[i]][j]:<{tab}}',end=' ')
    print()
'''
cont = 0
for i in opc:
    print(cont, i)
    cont += 1
esc = int(input('Selecione o curso a pesquisar: '))
for i in range(len(opc)):
    if esc == i:
        pesq = opc[i]

#print pesquisado pelo curso
for i in range(len(df['Nomes'])):
    print(df['Curso'][i])
    if df['Curso'][i] == pesq:
        cod.append(i)

for i in cols:
    print(f'{i:<{tab}}',end=' ')
print('')
for j in cod:
    for i in range(len(cols)):
        print(f'{df[cols[i]][j]:<{tab}}',end=' ')
    print()
