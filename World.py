import Engine
import Bot
import Map
import Game
import pygame
import time

pygame.init()

bots = []

engine = Engine.engine(20, 10, 30)
map = Map.Map(engine)
map.create_map(20, 10)

#bot1 = Bot.Bot(map, 101)
#bot2 = Bot.Bot(map, 102)
#bot3 = Bot.Bot(map, 103)
#bot4 = Bot.Bot(map, 104)
#bot5 = Bot.Bot(map, 105)
#bot6 = Bot.Bot(map, 106)
#bot7 = Bot.Bot(map, 107)
#bot8 = Bot.Bot(map, 108)
#bot9 = Bot.Bot(map, 109)
#bot10 = Bot.Bot(map, 110)
#bot11 = Bot.Bot(map, 111)
#bot12 = Bot.Bot(map, 112)
#bot13 = Bot.Bot(map, 113)
#bot14 = Bot.Bot(map, 114)
#bot15 = Bot.Bot(map, 115)


#bots.append(bot1)
#bots.append(bot2)
#bots.append(bot3)
#bots.append(bot4)
#bots.append(bot5)
#bots.append(bot6)
#bots.append(bot7)
#bots.append(bot8)
#bots.append(bot9)
#bots.append(bot10)
#bots.append(bot11)
#bots.append(bot12)
#bots.append(bot13)
#bots.append(bot14)
#bots.append(bot15)

#map.create_resource(50)

engine.draw_grid()
engine.update(map)

while True:
    Game.events()
    engine.clear()
    engine.draw_grid()

    #for bot_in_list in bots:
    #    bot_in_list.step()

    time.sleep(0.001)
    engine.update(map)

    #if map.count_of_resources == 0:
    #    for bot_in_list in bots:
    #        print(f"The bot with {bot_in_list.get_id()} eaten {bot_in_list.eaten}")
    #    break
