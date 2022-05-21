from pygame import *
from random import *

window = display.set_mode((700, 500))
display.set_caption("ping-pong")
background = transform.scale(image.load("фон.jpg"), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

    def update_r(self): 
        keys_pressed = key.get_pressed()  
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            global lost
            lost += 1
            self.rect.x = randint(0,635)
            self.rect.y = 0

speed_x = 3
speed_y = 3

cool = True
finish = False 
FPS = 60
clock = time.Clock()

paiper = Player("damocka.jpg", 3, 250, 5, 80, 200)
emz = Player("спрайт 2.png", 620, 250, 5, 80, 200)
ball = GameSprite("ball.png", 450, 345, 0, 50, 50)

font.init()
font1 = font.SysFont("verdana", 45)

while cool:
    if finish != True:
        window.blit(background, (0,0))
        paiper.reset()
        paiper.update_l()
        emz.reset()
        emz.update_r()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(paiper, ball) or sprite.collide_rect(emz, ball):
            speed_x*=-1

        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *=-1
        
        if ball.rect.x < 0:
            #проиграл игрок слево
            lose1 = font1.render("Проиграл игрок слево", True, (255,0,0))
            window.blit(lose1, (125, 225))
            finish = True
        if ball.rect.x > 655:
            #проиграл игрок справа
            lose2 = font1.render("Проиграл игрок справа", True, (255,0,0))
            window.blit(lose2, (125, 255))
            finish = True
    
    for e in event.get():
        if e.type == QUIT:
            cool = False



    display.update()
    clock.tick(FPS)
