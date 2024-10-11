def menu_():
    string = " Menu "
    length = 20 
    caracter_preenchimento = "="
    print(string.center(length, caracter_preenchimento))

def depositar(saldo):
    valor = int(input("\n Qual é o valor do depósito: "))
    if valor > 0:
        saldo += valor
        print(f"\nVocê depositou: R$ {valor}")
    else:
        print("Valor de depósito inválido.")
    return saldo

def sacar(saldo, limite, numero_saques, LIMITE_SAQUES):
    valor = int(input("Qual é o valor do saque: "))
    if valor > saldo:
        print("\nSaldo insuficiente para saque.")
    elif valor > limite:
        print("\nO valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("\nNúmero máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        print(f"Você sacou: R$ {valor}")
    else:
        print("Valor de saque inválido.")
    return saldo, numero_saques

def exibir_extrato(saldo):
    print(f"\nSeu saldo bancário é: R$ {saldo}")

def chooses(options, saldo, limite, numero_saques, LIMITE_SAQUES):
    if options == 'd':
        saldo = depositar(saldo)
    elif options == 's':
        saldo, numero_saques = sacar(saldo, limite, numero_saques, LIMITE_SAQUES)
    elif options == 'e':
        exibir_extrato(saldo)
    else:
        print("Opção inválida")
    return saldo, numero_saques

menu_()

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """
    print(menu)

    options = input("Escolha a opção: ")
    if options == 'q':
        print("Você escolheu sair. Até mais!")
        break

    saldo, numero_saques = chooses(options, saldo, limite, numero_saques, LIMITE_SAQUES)