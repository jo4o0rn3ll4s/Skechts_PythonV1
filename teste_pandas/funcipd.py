'''
Transformar em funções
#######################################################
#print em toda tabela
for i in cols:
    print(f'{i:<{tab}}',end=' ')
print('')
for j in range(len(df['Nomes'])):
    for i in range(len(cols)):
        print(f'{df[cols[i]][j]:<{tab}}',end=' ')
    print()
#######################################################
#seletor de opção
cont = 0
for i in opc:
    cont += 1
    print(cont, i)
esc = int(input('Selecione o curso a pesquisar: '))
for i in range(len(opc)):
    if esc == i:
        pesq = opc[i]
#######################################################
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
#######################################################
'''