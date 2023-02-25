'''
from database import form
'''
import json
form = json.load(open('ex_form/teste02.json', 'r'))

resp = list()
point = 0
i = 0

while i < len(form['per']):
    
    print(form['per'][i])
    
    for j in range(3):
        print('{:<10}'.format(form['opc'][i][j]))
    
    inter = (input('Sua resposta: ')).lower()
    if inter == 'a' or inter == 'b' or inter == 'c':
        resp.append(inter)
        i += 1
    else:
        print('\nresponda com uma das opções oferecidas\n')

for i in range(len(form['gab'])):
    point += 1 if form['gab'][i] == resp[i] else 0

print(resp, point)
