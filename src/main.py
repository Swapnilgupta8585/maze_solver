from graphics import Window
from maze import Maze

def main():
    win = Window(800,600)
    maze = Maze(550, 200, 10, 10, 80, 80, win)
   
    win.wait_for_close()

main()