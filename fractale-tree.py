import turtle

def mandala():
    ninja = turtle.Turtle()
    ninja.speed(100)
    for i in range(50):
        ninja.forward(50)
        ninja.left(123)
    
        ninja.pencolor("red")
        for i in range(25):
            ninja.forward(200)
            ninja.left(123)
    
    turtle.done()

def tree(size, n):
    if n == 0:
        ninja.forward(size)
    else:
        ninja.color("red")
        ninja.forward(size/2.0)
        ninja.color("green")
        ninja.left(45)
        tree(size/2.0,n-1)
        ninja.penup()
        ninja.backward(size/2.0)
        ninja.right(90)
        ninja.pendown()
        tree(size/2.0,n-1)
        ninja.penup()
        ninja.backward(size/2.0)
        ninja.left(45)
        ninja.pendown()
        tree(size/2.0,n-1)


if __name__ == "__main__":
    ninja = turtle.Turtle()
    ninja.speed(1)
    tree(200, 4)
