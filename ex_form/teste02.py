form = dict(per =  ['1 - meu nome é?',
                    '2 - minha idade é?',
                    '3- sou formado em?'], 
            opc = [ ['a- José', 'b- João', 'c- Jairo'],
                    ['a- 18','b- 19','c- 20'],
                    ['a- info','b- mec','c- el']],
            gab = ['b','b','c'])

resp = list()
point = 0

for i in range(3):
    print(form['per'][i])
    for j in range(3):
        print('{:<10}'.format(form['opc'][i][j]))
    print(i, j)
    inte = (input('Sua resposta: ')).lower()
    if inte == 'a' or inte == 'b' or inte == 'c':
        resp.append(inte)
    else:
        i -= 1

for i in range(3):
    point += 1 if form['gab'][i] == resp[i] else 0

print(resp, point)
