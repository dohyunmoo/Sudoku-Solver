import pygame
import verification

width = 540
height = 600
grid_size = 60
board_size = grid_size * 9

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

window = pygame.display.set_mode((width, height))
window.fill(WHITE)

# initial empty grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

user_grid = [[0] * 9 for _ in range(9)]

def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(window, BLACK, (0, i * grid_size), (board_size, i * grid_size), thickness)
        pygame.draw.line(window, BLACK, (i * grid_size, 0), (i * grid_size, board_size), thickness)


pygame.display.set_caption("Sudoku Solver")

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid()
    # Update game logic

    # Render the game

    pygame.display.update()

pygame.quit()