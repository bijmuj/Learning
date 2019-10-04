turn = 'X'
win = False
spaces = 9


def draw(board):
    global turn
    for i in range(2, -1, -1):
        print(' ' + board[i*3+1] + '|' +
              board[i*3+2] + '|' + board[i*3+3])


def takeinput(board):
    pos = -1
    global turn
    print(turn + "'s turn:")

    while pos == -1:
        try:
            print("Pick position 1-9:")
            pos = int(input())
            if(pos < 1 or pos > 9):
                pos = -1
            if board[pos] != ' ':
                pos = -1
            if pos != -1:
                spaces -= 1
        except:
            print("enter a valid position")

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
                return board[i*3+1]
        elif board[1+i] == board[4+i] and board[1+i] == board[7+i]:
            if not(board[i+1] == ' '):
                win = True
                return board[1+i]

    if (board[1] == board[5] and board[5] == board[9]):
        if board[1] != ' ':
            win = True
            return board[1]

    if (board[3] == board[5] and board[5] == board[7]):
        if board[3] != ' ':
            win = True
            return board[3]

    return 'na'


board = [' ']*10

while not win and spaces:
    draw(board)

    takeinput(board)

    checkwin(board)

draw(board)

if not win and not spaces:
    print("draw")
elif win:
    print('{0} wins'.format(checkwin(board)))
