from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create a root widget (window) where every other widget will reside.
        self.__root = Tk()
        
        # Set the title of the window.
        self.__root.title("Maze Solver")
        
        # Initialize a Canvas widget with the root widget as its master.
        # The Canvas helps in drawing graphics and complex drawings.
        self.__canvas = Canvas(self.__root, bg="#8b949e", height=height, width=width)
        
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

    # This method sets __window_running to False,
    # which stops the continuous calls to the redraw method 
    # from the wait_for_close method.
    def close(self):
        self.__window_running = False