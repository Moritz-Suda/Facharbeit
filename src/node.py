import pygame
import constants as constants

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.y = row * width
        self.x = col * width
        self.color = constants.white
        self.width = width

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid, rows, width):
        self.neighbors = []
        if self.row < rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == constants.red

    def is_open(self):
        return self.color == constants.green

    def is_barrier(self):
        return self.color == constants.black

    def is_start(self):
        return self.color == constants.orange

    def is_end(self):
        return self.color == constants.green

    def reset(self):
        self.color = constants.white

    def make_start(self):
        self.color = constants.orange

    def make_closed(self):
        self.color = constants.red

    def make_open(self):
        self.color = constants.turquoise

    def make_barrier(self):
        self.color = constants.black

    def make_end(self):
        self.color = constants.green

    def make_path(self):
        self.color = constants.purple