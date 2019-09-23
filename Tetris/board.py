import random
import pygame
import copy


class Board():
    """
    Holds all logic and stores all positions and shit
    """

    def __init__(self):
        # creating an array each element represents the block in that position
        # if no block then 0
        # other values correspond to color
        # has 10 columns and 20 rows
        self.blocks = [[0 for i in range(10)] for j in range(20)]
        # need to store the position of currently falling set of blocks
        # each set of blocks is a "piece"
        self.falling = [[0 for i in range(3)] for j in range(4)]
        # also need to store held and next piece
        self.held_piece = [[0 for i in range(3)] for j in range(4)]
        self.next_piece = [[0 for i in range(3)] for j in range(4)]
        # need to populate atleast next and falling initially
        self.next_piece = self.generate()
        self.falling = self.generate()
        self.swapped = 0
        self.level = 1

    def generate(self):
        """
        Generates new pieces and switches next_piece into falling
        """
        # TODO: there has to be a more efficient way to do this
        # 1st column=>row
        # 2nd column=>column
        # 3rd column=>color
        # currently only makes squares
        gen = []
        col = random.randint(1, 3)
        sh = random.randint(0, 6)
        if sh == 0:
            gen.append([0, 5, col])
            gen.append([0, 6, col])
            gen.append([0, 7, col])
            gen.append([0, 8, col])
        elif sh == 1:
            # cube
            gen.append([0, 5, col])
            gen.append([0, 6, col])
            gen.append([1, 5, col])
            gen.append([1, 6, col])
        elif sh == 2:
            # left l
            gen.append([0, 5, col])
            gen.append([1, 5, col])
            gen.append([1, 6, col])
            gen.append([1, 7, col])
        elif sh == 3:
            # right l
            gen.append([0, 7, col])
            gen.append([1, 5, col])
            gen.append([1, 6, col])
            gen.append([1, 7, col])
        elif sh == 4:
            # z
            gen.append([0, 5, col])
            gen.append([0, 6, col])
            gen.append([1, 6, col])
            gen.append([1, 7, col])
        elif sh == 5:
            # s
            gen.append([0, 7, col])
            gen.append([0, 6, col])
            gen.append([1, 5, col])
            gen.append([1, 6, col])
        else:
            # t
            gen.append([0, 6, col])
            gen.append([1, 5, col])
            gen.append([1, 6, col])
            gen.append([1, 7, col])
        return gen

    def fall(self):
        """
        Need something that moves falling piece down by 1 every call
        """
        lock = 0
        c = self.falling
        # if any block reaches bottom row then lock in place
        for i in range(4):
            if c[i][0] == 19:
                lock = 1

        # TODO: find a better way to implement this and the next bit
        if not lock:
            for i in range(4):
                # checking for blocks under each block of new_piece
                if self.blocks[c[i][0]+1][c[i][1]] != 0:
                    lock = 1

        if not lock:
            # if they dont pass then we can shift falling piece down by 1
            for i in range(4):
                self.falling[i][0] += 1
        return lock

    def lock_in(self):
        # if any of the above pass then we move falling piece into blocks array
        for i in range(4):
            self.blocks[self.falling[i][0]
                        ][self.falling[i][1]] = self.falling[0][2]
        # replacing the current falling with next_piece
        self.falling = copy.deepcopy(self.next_piece)
        # making a new next_piece
        self.next_piece = self.generate()
        # also check if any line is complete
        self.row_check()
        # allow swaps again for next piece
        self.swapped = 0

    def row_check(self):
        """
        Checks each row
        If row is complete shift all above rows down 1
        """
        i = 19
        # starting at the bottom check every row
        while i > -1:
            if self.blocks[i].count(0) == 0:
                # if no empty space left in row then delete row
                self.blocks[i][0:] = [0 for i in range(10)]
                # then shift above rows down
                for j in range(i, 0, -1):
                    self.blocks[j][0:], self.blocks[j -
                                                    1][0:] = self.blocks[j-1][0:], self.blocks[j][0:]
                self.level += 0.25
            else:
                # if empty spaces exist then check the row above
                i -= 1

    def manip(self, key):
        """
        Checks inputs and calls other shit when necessary

        Arguments:
            key {pygame.key} -- keypressed
        """
        if key == pygame.K_w:
            pass
        elif key == pygame.K_a:
            self.shift(-1)
        elif key == pygame.K_d:
            self.shift(1)
        elif key == pygame.K_s:
            self.fall()
        elif key == pygame.K_r:
            self.swap()

    def shift(self, val):
        """
        Shifts each block in falling piece by val if possible

        Arguments:
            val {1|-1} -- -1 to shift left and 1 to shift right
        """
        possible = 1
        for i in range(4):
            # checking if any blocks of falling are already at an edge
            if self.falling[i][1]+val == -1 or self.falling[i][1]+val == 10:
                possible = 0
            elif self.blocks[self.falling[i][0]][self.falling[i][1]+val]:
                possible = 0

        if possible:
            for i in range(4):
                self.falling[i][1] += val

    def swap(self):
        """
        Swap between held and falling piece
        """
        if not self.held_piece[0][2]:
            self.held_piece = copy.deepcopy(self.falling)
            self.falling = copy.deepcopy(self.next_piece)
            self.next_piece = self.generate()
        # literally swapping positions in
        if not self.swapped:
            for i in range(4):
                self.falling[i][0:], self.held_piece[i][0:
                                                        ] = self.held_piece[i][0:], self.falling[i][0:]
            self.swapped = 1

    def rotate(self):
        """
        Rotates piece
        """
        pass
