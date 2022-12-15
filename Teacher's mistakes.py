

from pygame import * 
font.init()
from random import randint, choice


WIDTH, HEIGHT = 800, 640
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()



class ImageSprite(sprite.Sprite):
    def __init__(self, filename, position, size):
        super().__init__()
        self.rect = Rect(position, size)
        self.image = image.load(filename)
        self.image = transform.scale(self.image, size)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class PlayerSprite(ImageSprite):
    def __init__(self,filename,position, size, velocity):
        super().__init__(filename, position, size)
        self.vel = Vector2(0,0)
        self.base_vel = Vector2(velocity)
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.vel.y = self.base_vel.y * -1
        if keys[K_s]:
            self.vel.y = self.base_vel.y
       
        if not keys[K_w] and not keys [K_s]:
            self.vel.y = 0
        

        self.rect.topleft += self.vel  


        if self.rect.top <0:
            self.rect.top = 0   
        if self.rect.bottom >HEIGHT:
            self.rect.bottom = HEIGHT


class PlayerSprite2(ImageSprite):
    def __init__(self,filename,position, size, velocity):
        super().__init__(filename, position, size)
        self.vel = Vector2(0,0)
        self.base_vel = Vector2(velocity)
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.vel.y = self.base_vel.y * -1
        if keys[K_DOWN]:
            self.vel.y = self.base_vel.y
       
        if not keys[K_UP] and not keys [K_DOWN]:
            self.vel.y = 0
        

        self.rect.topleft += self.vel  


        if self.rect.top <0:
            self.rect.top = 0   
        if self.rect.bottom >HEIGHT:
            self.rect.bottom = HEIGHT

class Ball(ImageSprite):
    def __init__(self,filename,position, size, velocity):
        super().__init__(filename, position, size)
        self.vel = Vector2(velocity)
    def update(self):
        self.rect.topleft += self.vel
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.vel.y = self.vel.y*-1




bg = ImageSprite(filename='download.png', position=(0,0), size=(800,640))
player = PlayerSprite(filename='Capture.PNG', position=(30,320), size=(20,80), velocity=(0,8))
player2 = PlayerSprite2(filename='Capture.PNG', position=(730,320), size=(20,80), velocity=(0,8))
ball = Ball(filename='ball2.png', position=(400, 320), size=(20,20), velocity=(4,5))
p1_w = ImageSprite(filename='P1 WINS.png', position=(0,0), size=(800,640))
p2_w = ImageSprite(filename='P2 WINS.png', position=(0,0), size=(800,640))

while not event.peek(QUIT):
    window.fill('black')
    if sprite.collide_rect(ball, player):
        ball.vel.x = ball.vel.x*-1
    if sprite.collide_rect(ball, player2):
        ball.vel.x = ball.vel.x*-1

    bg.draw(window)
    player.update()
    player2.update()
    player.draw(window)
    player2.draw(window)
    if ball.rect.right > WIDTH:
        p1_w.draw(window)
    if ball.rect.left < 0:
        p2_w.draw(window)
    ball.update()
    ball.draw(window)


    display.update()
    clock.tick(60)
