import json
base = json.load(open('teste_json/teste03.json', 'r'))

point = 0
resp = list()

i = 0
while i < len(base['form']):
    
    print(base['form'][i]['per'])

    for j in base['form'][i]['opc']:
        print(j)
    resp.append(int(input('-> ')))
    print('\n')
    i+=1

#print(resp)

for k in range(len(base['form'])):
    point += 1 if resp[k] == base['form'][k]['gab'] else 0
    print(point,' ',resp[k],' ',base['form'][k]['gab'])

print('\033[32;40mAPROVADO\033[m' if point >= 2 else '\033[31;40mREPROVADO\033[m')