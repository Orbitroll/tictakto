board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def print_boadrd(board):
    for row in board:
        for cell in row:
            print(f' {cell}', end=' ')
        print()

def Users():
    player_1 =input(f'Please write First user name : ')
    player_2 =input(f'Please write Secend user name : ')

input(Users())
