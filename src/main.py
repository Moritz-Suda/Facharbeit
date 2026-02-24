import pygame
import setup
import constants as constants
import algorithm


global ROWS
ROWS = 10

def main(win, width):
    grid = setup.make_grid(ROWS, width)

    start = None
    end = None
    startnode = None
    endnode = None

    run = True
    while run:
        setup.draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = setup.get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                    startnode = row, col
                elif not end and node != start:
                    end = node
                    end.make_end()
                    endnode = row, col
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = setup.get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    setup.reset_grid(grid)

                if event.key == pygame.K_SPACE:
                    if start and end:
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid, ROWS, width)
                        
                        algorithm.bfs(lambda: setup.draw(win, grid, ROWS, width), grid, start, end)                
                
                if event.key == pygame.K_ESCAPE:
                    exit(0)
                    
    pygame.quit()
try:
    if __name__ == "__main__":
        WIDTH = 800
        WIN = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("Path Finding Algorithm")
        main(WIN, WIDTH)
except:
    print("An error occurred. Please try again.")
