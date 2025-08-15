board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
dict_board = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
player_list = []


def print_boadrd(board):
    for row in board:
        for cell in row:
            print(f' {cell}', end=' ')
        print()


def Users():
    player_1 = input(f' please write player 1 name : ')
    player_2 = input(f' please write player 2 name : ')
    player_list.append(player_1)
    player_list.append(player_2)
    return player_1, player_2

    print(player_list)



def Player_move(player, symbol=None):
    if symbol:
        return 'O' if symbol == 'X' else 'X'

        # print(f'Where you want Move dir Sir or Lady Or A Dog')
        # input(f'Tell Me from 1-9 when the 1 is to lower left and the 9 is upper right')
        # if (1):
        #     print(print_boadrd(board[0, player_move]))


print(f'Welcome to the most Exsiding TicTacToc Ever!! you playing for your Life!')
p1, p2 = Users()
print(f'Lets Start The Game ')
print(print_boadrd(board))
# for player in player_list:
#     print(Player_move())
# if Player_move(player) == Player_move(player):
#     print(f'Fuck You')

print(f' {p1}')
