import pygame
import setup
import constants as constants
import test_visualisation
    


def main(win, width):
    ROWS = 10
    grid = setup.make_grid(ROWS, width)

    start = None
    end = None
    
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
                    start.color = constants.red
                    node.color = constants.red
                    startnode = row, col
                elif not end and node != start:
                    end = node
                    end.color = constants.green
                    node.color = constants.green
                    endnode = row, col
                elif node != end and node != start:
                    node.color = constants.black
                    wall = []
                    wall.append((row, col))

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = setup.get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.color = constants.white
                if node == start:
                    start = None
                elif node == end:
                    end = None
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    test_visualisation.ripple_cascade(WIN, grid, ROWS, width, start, constants.yellow)
                if event.key == pygame.K_r: # Reset Key
                    start = None
                    end = None
                    setup.reset_grid(grid)
                
                if event.key == pygame.K_c:
                    print("\033[H\033[J")  # Clear console
                    print("Current Start and End Nodes:")
                    print(f"Start: {startnode}")
                    print(f"End: {endnode}")
                
                if event.key == pygame.K_ESCAPE:
                    exit(0)
                    
    pygame.quit()

if __name__ == "__main__":
    WIDTH = 800
    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Path Finding Algorithm")
    main(WIN, WIDTH)
