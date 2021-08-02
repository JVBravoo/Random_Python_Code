def somatorio(x):
    soma = 0
    c = 0
    while c <= x:
        soma = soma + c
        c = c + 1
    return soma

def wesley_safadao(dia,mes,ano):
    
    safadeza = (somatorio(mes) + ((ano/100) * (50-dia))) /100
    anjo = 100 - safadeza

    print('De acordo com os meus cálculos você tem {} de safadeza e {} de anjo'.format(safadeza, anjo))

dia = int(input('Digite o dia do seu aniversário: '))
mes = int(input('Digite o mês do seu aniversário: '))
ano = int(input('Digite o ano do seu aniversário: ')) 

wesley_safadao(dia,mes,ano)