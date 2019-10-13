import tkinter,random,math,time,datetime




def drawPoint(x,y,size = 1):
    mycanvas.create_oval(x-size+screenWidth/2,y-size+screenHeight/2,x+size+screenWidth/2,y+size+screenHeight/2)

def distance(x1,y1,x2,y2):
    return(math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))

class circle:
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
    def pointOnCircle(self,angle):
        angle = math.radians(angle)
        return([self.x + self.radius * math.cos(angle),self.y + self.radius * math.sin(angle)])
    def circumference(self):
        return(math.pi*self.radius*self.radius)
    def pointOnCircumference(self,angle,startx,starty):
        # returns the point on the circumference of the circle
        # where the angle between the cirrent point and the returned point is angle
        angle = - angle
        return([ startx + 2*self.radius*math.cos(math.radians(90-(angle/2)))* math.cos(math.radians((360-angle)/2))   , starty + 2*self.radius*math.cos(math.radians(90-(angle/2)))* math.sin(math.radians((360-angle)/2))])
    def pointPerpendicularToCircumference(self,angle,startx,starty,distAway):
        a = self.pointOnCircumference(angle,startx,starty)
        newPoint = ([a[0] - (a[0]-self.x) * (distAway/self.radius),a[1] - (a[1]-self.y) * (distAway/self.radius) ])
        return(newPoint)

bigCircle = circle(0,0,500)
smallCircleRadius = 240
smallCircle = circle(0,bigCircle.radius-smallCircleRadius,smallCircleRadius)
def setup():
    mycanvas.create_oval(bigCircle.x-bigCircle.radius+screenWidth/2,bigCircle.y-bigCircle.radius+screenHeight/2,bigCircle.x+bigCircle.radius+screenWidth/2,bigCircle.y+bigCircle.radius+screenHeight/2)

def update():
    global interval
    interval += 0.2
    amountToDo = (bigCircle.circumference() * (interval/720)%smallCircle.circumference())/smallCircle.circumference()
    if(amountToDo > 0.5):
        amountToDo = 1 - amountToDo
    amountToDo = amountToDo * 2
    point = bigCircle.pointPerpendicularToCircumference(interval,bigCircle.x,bigCircle.y-bigCircle.radius,smallCircle.radius*2 * amountToDo )
    drawPoint(point[0],point[1])
    mycanvas.update()
    window.after(1,update)

screenSize = 1
screenWidth = int(1920 * screenSize)
screenHeight = int(1080 * screenSize)
centerX = screenWidth/2
centerY = screenHeight/2
window = tkinter.Tk()
mycanvas = tkinter.Canvas(width=screenWidth,height=screenHeight)#,background="black")
mycanvas.pack()
interval = 0
setup()
update()
tkinter.mainloop()
