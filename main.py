import pygame
import random
import time

pygame.init()

tiles = [[0 for i in range(20)] for i in range(10)]

botx, boty = 0, 0
foodx = 1 * 30
foody = 1 * 30
#foodx = random.randint(1, 20) * 30
#foody = random.randint(1, 10) * 30

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Simulation of life")
clock = pygame.time.Clock()

num = 0

def search_food(foody):
    global foodx, botx, boty, food
    screen.fill(white)
    [pygame.draw.line(screen, pygame.Color('darkslategray'), (x, 0), (x, 300)) for x in range(0, 600, 30)]
    [pygame.draw.line(screen, pygame.Color('darkslategray'), (0, y), (600, y)) for y in range(0, 300, 30)]
    botx += 30
    bot = pygame.draw.rect(screen, blue, (botx, boty, 30, 30))
    food = pygame.draw.rect(screen, red, (foodx, foody, 30, 30))
    for y in range(2):
        for x in range(2):
            if tiles[botx+x][boty+y] == 2:
                screen.fill(white)
                [pygame.draw.line(screen, pygame.Color('darkslategray'), (x, 0), (x, 300)) for x in range(0, 600, 30)]
                [pygame.draw.line(screen, pygame.Color('darkslategray'), (0, y), (600, y)) for y in range(0, 300, 30)]
                botx += 30
                bot = pygame.draw.rect(screen, blue, (botx, boty, 30, 30))
                foodx = random.randint(1, 20) * 30
                foody = random.randint(1, 10) * 30
                food = pygame.draw.rect(screen, red, (foodx, foody, 30, 30))
                tiles[foody // 30][foodx // 30] = 2
                pygame.display.flip()
    for i in range(8):
        screen.fill(white)
        [pygame.draw.line(screen, pygame.Color('darkslategray'), (x, 0), (x, 300)) for x in range(0, 600, 30)]
        [pygame.draw.line(screen, pygame.Color('darkslategray'), (0, y), (600, y)) for y in range(0, 300, 30)]
        time.sleep(1)
        boty += 30
        bot = pygame.draw.rect(screen, blue, (botx, boty, 30, 30))
        food = pygame.draw.rect(screen, red, (foodx, foody, 30, 30))
        pygame.display.flip()
    for i in range(3):
        screen.fill(white)
        [pygame.draw.line(screen, pygame.Color('darkslategray'), (x, 0), (x, 300)) for x in range(0, 600, 30)]
        [pygame.draw.line(screen, pygame.Color('darkslategray'), (0, y), (600, y)) for y in range(0, 300, 30)]
        time.sleep(1)
        botx += 30
        bot = pygame.draw.rect(screen, blue, (botx, boty, 30, 30))
        food = pygame.draw.rect(screen, red, (foodx, foody, 30, 30))
        pygame.display.flip()
    #if botx == foodx and boty == foody:
    #    foodx = random.randint(1, 20) * 30
    #    foody = random.randint(1, 10) * 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #clock.tick(1)
    screen.fill(white)
    [pygame.draw.line(screen, pygame.Color('darkslategray'), (x, 0), (x, 300)) for x in range(0, 600, 30)]
    [pygame.draw.line(screen, pygame.Color('darkslategray'), (0, y), (600, y)) for y in range(0, 300, 30)]
    food = pygame.draw.rect(screen, red, (foodx, foody, 30, 30))
    tiles[foody // 30][foodx // 30] = 2
    tiles[boty // 30][botx // 30] = 1
    botx += 30

