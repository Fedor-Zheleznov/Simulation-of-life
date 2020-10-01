import Engine
import Bot
import Map
import Game
import pygame
import time
pygame.init()

file = open("UTK.txt", "a")

how_many_bots = 10
eaten = []
bots = []
last_utks = {}
bot_UTKs = [None, None, None, None, None, None, None, None, None, None, None]
bot_types = [None, None, None, None, None, None, None, None, None, None, None]

x = 63
y = 33
w = 15


for i in range(3):
    engine = Engine.engine(x, y, w)
    map = Map.Map(engine)
    map.create_map(x, y)

    for i in range(1, how_many_bots + 1):
        globals()["bot" + str(i)] = Bot.Bot(map, int("10" + str(i)), bot_UTKs[i], bot_types[i])
        bots.append(globals()["bot" + str(i)])

    map.create_resource(100)
    engine.draw_grid()
    engine.update(map)

    while True:
        Game.events()
        engine.clear()
        engine.draw_grid()

        for bot_in_list in bots:
            bot_in_list.step()

        if map.count_of_resources == 0:
            for bot_in_list in bots:
                if bot_in_list.eaten > 20:
                    last_utks[bot_in_list.eaten] = bot_in_list.UTK
                    eaten.append(bot_in_list.eaten)
            eaten.sort()
            try:
                file.write(str(eaten[-1]) + str(last_utks[eaten[-1]]) + "\n")
                break
            except IndexError:
                break

        time.sleep(1)

        engine.update(map)

file.close()
