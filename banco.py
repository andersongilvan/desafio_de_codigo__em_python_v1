import datetime

data_atual = datetime.datetime.now()



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



def depositar(valor):
    
     
        # Função para realizar um depósito na conta.

        # Parâmetros:
        # valor (float): O valor a ser depositado na conta.

        # Regras:
        # - O valor deve ser maior que zero.
        # - O saldo é atualizado com o valor depositado.
        # - Um registro do depósito é adicionado ao extrato.

        # Retorno:
        # - Exibe uma mensagem indicando o sucesso ou falha da operação.
    
    
    
    global saldo, extrato

    if valor > 0:
        
        saldo += valor
        print(f"\nDepósito no valor de R$ {valor:.2f} - {data_atual}\n")
        extrato += f"Depósito no valor de R$ {valor:.2f} - {data_atual}"
    else:
        print("O valor tem que ser maior que zero")


def sacar(valor):
    
    # Função para realizar um saque na conta.

    # Parâmetros:
    # valor (float): O valor a ser sacado da conta.

    # Regras:
    # - O valor deve ser maior que zero.
    # - O valor do saque deve ser menor ou igual ao limite de saque.
    # - O valor do saque deve ser menor ou igual ao saldo disponível.
    # - O número de saques diários não pode exceder o limite definido.
    
    
    global saldo, extrato, limite, LIMITE_SAQUES, numero_saques
    
    if valor > 0:
        if valor <= limite:
            if valor <= saldo:
                if numero_saques < LIMITE_SAQUES:
                    saldo -= valor
                    numero_saques += 1
                    
                    print(f"\nSaque no valo de R$ {valor:.2f} realizado com sucesso")
                    print(f"Saldo: R$ {saldo:.2f}")
                    extrato += f"\nSaque no valo de R$ {valor:.2f} realizado com sucesso - {data_atual}"
                else:
                    print("Você atingiu o limite de saques diário. Por favor tentar outro dia.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saque até R$ 500")
    else:
        print(f"O valor tem que ser maior que zero - {valor}")


def exibir_extrato():
    
    # Função para exibir o extrato da conta.

    # Regras:
    # - Exibe todas as operações realizadas na conta.
    # - Se não houver operações, informa que não existem registros.

    # Retorno:
    # - Exibe o extrato da conta.
    
    if len(extrato) == 0:
        print("\nNão existe operações nessa conta\n")
        
    else:    
        print("\nExtrato\n")
        print(extrato)