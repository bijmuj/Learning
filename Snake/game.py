"""
pygame 1.9.6
"""
import pygame as pg
import snake as sn
import apple as ap


class Game():
    """
    Main game logic
    """

    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 600
        self.fps = 120
        self.screen = pg.display.set_mode(
            (840, 640), pg.DOUBLEBUF)
        self.background = pg.Surface((840, 640)).convert()
        self.play = pg.Surface((800, 600)).convert()
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('mono', 18, bold=True)
        self.snake = sn.Snake(self.width//2, self.height//2)
        self.apple = ap.Apple(self.width, self.height)
        self.text = "Length="+str((len(self.snake.x)-1))
        self.fw, self.fh = self.font.size(self.text)

    def draw(self):
        """
        Draw on screen and update
        """
        pg.draw.rect(self.background, (255, 255, 255), (18, 18, 804, 604))
        self.screen.blit(self.background, (0, 0))
        pg.draw.circle(self.play, (255, 0, 0),
                       (self.apple.x, self.apple.y), 10)
        self.snake.drawsnake(self.play)
        self.screen.blit(self.play, (20, 20))
        self.text = "Length="+str((len(self.snake.x)-1))
        textsurf = self.font.render(self.text, True, (0, 255, 0))
        self.screen.blit(textsurf, ((self.width - self.fw) //
                                    2, 0))
        pg.display.flip()

    def eat(self):
        """
        Reinitialize apple and extend snake
        """
        self.apple = ap.Apple(self.width, self.height)
        self.snake.ate()

    def gameover(self):
        """
        Called when game ends
        """
        self.text = "GAMEOVER"
        textsurf = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(textsurf, ((self.width - self.fw) //
                                    2, (self.height-self.fh)//2))
        pg.display.flip()

    def run(self):
        """
        Main game loops
        """
        running = True
        while running and self.snake.alive:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    else:
                        self.snake.move(event.key)
            if self.snake.x[0]+10 == self.apple.x and self.snake.y[0]+10 == self.apple.y:
                self.eat()
            self.clock.tick(self.fps//6)
            self.snake.update()
            self.draw()
        if not self.snake.alive:
            self.gameover()
            self.clock.tick(1)
            pg.display.quit()
        pg.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
