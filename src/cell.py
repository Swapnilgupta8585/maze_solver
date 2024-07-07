from graphics import Line, Point


class Cell:
    # The constructor takes x1,y1(top-left-corner) and x2,y2(bottom-right-corner)
    # and a window instance and whether the walls exists or not
    def __init__(self,window=None,):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        # This method just checks if a wall exists or not
        # If they exist simply draw that wall on canvas through draw_line method of window class

        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "#343434")
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white")
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "#343434")
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "#343434")
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "#343434")

    def draw_move(self, to_cell, undo=False):
        """
        Draw a move from the current cell to the target cell (`to_cell`).

        The line will be drawn from the center of the current cell to the center of the target cell.
        - If the `undo` flag is set to True, the line will be drawn in gray.
        - Otherwise, the line will be drawn in red.

        Assumptions:
        - All cells are square.
        - Coordinates are even numbers.

        Steps to calculate the center of a cell:
        1. `center_1_x` = left wall x-coordinate + half the distance between left and right walls.
        2. `center_1_y` = top wall y-coordinate + half the distance between top and bottom walls.
        3. Similarly, calculate `center_2` for the target cell.
        """

        # Calculate center of the current cell
        center_1 = Point((self._x1 + (self._x2 - self._x1)/2),
                         (self._y1 + (self._y2 - self._y1)/2))

        # Calculate center of the target cell
        center_2 = Point((to_cell._x1 + (to_cell._x2 - to_cell._x1)/2),
                         (to_cell._y1 + (to_cell._y2 - to_cell._y1)/2))

        # Create a line from the center of the current cell to the center of the target cell
        line = Line(center_1, center_2)

        # Draw the line in gray if undo is True, otherwise in red
        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")
