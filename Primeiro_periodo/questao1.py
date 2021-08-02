soma = quant = media = maior = menor = 0
for c in range(0,10):
    x = int(input('Digite um valor: '))
    soma += x
    quant += 1
    if quant == 1:
        menor = maior = x
    if x > maior:
        maior = x
    if x < menor:
        menor = x


media = soma / quant
print('Você digitou {} número(s) e a média dele(s) foi {}'.format(quant,media))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))