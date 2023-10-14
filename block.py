import pygame
from colors import Colors
from position import Position
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.roww_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
    
    def move(self, rows, columns):
        self.roww_offset += rows
        self.column_offset += columns

    def get_self_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.roww_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
   
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    
    def draw(self, screen):
        tiles = self.get_self_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
