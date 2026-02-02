# utils.py
import pygame
import setup
import constants as constants

found_end = False

def ripple_cascade(win, grid, rows, width, start_node, color):
    max_dist = rows * 2 
    node_number = 0
    start_r, start_c = start_node.row, start_node.col

    for dist in range(max_dist):
        found_any = False
        for r in range(rows):
            for c in range(rows):
                if abs(r - start_r) + abs(c - start_c) == dist:
                    node = grid[r][c]
                    node_number += 1
                    print("Distance of node {} is {}".format(node_number, dist))
                    if node.color == (255, 255, 255): 
                        node.color = color
                        found_any = True
                    elif node.color == constants.black:
                        print("Hit a wall at ({}, {})".format(r, c))
                    elif node.color == constants.green:
                        print("Reached the end node at ({}, {})".format(r, c))
                        found_end = True
                        if found_end == True: 
                            return
        
        if not found_any and dist > 0:
            break
            
        setup.draw(win, grid, rows, width)
        pygame.time.delay(100)