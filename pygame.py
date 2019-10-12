"""
pygame 1.9.6
"""
import pygame
import random


class App:
    def __init__(self, width=1280, height=720, fps=60):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.screen = pygame.display.set_mode(
            (width, height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.font = pygame.font.SysFont('mono', 20, bold=True)
        # self.surf=pygame.Surface((100,100)).convert()
        # self.surf.set_colorkey((0,0,0))
        self.color = [0, 255, 0]
        self.circ = Circle()

    def run(self):
        """
        The mainloop
        """
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.circ.move()

            # milliseconds = self.clock.tick(self.fps)
            # self.playtime += milliseconds / 1000.0
            # self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
            #                self.clock.get_fps(), " "*5, self.playtime))
            self.draw()
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()

        pygame.quit()

    # def rand(self):
    #     for i in range(3):
    #         self.color[i]=random.randint(1,255)

    def draw(self):
        self.background.fill((0, 0, 0
                              ))
        pygame.draw.circle(
            self.background, (self.color[0], self.color[1], self.color[2]), self.circ.getvals(), 50, 3)
    #     # pygame.draw.polygon(Surface, color, pointlist, width=0): return circ
    #     pygame.draw.polygon(self.background, (self.color[0], self.color[1], self.color[2]),
    #                         ((400, 150), (238, 600), (650, 300), (150, 300),  (562, 600), (400, 150)))
    #     pygame.draw.circle(self.surf, (self.color[0],self.color[1],self.color[2]), (50,50),50)

    # def draw_text(self, text):
    #     """Center text in window
    #     """
    #     fw, fh = self.font.size(text)  # fw: font width,  fh: font height
    #     surface = self.font.render(text, True, (self.color[0],self.color[1],self.color[2])
    #     )

    #     # // makes integer division in python3
    #     self.screen.blit(surface, ((self.width - fw) //
    #                                2, (self.height - fh) // 2))


class Circle():
    def __init__(self, x=50, y=50):
        self.x = x
        self.y = y
        self.radius = 25

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.y > 0:
            self.y -= 10
        elif keys[pygame.K_d] and self.y < 700:
            self.x += 10
        elif keys[pygame.K_a] and self.x > 0:
            self.x -= 10
        elif keys[pygame.K_s] and self.x < 700:
            self.y += 10

    def getvals(self):
        return (self.x, self.y)


if __name__ == '__main__':
    # call with width of window and fps
    App(800, 800).run()
