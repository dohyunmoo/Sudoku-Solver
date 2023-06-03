import pygame

width = 800
height = 600
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("My Game")

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render the game

pygame.quit()