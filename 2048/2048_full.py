__author__ = 'nilmadhab'

"""
Clone of 2048 game.
http://www.codeskulptor.org/#user39_eIAM4mQql2_22.py
"""
"""
Clone of 2048 game.
"""

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
import random
# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    line1 = list(line)
    for ind in range(len(line1)):
        #print ind
        if line1[ind] == 0:
            #pass
            line1.remove(line1[ind])
            line1.append(0)
        #print line
    line2 = list(line1)
    for ind in range(len(line2)-1):
        if line2[ind] == line2[ind+1]:
            line2[ind] *= 2
            line2[ind+1] = 0 #remove(line2[ind+1])
            #line2.append(0)
            #ind += 1
        #print line
    line1 = list(line2)
    for ind in range(len(line1)):
        #print ind
        if line1[ind] == 0:
            #pass
            line1.remove(line1[ind])
            line1.append(0)

    return line1

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = []
        self._look = {"LEFT": [],"RIGHT": [],"DOWN": [],"UP": []}
        #self.cells = [ [for col in range(grid_width)] for row in range(grid_height)]
        for dummy_col in range(grid_height):
            nil = []
            for dummy_row in range(grid_width):
                nil.append(0)
            self._cells.append(nil)
        print self._cells
        for row in range(self.get_grid_height()):
            nil = []
            nil.append((row,0))
            self._look["LEFT"].append(nil)
            self._look["RIGHT"].append(nil)
        for col in range(self.get_grid_width()):
                #self._look["UP"].append((row,col))
            nil = []
            nil.append((0,col))
            self._look["UP"].append(nil)
            self._look["DOWN"].append(nil)
        #print self._look["LEFT"]
        #print "UP",self._look["UP"]
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                for ind in  self._look["UP"]:
                    if col == ind[0][1] and row != 0:
                        ind.append((row,col))
                for ind in  self._look["LEFT"]:
                    if row == ind[0][0] and col != 0:
                        ind.append((row,col))

        #print self._look["LEFT"]


        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code

        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                self.set_tile(row,col,0)

        self.new_tile()
        self.new_tile()
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code

        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        if direction == 1:
            for ind in  self._look["UP"]:
                nil = []
                #print ind
                for indx in range(len(ind)):
                    print ind[indx][0]
                    nil.append(self._cells[ind[indx][0]][ind[indx][1]])
                #print nil
                nil = merge(nil)
                #print nil
                count = 0
                for dummy in ind:
                    self.set_tile(dummy[0], dummy[1], nil[count])
                    count+=1
            self.new_tile()
            return
        if direction == 2:
            for ind in  self._look["DOWN"]:
                nil = []
                #print ind
                for indx in range(len(ind)):
                    #print ind[indx][0]
                    nil.append(self._cells[ind[indx][0]][ind[indx][1]])
                #print nil
                nil = nil[::-1]
                nil = merge(nil)
                nil = nil[::-1]
                #print nil
                count = 0
                for dummy in ind:
                    self.set_tile(dummy[0], dummy[1], nil[count])
                    count+=1
            self.new_tile()
            return
        if direction == 3:
            for ind in  self._look["LEFT"]:
                nil = []
                #print ind
                for indx in range(len(ind)):
                    #print ind[indx][0]
                    nil.append(self._cells[ind[indx][0]][ind[indx][1]])
                #print nil
                nil = merge(nil)
                #print nil
                count = 0
                for dummy in ind:
                    self.set_tile(dummy[0], dummy[1], nil[count])
                    count+=1
            self.new_tile()
            return
        if direction == 4:
            for ind in  self._look["RIGHT"]:
                nil = []
                #print ind
                for indx in range(len(ind)):
                    #print ind[indx][0]
                    nil.append(self._cells[ind[indx][0]][ind[indx][1]])
                #print nil
                nil = nil[::-1]
                nil = merge(nil)
                #print nil
                nil = nil[::-1]
                count = 0
                for dummy in ind:
                    self.set_tile(dummy[0], dummy[1], nil[count])
                    count+=1
            self.new_tile()
            return


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        rowx = random.randint(0,self.get_grid_height()-1)
        colx = random.randint(0,self.get_grid_width()-1)
        count = 0
        while self.get_tile(rowx,colx) != 0:
            rowx = random.randint(0,self.get_grid_height()-1)
            colx = random.randint(0,self.get_grid_width()-1)
            count = 0
            for row in range(self.get_grid_height()):
                for col in range(self.get_grid_width()):
                    if self.get_tile(row, col) == 0:
                        count +=1
            if count == 0:
                return

        nil = random.randint(1,10)
        if nil == 5:
            self.set_tile(rowx,colx,4)
        else:
            self.set_tile(rowx,colx,2)
        return

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        #self.
        #print row,col
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        #print row,col
        return  self._cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(5, 4))
