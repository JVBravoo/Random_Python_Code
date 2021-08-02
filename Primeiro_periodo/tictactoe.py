######################################################################
# JOGO DA VELHA
######################################################################
board = [['', '', ''], ['', '', ''], ['', '', '']]
def print_board(): 
    print('=======================')
    print(board[0][0],'|' , board[0][1],'|' , board[0][2])
    print('________')
    print(board[1][0],'|' , board[1][1],'|' , board[1][2])
    print('________')
    print(board[2][0],'|' , board[2][1],'|' , board[2][2])
    print('=======================')

def jogada1():
    while True:
        jog1 = input('Jogador 1: Qual a sua jogada? (Coordenada separadas por espaço)')
        jog1 = jog1.split()
    
    
        if board[int(jog1[0])][int(jog1[1])] == "":
            board[int(jog1[0])][int(jog1[1])] = 'X'
            print_board
            return
        else:
            print('Jogada inválida')

def jogada2():
    while True:
        jog2 = input('Jogador 2: Qual a sua jogada? (Coordenada separadas por espaço)')
        jog2 = jog2.split()
    
    
        if board[int(jog2[0])][int(jog2[1])] == "":
            board[int(jog2[0])][int(jog2[1])] = 'X'
            print_board
            return
        else:
            print('Jogada inválida')

def check_winner():
    count = 0
    
    for l in range(3):
        for x in board[0]:
            if (x == 'X'):
                count = count + 1    
            elif (x == 'O'):
                count = count - 1
        if count == 3 or count == 3:
            print ('Jogador 1 ganhou!!!')
            return
        if count == 3:
            print ('Jogador 2 ganhou!!!')
            return
        
        count = 0
    
while    countColuna c = range(3):
    for l in range(3):
        
            if board[l][c] == 'X':
                count = count + 1    
            elif board[l][c] == 'O':
                count = count - 1
        
        if count == 3:
            print ('Jogador 1 ganhou!!!')
            return
        if count == - 3:
            print ('Jogador 2 ganhou!!!')
            return

        count = 0
    count = 0

    for l in range(3):
        if board[l][l] == 'X':
            count = count + 1
        elif board[l][l] == 'O'
            count = count - 1
        
    if count = 3
        print ('Jogador 1 ganhou!!!')
        acabou = True
        return
    
    if count = - 3
        print ('Jogador 2 ganhou!!!')
        acabou = True
        return
    count = 0
    it = 2
    for l in range(3):
        if board[it][l] == 'X':
            count = count + 1
        elif board[it][l] == 'O':
            count = count - 1
        it = it - 1
    if count == 3:
        print('Jogador 1 ganhou!!!')
        acabou = True
        break
    if count == - 3:
        print('Jogador 2 ganhou!!!')
        acabou = True
        break

jogadas = 0
while not acabou:
    print_board()
    jogada1()
    check_winner()
    jogada = jogada + 1
    if jogada > 9:
        acabou = True
    if acabou:
        break

    
    print_board()
    jogada2()
    check_winner()
    jogada = jogada + 1
    if jogada == 9:
        print_board()
        print('Deu velha')
        acabou = True
    if acabou:
        break
