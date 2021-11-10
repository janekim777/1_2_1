# a121_catch_a_turtle.py
import turtle as trtl
dot = trtl.Turtle()
#-----import statements-----
import random as rand
import leaderboard as lb
#-----game configuration----

shape_color = "purple"
shape_size = 3
shape_shape = "turtle"
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
score = 0
sizes = [1,2,3,4,5]
colors = ["pink","green","orange","red","yellow"]
score_writer_color = "white"


colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
size = [ 1, 2 ,3, 4, 5]
#countdown variables
font_setup = ("Arial", 25, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name: ")
#-----countdown writer-----
counter =  trtl.Turtle()



#-----initialize turtle-----
dot = trtl.Turtle()
dot.shape(shape_shape)
dot.color(shape_color)
dot.shapesize(shape_size)


score_writer = trtl.Turtle()
score_writer.color(score_writer_color)
score_writer.pu()
score_writer.goto(200,200)

writing_score = trtl.Turtle()
writing_score.color(score_writer_color)
writing_score.pu()
writing_score.goto(200,200)
#-----game functions--------
def dot_clicked(x,y):
  global timer_up
  if (not timer_up):
    change_score()
    color_change()
    size_change()
    change_position()
  else:
    writing_score.hideturtle()
    change_score()


def change_position():
  new_xpos=rand.randint(-100,300)
  new_ypos=rand.randint(-400,200)
  dot.goto(new_xpos,new_ypos)


def color_change():
  new_color = rand.choice(colors)
  dot.color(new_color)


def size_change():
  new_size = rand.choice(sizes)
  dot.shapesize(sizes)

def change_score():
  global score
  score += 1
  writing_score.clear()
  writing_score.write(score, font=font_setup)



  
 
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leadership()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
  
  


def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)



#-----events----------------


wn = trtl.Screen()
wn.bgcolor("blue")
wn.ontimer(countdown, counter_interval) 
dot.onclick(dot_clicked)
wn.mainloop()