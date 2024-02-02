from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping pong game")
background = transform.scale(image.load('bg.jpg'), (win_width, win_height))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 480 :
            self.rect.y += self.speed
        
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 480 :
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        keys = key.get_pressed()
        
game = True

sprite1 = Player1('tennis racket 1.jpg', 5, 350, 5, 10, 100)
sprite2 = Player2('tennis racket 2.jpg', 685, 350, 5, 10, 100)
sprite3 = Ball('balll.png', 250, 250, 5, 65, 65)

while game:
    window.blit(background, (0, 0))
    sprite1.reset()
    sprite1.update()
    sprite2.update()
    sprite2.reset()
    sprite3.update()
    sprite3.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)