
def vericpf(cpf):
    if False:#cpf <= 11111111111 or cpf >= 99999999999:
            return False
    else:
        sep = list()
        num = list()
        ckcpf = list()
        val = [0, 0, 0]
        dig = [0, 0, 0]
     
    #separa o numero com 11 casas decimais em uma lista com os digitos independentes
        for i in range(0,11):
            sep.insert(i, cpf//10**(10-i))
     
        num.insert(0,sep[0])
        for i in range(1,11):
            num.insert(i, sep[i]-sep[i-1]*10)
        
    #começa a etapa de verificação dos digitos
     
    #laço para reaçização dos testes nos 2 digitos finais
        for i in range(2, 0, -1):
            som = 0
            multi = 10 if i == 2 else 11
    #faz a multiplicação em decaimento partindo de 10 e depois de 11 a 2
            for j in range(0, 11-i, 1):
                ckcpf.insert(j, num[j]*multi)
                som = som + ckcpf[j]
                multi = multi - 1
    #armazenamento do valor calculado
            val.insert(i, som % 11)
            dig.insert(i, 0 if val[i] >= 10 else 11 - val[i])
            ckcpf.clear()
    #resposta da função
    return True if num[9] == dig[3] and num[10] == dig[1] else False