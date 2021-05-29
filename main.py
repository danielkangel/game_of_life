import board as b
from time import sleep
import pygame

# set the window dimensions
x_size = 30
y_size = 30
cell_size = 20

# set the initial update speed and pause/unpause flag
speed = 0.1
next_state = 1

# set the background color and the path for the icons
background_color = (185, 185, 185)
path = "./assets/icons/"

# initialize the window
pygame.init()
surface = pygame.display.set_mode((x_size * cell_size, y_size * cell_size + 2 * cell_size))
surface.fill(background_color)
pygame.display.set_caption("Conway's Game of Life")

# initialize the font for the speed
cour = pygame.font.Font("./assets/font/cour.ttf", 24)

# create a new board object
board_1 = b.Board(x_size, y_size)

# load all the images into pygame surfaces
new_img = pygame.image.load(path + "clear_board.png")
pause1_img = pygame.image.load(path + "pause_unclicked.png")
pause2_img = pygame.image.load(path + "pause_clicked.png")
shuffle_img = pygame.image.load(path + "random_board.png")
slow_img = pygame.image.load(path + "slow_down.png")
fast_img = pygame.image.load(path + "speed_up.png")
logo = pygame.image.load(path + "logo.png")

# set the logo for the window
pygame.display.set_icon(logo)

# scale each of the images to the correct size
new_img = pygame.transform.scale(new_img, (2 * cell_size, 2 * cell_size))
pause1_img = pygame.transform.scale(pause1_img, (2 * cell_size, 2 * cell_size))
pause2_img = pygame.transform.scale(pause2_img, (2 * cell_size, 2 * cell_size))
shuffle_img = pygame.transform.scale(shuffle_img, (2 * cell_size, 2 * cell_size))
slow_img = pygame.transform.scale(slow_img, (2 * cell_size, 2 * cell_size))
fast_img = pygame.transform.scale(fast_img, (2 * cell_size, 2 * cell_size))


# render the board and update the window
def redisplay(board):
    board.render(surface, cell_size)
    pygame.display.update()


# display all the buttons except the pause button
def display_buttons(screen):
    screen.blit(new_img, (0, 0))
    screen.blit(shuffle_img, (4 * cell_size, 0))
    screen.blit(slow_img, (6 * cell_size, 0))
    screen.blit(fast_img, (8 * cell_size, 0))


# get the index of the mouse position
def get_cell_idx(place):
    x, y = place
    y -= 2 * cell_size
    x /= cell_size
    y /= cell_size
    return int(x), int(y)


# loop until the window is exited
while True:
    swap_cells = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_SPACE]:
                next_state = -next_state + 1

            if pressed[pygame.K_LEFT]:
                if speed < 0.3:
                    speed += 0.025

            if pressed[pygame.K_RIGHT]:
                if speed > 0.05:
                    speed -= 0.025

            if pressed[pygame.K_n]:
                board_1.clear_board()

            if pressed[pygame.K_r]:
                board_1.random_state()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # locate where user pressed and update that one cell
            loc = pygame.mouse.get_pos()
            if loc[-1] > 2 * cell_size:
                x, y = get_cell_idx(loc)
                board_1.swap_cell(x, y)
                swap_cells = True

            else:
                x_pos = loc[0]
                if x_pos < 2 * cell_size:
                    board_1.clear_board()

                elif x_pos < 4 * cell_size:
                    next_state = -next_state + 1

                elif x_pos < 6 * cell_size:
                    board_1.random_state()

                elif x_pos < 8 * cell_size:
                    if speed < 0.2:
                        speed += 0.025

                elif x_pos < 10 * cell_size:
                    if speed > 0.05:
                        speed -= 0.025

    text = cour.render(f"x{round(0.1 / speed, 1)}", True, (0, 0, 0))
    surface.fill(background_color)

    if next_state:
        if not swap_cells:
            board_1.next_state()
        surface.blit(pause1_img, (2 * cell_size, 0))
        sleep(speed)
    else:
        surface.blit(pause2_img, (2 * cell_size, 0))

    display_buttons(surface)
    surface.blit(text, ((x_size - 3) * cell_size, 0.5 * cell_size))
    redisplay(board_1)
