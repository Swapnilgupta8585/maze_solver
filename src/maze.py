from cell import Cell
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        """
        x1 is the position of maze from the left side of the canvas and y1
        is from the top of the canvas

        we are calling the self._create_cells method in the constructor so that
        we can initialize self._cells 2D array so that we can use it as a data member
        in testing Maze class and it's methods
        """

        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(4, 7)
        self._reset_cells_visited()

    def _create_cells(self):
        """
        creating cells by first making a empty array self._cells,
        then we will populate this array and will make it a 2D array for storing the
        cell objects by calling _draw_cell method on each cells in the 2D array
        the first element of 2D array will be the array of first column and the second one
        is the second column and so on..
        the first element in the first column array is the first row for that
        column

        """

        for i in range(self.num_cols):
            self._cols = []
            for j in range(self.num_rows):
                self._cols.append(Cell(self._win))
            self._cells.append(self._cols)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        """
        In this method we take i,j as inputs which are the position of the cell in the
        2D array with the help of it we can tell the position of the cell on the canvas
        first we calculate the top-left-corner point(x1,y1) and then calculates the bottom right
        corner (x2,y2) and then we make a Cell instance and calls it's draw method
        """

        if self._win:
            x1 = self.x1 + self.size_x * (i)
            y1 = self.y1 + self.size_y * (j)
            x2 = x1 + self.size_x
            y2 = y1 + self.size_y
            self._cells[i][j].draw(x1, y1, x2, y2)
            self._animate()

    def _animate(self):

        # helps us in visualizing the maze formation by redrawing the window and then sleep for 0.05 sec so that
        # our eyes can see the change
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows -1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        """
        It breaks walls recursively,first we set current cell as visited
        """

        self._cells[i][j]._visited = True
        while True:

            # intialise possible_directions for collecting the adjacent cells to the current cell
            possible_directions = []

            #right cell wrt to current cell
            if 0 <= i+1 < self.num_cols and 0 <= j < self.num_rows and not self._cells[i+1][j]._visited:
                possible_directions.append((i+1, j))

            #down cell wrt to current cell
            if 0 <= i < self.num_cols and 0 <= j+1 < self.num_rows and not self._cells[i][j+1]._visited:
                possible_directions.append((i, j+1))

            #left cell wrt to current cell
            if 0 <= i-1 < self.num_cols and 0 <= j < self.num_rows and not self._cells[i-1][j]._visited:
                possible_directions.append((i-1, j))

            #top cell wrt to current cell
            if 0 <= i < self.num_cols and 0 <= j-1 < self.num_rows and not self._cells[i][j-1]._visited:
                possible_directions.append((i, j-1))
            
            #if no direction to go just return
            if len(possible_directions) == 0:
                return

            #generating a random number so that we can randomly choose any adjacent cell of the current cell
            random_num = random.randrange(0, len(possible_directions))

            #get a random adjacent cell
            ni, nj = possible_directions[random_num]

            # Knock down the walls between the current cell and the chosen cell
            
            #if adjacent cell is right to current cell then remove right wall of current cell
            #and left wall of the adjacent cell 
            if ni == i+1 and nj == j:
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False

            #if adjacent cell is down to current cell then remove bottom wall of current cell
            #and top wall of the adjacent cell
            elif ni == i and nj == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False

            #if adjacent cell is left to current cell then remove left wall of current cell
            #and right wall of the adjacent cell
            elif ni == i-1 and nj == j:
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False

            #if adjacent cell is up to current cell then remove top wall of current cell
            #and bottom wall of the adjacent cell
            elif ni == i and nj == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False

            # whatever the cell is to the cuurent cell draw that cell as the changes are not visible in the canvas
            #even after change in the memory so we have to draw the cell again
            self._draw_cell(ni, nj)

            # Recursively call _break_walls_r for the chosen cell
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):

        #reseting every cell's self._visited property to False for reusing it to solve the maze
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j]._visited = False