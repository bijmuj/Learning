"""
pygame 1.9.6
"""
import pygame as pg


class Snake():
    """
    Snakey
    """

    def __init__(self, x=400, y=300):
        self.x = [x, x-20]
        self.y = [y, y]
        self.speed = [20, 0]
        self.alive = True

    def move(self, key):
        """
        Manages all changes of movement direction

        Arguments:
            key {pg.event.key} -- [pygame key object]
        """
        if (key == pg.K_UP or key == pg.K_w) and self.speed[1] == 0:
            self.speed[1] = -20
            self.speed[0] = 0
        elif (key == pg.K_DOWN or key == pg.K_s) and self.speed[1] == 0:
            self.speed[1] = 20
            self.speed[0] = 0
        elif (key == pg.K_LEFT or key == pg.K_a) and self.speed[0] == 0:
            self.speed[0] = -20
            self.speed[1] = 0
        elif (key == pg.K_RIGHT or key == pg.K_d) and self.speed[0] == 0:
            self.speed[0] = 20
            self.speed[1] = 0

    def ate(self):
        """
        Lengthens snake after eating
        """
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

    def update(self):
        """
        Moves snake every turn
        Makes new list with locations of snake sections
        Shifts to right and adds to first location
        """
        x = self.x.copy()
        y = self.y.copy()
        x.insert(0, self.x[0])
        y.insert(0, self.y[0])
        x[0] += self.speed[0]
        y[0] += self.speed[1]
        x.pop()
        y.pop()
        self.x = x
        self.y = y
        self.alive = self.collision()

    def collision(self):
        """
        Checks for collisions against walls and snakes own body
        """
        for i in range(1, len(self.x)):
            if self.x[i] == self.x[0] and self.y[i] == self.y[0]:
                return False
        if self.x[0] > 780:
            return False
        elif self.x[0] < 0:
            return False
        elif self.y[0] > 580:
            return False
        elif self.y[0] < 0:
            return False
        else:
            return True

    def drawsnake(self, surface):
        """
        Draw snake on screen to be blit

        Arguments:
            surface {pg.Surface} -- [pygame surface element]
        """
        pg.draw.rect(surface, (0, 0, 0),
                     (self.x[-1], self.y[-1], 20, 20))
        pg.draw.rect(surface, (255, 255, 255),
                     (self.x[0], self.y[0], 20, 20))
