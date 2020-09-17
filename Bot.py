import random


class Bot:
    def __init__(self, map, id):
        self.eaten = 0
        self.id = id
        self.map = map
        self.moves = [map.bot_down, map.bot_right, map.bot_up, map.bot_left, map.stay_bot]
        map.set_new_bot(self.id)

    def my_coord(self):
        self.map.bot_coord(self.id)

    def get_id(self):
        return self.id

    def what_is_here(self):
        if self.map.what_is_around_bot(self.id) == 1:
            self.eaten += 1

    def step(self):
        self.what_is_here()
        self.moves[random.randint(0, 4)](self.id)

