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



cool = True
finish = False 
FPS = 60
clock = time.Clock()
dracon1 = Player("спрайт.png", 3, 250, 5, 180, 200)
dracon2 = Player("спрайт 2.png", 530, 250, 5, 180, 200)
while cool:
    if finish != True:
        window.blit(background, (0,0))
        dracon1.reset()
        dracon1.update_l()
        dracon2.reset()
        dracon2.update_r()
    
    for e in event.get():
        if e.type == QUIT:
            cool = False



    display.update()
    clock.tick(FPS)
