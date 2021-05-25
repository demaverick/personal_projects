from typing import Text
import graphics

def main():
    win = graphics.GraphWin("My Window", 407,407)
    win.setBackground(graphics.color_rgb(200,200,50))
    pt = graphics.Point(250,250)
    txt = Text(pt,  "Whats up")
    txt.draw(win)
    win.getMouse()
    win.close()

main()