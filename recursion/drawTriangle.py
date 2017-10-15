import turtle


def drawTriangle(points, color, my_turtle):
    my_turtle.fillColor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def getmid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) /2)


def sierpinski(points, degree, myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getmid(points[0], points[1]),
                        getmid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getmid(points[0], points[1]),
                        getmid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getmid(points[2], points[1]),
                        getmid(points[0], points[2])],
                   degree-1, myTurtle)


def main():
   my_turtle = turtle.Turtle()
   my_win = turtle.Screen()
   my_points = [[-100, -50],[0, 100],[100, -50]]
   sierpinski(my_points, 3, my_turtle)
   my_win.exitonclick()


main()