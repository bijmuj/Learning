"""
Checkers with oop
"""


class Board():
    """
    board class
    """

    def __init__(self):
        self.pieces = []
        self.pieces.append(Piece(0, 'end'))
        # contains all pieces
        # 1-12 inclusive are black 13-24 inclusive are red
        for i in range(2, 28, 2):
            if i % 9 != 0:
                self.pieces.append(Piece(i, 'b'))
        for i in range(46, 72, 2):
            if i % 9 != 0:
                self.pieces.append(Piece(i, 'r'))
        self.pieces.append(Piece(72, 'end'))

    def draw(self, turn):
        """Draws the board

        Arguments:
            turn {char} -- b/r valid
        """
        c = '.'
        for f in range(1, 72):
            print(" ", end='')
            if (f % 9 == 0):
                print("")
            elif(self.filledby(f) == c):
                print(c, end='')
            else:
                print(self.filledby(f), end='')
        print("")
        print(turn+"'s turn:")

    def filledby(self, pos):
        """
        When given a position returns what that position is filled by
        Returns . if position is empty

        Arguments:
            pos {int} -- the position we need to check
        """
        for i in range(1, 25):
            if self.pieces[i].pos == pos:
                return self.pieces[i].color
        return '.'
        # maybe get this to work somehow
        # if pos in self.pieces[]:

    def updateboard(self, newpos, index):
        """
        When a move is made updates board

        Arguments:
            newpos {int} -- the place we need to move to
            index {int} -- the index in the pieces array for the piece we're updating
        """
        # needs to update lists with new positions everymove
        self.pieces[index].pos = newpos
        self.pieces[index].highlight(False)
        if self.pieces[index].color.lower() == 'b' and newpos > 63:
            self.pieces[index].promote()
        elif self.pieces[index].color.lower() == 'r' and newpos < 9:
            self.pieces[index].promote()

    def getpiece(self, pos):
        """
        Takes a position and returns the index of piece in that position

        Arguments:
            pos {int} -- position to check
        """
        # returns index of piece in given postion
        for i in range(1, 25):
            if self.pieces[i].pos == pos:
                return i
        return 0

    def validmoves(self, index):
        """
        Takes the index of the piece and generates all valid moves

        Arguments:
            index {int} -- index in the array of pieces
        """
        # returns a list of possible moves
        # validmoves[]=[se,sw,ne,nw]
        pos = self.pieces[index].pos
        se = pos+10
        sw = pos+8
        ne = pos-8
        nw = pos-10
        turn = self.pieces[index].color
        ret = [se, sw, ne, nw]
        if turn == 'b':
            # checking for 'b'
            for i in range(1, 13):
                if self.pieces[i].pos == se:
                    se = 0
                elif self.pieces[i].pos == sw:
                    sw = 0
            # checking for 'r'
            for i in range(13, 25):
                if self.pieces[i].pos == se and se > 0:
                    se += 10
                    for j in range(1, 25):
                        if self.pieces[j].pos == se:
                            se = 0
                elif self.pieces[i].pos == sw and sw > 0:
                    sw += 8
                    for j in range(1, 25):
                        if self.pieces[j].pos == sw:
                            sw = 0

        if turn == 'r':
            se = 0
            sw = 0
            # only checking south
            # checking for 'r'
            for i in range(13, 25):
                if self.pieces[i].pos == ne:
                    ne = 0
                elif self.pieces[i].pos == nw:
                    nw = 0
            # checking for 'b'
            for i in range(1, 13):
                if self.pieces[i].pos == ne and ne > 0:
                    ne -= 8
                    for j in range(1, 25):
                        if self.pieces[j].pos == ne:
                            ne = 0
                elif self.pieces[i].pos == nw and nw > 0:
                    nw -= 10
                    for j in range(1, 25):
                        if self.pieces[j].pos == nw:
                            nw = 0

        if turn == 'B' or turn == 'R':
            for i in range(1, 25):
                if self.pieces[i].pos == se and se > 0:
                    if self.pieces[i].color.lower() != turn.lower():
                        se += 10
                        for j in range(1, 25):
                            if self.pieces[j].pos == se:
                                se = 0
                    else:
                        se = 0

                elif self.pieces[i].pos == sw and sw > 0:
                    if self.pieces[i].color.lower() != turn.lower():
                        sw += 8
                        for j in range(1, 25):
                            if self.pieces[j].pos == sw:
                                sw = 0
                    else:
                        sw = 0

                elif self.pieces[i].pos == nw and nw > 0:
                    if self.pieces[i].color.lower() != turn.lower():
                        nw -= 10
                        for j in range(1, 25):
                            if self.pieces[j].pos == nw:
                                nw = 0
                    else:
                        nw = 0

                elif self.pieces[i].pos == ne and ne > 0:
                    if self.pieces[i].color.lower != turn.lower():
                        ne -= 8
                        for j in range(1, 25):
                            if self.pieces[j].pos == ne:
                                ne = 0
                    else:
                        ne = 0
        ret[0] = se
        ret[1] = sw
        ret[2] = ne
        ret[3] = nw
        return ret


