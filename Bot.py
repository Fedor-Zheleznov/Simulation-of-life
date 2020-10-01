import random


class Bot:
    def __init__(self, map, id, utk=None, type_of_bot=None):
        self.eaten = 0
        self.id = id
        self.map = map
        self.moves = {1: map.bot_down,
                      2: map.bot_right,
                      3: map.bot_up,
                      4: map.bot_left,
                      5: map.stay_bot}
        self.types_functions = [map.set_new_wild_bot, map.set_new_herbivorous_bot]
        self.types_str = ["map.set_new_wild_bot", "map.""set_new_herbivorous_bot"]

        if utk is None:
            self.UTK = [random.randint(1, 10) for z in range(64)]
        else:
            self.UTK = utk

        self.UTK_index = 0

        if type_of_bot == "herbivorous_bot":
            map.set_new_herbivorous_bot(self.id)
            self.type = "herbivorous_bot"
        elif type_of_bot == "wild_bot":
            map.set_new_wild_bot(self.id)
            self.type = "wild_bot"
        if type_of_bot is None:
            self.types_functions[random.randint(0, 1)](self.id)
            self.type = [random.randint(0, 1)]

    def my_coord(self):
        self.map.bot_coord(self.id)

    def get_id(self):
        return self.id

    def what_is_here(self):
        if self.map.what_is_around_bot(self.id) == 1:
            self.eaten += 1

    def chek_collision(self):
        self.map.chek_and_acquire_the_collision(self.id)

    def step(self):
        self.what_is_here()
        self.chek_collision()
        if self.UTK[self.UTK_index & 63] in self.moves:
            print("move")
            self.moves[self.UTK[self.UTK_index & 63]](self.id)
            self.UTK_index = self.UTK_index + self.UTK[self.UTK_index & 63]
        else:
            print("+ 1")
            self.UTK_index += 1
