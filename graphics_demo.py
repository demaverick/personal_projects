from typing import Text
from graphics import *
import random



def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def main():
    win = GraphWin("2048", 407,407)
    win.setBackground(color_rgb(200,200,50))
    inp = "Left"
    board = [0]*16
    while inp in ["Left", "Up", "Down", "Right"]:
        print("Entere")
        index = 0
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
                num = board[index]
                text = Text(center, str(num))
                text.setTextColor(color_rgb(255,255,255))
                text.draw(win)
                index+=1
        print("Getting input")
        inp = win.getKey()
        clear(win)
main()