class Piece():
    """
    Piece object
    """

    def __init__(self, pos, color):
        self.color = color
        self.pos = pos
        self.promo = False

    def promote(self):
        """
        When a piece reaches the other end it gets promoted and can move backwards 
        """
        if self.color == 'b':
            self.color = 'B'
        elif self.color == 'r':
            self.color = 'R'

    def highlight(self, flag):
        """
        Highlights the selected piece
        Unhighlights it when deselected or moved 

        Arguments:
            flag {bool} -- True if highlighting, False otherwise
        """
        if (flag):
            if self.color == 'b':
                self.color = 'b̲'
            elif self.color == 'r':
                self.color = 'r̲'
            elif self.color == 'B':
                self.color = 'B̲'
            elif self.color == 'R':
                self.color = 'R̲'
        else:
            if self.color == 'b̲':
                self.color = 'b'
            elif self.color == 'r̲':
                self.color = 'r'
            elif self.color == 'B̲':
                self.color = 'B'
            elif self.color == 'R̲':
                self.color = 'R'


class Game():
    """
    Game class
    """

    def __init__(self, turn):
        self.turn = turn
        self.board = Board()

    def winner(self):
        """
        Checks if anyone has won
        """
        dead = 0
        for i in range(1, 13):
            if self.board.pieces[i].pos == 0:
                dead += 1
        if dead == 12:
            return 'r'
        dead = 0
        for i in range(13, 25):
            if self.board.pieces[i].pos == 0:
                dead += 1
        if dead == 12:
            return 'b'
        return 'n'

    def move(self):
        """
        Moving done through here
        """
        i = 0
        while i == 0:
            oldpos = 0
            print("Pick a piece(x,y):")
            try:
                x = int(input())
                y = int(input())
                pos = (y-1)*9+x
                i = self.board.getpiece(pos)
            except TypeError:
                i = 0
            if i == 0 or self.board.pieces[i].color.lower() != self.turn:
                print("Invalid piece")
                i = 0
            else:
                oldpos = pos
                moves = self.board.validmoves(i)
                self.board.pieces[i].highlight(True)
                self.board.draw(self.turn)
                # print(moves[0],moves[1],moves[2],moves[3])
                # DO SOMETHING ABOUT EATING
                # DID SOMETHING, CANT DO ANYTHING ELSE AFTERWARDS
                while True:
                    print("Pick new pos(x,y)(0,0 to undo):")
                    try:
                        x = int(input())
                        y = int(input())
                        pos = (y-1)*9+x
                    except TypeError:
                        pos = 0
                    if pos % 9 != 0 and (pos in moves):
                        if abs(pos-oldpos) > 10:
                            print(pos, oldpos, (pos+((pos-oldpos)/2)))
                            replace = self.board.getpiece(
                                int((pos+((oldpos-pos)/2))))
                            print(replace)
                            self.board.updateboard(0, replace)
                            self.board.updateboard(pos, i)
                            break
                        else:
                            self.board.updateboard(pos, i)
                            break
                    elif x == 0 and y == 0:
                        self.board.pieces[i].highlight(False)
                        self.board.draw(self.turn)
                        i = 0
                        break
                    else:
                        print("Invalid move")

    def swap(self):
        """
        Swapping turns. 
        Probably could've done somewhere else
        """
        if self.turn == 'b':
            self.turn = 'r'
        else:
            self.turn = 'b'

    def play(self):
        """
        To play
        """
        while self.winner() == 'n':
            self.board.draw(self.turn)
            self.move()
            self.swap()


if __name__ == "__main__":
    t = ''
    while t.lower() != 'r' and t.lower() != 'b':
        print("Starting color (b/r):")
        t = input()
    game = Game(t)
    game.play()
