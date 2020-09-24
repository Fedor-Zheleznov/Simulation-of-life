import pygame

pygame.init()


class engine():
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.screen = pygame.display.set_mode((x * w, y * w))
        self.screen.fill((255, 255, 255))
        #clock = pygame.time.Clock()
        #clock.tick(0.5)

    def clear(self):
        self.screen.fill((255, 255, 255))
        x = self.x
        y = self.y
        for i in range(0, x):
            pygame.draw.line(self.screen, pygame.Color('darkslategray'), [i * self.w, 0], [i * self.w, y * self.w])
        for i in range(0, y):
            pygame.draw.line(self.screen, pygame.Color('darkslategray'), [0, i * self.w], [x * self.w, i * self.w])

    def update(self, map):
        for y in range(self.y):
            for x in range(self.x):
                if map.cells[y][x].get("type") == "bot":
                    width = self.w
                    pygame.draw.rect(self.screen, (0, 0, 255), (x * width + 1, y * width + 1, width - 1, width - 1))
                if map.cells[y][x].get("type") == "resource":
                    width = self.w
                    pygame.draw.rect(self.screen, (255, 0, 0), (x * width + 1, y * width + 1, width - 1, width - 1))
        pygame.display.flip()

    def draw_grid(self):
        x = self.x
        y = self.y
        for i in range(0, x):
            pygame.draw.line(self.screen, pygame.Color('darkslategray'), [i * self.w, 0], [i * self.w, y * self.w])
        for i in range(0, y):
            pygame.draw.line(self.screen, pygame.Color('darkslategray'), [0, i * self.w], [x * self.w, i * self.w])
