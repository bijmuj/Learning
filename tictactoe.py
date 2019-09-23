turn = 'X'
win = False


def draw(board):
    global turn
    for i in range(0, 3):
        print(' ' + board[i*3+1] + '|' +
              board[i*3+2] + '|' + board[i*3+3])


def takeinput(board):
    pos = -1
    global turn
    print(turn + "'s turn:")

    while pos == -1:
        print("Pick position 1-9:")
        pos = int(input())
        if(pos < 1 or pos > 9):
            pos = -1
        if board[pos] != ' ':
            pos = -1

    board[pos] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


def checkwin(board):
    global win
    for i in range(0, 3):
        if board[i*3+1] == board[i*3+2] and board[i*3+1] == board[i*3+3]:
            if not(board[i*3+1] == ' '):
                win = True
                break
        elif board[1+i] == board[4+i] and board[1+i] == board[7+i]:
            if not(board[i+1] == ' '):
                win = True
                break

    if (board[1] == board[5] and board[5] == board[9]):
        if board[1] != ' ':
            win = True

    if (board[3] == board[5] and board[5] == board[7]):
        if board[3] != ' ':
            win = True


board = [' ']*10

while not win:
    draw(board)

    takeinput(board)

    checkwin(board)

draw(board)
