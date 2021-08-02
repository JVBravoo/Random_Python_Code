import math
catop = int(input('Digite um valor para ser o cateto oposto de um triangulo: '))
catadj = int(input('Digite um valor para ser o cateto adjacente de um triangulo: '))
hipo = math.hypot(catop, catadj)
print('O valor da Hipotenusa é {}'.format(hipo))
