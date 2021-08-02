x = (int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')))             
print(x)
print('O número 9 aparece {} vezes'.format(x.count(9)))
if 3 in x:
    print('Os número 3 apareceu na posição {}'.format(x.index(3)))
else:
    print('O valor 3 não apareceu em nenhuma posição')
print('Os números pares digitados foram ', end = (''))
for n in x:
    if (n % 2 == 0):
        print(n, end = (' '))