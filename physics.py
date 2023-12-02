import pygame

class Window:
    def __init__(self, width ,height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

    def draw(self):
        ball = Ball(100, 100, 1, 3.3)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("purple")
            ball.draw(self.screen, self.width, self.height)
            pygame.display.flip()
            self.clock.tick(60)

class Ball:
    def __init__(self, x, y, xspeed, yspeed):
        self.location = Vector(x, y)
        self.velocity = Vector(xspeed, yspeed)

    def draw(self, cnv, width, height):
        self.location.add(self.velocity)
        if self.location.x > width or self.location.x < 0:
            self.velocity.x = self.velocity.x * -1
        if self.location.y > height or self.location.y < 0:
            self.velocity.y = self.velocity.y * -1
        # print(f"x: {self.location.x}\ny: {self.location.y}")
        pygame.draw.circle(cnv, [255, 0, 0], [self.location.x, self.location.y], 20)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.y = self.y + vector.y
        self.x = self.x + vector.x


def main():
    win = Window(600, 600)
    win.draw()
    pygame.quit()

if __name__ == "__main__":
    main()