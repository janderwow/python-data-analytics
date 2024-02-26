'''saldo = 50

def sacar(valor):
    if saldo >= valor:
        print("Valor sacado")
    elif saldo < valor:
        print("Saldo Insuficiente")

sacar(100)
'''
'''
IDADE_MININA = 18

idade = int(input("Informe sua idade: "))

if idade >= IDADE_MININA:
    print("Pode tirar habilitação")
else:
    print("Não pode tirar habilitação")
'''

# if aninhado
tipo_conta = int(input("Selecione o tipo de conta: [1] - Normal [2] - Conta Universitária: "))
saldo = 100
cheque_especial = 500
saque = 100

if tipo_conta == 1:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial")
    else:
        print("Não foi possível realizar o saque")
elif tipo_conta == 2:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")

else:
    print("Sistema não reconheceu seu tipo de conta. Entre em contato com seu gerente")
            

#if ternario
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
