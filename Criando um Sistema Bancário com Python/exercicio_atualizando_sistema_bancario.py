import random

clientes = []
contas = []
#Criar conta
def criar_conta(agencia, numero_conta, usuario, cpf):
    conta = {
        'agência' : agencia,
        'numero_conta' : numero_conta,
        'usuário' : usuario,
        'cpf' : cpf
    }
    contas.append(conta)

#Criar Usuário(Cliente)
def criar_cliente(nome, data_nasc, cpf, logradouro, nro, bairro, cidade, uf):
    cliente = {
        'nome' : nome,
        'data_nasc' : data_nasc,
        'cpf' : cpf,
        'endereço' : {
            'logradouro' : logradouro,
            'número' : nro,
            'bairro' : bairro,
            'cidade' : cidade,
            'uf' : uf
        }
        
    }
    clientes.append(cliente)

# Função para gerar um número de conta aleatório com 6 dígitos
def gerar_numero_conta():
    return str(random.randint(100000, 999999))

opc_1 = int(input("Você possui cadastro conosco? [1] PARA SIM [2] PARA NÃO"))
if opc_1 == 2:
    print("Cadastre-se agora:")
    nome = input("Digite Seu Nome: ")
    cpf = input("Digite seu CPF: ")
    data_nasc = input("Digite sua data de nascimento: ")
    print("Digite seu endereço: ")
    logradouro = input("Digite sua rua: ")
    nro = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a sua cidade: ")
    estado = input("Digite o Estado da sua cidade: ")
    criar_cliente(nome, data_nasc, cpf, logradouro, nro, bairro, cidade, estado)
    criar_conta('0001', gerar_numero_conta(), nome, cpf)

while True:
    opc_1 = int(input("Você deseja criar mais uma conta? [1] SIM  [2] NÃO"))
    if opc_1 == 1:
        criar_conta('0001', gerar_numero_conta(), nome, cpf)
        print("Conta gerada com sucesso!")
    elif opc_1 == 2:
        break


print(clientes)
print(contas)

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
extrato_str = ""  
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valores_deposito):
    deposito = int(input("Digite o valor a ser depositado: "))
    if deposito <= 0:
        print("Valor inválido. Não foi possível realizar o depósito.")
    else:
        while True:
            confirma = int(input("""Confirma o depósito?
                    [1] SIM
                    [2] NÃO
                    """))
            if confirma == 1:
                saldo += deposito
                valores_deposito.append(deposito)
                global qntd_depositos
                qntd_depositos += 1
                break
            else:
                deposito = int(input("Digite o valor a ser depositado: "))
    return saldo

def sacar(numero_saques, saldo, valores_saques):
    if numero_saques == LIMITE_SAQUES:
        print("Valor diário de saques limites foi atingido. Tente outro dia.")
    else:
        valor_saque = int(input("Digite o valor a ser sacado: "))
        if valor_saque > limite:
            print("Valor não permitido. Tente novamente.")
        else:
            while True:
                confirma_saque = int(input("""Confirma o Saque?
                        [1] SIM
                        [2] NÃO
                        """))
                if confirma_saque == 1:
                    numero_saques += 1
                    saldo -= valor_saque   
                    valores_saques.append(valor_saque)     
                    break
                else:
                    valor_saque = int(input("Digite o valor a ser sacado: "))
    return numero_saques, saldo

def mostrar_extrato(saldo, qntd_depositos, numero_saques, valores_deposito, valores_saques):
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

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        saldo = depositar(saldo, valores_deposito)
    elif opcao == "2":
        print("Saque")
        numero_saques, saldo = sacar(numero_saques, saldo, valores_saques)
    elif opcao == "3":
        mostrar_extrato(saldo, qntd_depositos, numero_saques, valores_deposito, valores_saques)
    elif opcao == "0":
        print("### FINALIZANDO ###")
        print(saldo)
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



