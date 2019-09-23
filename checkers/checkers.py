turn='b'

def init(board):
    for i in range (2,28,2):
        board[i]='b'
        board[i+44]='r'
    for i in range (9,72,9):
        board[i]='Z'
    
def draw(board):
    for i in range(0,8):
        for j in range(1,9):
            print(" " + board[j+i*9], end='')
        print(" ")

# def takeinput(board):
#     pos=-1
#     global turn
#     print(turn + "'s turn:")

#     while pos==-1 :
#         print("Pick a piece (x,y):")
#         x=int(input())
#         y=int(input())
#         pos1=(x-1)*9 + y
#         if(validpiece(pos1,x,y)):
#             if (board[pos1]=='b'):
#                 board[pos1]='b̲'
#             else:
#                 board[pos1]='r̲'
#             while True:
#                 draw(board)
#                 print("End position (x2,y2):")
#                 x2=int(input())
#                 y2=int(input())
#                 pos2=(x2-1)*9+y2
#                 end=validend(pos1,pos2, x2, y2)
#                 if (end==1):
#                     pos=1
#                     break
#                 elif (end==2):
#                     pos=1
#                     board[pos2]='.'
#                     pos2+=(pos2-pos1)
#                     break
        
#     if board[pos1]=='b̲' or board[pos1]=='r̲':
#         board[pos2]=turn
#     else:
#         board[pos2]=turn.upper()
#     board[pos1]='.'
    
#     if (turn=='r' and pos2<9) or (turn=='b' and pos2>63):
#         promote(board, pos2)
        
#     if turn=='b':
#         turn='r'
#     else:
#         turn='b'

# def validpiece(pos1,x,y):
#     ret=diagchecks(board,pos1)
#     global turn
#     if(x>0 and x<9) and (y>0 and y<9):
#         if (board[pos1]==turn):
#             if turn=='b' and (ret%2==0 or ret%3==0):
#                 return True
#             elif turn=='r' and (ret%5==0 or ret%7==0):
#                 return True
#         elif (board[pos1]==turn.upper()) and ret!=1:
#             return True
#     return False

# def validend(pos1, pos2, x2, y2):
#     # I AM LOST
#     if (x2>0 and x2<9) and (y2>0 and y2<9): 
#         if board[pos2]=='.':
#             if (board[pos1]=='b') and (pos2==pos1+10 or pos2==pos1+8):
#                 return 1
#             elif (board[pos1]=='r') and (pos2==pos1-10 or pos2==pos1-8):
#                 return 1
#         elif board[pos2]!=turn:
#             #still lost
            
            
#     return 0

# def diagchecks(board, pos1):
#     global turn 
#     ret=1
#     if (board[pos1+10]=='.') and ((pos1+10)%9!=0):
#         # ret+'se'
#         ret*=2
#     if (board[pos1+8]=='.') and ((pos1+8)%9!=0):
#         # ret+'sw'
#         ret*=3
#     if (board[pos1-10]=='.') and ((pos1-10)%9!=0):
#         # ret+'nw'
#         ret*=5
#     if(board[pos1-8]=='.') and ((pos1-8)%9!=0):
#         # ret+'ne' 
#         ret*=7
                
#     return ret

def move(board):
    pos=-1
    global turn
    print(turn,"'s turn") 
    while pos==-1:
        print("Pick piece(x1,y1):")
        x1=int(input())
        y1=int(input())
        pos1=(x1-1)*9+y1
        pos=validity(board,pos1,x1,y1)#takes both sets of inputs and returns !-1 if valid 
    
    while pos==1:
        print ("Pick end position(x2,y2):")
        x2=int(input())
        y2=int(input())
        pos2=(x2-1)*9+y2
        pos=validity(board,pos2,x2,y2)#probably should call something else

    if pos==1:#if single move not eaten
        if board[pos1]=='b̲' or board[pos1]=='r̲':
            board[pos2]=turn
        else:
            board[pos2]=turn.upper()
        board[pos1]='.'
    elif pos==2:#if single move single eaten
        board[pos2]='.'
        pos2+=(pos2-pos1)
        if board[pos1]=='b̲' or board[pos1]=='r̲':
            board[pos2]=turn
        else:
            board[pos2]=turn.upper()
        board[pos1]='.'
    # make something such that eating gives extra turn
    # elif pos==3:
    #     board[pos2]='.'
       
def validity(board,pos1,x,y):      
    if (x<1 or x>8) or (y<1 or y>8):
        return -1
    if board[pos1].lower()!=turn:
        return -1
    if (board[pos1]=='b') and (ret%2!=0 or ret%3!=0):
        return -1
    elif (board[pos1]=='r') and (ret%5!=0 or ret%7!=0):
        return -1
    elif (board[pos1]=='B' or board[pos1]=='R') and ret==1:
        return -1
    

    
    
def win(board):
    b=0
    r=0
    for i in range(0,72):
        if board[i].lower()=='b':
            b+=1
        elif board[i].lower()=='r':
            r+=1
            
    if (b==0):
        return 1
    elif (r==0):
        return 2
    else:
        return 0

def promote(board, pos2):
    a=turn.upper()
    board[pos2]=a
        
board=['.']*72 
init(board)    
while (win(board)==0):   
    draw(board)
    move(board)
draw(board)