import graphics

def main():
    win = graphics.GraphWin("My Window", 407,407)
    win.setBackground(graphics.color_rgb(200,200,50))
    for j in range(0,400,102):
        for i in range(0,400,102):
            pt = graphics.Point(i,j)
            pt2 = graphics.Point(i+100,j+100)
            print("(",i,",",j,") to (" ,i+j+100,j+100,")")
            sq = graphics.Rectangle(pt, pt2)
            sq.setFill(graphics.color_rgb(0,0,0))
            sq.draw(win)
    win.getMouse()
    win.close()

main()
