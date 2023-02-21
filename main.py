def board_displayer(board):
    print(board[0])
    print(board[1])
    print(board[2])

def user_input (text_request):
    result = input(text_request)
    return result 

def new_board():
    row_01 = [' ',' ',' ']
    row_02 = [' ',' ',' ']
    row_03 = [' ',' ',' ']
    board = [row_01, row_02, row_03]
    return board

board_01 = new_board()

board_displayer(board_01)