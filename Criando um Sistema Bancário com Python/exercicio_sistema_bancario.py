menu = f"""
        #####  MENU  ####
        DIGITE A OPÇÃO DESEJADA:
        [1] DEPÓSITO
        [2] SAQUE
        [3] EXTRATO
        [0] SAIR
"""
valores_deposito = []
valores_saques = []
qntd_depositos = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        deposito =  int(input("Digite o valor a ser depositado: "))
        if deposito <= 0:
            print("Valor inválido. Não foi possível realizar o depósito.")
        else:
            while True:
                confirma = int(input("""Confirma o depósito?
                    [1] SIM
                    [2] NÃO
                    """))
                if(confirma == 1):
                    saldo += deposito
                    valores_deposito.append(deposito)
                    qntd_depositos += 1
                    break
                else:
                    deposito = int(input("Digite o valor a ser depositado: "))
    elif opcao == "2":
        print("Saque")
        if(numero_saques == LIMITE_SAQUES):
            print("Valor diário de saques limites foi atingido. Tente outro dia.")
        else:
            valor_saque = int(input("Digite o valor a ser sacado: "))
            if(valor_saque > limite):
                print("Valor não permitido. Tente novamente.")
            else:
                while True:
                    confirma_saque = int(input("""Confirma o Saque?
                            [1] SIM
                            [2] NÃO
                            """))
                    if(confirma_saque == 1):
                        numero_saques += 1
                        saldo -= valor_saque   
                        valores_saques.append(valor_saque)     
                        break
                    else:
                        valor_saque = int(input("Digite o valor a ser sacado: "))
    elif opcao == "3":
        valores_deposito_formatados = ", ".join([f"R${valor:.2f}" for valor in valores_deposito])
        valores_saques_formatados = ", ".join([f"R${valor:.2f}" for valor in valores_saques])
        print("Extrato")
        print(f"""
        Seu saldo é R${saldo:.2f}
        Quantidade de depósitos realizados no dia {qntd_depositos}
        Valores depositados no dia {valores_deposito_formatados}
        Quantidade de saques realizados no dia {numero_saques}
        Valores sacados {valores_saques_formatados}
        """)
    elif opcao == "0":
        print("### FINALIZANDO ###")
        print(saldo)
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejadoa.")