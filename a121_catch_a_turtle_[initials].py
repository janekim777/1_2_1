# a121_catch_a_turtle.py
import turtle as trtl
dot = trtl.Turtle()
#-----import statements-----
import random as rand

#-----game configuration----

shape_color = "purple"
shape_size = 3
shape_shape = "turtle"
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle()

#-----game functions-----


#---------events---------


#-----initialize turtle-----
  
dot.shape(shape_shape)
dot.color(shape_color)
dot.shapesize(shape_size)
#-----game functions--------

def change_position():
  new_xpos=rand.randint(-100,300)
  new_ypos=rand.randint(-400,200)
  dot.penup()
  dot.goto(new_xpos,new_ypos)
  dot.pendown()
def dot_clicked(x,y):
  global timer
  if timer_up is False:
    countdown()
    change_position()
  else:
    dot.hideturtle()
  
 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
  

#-----events----------------
dot.onclick(dot_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()