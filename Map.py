import random


class Cell:
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def get(self, what):
        if what == "id":
            return self.id
        if what == "type":
            return self.type

    def set(self, what, num):
        if what == "id":
            self.id = num
        if what == "type":
            self.type = num


class Map:
    def __init__(self, engine):
        self.resources = []
        self.count_of_resources = 0
        self.resid = 199
        self.engine = engine

    def create_map(self, x, y):
        self.x = x
        self.y = y

        cell = Cell("free", 0)
        self.cells = [[cell for self.i in range(self.x)] for self.z in range(self.y)]


    def set_new_bot(self, id):
        y = random.randint(0, self.y)
        x = random.randint(0, self.x)
        self.cells[y][x] = Cell("bot", id)
        return (x, y)

    def set_bot(self, id, x, y):
        if 0 <= x <= self.x - 1 and 0 <= y <= self.y - 1:
            if self.cells[y][x].get("type") == "free":
                last_bot_coord = self.bot_coord(id)
                self.cells[y][x] = Cell("bot", id)
                self.cells[last_bot_coord[1]][last_bot_coord[0]] = Cell("free", 0)
        else:
            self.stay_bot(id)

    def bot_coord(self, id):
        for y in range(self.y):
            for x in range(self.x):
                if self.cells[y][x].get("id") == id:
                    coord = (int(x), int(y))
                    return coord

    def stay_bot(self, id):
        self.cells[self.bot_coord(id)[1]][self.bot_coord(id)[0]] = Cell("bot", id)

    def bot_up(self, id):
        self.set_bot(id, self.bot_coord(id)[0], self.bot_coord(id)[1] - 1)

    def bot_down(self, id):
        self.set_bot(id, self.bot_coord(id)[0], self.bot_coord(id)[1] + 1)

    def bot_right(self, id):
        self.set_bot(id, self.bot_coord(id)[0] + 1, self.bot_coord(id)[1])

    def bot_left(self, id):
        self.set_bot(id, self.bot_coord(id)[0]-1, self.bot_coord(id)[1])

    def chek_and_acquire_above_the_bot(self, id):
        if self.bot_coord(id)[1] != 0:
            if self.cells[self.bot_coord(id)[1] - 1][self.bot_coord(id)[0]].get("type") == "resource":
                self.cells[self.bot_coord(id)[1] - 1][self.bot_coord(id)[0]] = Cell("free", 0)
                self.count_of_resources -= 1
                return 1

    def chek_and_acquire_under_the_bot(self, id):
        if self.bot_coord(id)[1] != self.y - 1:
            if self.cells[self.bot_coord(id)[1] + 1][self.bot_coord(id)[0]].get("type") == "resource":
                self.cells[self.bot_coord(id)[1] + 1][self.bot_coord(id)[0]] = Cell("free", 0)
                self.count_of_resources -= 1
                return 1

    def chek_and_acquire_the_left_of_the_bot(self, id):
        if self.bot_coord(id)[0] != 0:
            if self.cells[self.bot_coord(id)[1]][self.bot_coord(id)[0] - 1].get("type") == "resource":
                self.cells[self.bot_coord(id)[1]][self.bot_coord(id)[0] - 1] = Cell("free", 0)
                self.count_of_resources -= 1
                return 1

    def chek_and_acquire_the_right_of_the_bot(self, id):
        if self.bot_coord(id)[0] != self.x - 1:
            if self.cells[self.bot_coord(id)[1]][self.bot_coord(id)[0] + 1].get("type") == "resource":
                self.cells[self.bot_coord(id)[1]][self.bot_coord(id)[0] + 1] = Cell("free", 0)
                self.count_of_resources = self.count_of_resources - 1
                return 1

    def what_is_around_bot(self, id):
        if self.chek_and_acquire_under_the_bot(id) == 1:
            return 1
        if self.chek_and_acquire_above_the_bot(id) == 1:
            return 1
        if self.chek_and_acquire_the_right_of_the_bot(id) == 1:
            return 1
        if self.chek_and_acquire_the_left_of_the_bot(id) == 1:
            return 1



    def create_resource(self, how_much):
        # self.resources_drawn = False
        for i in range(how_much):
            if self.count_of_resources < how_much:
                self.resx = random.randint(0, self.x - 1)
                self.resy = random.randint(0, self.y - 1)
                if self.cells[self.resy][self.resx].get("type") == "free":
                    self.resid += 1
                    self.cells[self.resy][self.resx] = Cell("resource", self.resid)
                    self.resources.append(self.cells[self.resy][self.resx])
                    self.count_of_resources += 1
            # elif self.resources_drawn is False:
            #    self.count_of_resources = 0
            #    for y in range(self.y):
            #        for x in range(self.x):
            #            for i in self.resources:
            #                if self.cells[y][x].get("id") == i.get("id"):
            #                    self.count_of_resources += 1
            #                    if self.count_of_resources == 5:
            #                        self.resources_drawn = True
            #                        self.resources_drawn = True
