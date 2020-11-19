import pygame as pg

W = 800
H = 600

pg.init()
surface = pg.display.set_mode((W, H))
pg.display.set_caption("Flappy Bird")

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

STEP = 10
FALL = 1
SPEED = 2

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
    def __init__(self, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/t.png")
        self.rect = self.image.get_rect()
        self.rect.center = (W//2, y)
    
    def update(self):   
        if self.rect.x > -100:
            self.rect.x -= SPEED 
        else:
            self.kill()

flappy = Bird(W//2, H//2, "images/red.png")
obstacles = pg.sprite.Group() 
obstacleUp = Obstacle(50)
obstacleDown = Obstacle(550)
        
if __name__ == '__main__':
    while True:
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
            flappy.moveLeft()
            
        mouse = pg.mouse.get_pressed()
        
        if mouse[0]:
            if pg.mouse.get_pos()[1] < flappy.rect.y:
                flappy.moveUp()
            else:
                flappy.moveDown()
                
        surface.fill(GREEN)
        surface.blit(flappy.image, flappy.rect)
        surface.blit(obstacleUp.image, obstacleUp.rect)
        surface.blit(obstacleDown.image, obstacleDown.rect)
        flappy.update()
        obstacleUp.update()
        obstacleDown.update()
        pg.display.update()
        pg.time.delay(20)