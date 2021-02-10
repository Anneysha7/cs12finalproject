import turtle 
import time 
import random 
delay = 0.08

# setup 
wn = turtle.Screen()
wn.setup(600,600)
wn.title('feed me ')
wn.bgcolor('spring green')

############ head ##################
head = turtle.Turtle()
head.shape('circle')
head.color('black')
head.penup()
head.goto(0,0)
head.speed(0) #this is animation speed 
# not the actual speed . 0 is the fastest speed 
head.direction = 'stop' # if up , head will go up 

################# snake food
food = turtle.Turtle()
food.shape('triangle')
food.color('black')
food.penup()
food.goto(0,50)
food.speed(0) 

################################
parts = []

 




#####funtions###################
def move():

    if head.direction == 'right':

        x = head.xcor()
        head.setx(x+20)


    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20) 


    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)


        
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)


def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'
def go_left():
    head.direction = 'left'
def go_right():
    head.direction = 'right'



#################################
### keyboard connction 
wn.listen()
wn.onkeypress(go_up , 'w')
wn.onkeypress(go_down , 's')
wn.onkeypress(go_left , 'a')
wn.onkeypress(go_right , 'd')
##################################


   


#@@@@@@@## main game loop 
while True :


    wn.update()
# ckeck for collision 

    if head.distance(food) < 20 :
        # move the food to random postion on scewwn
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # add a bodypart 
        new_part = turtle.Turtle()
        new_part.speed(0) # animation speed 
        new_part.shape('circle')
        new_part.color('black')
        new_part.penup()
        parts.append(new_part)

    for index in range(len(parts)-1,0,-1):
        x = parts[index-1].xcor()
        y = parts[index-1].ycor()
        parts[index].goto(x,y)

    
    if len(parts) > 0 :
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x,y)



   





    time.sleep(delay)
    move()









'''turtle.done()''' # we can use this as well 
wn.mainloop() # will keep winow open 
