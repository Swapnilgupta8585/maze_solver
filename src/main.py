from graphics import Window  
from maze import Maze        

def main():
    # Create a new window with a width of 800 pixels and a height of 600 pixels
    win = Window(800, 600)
    
    # Initialize a Maze object with specified parameters
    # Parameters: width, height, cell_width, cell_height, start_x, start_y, window
    maze = Maze(550, 200, 20, 20, 40, 40, win)
    
    # Solve the maze
    maze.solve()
    
    # Wait for the user to close the window before exiting the program
    win.wait_for_close()

# Call the main function to execute the program
main()
