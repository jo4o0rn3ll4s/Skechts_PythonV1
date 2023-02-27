import pandas as pd

df = pd.read_csv('teste_pandas/teste_pd - Página1.csv')
cols = ('Nomes','RG','CPF','CEP','Curso')

for i in cols:
    print(i,end=' ')
print('')
for i in range(len(cols)):
    print(df[cols[i]][0],end=' ')

print(df['Nomes'][0])
