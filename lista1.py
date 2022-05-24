# Nome:         Luiz Sérgio Samico Maciel Filho
# Matrícula:    202204940042

import random

# Questão 1 ########################################################
m = int(input('Insira um número inteiro: '))
n = int(input('insira outro número inteiro: '))
soma = 0
while m < n:
    print(m)
    soma += m
    m += 1
print(soma)

# Questão 2 ########################################################
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

# Questão 3 ########################################################
n = int(input('Insira um número inteiro: '))
t1 = random.randint(1,10)
t2 = random.randint(1,10)
print(t1, t2)
while t1 + t2 != n:
    t1 = random.randint(1,10)
    t2 = random.randint(1,10)
    print(t1, t2)

# Questão 4 ########################################################
n = int(input('Insira um número inteiro: '))
for i in range(n):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    print(f'{i+1}) {n1} + {n2} = {n1+n2}')

# Questão 5 ########################################################
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

# Questão 6 ########################################################
base = int(input('Insira um número inteiro positivo para ser a base: '))
expoente = int(input('Insira um número inteiro positivo para ser o expoente: '))
resultado = 1
contador = 0
while contador < expoente:
    resultado *= base
    contador += 1
print(resultado)

# Questão 7 ########################################################
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

# Questão 8 ########################################################
x1 = int(input('Digite a coordenada x1: '))
y1 = int(input('Digite a coordenada y1: '))
x2 = int(input('Digite a coordenada x2: '))
y2 = int(input('Digite a coordenada y2: '))
x3 = int(input('Digite a coordenada x3: '))
y3 = int(input('Digite a coordenada y3: '))

d1 = ((x2-x1)**2+(y2-y1)**2)**0.5
d2 = ((x3-x1)**2+(y3-y1)**2)**0.5
d3 = ((x2-x3)**2+(y2-y3)**2)**0.5

triangulo = None
if d1 > 0 and d2 > 0 and d3 > 0:
    if abs(d2-d3) < d1 and d1 < d2 + d3 or abs(d1-d3) < d2 and d2 < d1 + d3 or abs(d1-d2) < d3 and d3 < d1 + d2:
        triangulo = True
    else:
        print('um dos lados precisa ser menor que a soma dos outros dois e maior que o valor absoluto da diferença entre os lados.')
else:
    print('Para que exista um triângulo, todos os lados precisam ser maiores que zero.')

if triangulo:
    tipo = ''
    if d1 == d2 and d1 == d3 and d2 == d3:
        tipo = 'Equilátero'
    elif d1 != d2 and d1 != d3 and d2 != d3:
        tipo = 'Escaleno'
    else:
        tipo = 'Isóceles'
    print(f'O triângulo é do tipo {tipo} e tem lados ({round(d1, 1)}, {round(d2, 1)}, e {round(d3, 1)}).')
else:
    print('os pontos não formam um triângulo.')

# Questão 9 ########################################################
e1 = int(input('Digite a estatura da primeira pessoa (em cm): '))
e2 = int(input('Digite a estatura da segunda pessoa (em cm): '))
e3 = int(input('Digite a estatura da terceira pessoa (em cm): '))
meio = 0
if e1 != max(e1, e2, e3) and e1 != min(e1, e2, e3):
    meio = e1
if e2 != max(e1, e2, e3) and e2 != min(e1, e2, e3):
    meio = e2
if e3 != max(e1, e2, e3) and e3 != min(e1, e2, e3):
    meio = e3
print(f'As estaturas em ordem decrescente são:\n{max(e1, e2, e3)} cm, {meio} cm, e {min(e1, e2, e3)} cm.')