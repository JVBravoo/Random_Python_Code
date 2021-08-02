from random import randint
n = (randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000))
print(n)
print('O maior valor foi {}: '.format(max(n)))
print('O menor valor foi {}: '.format(min(n)))