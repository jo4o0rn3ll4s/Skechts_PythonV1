import pandas as pd

mid = list()
pos_mid = list()

df = pd.read_csv('teste_pandas/02.csv')

mid.append('nome')

for i in df['nome']:
    mid.append(i)

pos_mid.append('b')
mid.append(pos_mid)

pos_mid.append('d')
mid.append(pos_mid)


print(mid)

dg = pd.DataFrame(mid)
dg.to_csv('teste_pandas/02.csv', index=False)