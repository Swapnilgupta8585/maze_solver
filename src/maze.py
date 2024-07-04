from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size_x = cell_size_x
        self.size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cols = []
            for j in range(self.num_rows):
                self._cols.append(self._draw_cell(i,j))
            self._cells.append(self._cols)

    def _draw_cell(self, i, j):
        if self._win:
            x1 = self.x1 + self.size_x * (i)
            y1 = self.y1 + self.size_y * (j)
            x2 = x1 + self.size_x
            y2 = y1 + self.size_y
            cell = Cell(self._win)
            cell.draw(x1,y1,x2,y2)
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
        

