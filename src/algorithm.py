from collections import deque
import constants
import pygame



def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def bfs(draw, grid, start, end):
    queue = deque()
    queue.append(start)
    came_from = {}
    
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = queue.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if not neighbor.is_open() and not neighbor.is_closed() and not neighbor.is_start():
                came_from[neighbor] = current
                queue.append(neighbor)
                neighbor.make_open()
        
        draw()

        if current != start:
            current.make_closed()

    return False

