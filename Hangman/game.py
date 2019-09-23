"""
pygame 1.9.6
"""
import pygame as pg
import hangmanpg as h


class Game():
    """
    has everything else
    """

    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)
        self.fps = 60
        self.screen = pg.display.set_mode(self.size, pg.DOUBLEBUF)
        self.play = pg.Surface(self.size).convert()
        self.hangman = h.Hangman()
        self.font = pg.font.SysFont('mono', 18, bold=True)
        self.text = ''
        self.fw, self.fh = self.font.size(self.text)
        self.color = (125, 125, 125)

    def draw(self, clear):
        """
        draw all the shit including spaces and letters
        """
        # draw noose
        pg.draw.line(self.play, self.color, (600, 100), (600, 50), 5)
        pg.draw.line(self.play, self.color, (600, 50), (750, 50), 5)
        pg.draw.line(self.play, self.color, (750, 50), (750, 550), 5)
        pg.draw.line(self.play, self.color, (600, 550), (750, 550), 5)
        # draw dashes
        # TODO: MAKE THIS A TEXT BLIT
        for i in range(1, len(self.hangman.word)+1):
            pg.draw.line(self.play, self.color,
                         (30*i, 150), (30*i+20, 150), 1)
        # self.hangman.attempts = 0
        # draw hangman
        if clear == 1:
            self.color = (0, 0, 0)
        if self.hangman.attempts < 6:
            pg.draw.circle(self.play, self.color, (600, 150), 50, 5)
        if self.hangman.attempts < 5:
            pg.draw.line(self.play, self.color, (600, 200), (600, 400), 5)
        if self.hangman.attempts < 4:
            pg.draw.line(self.play, self.color, (600, 250), (500, 350), 5)
        if self.hangman.attempts < 3:
            pg.draw.line(self.play, self.color, (600, 250), (700, 350), 5)
        if self.hangman.attempts < 2:
            pg.draw.line(self.play, self.color, (600, 400), (500, 500), 5)
        if self.hangman.attempts < 1:
            pg.draw.line(self.play, self.color, (600, 400), (700, 500), 5)
        self.screen.blit(self.play, (0, 0))
        pg.display.flip()
        if clear == 1:
            self.color = (255, 255, 255)

    def run(self):
        """
        game loop
        """
        running = True
        self.draw(1)
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    else:
                        self.text += event.unicode
                        self.hangman.check(self.text)
                        self.text = self.text[:-1]
            print(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
