number = int(input())

lista = list(map(int,input().strip().split()))
lista.reverse()
print(*lista)