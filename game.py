from grid import Grid
from blocks import *
import random
class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), LBlock(), OBlock(), SBlock(), TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) > 0:
            block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False:
            self.current_block.move(0, -1)



    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False:
            self.current_block.move(-1, 0)
    
    def rotate(self):
        self.current_block.rotate() 
        if self.block_inside() == False:
            self.current_block.undo()
        
    def undo(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells)


    def block_inside(self):
        tiles = self.current_block.get_self_positions()
        for tile in tiles: 
            if self.grid.is_inside(tile.row, tile.column) ==  False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
