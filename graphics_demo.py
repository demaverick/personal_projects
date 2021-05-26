from typing import Text
from graphics import *
import random

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
            num = random.randint(0,10)
            text = Text(center, str(num))
            text.setTextColor(color_rgb(255,255,255))
            text.draw(win)
    inp = win.getKey()
    print(inp)
    if inp == 'Left':
        print("left pressed")
        win.close()
        main()
    elif inp == "Right":
        print("Right Pressed")
        win.close()
        main()
    elif inp == "Up":
        print("Up pressed")
        win.close()
        main()
    elif inp == "Down":
        print("Down pressed")
        win.close()
        main()
    else:
        print("Exiting")
        win.close()
main()
