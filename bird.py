import pygame as pg
from random import randint 

W = 288
H = 512

pg.init()
surface = pg.display.set_mode((W, H))
pg.display.set_caption("Flappy Bird")

BLUE = (0, 0, 255)

STEP = 10
FALL = 1
SPEED = 2
DIFF = 200
TH = 300

obsFlag = True
lifes = 10
score = 0

font = pg.font.SysFont('verdana', 32)
text = font.render(str(score), True, BLUE) 
textRect = text.get_rect()  
textRect.center = (W - 50, 50) 

class Background (pg.sprite.Sprite):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/bg.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x + W // 2, H // 2)
        self.x = x
        
    def update(self):
        self.rect.x -= SPEED
        if self.rect.x < self.x - W//2:
            self.rect.x = self.x
            
class Life (pg.sprite.Sprite):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/heart.png")
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, 50)

class Bird (pg.sprite.Sprite):
    def __init__(self, x, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename)
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (W // 4, H // 2)
        
    def moveUp(self):
        if self.rect.y > 0:
            self.rect.y -= STEP
            
    def moveDown(self):
        if self.rect.y < H:
            self.rect.y += STEP
            
    def moveLeft(self):
        if self.rect.x > 0:
            self.rect.x -= STEP
    
    def moveRight(self):
        if self.rect.x < W:
            self.rect.x += STEP
            
    def update(self):
        if self.rect.y < H - 5:
            self.rect.y += FALL

class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/t.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):   
        if self.rect.x > - 100:
            self.rect.x -= SPEED 
        else:
            print("KILL obstacle")
            self.kill()
            global obsFlag, score
            obsFlag = False
            score += 1

flappy = Bird(W//2, H//2, "images/red.png")
obstacles = pg.sprite.Group() 
obstacles.add(Obstacle(W, 50))
obstacles.add(Obstacle(W, 550))

bg = pg.sprite.Group() 
bg.add(Background(0))
bg.add(Background(W))

heartsList = [Life(i*15 + 20) for i in range(lifes)]
        
if __name__ == '__main__':
    counter = 0
 
    while lifes:
        counter += 1
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
        
        keys = pg.key.get_pressed()
 
        if keys[pg.K_UP]:
            flappy.moveUp()
            
        elif keys[pg.K_RIGHT]:
            flappy.moveRight()
            
        elif keys[pg.K_LEFT]:
            flappy.moveLeft()
        
        elif keys[pg.K_DOWN]:
            flappy.moveDown()
            
        mouse = pg.mouse.get_pressed()
        
        if mouse[0]:
            if pg.mouse.get_pos()[1] < flappy.rect.y:
                flappy.moveUp()
            else:
                flappy.moveDown()
                
        if pg.sprite.spritecollideany(flappy, obstacles):
            lifes -= 1
            
            for i in obstacles:
                i.kill()
            obsFlag = False
            print("lifes = ", lifes)
            heartsList.pop(-1)
        
        for i in bg:
            surface.blit(i.image, i.rect)
        for i in obstacles:
            surface.blit(i.image, i.rect)
        for i in heartsList:
            surface.blit(i.image, i.rect)
            
        text = font.render(str(score//2), True, BLUE) 
        surface.blit(text, textRect)
        surface.blit(flappy.image, flappy.rect)
        bg.update()
        flappy.update()
        obstacles.update()
        pg.display.update()
        pg.time.delay(20)
        
        if obsFlag == False:
           print("new obstacles created") 
           height = randint (0, TH // 2)
           obstacles.add(Obstacle(W + DIFF, height ))
           obstacles.add(Obstacle(W + DIFF, height + TH  + DIFF)) 
           print(height, height + DIFF + TH // 2)
           obsFlag = True
        
        if counter > 1000:
            counter = 0
            if DIFF > 120:
                DIFF -= 5
            SPEED += 1