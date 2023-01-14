from tkinter import *
from threading import Thread
import termios, fcntl, sys, os
import random
from time import sleep
import os

T1Placed = False
T2Placed = False
game = Tk()
game.geometry('450x450')
game.maxsize(450, 450)
game.minsize(450, 450)
board = Canvas(game, bg='green', width=450, height=450)
board.place(x=0, y=0)
board.create_rectangle(1, 51, 51, 101, outline="white")
board.create_rectangle(1, 101, 51, 151, outline="white")
board.create_rectangle(1, 151, 51, 201, outline="white")
board.create_rectangle(1, 201, 51, 251, outline="white")
board.create_rectangle(1, 251, 51, 301, outline="white")
board.create_rectangle(1, 301, 51, 351, outline="white")
board.create_rectangle(1, 351, 51, 401, outline="white")
board.create_rectangle(1, 401, 51, 449, outline="white")
board.create_rectangle(51, 51, 101, 101, outline="white")
board.create_rectangle(51, 101, 101, 151, outline="white")
board.create_rectangle(51, 151, 101, 201, outline="white")
board.create_rectangle(51, 201, 101, 251, outline="white")
board.create_rectangle(51, 251, 101, 301, outline="white")
board.create_rectangle(51, 301, 101, 351, outline="white")
board.create_rectangle(51, 351, 101, 401, outline="white")
board.create_rectangle(51, 401, 101, 449, outline="white")
board.create_rectangle(101, 51, 151, 101, outline="white")
board.create_rectangle(101, 101, 151, 151, outline="white")
board.create_rectangle(101, 151, 151, 201, outline="white")
board.create_rectangle(101, 201, 151, 251, outline="white")
board.create_rectangle(101, 251, 151, 301, outline="white")
board.create_rectangle(101, 301, 151, 351, outline="white")
board.create_rectangle(101, 351, 151, 401, outline="white")
board.create_rectangle(101, 401, 151, 449, outline="white")
board.create_rectangle(101, 51, 151, 101, outline="white")
board.create_rectangle(101, 101, 151, 151, outline="white")
board.create_rectangle(101, 151, 151, 201, outline="white")
board.create_rectangle(101, 201, 151, 251, outline="white")
board.create_rectangle(101, 251, 151, 301, outline="white")
board.create_rectangle(101, 301, 151, 351, outline="white")
board.create_rectangle(101, 351, 151, 401, outline="white")
board.create_rectangle(101, 401, 151, 449, outline="white")
board.create_rectangle(151, 51, 201, 101, outline="white")
board.create_rectangle(151, 101, 201, 151, outline="white")
board.create_rectangle(151, 151, 201, 201, outline="white")
board.create_rectangle(151, 201, 201, 251, outline="white")
board.create_rectangle(151, 251, 201, 301, outline="white")
board.create_rectangle(151, 301, 201, 351, outline="white")
board.create_rectangle(151, 351, 201, 401, outline="white")
board.create_rectangle(151, 401, 201, 449, outline="white")
board.create_rectangle(201, 51, 251, 101, outline="white")
board.create_rectangle(201, 101, 251, 151, outline="white")
board.create_rectangle(201, 151, 251, 201, outline="white")
board.create_rectangle(201, 201, 251, 251, outline="white")
board.create_rectangle(201, 251, 251, 301, outline="white")
board.create_rectangle(201, 301, 251, 351, outline="white")
board.create_rectangle(201, 351, 251, 401, outline="white")
board.create_rectangle(201, 401, 251, 449, outline="white")
board.create_rectangle(251, 51, 301, 101, outline="white")
board.create_rectangle(251, 101, 301, 151, outline="white")
board.create_rectangle(251, 151, 301, 201, outline="white")
board.create_rectangle(251, 201, 301, 251, outline="white")
board.create_rectangle(251, 251, 301, 301, outline="white")
board.create_rectangle(251, 301, 301, 351, outline="white")
board.create_rectangle(251, 351, 301, 401, outline="white")
board.create_rectangle(251, 401, 301, 449, outline="white")
board.create_rectangle(301, 51, 351, 101, outline="white")
board.create_rectangle(301, 101, 351, 151, outline="white")
board.create_rectangle(301, 151, 351, 201, outline="white")
board.create_rectangle(301, 201, 351, 251, outline="white")
board.create_rectangle(301, 251, 351, 301, outline="white")
board.create_rectangle(301, 301, 351, 351, outline="white")
board.create_rectangle(301, 351, 351, 401, outline="white")
board.create_rectangle(301, 401, 351, 449, outline="white")
board.create_rectangle(351, 51, 401, 101, outline="white")
board.create_rectangle(351, 101, 401, 151, outline="white")
board.create_rectangle(351, 151, 401, 201, outline="white")
board.create_rectangle(351, 201, 401, 251, outline="white")
board.create_rectangle(351, 251, 401, 301, outline="white")
board.create_rectangle(351, 301, 401, 351, outline="white")
board.create_rectangle(351, 351, 401, 401, outline="white")
board.create_rectangle(351, 401, 401, 449, outline="white")
board.create_rectangle(401, 51, 449, 101, outline="white")
board.create_rectangle(401, 101, 449, 151, outline="white")
board.create_rectangle(401, 151, 449, 201, outline="white")
board.create_rectangle(401, 201, 449, 251, outline="white")
board.create_rectangle(401, 251, 449, 301, outline="white")
board.create_rectangle(401, 301, 449, 351, outline="white")
board.create_rectangle(401, 351, 449, 401, outline="white")
board.create_rectangle(401, 401, 449, 449, outline="white")
with open('direction.txt', 'w+') as dir:
    True
