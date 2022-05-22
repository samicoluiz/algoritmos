import random

# Questão 1
m = int(input('Insira um número inteiro: '))
n = int(input('insira outro número inteiro: '))
soma = 0
while m < n:
    print(m)
    soma += m
    m += 1
print(soma)

# Questão 2
qtdSeq = int(input('Insira a quantidade de números da sequência de Fibonacci que deseja saber: '))
termo0 = 0
termo1 = 1
for i in range(qtdSeq-1):
    if i == 0:
        print(0)
    if i == 1:
        print(1)
    else:
        termo2 = termo0 + termo1
        print(termo2)
        termo0, termo1 = termo1, termo2

# Questão 3
n = int(input('Insira um número inteiro: '))
t1 = random.randint(1,10)
t2 = random.randint(1,10)
print(t1, t2)
while t1 + t2 != n:
    t1 = random.randint(1,10)
    t2 = random.randint(1,10)
    print(t1, t2)

# Questão 4
n = int(input('Insira um número inteiro: '))
for i in range(n):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    print(f'{i+1}) {n1} + {n2} = {n1+n2}')

# Questão 5
n = int(input('Insira um número inteiro: '))
primo = True
for i in range(2,abs(n)):
    if abs(n) % i == 0:
        primo = False
        break
if primo:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')

# Questão 6
base = int(input('Insira um número inteiro positivo para ser a base: '))
expoente = int(input('Insira um número inteiro positivo para ser o expoente: '))
resultado = 1
contador = 0
while contador < expoente:
    resultado *= base
    contador += 1
print(resultado)

# Questão 7
while True:
    print('**********************************************************')
    print('*             CÁLCULO DE GRANDEZAS ELÉTRICAS             *')
    print('**********************************************************')
    print('1. Tensão (em Volt)')
    print('2. Resistência (em Ohm)')
    print('3. Corrente (em Ampére)')
    print('**********************************************************')

    operacao = int(input('Qual grandeza deseja calcular?'))

    if operacao == 1:
        resistencia = float(input('Insira um valor de resistência (em Ohm)'))
        corrente = float(input('Insira um valor de corrente (em Ampére)'))
        print(f'A tensão é {round(resistencia * corrente, 2)}V')
        continuar = input('Deseja realizar outra operação? [s/n]')
        if continuar == 's':
            continue
        elif continuar == 'n':
            break
        else:
            print('Digite "s" para realizar outra operação ou "n" para sair do programa.')
    elif operacao == 2:
        tensao = float(input('Insira um valor de tensão (em Volt)'))
        corrente = float(input('Insira um valor de corrente (em Ampére)'))
        print(f'A resistência é {round(tensao / corrente, 2)}\u03A9')
        continuar = input('Deseja realizar outra operação? [s/n]')
        if continuar == 's':
            continue
        elif continuar == 'n':
            break
        else:
            print('Digite "s" para realizar outra operação ou "n" para sair do programa.')
    elif operacao == 3:
        tensao = float(input('Insira um valor de tensão (em Volt)'))
        resistencia = float(input('Insira um valor de resistência (em Ohm)'))
        print(f'A corrente é {round(tensao/resistência, 2)}A')
        continuar = input('Deseja realizar outra operação? [s/n]')
        if continuar == 's':
            continue
        elif continuar == 'n':
            break
        else:
            print('Digite "s" para realizar outra operação ou "n" para sair do programa.')
    else:
        print('Número inválido. Digite um número de 1 a 3.')

# Questão 8

# Questão 9
e1 = int(input('Digite a estatura da primeira pessoa (em cm): '))
e2 = int(input('Digite a estatura da segunda pessoa (em cm): '))
e3 = int(input('Digite a estatura da terceira pessoa (em cm): '))

print()