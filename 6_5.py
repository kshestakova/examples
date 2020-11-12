"""
Нарисуйте квадрат. 
Заставьте его перемещаться вверх, вниз, вправо и влево в ответ на нажатия кнопок на клавиатуре. 
Квадрат не должен выходить за границы окна. 

"""

import pygame
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
x, y = 0, 0
r = 50

W, H = 800, 600

sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10
    elif keys[pygame.K_RIGHT]:
        x += 10
    elif keys[pygame.K_UP]:
        y -= 10
    elif keys[pygame.K_DOWN]:
        y += 10
    
    if x > W-r:
        x = W-r
    if x < 0:
        x = 0
    if y > H-r:
        y = H-r
    if y < 0:
        y = 0    
    
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, [x, y, r, r], 3)
    pygame.display.update()
    pygame.time.delay(10)     
