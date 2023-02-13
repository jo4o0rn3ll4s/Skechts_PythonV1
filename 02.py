ques = ['Meu nome é: ','Minha idade é: ']
resp = [['Maria','José','João'],['19','27','8']]

form = dict(perg = ques,esco = resp)

print(form['perg'][1])
for i in form['perg']:
    print(i)