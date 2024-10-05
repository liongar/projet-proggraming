import random

saldo = 0
times = ['flamengo', 'fortaleza', 'bahia', 'cruzeiro', 'guarani', 'palmeiras', 'cuiabá', 'são paulo']
while True:
    print("1.saldo\n2.saque\n3.deposito\n4.apostar")
    comando = int(input('comando: '))
    if comando == 1:
        print(saldo)

    elif comando == 2:
        saque = float(input("quanto voce quer sacar"))
        if saldo -  saque >= 0:
            saldo -= saque
        else:
            print("não possui saldo suficiente")

    elif comando == 3:
        saldo += int(input("quanto quer depositar?"))

    elif comando == 4:
        print("qual jogo deseja apostar?\n1. palmeiras x guarani\n2. são paulo x cruzeiro\n3. flamengo x forteleza\n4. cuiabá x são paulo")
        break