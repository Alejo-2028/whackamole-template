import pygame
import random

def main():
    pygame.init()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 512
    GRID_SIZE = 32
    GRID_COLUMNS = SCREEN_WIDTH // GRID_SIZE
    GRID_ROWS = SCREEN_HEIGHT // GRID_SIZE

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Whack-a-Mole")

    mole_image = pygame.image.load("mole.png")
    mole_image = pygame.transform.scale(mole_image, (GRID_SIZE, GRID_SIZE))

    mole_x = 0
    mole_y = 0

    def draw_grid():
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))

    def move_mole():
        nonlocal mole_x, mole_y
        mole_x = random.randrange(GRID_COLUMNS) * GRID_SIZE
        mole_y = random.randrange(GRID_ROWS) * GRID_SIZE

    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + GRID_SIZE and mole_y <= mouse_y < mole_y + GRID_SIZE:
                        move_mole()

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
