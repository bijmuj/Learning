"""
Asteroids with pygame
Ver 1.0
"""
from copy import deepcopy
from random import randint
import math
import pygame as pg


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Player():
    """
    Ship class
    """

    def __init__(self):
        self.pos = [300, 300, 310, 300]
        self.vel = 0
        self.rotation = 0
        # bullets have x, y positions and rotation when shot
        self.bullets = []

    def control(self, keys):
        """
        Controls for the ship

        Arguments:
            keys {pygame.key.get_pressed} -- a pygame element consisting of a list of pressed keys
        """
        ret = 0
        # rotating the ship
        self.vel = 0
        if keys[pg.K_a] and not keys[pg.K_d]:
            self.rotation += 3
            self.rotate()
            ret = 1
        elif keys[pg.K_d] and not keys[pg.K_a]:
            self.rotation -= 3
            self.rotate()
            ret = 1

        if self.rotation > 360:
            self.rotation -= 360
        if self.rotation < 0:
            self.rotation += 360

        # THRUST THRUST
        if keys[pg.K_w]:
            self.vel = 3
        elif keys[pg.K_w]:
            self.vel = -3
        else:
            self.vel = 0

        return ret

    def shoot(self):
        """
        To fire a projectile
        Each row in self. bullets is a projectile
        """
        if len(self.bullets) <= 15:
            self.bullets.append(deepcopy(self.pos))

    def rotate(self):
        """[summary]
        """
        self.pos[2] = self.pos[0]+10*math.cos(3.1415*self.rotation/180)
        self.pos[3] = self.pos[1]+10*math.sin(3.1415*self.rotation/180)

    def update(self):
        """
        Moving the ship every frame and moving the bullets
        """
        # moving ship
        if self.vel != 0:
            v_x = (self.pos[2]-self.pos[0])
            v_y = (self.pos[3]-self.pos[1])

        if self.vel > 0:
            self.pos[0] += v_x/5
            self.pos[2] += v_x/5
            self.pos[1] -= v_y/5
            self.pos[3] -= v_y/5

        elif self.vel < 0:
            self.pos[0] -= v_x/5
            self.pos[2] -= v_x/5
            self.pos[1] += v_y/5
            self.pos[3] += v_y/5

        # wrap around code
        # probably horribly inefficient
        if self.pos[0] > 600:
            self.pos[0] -= 600
            self.pos[2] -= 600
        elif self.pos[0] < 0:
            self.pos[0] += 600
            self.pos[2] += 600
        if self.pos[1] > 600:
            self.pos[1] -= 600
            self.pos[3] -= 600
        elif self.pos[1] < 0:
            self.pos[1] += 600
            self.pos[3] += 600

        # moving bullets\
        new_bullets = []
        for i in range(len(self.bullets)):
            v_x = (self.bullets[i][2]-self.bullets[i][0])
            v_y = (self.bullets[i][3]-self.bullets[i][1])

            self.bullets[i][0] += 6*v_x/10
            self.bullets[i][2] += 6*v_x/10
            self.bullets[i][1] -= 6*v_y/10
            self.bullets[i][3] -= 6*v_y/10

            if self.bullets[i][0] > 0 and self.bullets[i][1] > 0:
                if self.bullets[i][0] < 600 and self.bullets[i][1] < 600:
                    new_bullets.append(deepcopy(self.bullets[i]))

        self.bullets = deepcopy(new_bullets)


class Asteroids():
    """
    Class for the asteroids
    """

    def __init__(self):
        self.values = []

        self.generate(300, 300)

    def get_position(self, index):
        """Gets where the top left of the asteroid surf should be

        Arguments:
            index {int} -- the index of the asteroid we're looking for
        """
        size = self.values[index][2]+1
        return (self.values[index][0]-5*size, self.values[index][1]-5*size)

    def generate(self, x_off, y_off):
        """
        Generates a new asteroid and adds to the lists
        """
        if len(self.values) < 15:
            where, offset = randint(0, 3), randint(0, 600)
            values = [0 for i in range(5)]
            if where == 0:
                values[0], values[1] = 0, offset
            elif where == 1:
                values[0], values[1] = offset, 600
            elif where == 2:
                values[0], values[1] = 600, offset
            else:
                values[0], values[1] = offset, 0

            size = randint(0, 2)
            values[2] = size

            vel = [x_off-values[0] +
                   randint(-10, 10), y_off-values[1] + randint(-10, 10)]
            vel_mag = vel[0]**2 + vel[1]**2
            vel_mag = math.sqrt(vel_mag)
            values[3] = vel[0]/vel_mag
            values[4] = vel[1]/vel_mag

            self.values.append(values)

    def update(self):
        """
        Moves the asteroids
        """
        ret = 0
        new_values = []
        for i in range(len(self.values)):
            self.values[i][0] += self.values[i][3]
            self.values[i][1] += self.values[i][4]
            # no wraparound for the asteroids
            if self.values[i][0] < 600 and self.values[i][1] < 600:
                if self.values[i][0] > 0 and self.values[i][0] > 0:
                    new_values.append(self.values[i])

        ret = len(self.values)-len(new_values)
        self.values = deepcopy(new_values)
        return ret


