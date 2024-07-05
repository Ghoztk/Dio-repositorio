menu = """

d = Depositar
s = Sacar
e = Extrato
q = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))
        if valor >=1:
            saldo+= valor
            print(f"Deposito feito com sucesso. Seu novo saldo é: R${saldo:.2f}")
            extrato += f"\nDeposito: R${saldo:.2f}"
        else:
            print("ERROR")
    
    elif opcao == "s":
        saque = float(input("informe o valor do saque: "))
        
        if saque > saldo: print(f"Não é possivel sacar mais do que possui em saldo, atualmente possui {saldo:.2} de saldo, tente novamente")
        elif saque > limite: print(f"Não é possivel sacar uma quantia maior que o limite atual, atualmente possui {limite} de limite, tente novamente")
        elif numero_saques >= limite_saques: print(f"Não é possivel sacar mais pois passou do limite diario de saques, tente novamente mais tarde")

        elif valor >=1:
            numero_saques+=1
            print("Saque realizado com sucesso") 
            saldo-=saque
            print(f"Você possui: R${saldo:.2f} restante")
            extrato += f"\nSaque: R${saque:.2f}"
            print(f"numero de saques restantes: {limite_saques-numero_saques}")
        else:
            print("ERROR")  

    elif opcao == "e":
        print(" ")
        print("#### Extrato ####")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#################")
        
    elif opcao == "q":
        break

    else:
        print("Ocorreu um erro, tente novamente")