import pygame
import random
import snake as sn
import cube as cb
import tkinter as tk
from tkinter import messagebox


def redraw_Window(surface):
    global screen_size, rows, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    pygame.display.update()


def random_Snack(rows, snk):
    positions = snk.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_Box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global screen_size, rows, s, snack

    screen_size = 500
    rows = 20

    win = pygame.display.set_mode((screen_size, screen_size))
    s = sn.snake((0, 255, 0), (10, 10))
    snack = cb.cube(random_Snack(rows, s), color=(255, 0, 0))

    clock = pygame.time.Clock()

    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()

        if s.body[0].pos == snack.pos:
            s.add_Cube()
            snack = cb.cube(random_Snack(rows, s), color=(255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                message_Box('Game Over', 'Play Again')
                s.reset((0, 255, 0), (10, 10))
                flag = False
                break

        redraw_Window(win)


main()
