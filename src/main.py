from graphics import Window, Line, Point

def main():
    win = Window(800,600)
    line = Line(Point(0,0), Point(488,488))
    win.draw_line(line, "yellow")
    win.wait_for_close()

main()