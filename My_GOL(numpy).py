import numpy as np
import os
import pygame

ALIVE = 1
DEAD = 0
vals = [ALIVE, DEAD]

#vals: C'est un tableau qui représente l'ensemble de valeurs parmi
# 		lesquelles nous voulons choisir, entre 0 et 1.

#N*N: C'est le nombre total d'éléments que nous voulons choisir. Dans ce cas,
# 		c'est égal à la taille de la grille, c'est-à-dire NxN.

#p=[0.2, 0.8]: C'est le paramètre de probabilité associé à chaque élément de
# 				vals. Il définit la probabilité d'apparition de chaque élément.
# 				La probabilité de choisir 0 (cellules mortes) est de 0.2,
# 				La probabilité de choisir 1 (cellules vivantes) est de 0.8.

#.reshape(N, N): C'est une fonction de manipulation des tableaux NumPy qui permet
# 				de remodeler le tableau résultant en une grille de taille NxN.
# 				La fonction numpy.random.choice renvoie un tableau à une dimension,
# 				et .reshape(N, N) le remodèle en une grille de taille NxN.

def init_grid(N):
    arr = 0
    arr = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
    print(arr)
    return (arr)

# une cellule morte possédant exactement 3 cellules voisines vivantes devient vivante.
# une cellule vivante, qui dispose de moins de 2 ou de plus de 3 voisines vivantes, meurt 

def update_grid(grid, N):
    new_grid = np.copy(grid)

    for i in range(N):
        for j in range(N):
            neighbord_alive = np.sum(grid[max(i-1, 0):min(i+2, N), max(j-1, 0):min(j+2, N)]) - grid[i, j]
            if grid[i, j] == ALIVE:
                if neighbord_alive < 2 or neighbord_alive > 3:
                    new_grid[i, j] = DEAD
            else:
                if neighbord_alive == 3:
                    new_grid[i, j] = ALIVE
    return new_grid

def draw_grid(grid, screen, cell_size, offset):
    for i in range(grid.shape[DEAD]):
        for j in range(grid.shape[ALIVE]):
            color = (255, 255, 255) if grid[i, j] == ALIVE else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size + offset, cell_size, cell_size))

def draw_generation_counter(screen, generation_counter):
    font = pygame.font.Font(None, 35)
    text_surface = font.render(f"Generation: {generation_counter}", True, (255,255, 255))
    text_rect = text_surface.get_rect(center=(N * cell_size // 2, 20))  # 20 est la distance du haut
    screen.blit(text_surface, text_rect)

def main(N, cell_size):
    pygame.init()
    margin = 40 # offset
    screen = pygame.display.set_mode((N * cell_size, N * cell_size + margin))
    pygame.display.set_caption("Game of Life by John Conway")
    grid = init_grid(N)
    generation_counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("want to escape")
                running = False
        os.system('cls' if os.name =='nt' else 'clear')
        screen.fill((0, 0, 0))  # Remplir l'écran avec un fond noir avant de dessiner
        draw_grid(grid, screen, cell_size, margin)
        draw_generation_counter(screen, generation_counter)
        pygame.display.flip()
        grid = update_grid(grid, N)
        generation_counter += 1
        pygame.time.delay(60)
    pygame.quit()

if __name__ == '__main__':
    N = int(input("Size of the grid: [30]"))
    cell_size = int(input("Size of the cell: [10]"))
    main(N, cell_size)
