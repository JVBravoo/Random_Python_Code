#função
def reverso(n):
    inverte = str(n)
    print(inverte[::-1])
n = int(input('Digite um valor: '))
reverso(n)

#lista

l = [1,2,3,4,5]
l.reverse()
print(l)