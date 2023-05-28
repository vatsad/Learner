import random
import time

board = [['_' for i in range(3)] for j in range(3)]


# def board_full(b):
#     for i in range(3):
#         for j in range(3):
#             if b[i][j] == '_':
#                 return True
#     return False


def show_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()


def swap_player(p):
    if p == 'X':
        p = 'O'
    elif p == 'O':
        p = 'X'

    return p


show_board(board)
t = random.randint(0, 1)
player = None
toss = int(input("Please enter 0 or 1 for toss: "))
if toss == t:
    print("you will start the game, your letter is O, computer will play with X")
    player = 'O'
else:
    print("Computer will start the game with letter X")
    player = 'X'


def list_of_free_cells(b):
    free_cells = []
    for i in range(3):
        for j in range(3):
            if b[i][j] == '_':
                free_cells.append((i, j))
    return free_cells


def check_free_spot(b, *args):
    freecells = list_of_free_cells(b)
    if args in freecells:
        return False
    else:
        return True


def check_winner(b, p):

    win = None
    for i in range(3):
        win = True
        for j in range(3):
            if b[i][j] != p:
                win = False
                break
        if win:
         return win
    for i in range(3):
        win = True
        for j in range(3):
            if b[j][i] != p:
                win = False
                break
        if win:
            return win

    win = True
    for i in range(3):
        if b[i][i] != p:
            win = False
            break
    if win:
        return win
    win = True
    for i in range(3):
        if b[i][3 - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False


while len(list_of_free_cells(board)):
    print("*******************************************")
    show_board(board)
    if player == 'X':
        print("Computer turn")
        time.sleep(2)
        free_spot = list_of_free_cells(board)
        row, col = random.choice(free_spot)
        board[row][col] = player
        winner = check_winner(board, player)
        if winner:
            print()
            print("computer Wins!")
            show_board(board)
            break
        if len(list_of_free_cells(board))  == 0:
            print("Match tied")
            show_board(board)
            quit()
    elif player == 'O':
        spot = input("Fix your spot by entering row and col. number: ")
        sopt = list(spot)
        row, col = int(sopt[0]), int(sopt[1])
        if check_free_spot(board, row - 1, col - 1):
            print("Row and col are already occupied. Please make your choice again")
            continue
        board[row - 1][col - 1] = player
        winner = check_winner(board, player)
        if winner:
            print()
            print("You Won!")
            show_board(board)
            break
        if len(list_of_free_cells(board)) == 0:
            print("Match tied")
            show_board(board)
            quit()
    player = swap_player(player)
