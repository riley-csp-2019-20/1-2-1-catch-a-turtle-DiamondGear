# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rdn
#-----game configuration----
shape = "turtle"
size = 4
color = "Aqua"
score = 0
timer = 30
timer_up = bool
counter_interval = 1000
#-----initialize turtle-----
drawer = trtl.Turtle(shape = shape)
draw_score = trtl.Turtle()
timer_turt = trtl.Turtle()
drawer.color(color)
drawer.shapesize(size)
drawer.speed(0)
draw_score.color("Blue")
draw_score.shapesize(score + 1)
draw_score.speed(0)
draw_score.penup()
draw_score.ht()
draw_score.goto(-400,320)
font = ("Arial", 30, "bold")
draw_score.write(score, font=font)
timer_turt.color("Black")
timer_turt.speed(0)
timer_turt.penup()
timer_turt.ht()
timer_turt.goto(-100,360)
timer_turt.write(timer, font=font)
#-----game functions--------
def turtle_clicked(x,y):
    change_pos()
    drawer.st()
    score_counter()
    draw_score.shapesize(score)


def change_pos():
    drawer.penup()
    drawer.ht()
    new_xpos = rdn.randint(-400,400)
    new_ypos = rdn.randint(-300,300)
    drawer.goto(new_xpos,new_ypos)

def score_counter():
    global score
    score += 1
    print(score)
    draw_score.clear()
    draw_score.write(score, font=font)

# Countdown Writer
def countdown():
  global timer, timer_up
  timer_turt.clear()
  if timer <= 0:
    timer_turt.write("Time's Up", font=font)
    timer_up = True
    gameover()  
  else:
    timer_turt.write("Timer: " + str(timer), font=font)
    timer -= 1
    timer_turt.getscreen().ontimer(countdown, counter_interval)

def gameover():
    drawer.goto(0,500)
    drawer.ht()
    

#-----events----------------
drawer.onclick(turtle_clicked)









wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
