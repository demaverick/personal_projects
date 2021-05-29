from typing import Text
from graphics import *
import random



def clear(win):
    for item in win.items[:]:
        if "Text" in str(item):
            item.undraw()
            print(item," Undrawn")
    win.update()


def main():
    win = GraphWin("2048", 407,407)
    win.setBackground(color_rgb(200,200,50))
    inp = "Left"
    board = [0]*16
    while inp in ["Left", "Up", "Down", "Right"]:
        index = 0
        for j in range(0,400,102):
            for i in range(0,400,102):
                pt = Point(i,j)
                pt2 = Point(i+100,j+100)
                # print("(",i,",",j,") to (" ,i+j+100,j+100,")")
                sq = Rectangle(pt, pt2)
                sq.setFill(color_rgb(0,0,0))
                center = sq.getCenter()
                sq.draw(win)
                num = board[index]
                text = Text(center, num)
                text.setTextColor(color_rgb(255,255,255))
                text.draw(win)
                index+=1
        inp = win.getKey()
        clear(win)
main()