apples = 0
x_choices = 25, 75, 175, 225, 275, 325, 375, 425
y_choices = 75, 125, 175, 225, 275, 325, 375, 425
tail_count = 0
AppleIsSpawned = False
with open('highscore.txt', 'r+') as hs:
    hs.seek(0)
    highscore = hs.read()
AppleAmnt = Label(game,
                  text=f"Score : {apples}",
                  bg="green",
                  height=2,
                  width=15)
AppleAmnt.place(x=75, y=8)
HighScore = Label(game,
                  text=f"High Score : {highscore}",
                  bg="green",
                  height=2,
                  width=15)
HighScore.place(x=225, y=8)
head = Canvas(game, bg="blue", height=35, width=35)
head.place(x=208, y=258)
head_x = 208
head_y = 258
apple_x = 0
apple_y = 0


def check_char():
    while True:
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while 1:
                sleep(0.2)
                try:
                    c = sys.stdin.read(1)
                    if c:
                        with open('direction.txt', 'w+') as direction:
                            direction.write(c)
                except IOError:
                    pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


def create_circle(x, y, r, canvasName):  #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill="red", tags="apl")


def move_up():
    global head_y
    if head_y - 50 < 50:
        print('Dead')
    else:
        head_y = head_y - 50
        head.place(x=head_x, y=head_y)


def move_down():
    global head_y
    if head_y + 50 > 450:
        print('Dead')
    else:
        head_y = head_y + 50
        head.place(x=head_x, y=head_y)


def move_left():
    global head_x
    if head_x - 50 < 0:
        print('Dead')
    else:
        head_x = head_x - 50
        head.place(x=head_x, y=head_y)


def move_right():
    global head_x
    if head_x + 50 > 450:
        print('Dead')
    else:
        head_x = head_x + 50
        head.place(x=head_x, y=head_y)


def move():
    global movement
    while True:
        with open('direction.txt', 'r+') as direction:
            movement = direction.read()
            if movement == "w":
                move_up()
                sleep(0.8)
            if movement == "s":
                move_down()
                sleep(0.8)
            if movement == "a":
                move_left()
                sleep(0.8)
            if movement == "d":
                move_right()
                sleep(0.8)


def spawn_apple():
    global AppleIsSpawned
    global apple_x
    global apple_y
    while True:
        sleep(0.1)
        if AppleIsSpawned == False:
            apple_x = random.choice(x_choices)
            apple_y = random.choice(y_choices)
            if apple_x != head_x + 17 and apple_y != head_y + 17:
                Apple = create_circle(apple_x, apple_y, 10, board)
                AppleIsSpawned = True


def check_collision():
    global AppleIsSpawned
    global apples
    while True:
        sleep(0.1)
        if apple_x == head_x + 17 and apple_y == head_y + 17:
            AppleIsSpawned = False
            apples = apples + 1
            board.delete('apl')
            AppleAmnt.configure(text=f"Score : {apples}")
            with open('highscore.txt', 'r+') as scores:
                scores.seek(0)
                highscore = scores.read()
                if apples > int(highscore):
                    scores.truncate(0)
                    scores.seek(0)
                    scores.write(str(apples))
                    HighScore.configure(text=f"High Score : {apples}")


sleep(1)
Check_Movement = Thread(target=check_char)
Check_Movement.start()
Move_Head = Thread(target=move)
Move_Head.start()
Spawn_Apple = Thread(target=spawn_apple)
Spawn_Apple.start()
Check_Collision = Thread(target=check_collision)
Check_Collision.start()
game.mainloop()
