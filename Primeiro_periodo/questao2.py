with open('acidentes2017.csv', 'r') as f:
    arq = f.readlines()
header = arq[0].split(';')
matriz = []
bairros = {}

for i in range(1, len(arq)):
    linha = arq[i].split(';')
    matriz.append(linha)
for i in range(0, len(matriz)):
    if matriz[i][4] not in bairros:
        bairros[matriz[i][4]] = 1
    else:
        bairros[matriz[i][4]] += 1
maior = max(bairros, key = bairros.get)
print(bairros)
print(maior)
print(bairros[maior])