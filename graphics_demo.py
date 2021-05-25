from typing import Text
import graphics

def main():
    win = graphics.GraphWin("2048", 407,407)
    win.setBackground(graphics.color_rgb(200,200,50))
    for j in range(0,400,102):
        for i in range(0,400,102):
            pt = graphics.Point(i,j)
            pt2 = graphics.Point(i+100,j+100)
            print("(",i,",",j,") to (" ,i+j+100,j+100,")")
            sq = graphics.Rectangle(pt, pt2)
            sq.setFill(graphics.color_rgb(0,0,0))
            center = sq.getCenter()
            sq.draw(win)
            cir = graphics.Circle(center, 20)
            cir.setFill(graphics.color_rgb(255,255,255))
            cir.draw(win)
            # text = Text(center, "Hello")
            # text.setTextColor(graphics.color_rgb(255,255,255))
            # text.draw(win)
    win.getMouse()
    win.close()

main()
