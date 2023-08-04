import numpy as np
import os
import pygame

ALIVE = 1
DEAD = 0
vals = [ALIVE, DEAD]

#vals: C'est un tableau ou une liste qui représente l'ensemble de valeurs parmi
# 		lesquelles nous voulons choisir. Dans votre cas, vals semble être [0, 1],
# 		car vous voulez choisir aléatoirement entre les valeurs 0 (cellules mortes)
# 		et 1 (cellules vivantes).

#N*N: C'est le nombre total d'éléments que nous voulons choisir. Dans ce cas,
# 		c'est égal à la taille de la grille, c'est-à-dire NxN.

#p=[0.2, 0.8]: C'est le paramètre de probabilité associé à chaque élément de
# 				vals. Il définit la probabilité d'apparition de chaque élément.
# 				Dans votre cas, vous avez spécifié [0.2, 0.8], ce qui signifie
# 				que la probabilité de choisir 0 (cellules mortes) est de 0.2,
# 				et la probabilité de choisir 1 (cellules vivantes) est de 0.8.

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
# une cellule vivante, possédant 2 ou 3 cellules voisines vivantes, reste vivante, sinon elle meurt.

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

def draw_grid(grid, screen, cell_size):
    for i in range(grid.shape[DEAD]):
        for j in range(grid.shape[ALIVE]):
            color = (255, 255, 255) if grid[i, j] == ALIVE else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

def draw_generation_counter(screen, generation_counter):
    font = pygame.font.Font(None, 35)
    text_surface = font.render(f"Generation: {generation_counter}", True, (255,255, 255))
    screen.blit(text_surface, (10, 10))

def main(N, cell_size):
    pygame.init()
    screen = pygame.display.set_mode((N * cell_size, N * cell_size))
    pygame.display.set_caption("Game of Life by John Conway")
    grid = init_grid(N)
    generation_counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.K_ESCAPE:
                print("want to escape")
                running = False
        os.system('cls' if os.name =='nt' else 'clear')
        draw_grid(grid, screen, cell_size)
        draw_generation_counter(screen, generation_counter)
        pygame.display.flip()
        grid = update_grid(grid, N)
        generation_counter += 1
        pygame.time.delay(60)
    pygame.quit()



if __name__ == '__main__':
    #N = int(input("Size of the grid: "))
    cell_size = 20  # Taille des cellules en pixels (vous pouvez ajuster selon vos préférences)
    N = 50
    main(N, cell_size)
