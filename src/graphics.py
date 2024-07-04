from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        # Create a root widget (window) where every other widget will reside.
        self.__root = Tk()

        # Set the title of the window.
        self.__root.title("Maze Solver")

        # Initialize a Canvas widget with the root widget as its master.
        # The Canvas helps in drawing graphics and complex drawings.
        self.__canvas = Canvas(self.__root, bg="#8b949e",
                               height=height, width=width)

        # Pack the Canvas widget into the window (root widget).
        # fill=BOTH makes the Canvas expand to fill the available space.
        # expand=1 makes the Canvas expand along with the window.
        self.__canvas.pack(fill=BOTH, expand=1)

        # Set the initial running state of the window to False.
        self.__window_running = False

        # Set up a protocol to handle window closing.
        # "WM_DELETE_WINDOW" is a predefined protocol name in Tkinter.
        # It represents the action of closing the window through the close button.
        # When the window closes, it sets __window_running to False, eventually
        # stopping the redraw method and stopping the program.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # Tkinter is not a reactive framework, so we need to redraw
    # graphics manually when we want to render visuals.
    # This method redraws all the graphics in the window.
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # This method will keep redrawing the graphics
    # while __window_running is True.
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
        print("window closed...")

    # This method draw a line on canvas by calling draw method of Line class on a Line instance
    # and a color(color of line)
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    # This method sets __window_running to False,
    # which stops the continuous calls to the redraw method
    # from the wait_for_close method.
    def close(self):
        self.__window_running = False


class Point:
    def __init__(self, x, y):
        # x = 0 => left of the screen
        # y = 0 => top of the screen
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    # This method draw a line on a canvas with the desired color of the line
    def draw(self, canvas, fill_color="white"):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    # The constructor takes x1,y1(top-left-corner) and x2,y2(bottom-right-corner)
    # and a window instance and whether the walls exists or not
    def __init__(self,
                 x1,
                 y1,
                 x2,
                 y2,
                 window,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self):
        # This method just checks if a wall exists or not
        # If they exist simply draw that wall on canvas through draw_line method of window class
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "red")
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "red")
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "red")
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "red")

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
        center_1 = Point((self._x1 + (self._x2 - self._x1)/2), (self._y1 + (self._y2 - self._y1)/2))
        
        # Calculate center of the target cell
        center_2 = Point((to_cell._x1 + (to_cell._x2 - to_cell._x1)/2), (to_cell._y1 + (to_cell._y2 - to_cell._y1)/2))
        
        # Create a line from the center of the current cell to the center of the target cell
        line = Line(center_1, center_2)
        
        # Draw the line in gray if undo is True, otherwise in red
        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")