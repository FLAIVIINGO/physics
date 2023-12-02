import pygame
from random import randrange

class Window:
    def __init__(self, width ,height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.walkers = [Walker(self.width/2, self.height/2)]

    def draw(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("purple")
            for walker in self.walkers:
                walker.step()
                walker.draw(self.screen)
            self.walkers.append(Walker(self.walkers[-1].x, self.walkers[-1].y))
            pygame.display.flip()
            self.clock.tick(60)

class Walker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, [255,0,0], [self.x, self.y], 5)

    def step(self):
        choice = randrange(4)
        if choice == 0:
            self.x = self.x + 1
        elif choice == 1:
            self.x = self.x - 1
        elif choice == 2:
            self.y = self.y + 1
        else:
            self.y = self.y - 1

def main():
    win = Window(600, 600)
    win.draw()
    pygame.quit()

if __name__ == "__main__":
    main()