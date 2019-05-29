import turtle

wn=turtle.Screen()
wn.setup(width=800,height=1000)
wn.bgcolor("black")
wn.title("Space Invaders")

temp = turtle.Turtle()
temp.hideturtle()
temp.pencolor("white")
temp.speed(0)
temp.penup()
temp.setposition(-200,-330)
temp.pendown()
temp.write("Use the arrow keys to move and space to shoot",font=("Arial", 20, "normal"))
temp.penup()

diff=iter(["Easy Mode","Medium Mode","Hard Mode"])
currdiff = next(diff)
diff_writer = turtle.Turtle()
diff_writer.hideturtle()
diff_writer.pencolor("white")
diff_writer.speed(0)
diff_writer.penup()
diff_writer.setposition(-50,310)
diff_writer.pendown()
diff_writer.write(currdiff,font=("Arial", 20, "normal"))

border_pen=turtle.Turtle()

border_pen.hideturtle()
border_pen.pencolor("white")
border_pen.pensize(3)
border_pen.speed(0)
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()

for _ in range(4):
	border_pen.forward(600)
	border_pen.left(90)

player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

enemy=turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(0,250)
enemy.setheading(-90)

enemyspeed = 4

bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate="ready"

def move_left():
	x=player.xcor()
	x-=playerspeed
	if x<-280:
		x=-280
	player.setx(x)

def move_right():
	x=player.xcor()
	x+=playerspeed
	if x>280:
		x=280
	player.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate="fire"
		x=player.xcor()
		y=player.ycor()
		bullet.setposition(x,y+10)
		bullet.showturtle()

def isCollision(t1,t2):
	distance=abs(complex(t1.xcor()-t2.xcor(),t1.ycor()-t2.ycor()))
	if distance < 15:
		return True
	else:
		return False

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

while True:

	if bulletstate == "fire":
		y=bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
		if bullet.ycor() > 275:
			bullet.hideturtle()
			bulletstate = "ready"
	

	x=enemy.xcor()
	x+=enemyspeed
	enemy.setx(x)

	if enemy.xcor() > 280 or enemy.xcor() < -280:
		enemyspeed *= -1
		y=enemy.ycor()
		y -= 50
		enemy.sety(y)

	if isCollision(bullet,enemy):
		if currdiff=="Hard Mode":
			enemy.hideturtle()
			player.hideturtle()
			bullet.hideturtle()
			diff_writer.clear()
			diff_writer.penup()
			diff_writer.setposition(-50,310)
			diff_writer.pendown()
			diff_writer.write("YOU WIN!",font=("Arial", 20, "normal"))
			break
		else:			
			enemy.setposition(0,250)
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0,-400)
			enemyspeed += 5
			currdiff = next(diff)
			diff_writer.clear()
			diff_writer.penup()
			diff_writer.setposition(-50,310)
			diff_writer.pendown()
			diff_writer.write(currdiff,font=("Arial", 20, "normal"))


	if isCollision(player,enemy):
		enemy.hideturtle()
		player.hideturtle()
		bullet.hideturtle()
		diff_writer.clear()
		diff_writer.penup()
		diff_writer.setposition(-50,310)
		diff_writer.pendown()
		diff_writer.write("YOU WIN!",font=("Arial", 20, "normal"))
		break

wn.mainloop()