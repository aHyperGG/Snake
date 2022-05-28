import turtle
import time
import random

score = 0
record = 0
retarder = 0.1
cheattp = False

fenêtre = turtle.Screen()
fenêtre.title("Snake Game")
fenêtre.bgcolor("black")
fenêtre.setup(width = 600, height = 600)
fenêtre.tracer(0)
tête = turtle.Pen()
tête.shape("square")
tête.color("green")
tête.speed(0)
tête.penup()
tête.goto(0,0)
tête.direction = "Stop"

#Fruit
fruit = turtle.Pen()
fruit.shape("circle")
fruit.color("white")
fruit.speed(0)
fruit.penup()
numberx = random.randint(-300,300)
numbery = random.randint(-300,300)
fruit.goto(numberx, numbery)

#Score
encodage = turtle.Turtle()
encodage.speed(0)
encodage.color("white")
encodage.penup()
encodage.hideturtle()
encodage.goto(0,250)
encodage.write("Score: 0 Record: 0", align = "center", font = ("Courier", 24, "bold"))
def monter() : 
    if tête.direction != "bas" : 
        tête.direction = "haut"

def descendre() : 
    if tête.direction != "haut" : 
        tête.direction = "bas"

def droite() : 
    if tête.direction != "gauche" : 
        tête.direction = "droite"

def gauche() : 
    if tête.direction != "droite" : 
        tête.direction = "gauche"

def bouger() : 
    if tête.direction == "haut" : 
        y = tête.ycor()
        tête.sety(y + 20)
    
    elif tête.direction == "bas" : 
        y = tête.ycor()
        tête.sety(y - 20)

    elif tête.direction == "gauche" : 
        x = tête.xcor()
        tête.setx(x - 20)

    elif tête.direction == "droite" : 
        x = tête.xcor()
        tête.setx(x + 20)

def cheattpstop() :
    global cheattp
    cheattp = False

def spacebar() : 
    if cheattp == True and turtle.onkeypress("space") : 
        tête.goto(1000, 1000)


#Listen
fenêtre.listen()
fenêtre.onkeypress(monter, "Up")

fenêtre.onkeypress(descendre, "Down")

fenêtre.onkeypress(gauche, "Left")

fenêtre.onkeypress(droite, "Right")

fenêtre.onkeypress(cheattpstop, "space")

#Boucle Principale

game_is_on = True

corps = []

while game_is_on : 
    fenêtre.update()
    if tête.distance(fruit) < 20 : 
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        fruit.goto(x, y)
        new_segment = turtle.Pen()
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        corps.append(new_segment)
        score += 10
        reccord += 0.00001

        if score > record : 
            record = score

        encodage.clear()
        encodage.write("Score: {} Record: {}".format(score, record),align = "center",font = ("Courrier", 24, "bold"))

    for index in range(len(corps)-1, 0, -1) : 
        x = corps[index-1].xcor()
        y = corps[index-1].ycor()
        corps[index].goto(x, y)

    if len(corps) > 0 : 
        x = tête.xcor()
        y = tête.ycor()
        corps[0].goto(x,y)

    bouger()
    time.sleep(retarder)

    #Cheat Code    
    if tête.xcor() > 270 and tête.ycor() > 270 :
        cheattp = True
        while cheattp == True : 
            tête.goto(fruit.xcor(), fruit.ycor())
            
            fenêtre.update()
            if tête.distance(fruit) < 20 : 
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                fruit.goto(x, y)
                new_segment = turtle.Pen()
                new_segment.shape("square")
                new_segment.color("blue")
                new_segment.penup()
                corps.append(new_segment)
                score += 10
                

                if score > record : 
                    record = score

                encodage.clear()
                encodage.write("Score: {} Record: {}".format(score, record),align = "center",font = ("Courrier", 24, "bold"))

            tête.goto(0, 0)

            for index in range(len(corps)-1, 0, -1) : 
                x = corps[index-1].xcor()
                y = corps[index-1].ycor()
                corps[index].goto(x, y)

            if len(corps) > 0 : 
                x = tête.xcor()
                y = tête.ycor()
                corps[0].goto(x,y)

            bouger()
            time.sleep(retarder)
              

    if tête.xcor() < -300 or tête.xcor() > 300 or tête.ycor() < -300 or tête.ycor() > 300 : 
        tête.goto(0,0)
        tête.direction = "Stop"
        for segment in corps : 
            segment.goto(1000,1000)
        corps.clear()
        score = 0
        encodage.clear()
        encodage.write("Score: {} Record: {}".format(score, record),align = "center",font = ("Courrier", 24, "bold"))

    for segment in corps : 
        if segment.distance(tête) < 20 : 
            tête.goto(0,0)
            tête.direction = "Stop"
            for segment in corps :
                segment.goto(1000,1000)
            corps.clear()
            encodage.clear()
            encodage.write("Score: {} Record: {}".format(score, record),align = "center",font = ("Courrier", 24, "bold")  )
