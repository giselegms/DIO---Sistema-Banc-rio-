def menu():
    print ("------------- MENU -------------")
    print ("1- Depositar")
    print ("2- Sacar")
    print ("3- Extrato")
    print ("4- Criar usuário")
    print ("5- Criar conta corrente")
    print ("6- Listar contas")
    print ("7- Sair")
    print ("--------------------------------")
    opcao= int(input("Qual operação deseja realizar? "))
    return opcao

def depositar (saldo, valor, extrato, /):
    if valor>0:
        print ("Depósito de R$ {:.2f} realizado com sucesso!".format(valor))
        saldo+=valor
        extrato+= f"Depósito: R$ {valor:.2f}\n"
    else:
        print ("Operação negada!")
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques):
    if (valor<=saldo and valor>0) and valor<=limite and numero_saques<3:
        saldo-=valor
        print ("Saque de R$ {:.2f} realizado com sucesso!".format(valor))
        extrato+= f"Saque: R$ {valor:.2f}\n"
    else:
        print ("Operação negada!")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print ("=-=-=-=-=-=-=-=-= EXTRATO =-=-=-=-=-=-=-=-=")
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print ("Saldo atual: R$ {:.2f}".format(saldo))
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def criar_usuario(usuarios):
    nome= str(input("Nome: "))
    nascimento= input("Data de nascimento (dd/mm/aaaa): ")
    endereco= input("Endereço (Logradouro, nro - bairro - cidade/sigla estado): ")
    cpf= input ("CPF (Apenas números): ")
    usuario= filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Já existe usuário com esse CPF.")
        return

    usuarios.append({"nome": nome, "nascimento":nascimento, "cpf":cpf, "endereco": endereco})
    print ("Usuário criado!")

def filtrar_usuario(cpf, usuarios):
    filtros= [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return filtros[0] if filtros else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf= input ("CPF (Apenas números): ")
    usuario= filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print ("Usuário não encontrado! :(")

def listar_contas(contas):
    for conta in contas:
        print ("Agência: {}".format(conta['agencia']))
        print ("Conta: {}".format(conta['numero_conta']))
        print ("Titular: {}".format(conta['usuario']["nome"]))

def main():
    AGENCIA= "0001"

    saldo=0
    limite= 500
    numero_saques=0
    extrato= ""
    usuarios= []
    contas= []
    

    while True:
        opcao= menu()

        if opcao==1:
            valor= float(input("Valor do depósito: "))
            saldo, extrato= depositar(saldo, valor, extrato)
        
        elif opcao==2:
            valor= float(input("Valor do saque: "))
            saldo, extrato= sacar(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite=limite,
                numero_saques= numero_saques,
            )
            numero_saques+=1
        elif opcao==3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao==4:
            criar_usuario(usuarios)

        elif opcao==5:
            numero_conta= len(contas)+1
            conta= criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao==6:
            listar_contas(contas)

        elif opcao==7:
            break
        else:
            print ("Opção inválida!")

main()

