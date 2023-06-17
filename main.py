import pygame
import copy

# external files
import verification
import solve

pygame.init()

WIDTH, HEIGHT = 540, 600
CELL_SIZE = WIDTH // 9

BUTTON_WIDTH = WIDTH // 5
BUTTON_HEIGHT = CELL_SIZE // 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))

run_button = pygame.Rect((WIDTH // 4 - BUTTON_WIDTH // 2, (HEIGHT - CELL_SIZE // 2) - BUTTON_HEIGHT // 2), (BUTTON_WIDTH, BUTTON_HEIGHT))
reset_button = pygame.Rect((3*WIDTH // 4 - BUTTON_WIDTH // 2, (HEIGHT - CELL_SIZE // 2) - BUTTON_HEIGHT // 2), (BUTTON_WIDTH, BUTTON_HEIGHT))

# initial empty board
board = [
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

selected_cell = None

def draw_grid():
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), thickness)


def draw_numbers():
    font = pygame.font.Font(None, 40)

    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                number = font.render(str(board[row][col]), True, BLACK)
                number_rect = number.get_rect()
                number_rect.center = ((col * CELL_SIZE) + (CELL_SIZE // 2), (row * CELL_SIZE) + (CELL_SIZE // 2))
                window.blit(number, number_rect)


def draw_selected_cell():
    if selected_cell is not None:
        pygame.draw.rect(window, RED, selected_cell, 5)


def get_selected_cell(mouse_pos):
    row = mouse_pos[1] // CELL_SIZE
    col = mouse_pos[0] // CELL_SIZE

    return pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)


def update_selected_cell(mouse_pos):
    global selected_cell
    selected_cell = get_selected_cell(mouse_pos)


def set_number(mouse_pos, number):
    row = mouse_pos[1] // CELL_SIZE
    col = mouse_pos[0] // CELL_SIZE

    board[row][col] = number


def draw_run_button():
    font = pygame.font.Font(None, 36)
    text = font.render("Run!", True, BLACK)

    if run_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, RED, run_button)
        text = font.render("Run!", True, WHITE)
    else:
        pygame.draw.rect(window, GRAY, run_button)

    text_rect = text.get_rect(center=run_button.center)
    window.blit(text, text_rect)


def draw_reset_button():
    font = pygame.font.Font(None, 36)
    text = font.render("Reset", True, BLACK)

    if reset_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, RED, reset_button)
        text = font.render("Reset", True, WHITE)
    else:
        pygame.draw.rect(window, GRAY, reset_button)

    text_rect = text.get_rect(center=reset_button.center)
    window.blit(text, text_rect)


def reset_board():
    for i in range(9):
        for j in range(9):
            board[i][j] = 0


def main():
    pygame.display.set_caption("Sudoku Solver")

    running = True

    while running:
        window.fill(WHITE)
        draw_grid()
        draw_numbers()
        draw_selected_cell()
        draw_run_button()
        draw_reset_button()
        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1] < 540:
                    update_selected_cell(mouse_pos)
                elif run_button.collidepoint(mouse_pos):
                    if verification.verify(board):
                        board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8] = map(copy.copy, solve.solve(board))
                elif reset_button.collidepoint(mouse_pos):
                    reset_board()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 1)
                elif event.key == pygame.K_2:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 2)
                elif event.key == pygame.K_3:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 3)
                elif event.key == pygame.K_4:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 4)
                elif event.key == pygame.K_5:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 5)
                elif event.key == pygame.K_6:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 6)
                elif event.key == pygame.K_7:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 7)
                elif event.key == pygame.K_8:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 8)
                elif event.key == pygame.K_9:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 9)
                elif event.key in [pygame.K_BACKSPACE, pygame.K_DELETE, pygame.K_0]:
                    if selected_cell is not None:
                        set_number(selected_cell.topleft, 0)


if __name__ == "__main__":
    main()
    pygame.quit()
