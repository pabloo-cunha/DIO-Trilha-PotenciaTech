saldo = 0
saque_diario = 0
extrato = []

def depositar():
    global saldo
    valor = float(input('Digite o valor a ser depositado: '))
    descricao = input('descricao: ')
    if valor > 0:
        saldo += valor
        extrato.append(f'''
                       deposito: {valor}
                       descrição: {descricao}
                       ''')
    else:
        print('Valor invalido')


def sacar():
    global saldo
    global saque_diario
    if saque_diario < 3:
        valor = float(input('Digite o valor de saque: '))
        if valor <= saldo and valor <= 500:
            descricao = str(input('descrição: '))
            saldo -= valor
            saque_diario +=1
            extrato.append(f'''
                       saque: {valor}
                       descrição: {descricao}
                       ''')
        else:
            print('saque não permitido')
    else:
        print('Operação diaria excedida')      
    

def extrair_extrato():
    print(extrato)



while True:
    print((
        '''
        Escolha uma opção:
            1 - Depositar
            2 - Sacar
            3 - Extrato
            4 - Saldo
            5 - Sair'''))
    
    
    op = int(input('Digite a opção escolhida: '))
    
    if op == 1:
        depositar()
    elif op == 2:
        sacar()
    elif op == 3:
        if len(extrato) == 0:
            print('sem movimentacao')
        else:
            for x in extrato:
                print(x)
            
    elif op == 4:
        print(f'Saldo: {saldo}')
        
    elif op == 5:
        print('Até mais!')
        break
    else:
        print('operação invalida.')
        continue