from random import randrange
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
sign = False
listalibres= [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
jugadas=0


def DisplatBoard(board):
    for i in range(3):
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print(f'|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |')
        print('|       |       |       |')
    print('+-------+-------+-------+')





def EnterMove(board):
    jugada = True
    while jugada:

        movimiento = input("Ingrese el movimiento que de sea realizar: ")
        if int(movimiento) <= 3:
            if movimiento == '1' and (0, 0) in listalibres and board[0][0]!='X':
                board[0][0] = 'O'
                jugada = False
            elif movimiento == '2' and (0, 1) in listalibres and board[0][1]!='X':
                board[0][1] = 'O'
                jugada = False
            elif movimiento == '3' and (0, 2) in listalibres and board[0][2]!='X':
                board[0][2] = 'O'
                jugada = False

        elif int(movimiento) <= 6:
            if movimiento == '4' and (1, 0) in listalibres and board[1][0]!='X':
                board[1][0] = 'O'
                jugada = False
            elif movimiento == '5' and (1, 1) in listalibres and board[1][1]!='X':
                board[1][1] = 'O'
                jugada = False
            elif movimiento == '6' and (1, 2) in listalibres and board[1][2]!='X':
                board[1][2] = 'O'
                jugada = False

        elif int(movimiento) <= 9:
            if movimiento == '7' and (2, 0) in listalibres and board[2][0]!='X':
                board[2][0] = 'O'
                jugada = False
            elif movimiento == '8' and (2, 1) in listalibres and board[2][1]!='X':
                board[2][1] = 'O'
                jugada = False
            elif movimiento == '9' and (2, 2) in listalibres and board[2][2]!='X':
                board[2][2] = 'O'
                jugada = False
        else:
            jugada = True
    return board


def MakeListOfFreeFields(board):
    global listalibres
    listalibres = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for i in range(2):
        for a in range(2):
            if board[i][a] == 'O' or board[i][a] == 'X':
                listalibres.remove((i, a))
    return listalibres


def VictoryFor(board):
    global sign
    sign= False
    for i in range(2):
        if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O' or board[i][0] == 'X' and board[i][
            1] == 'X' and board[i][2] == 'X':
            if board[i][0] == 'O':
                sign= True
                print('¡Has ganado la partida felicitaciones!')


            elif board[i][0] == 'X':
                sign = True
                print('La maquina ha ganado la partida')




        elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O' or board[0][i] == 'X' and board[1][
            i] == 'X' and board[2][i] == 'X':
            if board[0][i] == 'O':
                sign=True
                print('¡Has ganado la partida felicitaciones!')





            elif board[0][i] == 'X':
                sign=True
                print('La maquina ha ganado la partida')



        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or board[0][0] == 'X' and board[1][
            1] == 'X' and board[2][2] == 'X':
            if board[2][2] == 'O':
                sign=True
                print('¡Has ganado la partida felicitaciones!')



            elif board[2][2] == 'X':
                sign=True
                print('La maquina ha ganado la partida')



        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O' or board[0][2] == 'X' and board[1][
            1] == 'X' and board[2][0] == 'X':
            if board[0][2] == 'O':
                sign=True
                print('¡Has ganado la partida felicitaciones!')
            elif board[0][2]=='X':
                sign=True
                print ('La maquina ha ganado la partida')





def DrawMove(board):
    jugada=True

    while jugada:

        movimiento= str(randrange(1,10))
        if int(movimiento) <= 3:
            if movimiento == '1' and (0, 0) in listalibres and board[0][0]!='O':
                board[0][0] = 'X'
                jugada=False
            elif movimiento == '2' and (0, 1) in listalibres and board[0][1]!='O':
                board[0][1] = 'X'
                jugada=False
            elif movimiento == '3' and (0, 2) in listalibres and board[0][2]!='O':
                board[0][2] = 'X'
                jugada=False
            else:
                jugada = True

        elif int(movimiento) <= 6:
            if movimiento == '4' and (1, 0) in listalibres and board[1][0]!='O':
                board[1][0] = 'X'
                jugada = False
            elif movimiento == '5' and (1, 1) in listalibres and board[1][1]!='O':
                board[1][1] = 'X'
                jugada = False
            elif movimiento == '6' and (1, 2) in listalibres and board[1][2]!='O':
                board[1][2] = 'X'
                jugada = False
            else:
                jugada=True

        elif int(movimiento) <= 9:
            if movimiento == '7' and (2, 0) in listalibres and board[2][0]!='O':
                board[2][0] = 'X'
                jugada = False
            elif movimiento == '8' and (2, 1) in listalibres and board[2][1]!='O':
                board[2][1] = 'X'
                jugada = False
            elif movimiento == '9' and (2, 2) in listalibres and board[2][2]!='O':
                board[2][2] = 'X'
                jugada = False
            else:
                jugada = True
        else:
                jugada = True
    return board

#la función dibuja el movimiento de la maquina y actaliza el tablero.
DisplatBoard(board)
MakeListOfFreeFields(board)
while sign == False:

    EnterMove(board)
    jugadas+=1
    MakeListOfFreeFields(board)
    DisplatBoard(board)
    if jugadas==9:
        print('Ha sido un empate')
        break
    DrawMove(board)
    jugadas+=1
    MakeListOfFreeFields(board)
    DisplatBoard(board)
    VictoryFor(board)




