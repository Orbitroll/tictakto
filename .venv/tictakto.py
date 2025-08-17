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



def Player_Choose(player, symbol=None):
    if symbol:
        return 'O' if symbol == 'X' else 'X'
    choice = input(f'{player}, Please choose X or O: ').upper()
    while choice not in ('X', 'O'):
        print(f'Dir {player} Please Choose X or O  cuz if you dont ill kill you')
        choice = input(f'{player}, Please choose X or O: ').upper()
    return choice

def Player_move(player, symbol):
    while True:
        choice = int(input(f'{player}, Please select a Number between 1-9: '))
        if choice in dict_board:
            key, val = dict_board[choice]
            if board[key][val] != '_':
                print(f' place taken , go home')
            else:
                board[key][val] = symbol
                print_boadrd(board)
                return key, val
            break
        else:
            print(f' Why are you doing this to you mama??? tell me why??? please choose other option')

def check_win(board, symbol):
    wins = [
        # Lines
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        # raws
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        # alchson ze ason
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)],
    ]
    for triplet in wins:
        if all(board[r][c] == symbol for r, c in triplet):
            return True
    return False

def board_full(board):
    return all(cell != '_' for row in board for cell in row)

def Game_mechanics():
    result = None
    while  result not in ('Wan', 'Tie'):
        for player, symbol in [(p1, p1_symbol), (p2, p2_symbol)]:
            Player_move(player , symbol)
            if check_win(board, symbol) :
                print(f' {player} YOU WAN')
                result = 'Wan'
            elif board_full(board):
                print(f' next time losers')
                result = 'Tie'




print(f'Welcome to the most Exsiding TicTacToc Ever!! you playing for your Life!')
p1, p2 = Users()
p1_symbol = Player_Choose(p1)
p2_symbol = Player_Choose(p2, p1_symbol)
print(f'{p1} your symbol is {p1_symbol}')
print(f'{p2} your symbol is {p2_symbol}')
print(f'Lets Start The Game ')
Game_mechanics()
