menu = '''
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
'''

saldo= 0
limite= 500
numero_saques=0
limite_saques= 3
extrato= ""

while True:
    opcao= int(input(menu))

    if opcao==1:
        deposito= float(input("Informe o valor que irá depositar: "))
        if deposito>0:
            print ("Depósito de R$ {:.2f} realizado com sucesso!".format(deposito))
            saldo+=deposito
            extrato+= f"Depósito: R$ {deposito:.2f}\n"
        else:
            print ('Inválido')
    elif opcao==2:
        valor_saque= float(input("Informe o valor que deseja sacar: "))
        if (valor_saque<=saldo and valor_saque>0) and (valor_saque<=limite) and (limite_saques>0 and limite_saques<=3):
            saldo-=valor_saque
            print ("Saque de R$ {:.2f} realizado com sucesso!".format(valor_saque))
            numero_saques+=1
            limite_saques-=1
            extrato+= f"Saque: R$ {valor_saque: .2f}\n"

        else:
            print ("Operação negada!")
    elif opcao==3:
        if limite_saques==3 and numero_saques==0 and saldo==0:
            print ("Nenhuma operação realizada até o momento.")
        else:
            print ("=-=-=-=-=-=-=-=-= EXTRATO =-=-=-=-=-=-=-=-=")
            print ("Não foram realizadas movimentações." if not extrato else extrato)
            print ("Saldo atual: R$ {:.2f}".format(saldo))
            print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif opcao==4:
        break
    else:
        print ("Operação inválida. Tente novamente!")

