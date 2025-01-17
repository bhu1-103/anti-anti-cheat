import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import random

# Constants
WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 200
GRID_SIZE = 3
GRID_OFFSET = 50

# Colors
WHITE = (1, 1, 1)
GRAY = (0.5, 0.5, 0.5)
BLACK = (0, 0, 0)

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont(None, 48)

# Game grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

def draw_text(text, color, x, y):
    """Draws text on the screen."""
    font_surface = FONT.render(text, True, color)
    screen.blit(font_surface, (x, y))

def draw_grid():
    """Draws the game grid."""
    glColor3fv(GRAY)
    glBegin(GL_LINES)
    for i in range(1, GRID_SIZE):
        glVertex2f(i * BLOCK_SIZE + GRID_OFFSET, GRID_OFFSET)
        glVertex2f(i * BLOCK_SIZE + GRID_OFFSET, HEIGHT - GRID_OFFSET)
        glVertex2f(GRID_OFFSET, i * BLOCK_SIZE + GRID_OFFSET)
        glVertex2f(WIDTH - GRID_OFFSET, i * BLOCK_SIZE + GRID_OFFSET)
    glEnd()

def draw_blocks():
    """Draws the blocks on the game grid."""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                draw_block(j, i, grid[i][j])

def draw_block(x, y, value):
    """Draws a single block."""
    color = get_color(value)
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(x * BLOCK_SIZE + GRID_OFFSET, y * BLOCK_SIZE + GRID_OFFSET)
    glVertex2f((x + 1) * BLOCK_SIZE + GRID_OFFSET, y * BLOCK_SIZE + GRID_OFFSET)
    glVertex2f((x + 1) * BLOCK_SIZE + GRID_OFFSET, (y + 1) * BLOCK_SIZE + GRID_OFFSET)
    glVertex2f(x * BLOCK_SIZE + GRID_OFFSET, (y + 1) * BLOCK_SIZE + GRID_OFFSET)
    glEnd()
    draw_text(str(value), BLACK, x * BLOCK_SIZE + GRID_OFFSET + BLOCK_SIZE // 2 - 10, y * BLOCK_SIZE + GRID_OFFSET + BLOCK_SIZE // 2 - 10)

def get_color(value):
    """Returns the color for a block based on its value."""
    if value == 2:
        return (1, 0.8, 0.6)  # Light orange
    elif value == 4:
        return (1, 0.6, 0.4)  # Dark orange
    elif value == 8:
        return (1, 0.4, 0.2)  # Light red
    elif value == 16:
        return (1, 0.2, 0)  # Dark red
    elif value == 32:
        return (1, 0.8, 0.6)  # Light orange
    elif value == 64:
        return (1, 0.6, 0.4)  # Dark orange
    elif value == 128:
        return (1, 0.4, 0.2)  # Light red
    elif value == 256:
        return (1, 0.2, 0)  # Dark red
    elif value == 512:
        return (1, 0.8, 0.6)  # Light orange
    elif value == 1024:
        return (1, 0.6, 0.4)  # Dark orange
    elif value == 2048:
        return (1, 0.4, 0.2)  # Light red
    else:
        return (0.5, 0.5, 0.5)  # Gray

def add_new_block():
    """Adds a new block (2 or 4) to a random empty cell."""
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        x, y = random.choice(empty_cells)
        grid[y][x] = 2 if random.random() < 0.9 else 4

def shift(direction):
    """Shifts the grid in the specified direction."""
    global grid
    if direction == 'left':
        grid = np.hstack((np.delete(grid[i], np.where(grid[i] == 0)) if np.any(grid[i]) else np.array([0])) for i in range(GRID_SIZE))
    elif direction == 'right':
        grid = np.hstack((np.array([0]) if not np.any(grid[i]) else np.delete(grid[i], np.where(grid[i] == 0))) for i in range(GRID_SIZE))
    elif direction == 'up':
        grid = np.vstack((np.delete(grid[:, i], np.where(grid[:, i] == 0)) if np.any(grid[:, i]) else np.array([0])) for i in range(GRID_SIZE))
    elif direction == 'down':
        grid = np.vstack((np.array([0]) if not np.any(grid[:, i]) else np.delete(grid[:, i], np.where(grid[:, i] == 0))) for i in range(GRID_SIZE))
    add_new_block()

def check_game_over():
    """Checks if the game is over."""
    return not (np.any(grid == 0) or can_merge())

def can_merge():
    """Checks if any two adjacent blocks can merge."""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if grid[i][j] == grid[i][j + 1] or grid[j][i] == grid[j + 1][i]:
                return True
    return False

def init():
    """Initialization function for OpenGL."""
    glClearColor(*WHITE, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, HEIGHT, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    init()

    add_new_block()
    add_new_block()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    shift('left')
                elif event.key == K_RIGHT:
                    shift('right')
                elif event.key == K_UP:
                    shift('up')
                elif event.key == K_DOWN:
                    shift('down')

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_grid()
        draw_blocks()
        pygame.display.flip()

        if check_game_over():
            draw_text("Game Over!", BLACK, WIDTH // 2 - 100, HEIGHT // 2 - 25)
            pygame.display.flip()
            pygame.time.wait(2000)  # Display "Game Over" for 2 seconds
            grid.fill(0)
            add_new_block()
            add_new_block()

if __name__ == "__main__":
    main()

