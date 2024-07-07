from graphics import Window
from maze import Maze

def main():
    win = Window(800,600)
    maze = Maze(550, 200, 20, 20, 40, 40, win)
    maze.solve()
    win.wait_for_close()

main()