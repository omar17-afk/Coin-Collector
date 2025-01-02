import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "CION COLLECTOR"
BACKGROUND_COLOR = (40, 43, 59)
SCORE = 0
BEST_SCORE = 0
GAMEOVER = False
TIME_LEFT = 35
PLAYER_NAME = ""
FOX = Actor("fox.png")
FOX.pos = 100, 100
COIN = Actor("coin.png")
COIN.pos = 300, 300
FOX_SPEED = 2  

def player_name():
    global PLAYER_NAME
    PLAYER_NAME = input("Enter your name: ")

def time_up():
    global GAMEOVER
    GAMEOVER = True

def update_time_left():
    global TIME_LEFT
    TIME_LEFT -= 1
    if TIME_LEFT == 0:
        time_up()

def reset_fox_speed():
    global FOX_SPEED
    FOX_SPEED = 2 

def draw():
    global GAMEOVER, SCORE, BEST_SCORE, TIME_LEFT
    if not GAMEOVER:
        screen.clear()
        screen.blit("background.png", (0, 0))
        screen.draw.text("COIN COLLECTOR", (WIDTH/2-40, 30),fontsize=15, color="white",gcolor="golden rod")
        screen.draw.text("Score: " + str(SCORE), (10, 30), fontsize=15, color="white",gcolor="golden rod")
        screen.draw.text(f"Player: {PLAYER_NAME}", (10, 10), fontsize=15, color="white", gcolor="golden rod")
        screen.draw.text("Best Score: " + str(BEST_SCORE), (10, 50),fontsize=15, color="white",gcolor="golden rod")
        screen.draw.text("Time left: " + str(TIME_LEFT), (10, 70), fontsize=15, color="white",gcolor="golden rod")
        FOX.draw()
        COIN.draw()
    else:
        screen.clear()
        screen.fill(BACKGROUND_COLOR)
        screen.draw.text("COIN COLLECTOR", (WIDTH/2-60, 10),fontsize=15, color="white",gcolor=BACKGROUND_COLOR)
        screen.draw.text("GAME OVER", (200, 200), fontsize=15, color="white",gcolor=BACKGROUND_COLOR)
        screen.draw.text("Score: " + str(SCORE), (200, 270),fontsize=15, color="white",gcolor=BACKGROUND_COLOR)
        screen.draw.text("Player: " + PLAYER_NAME, (200, 250),fontsize=15, color="white",gcolor=BACKGROUND_COLOR)
        screen.draw.text("Best Score: " + str(BEST_SCORE), (200, 300), fontsize=15, color="white",gcolor=BACKGROUND_COLOR)
        screen.draw.text("Press ENTER to try again", (130, 330),fontsize=15, color="white",gcolor=BACKGROUND_COLOR)

def update():
    global SCORE, BEST_SCORE, TIME_LEFT, FOX_SPEED, GAMEOVER
    if not GAMEOVER:
        if keyboard.Right:
            if FOX.x < WIDTH:
                FOX.x += FOX_SPEED
            else:
                FOX.x = 0
        if keyboard.Left:
            if FOX.x > 0:
                FOX.x -= FOX_SPEED
            else:
                FOX.x = WIDTH
        if keyboard.Up:
            if FOX.y > 0:
                FOX.y -= FOX_SPEED
            else:
                FOX.y = HEIGHT
        if keyboard.Down:
            if FOX.y < HEIGHT:
                FOX.y += FOX_SPEED
            else:
                FOX.y = 0
        if FOX.colliderect(COIN):
            COIN.pos = randint(0, 500), randint(0, 500)
            SCORE += 1
            if SCORE > BEST_SCORE:
                BEST_SCORE = SCORE
            TIME_LEFT += 1
            FOX_SPEED = 4
            clock.schedule(reset_fox_speed, 1)
def on_key_down(key):
    global GAMEOVER, SCORE, TIME_LEFT, FOX_SPEED
    if GAMEOVER and key == keys.RETURN:
        GAMEOVER = False
        SCORE = 0
        TIME_LEFT = 30
        FOX.pos = 100, 100
        COIN.pos = 300, 300
        FOX_SPEED = 2

clock.schedule_interval(update_time_left, 1)
player_name()
pgzrun.go()
