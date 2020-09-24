import random


class Bot:
    def __init__(self, map, id):
        self.eaten = 0
        self.id = id
        self.map = map
        self.moves = {1: map.bot_down,
                      2: map.bot_right,
                      3: map.bot_up,
                      4: map.bot_left,
                      5: map.stay_bot}
        self.UTK = [random.randint(1, 10) for z in range(64)]
        self.UTK_index = 0
        map.set_new_bot(self.id)

    def my_coord(self):
        self.map.bot_coord(self.id)

    def get_id(self):
        return self.id

    def what_is_here(self):
        if self.map.what_is_around_bot(self.id) == 1:
            self.eaten += 1

    def step(self):
        print(self.UTK_index & 63)
        print(self.UTK)
        self.what_is_here()
        if self.UTK[self.UTK_index & 63] in self.moves:
            self.moves[self.UTK[self.UTK_index & 63]](self.id)
            self.UTK_index = self.UTK_index + self.UTK[self.UTK_index & 63]
        else:
            self.UTK_index += 1
