board = [['_','_','_'],['_','_','_'],['_','_','_']]
def print_boadrd(board):
    for row in board:
        for cell in row:
            print(f' {cell}' , end= ' ')
        print()

print(print_boadrd(board))