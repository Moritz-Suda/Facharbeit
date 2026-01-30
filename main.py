import pygame
import setup
import constants
    


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

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = setup.get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.color = constants.red
                    node.color = constants.red
                elif not end and node != start:
                    end = node
                    end.color = constants.green
                    node.color = constants.green
                elif node != end and node != start:
                    node.color = constants.black

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = setup.get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.color = constants.white
                if node == start:
                    start = None
                elif node == end:
                    end = None

    pygame.quit()

if __name__ == "__main__":
    WIDTH = 800
    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Path Finding Algorithm")
    main(WIN, WIDTH)
