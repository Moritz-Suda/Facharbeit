from collections import deque

import constants
import setup
import pygame
import time
import main
import node

def bfs(ROWS, startnode, endnode):
    print("BFS Algorithm Started")
    print(f"Start Node: {startnode}")
    print(f"End Node: {endnode}")
    print(f"Grid Size: {ROWS}x{ROWS}")

