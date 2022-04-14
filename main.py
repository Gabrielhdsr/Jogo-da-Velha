import os
import random

play_again = 's'
rounds = 0
player = True  # True = pessoa / False = pc
max_rounds = 9
vict = 'n'
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def screen():
    os.system('cls')  # limpa a tela

    print('    0   1   2')
    print(f'0:  {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('    ---------')
    print(f'1:  {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('    ---------')
    print(f'2:  {board[2][0]} | {board[2][1]} | {board[2][2]}')

    print(f'Jogadas: {rounds}')


def plays():
    global rounds
    global player
    global victory
    global max_rounds

    if player and rounds < max_rounds:
        try:
            line = int(input('Linha: '))
            column = int(input('Coluna: '))

            while board[line][column] != ' ':
                line = int(input('Linha: '))
                column = int(input('Coluna: '))

            board[line][column] = 'X'
            player = False
        except:
            print('Linha e/ou coluna inválida')


def pcPlays():
    global rounds
    global player
    global victory
    global max_rounds

    if not player and rounds < max_rounds:
        line = random.randrange(0, 3)
        column = random.randrange(0, 3)

        while board[line][column] != ' ':
            line = random.randrange(0, 3)
            column = random.randrange(0, 3)

        board[line][column] = 'O'
        rounds += 1
        player = True


def check_victory():
    global board
    victory = 'n'
    simbols = ['X', 'O']

    for c in simbols:
        victory = 'n'

        #  Verificando linhas
        checkl = 0
        checkc = 0

        while checkl < 2:
            sumx = 0
            checkc = 0

            while checkc < 3:
                if board[checkl][checkc] == c:
                    sumx += 1
                checkl += 1

            if sumx == 3:
                victory = c
                break
            checkl += 1

        if victory != 'n':
            break

        #  Verificando colunas
        checkl = 0
        checkc = 0

        while checkc < 3:
            sumx = 0
            checkl = 0

            while checkl < 3:
                if (board[checkl][checkc] == c):
                    sumx += 1
                checkl += 1

            if sumx == 3:
                victory = c
                break
            checkc += 1

        if victory != 'n':
            break

        #  Verificando diagonal
        sumx = 0
        checkd = 0
        checkdl = 0
        checkdc = 2

        while checkd < 3:
            if board[checkd][checkd] == c:
                sumx += 1
            if sumx == 3:
                victory = c
                break

        while checkdc >= 0:
            if board[checkdl][checkdc] == c:
                sumx += 1
            checkdl += 1
            checkdc -= 1

        if sumx == 3:
            victory = c
            break
    return victory


def reset():
    global rounds
    global player
    global max_rounds
    global victory
    global board

    rounds = 0
    player = True  # True = pessoa / False = pc
    max_rounds = 9
    victory = 'n'
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

while play_again == 's':
    while True:
        screen()
        plays()
        pcPlays()
        screen()
        vict = check_victory()
        print (vict)
        if vict != 'n':
            break

        print("FIM DE JOGO")

        if vict == 'X' or vict == 'O':
            print(f'Jogador {vict} venceu!')
        else:
            print('Empate')
        play_again = input('Deseja jogar novamente? (S/N)').lower()
        reset()



