from typing import Text
from graphics import *

def main():
    win = GraphWin("2048", 407,407)
    win.setBackground(color_rgb(200,200,50))
    for j in range(0,400,102):
        for i in range(0,400,102):
            pt = Point(i,j)
            pt2 = Point(i+100,j+100)
            print("(",i,",",j,") to (" ,i+j+100,j+100,")")
            sq = Rectangle(pt, pt2)
            sq.setFill(color_rgb(0,0,0))
            center = sq.getCenter()
            sq.draw(win)
            # cir = Circle(center, 20)
            # cir.setFill(color_rgb(255,255,255))
            # cir.draw(win)
            text = Text(center, "0")
            text.setTextColor(color_rgb(255,255,255))
            text.draw(win)
    win.getMouse()
    win.close()

main()
