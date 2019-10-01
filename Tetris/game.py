import board as bd
import pygame as pg


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((500, 660), pg.DOUBLEBUF)
        self.fps = 240
        self.background = pg.Surface((500, 660)).convert()
        self.play = pg.Surface((300, 600)).convert()
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('mono', 22, bold=True)
        self.fw, self.fh = self.font.size("Next")
        self.color = ((0, 0, 0),
                      (255, 0, 0),
                      (0, 255, 0),
                      (0, 0, 255),
                      (255, 255, 255))
        self.board = bd.Board()

    def first_draw(self):
        """
        First time draw
        Only needs to be called once
        """
        pg.draw.rect(self.background, self.color[4], (348, 98, 128, 68), 2)
        pg.draw.rect(self.background, self.color[4], (348, 198, 128, 68), 2)
        pg.draw.rect(self.background, self.color[4], (23, 23, 303, 603), 2)
        self.screen.blit(self.background, (0, 0))

    def run(self):
        """
        Game loop
        """
        running = True
        pressed = False
        tick = 0
        a = 0
        self.first_draw()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
            tick += 1
            if pressed and tick % 2 == 0:
                self.board.manip(pg.key.get_pressed())
            if not tick % 10:
                if not a:
                    a = self.board.fall()
                    tick = 0
                else:
                    tick -= 1
                    a += 1
                    if a == 2:
                        tick = 0
                        a = 0
                        self.board.lock_in()
            self.draw()
            pg.display.flip()
            self.clock.tick(self.fps*int(self.board.level)//10)
        pg.display.quit()
        pg.quit()

    def draw(self):
        self.wipe()

        for i in range(0, 20):
            for j in range(0, 10):
                c = self.board.blocks[i][j]
                pg.draw.rect(
                    self.play, self.color[c], (j*30, i*30, 29, 29))
        self.screen.blit(self.play, (25, 25))

        for i in range(4):
            c = self.board.falling[i]
            pg.draw.rect(
                self.play, self.color[c[2]], (c[1]*30, c[0]*30, 29, 29))
        self.screen.blit(self.play, (25, 25))

    def wipe(self):
        self.play.fill(self.color[0])


if __name__ == "__main__":
    g = Game()
    g.run()