class Game():
    """
    Game class
    """

    def __init__(self):
        pg.init()
        self.score = 1
        self.fps = 120
        self.size = (600, 600)
        self.screen = pg.display.set_mode(self.size, pg.DOUBLEBUF)
        self.background = pg.Surface(self.size).convert()
        self.ship_surf = pg.Surface((20, 20))
        self.ast_surf = [pg.Surface((20, 20)),
                         pg.Surface((30, 30)),
                         pg.Surface((40, 40))]
        self.ship = Player()
        self.asteroids = Asteroids()
        self.clock = pg.time.Clock()
        self.initial_draw()

    def update_screen(self):
        """
        Update screen with new positions blitted on
        """
        # draw bullets onto background
        self.background.fill(BLACK)
        for i in range(len(self.ship.bullets)):
            rect = (self.ship.bullets[i][0], self.ship.bullets[i][1], 2, 2)
            pg.draw.rect(self.background, WHITE, rect)
        # blit background
        self.screen.blit(self.background, (0, 0))
        # blit ship surface
        self.screen.blit(
            self.ship_surf, (self.ship.pos[0]-10, self.ship.pos[1]-10))
        # blit asteroid surfaces
        for i in range(len(self.asteroids.values)):
            size = self.asteroids.values[i][2]
            position = self.asteroids.get_position(i)
            self.screen.blit(self.ast_surf[size], position)

    def initial_draw(self):
        """
        Needs to draw 3 diff asteroids and the first ship
        """
        # drawing 3 diff sized asteroids
        for i in range(0, 3):
            pg.draw.circle(self.ast_surf[i], WHITE,
                           (5*(i+2), 5*(i+2)), 5*(i+2), 2)
        # drawing ship
        pg.draw.polygon(self.ship_surf, WHITE, ((20, 10), (0, 5), (0, 15)), 2)
        # pg.draw.rect(self.ship_surf, WHITE, (10, 0, 10, 10))
        self.ship_surf.set_colorkey(BLACK)
        for i in range(0, 3):
            self.ast_surf[i].set_colorkey(BLACK)

    def ship_redraw(self):
        """
        Redraws the ship surface when changed
        """
        self.ship_surf.fill(BLACK)

        points = [[10, 10] for i in range(3)]
        points[0][0] += 10*math.cos(3.1415*self.ship.rotation/180)
        points[0][1] -= 10*math.sin(3.1415*self.ship.rotation/180)

        points[1][0] += 10*math.cos(3.1415*(self.ship.rotation+150)/180)
        points[1][1] -= 10*math.sin(3.1415*(self.ship.rotation+150)/180)

        points[2][0] += 10*math.cos(3.1415*(self.ship.rotation+210)/180)
        points[2][1] -= 10*math.sin(3.1415*(self.ship.rotation+210)/180)

        for i in range(3):
            for j in range(2):
                points[i][j] = int(points[i][j])

        pg.draw.polygon(self.ship_surf, WHITE, tuple(points), 2)
        # pg.draw.rect(self.ship_surf, WHITE, (10, 0, 10, 10))

    def collision(self):
        """
        Collision detection (currently horribly inefficient)
        """
        score = 0
        for i in range(len(self.asteroids.values)):
            d_x = self.ship.pos[0]-self.asteroids.values[i][0]
            d_y = self.ship.pos[1]-self.asteroids.values[i][1]
            dist = math.sqrt(d_x**2 + d_y**2)-7
            if dist < (self.asteroids.values[i][2]+1)*5:
                return True

        indexes = []
        new_asteroids = []
        for i in range(len(self.ship.bullets)):
            for j in range(len(self.asteroids.values)):
                d_x = self.ship.bullets[i][0]-self.asteroids.values[j][0]
                d_y = self.ship.bullets[i][1]-self.asteroids.values[j][1]
                dist = math.sqrt(d_x**2 + d_y**2)-5
                if dist < (self.asteroids.values[j][2]+1)*5:
                    self.asteroids.values[j][2] -= 1
                    indexes.append(i)
                    break

        for i in indexes:
            del self.ship.bullets[i]

        for i in range(len(self.asteroids.values)):
            if self.asteroids.values[i][2] >= 0:
                new_asteroids.append(self.asteroids.values[i])
            else:
                score += 1

        self.asteroids.values = new_asteroids
        self.score += score
        for i in range(score):
            self.asteroids.generate(self.ship.pos[0], self.ship.pos[1])
        return False

    def run(self):
        """
        Game loop
        """
        running = True
        while running and not self.collision():
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    elif event.key == pg.K_SPACE:
                        self.ship.shoot()

            redraw_flag = self.ship.control(pg.key.get_pressed())
            if redraw_flag:
                self.ship_redraw()

            self.ship.update()

            levelup_flag = self.asteroids.update()
            while levelup_flag:
                levelup_flag -= 1
                self.asteroids.generate(self.ship.pos[0], self.ship.pos[1])

            if not self.score % 3:
                self.score = 1
                self.asteroids.generate(self.ship.pos[0], self.ship.pos[1])

            self.update_screen()

            pg.display.flip()
            self.clock.tick(self.fps)
        pg.display.quit()
        pg.quit()


game = Game()
game.run()
