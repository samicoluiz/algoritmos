# # Questão 1
m = int(input('Insira um número inteiro: '))
n = int(input('insira outro numero inteiro: '))
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
