from graphics import Window, Line, Point, Cell

def main():
    win = Window(800,600)
    cell = Cell(10,10,110,110,win,True,True,True,True)
    cell2 = Cell(110,10,210,110,win)
    cell.draw()
    cell2.draw()
    win.wait_for_close()

main()