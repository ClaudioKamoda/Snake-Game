import pygame
import cube as cb


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cb.cube(pos, color = color)
        self.body.append(self.head)
        self.dirx = 1
        self.diry = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT] and self.dirx != 1:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_RIGHT] and self.dirx != -1:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_UP] and self.diry != 1:
                    self.dirx = 0
                    self.diry = -1  # in pygame the y axis grows downwards
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_DOWN] and self.diry != -1:
                    self.dirx = 0
                    self.diry = 1   # in pygame the y axis grows downwards
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.diry == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirx, c.diry)

    def reset(self, color, pos):
        self.head = cb.cube(pos, color = color)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 1
        self.diry = 0

    def add_Cube(self):
        tail = self.body[-1]
        x, y = tail.dirx, tail.diry

        if x == 1 and y == 0:
            self.body.append(cb.cube((tail.pos[0]-1, tail.pos[1]), color = self.color))
        elif x == -1 and y == 0:
            self.body.append(cb.cube((tail.pos[0]+1, tail.pos[1]), color = self.color))
        elif x == 0 and y == 1:
            self.body.append(cb.cube((tail.pos[0], tail.pos[1]-1), color = self.color))
        elif x == 0 and y == -1:
            self.body.append(cb.cube((tail.pos[0], tail.pos[1]+1), color = self.color))

        self.body[-1].dirx = x
        self.body[-1].diry = y

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
