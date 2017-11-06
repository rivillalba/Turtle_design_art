#function file
def polygon(t,s,d):
    angle = 360/s
    for times in range(s):
        t.forward(d)
        t.right(angle)
        
def polygin(t,s,d):
    angle = 290/s
    for times in range(s):
        t.forward(d)
        t.right(angle)

def polygonFill(t,s,d,c):#parameters(imformation)
    a = 360/s #angle variableis inside the function
    t.color(c)
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)
        t.end_fill()

def jump(t,x,y):#parameters
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool(t,d,c1,c2):#parameters
    t.color(c1)
    polygon(t,6,d)#call to the functions
    t.color(c2)
    polygon(t,5,d)

def logo(t,d,c1,c2):#parameters
    t.color(c1)
    t.circle(d)
    t.color(c2)
    polygon(t,3,d)

def meh(t,t2):
    for times in range(256):
        t.width(1)
        t.right(190)
        t.color(91,175,91)
        polygon(t,8,times+10)
        t2.color(times,times,times)
        t2.right(190)
        polygon(t2,8,times+15)
        t.width(2)
        t.color(125,125,125)
        t.forward(1)
        t.color(127,0,255)
        t.circle(200)

def meh2(t,t2):
    for times in range(256):
        t.width(1)
        t.right(190)
        t.color(times,times,0)
        polygin(t,8,times+10)
        t2.color(times,times,times)
        t2.right(190)
        polygin(t2,8,times+15)
        t.width(1)
        t.color(125,125,125)
        t.forward(1)
        t.color(255,153,255)
        t.circle(200)
