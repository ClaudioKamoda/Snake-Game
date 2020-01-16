import cube

class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_Cube(self):
        pass

    def draw(self, surface):
        pass
