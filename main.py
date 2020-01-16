import pygame
import snake as sn


def draw_Grid(screen_size, rows, surface):
    sizeBtwn = screen_size // rows

    x = 0
    y = 0

    for lines in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, screen_size))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (screen_size, y))


def redraw_Window(surface):
    global screen_size, rows
    surface.fill((0, 0, 0))
    draw_Grid(screen_size, rows, surface)
    pygame.display.update()


def random_Snack(rows, items):
    pass


def message_Box():
    pass


def main():
    global screen_size, rows

    screen_size = 500
    rows = 20

    win = pygame.display.set_mode((screen_size, screen_size))
    snake = sn((0, 255, 0), (10, 10))

    clock = pygame.time.Clock()

    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_Window(win)

main()
