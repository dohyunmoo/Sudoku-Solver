import pygame
import verification

pygame.init()

WIDTH, HEIGHT = 540, 600
CELL_SIZE = WIDTH // 9

BUTTON_WIDTH = WIDTH // 5
BUTTON_HEIGHT = CELL_SIZE // 3

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))

button = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, (HEIGHT - CELL_SIZE // 2) - BUTTON_HEIGHT // 2), (BUTTON_WIDTH, BUTTON_HEIGHT))

# initial empty grid
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


def draw_button():
    font = pygame.font.Font(None, 36)
    text = font.render("Run!", True, BLACK)

    if button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, RED, button)
        text = font.render("Run!", True, WHITE)
    else:
        pygame.draw.rect(window, GRAY, button)

    text_rect = text.get_rect(center=button.center)
    window.blit(text, text_rect)


def main():
    pygame.display.set_caption("Sudoku Solver")

    running = True

    while running:
        window.fill(WHITE)
        draw_grid()
        draw_numbers()
        draw_selected_cell()
        draw_button()
        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1] < 540:
                    update_selected_cell(mouse_pos)
                elif button.collidepoint(mouse_pos):
                    print(verification.verify(board))
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
