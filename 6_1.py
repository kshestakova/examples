"""
Прерывистое движение
Нарисуйте квадрат. 
Заставьте его перемещаться вверх, вниз, вправо и влево в ответ на нажатия кнопок на клавиатуре. 
Сделайте так, чтобы если кнопка перемещения была нажата с Shift, размер квадрата увеличивался бы. 
Квадрат не должен выходить за границы окна. 

"""

import pygame
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
x, y = 0, 0
r = 10

W, H = 800, 600

sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 10
                if (i.mod & pygame.KMOD_SHIFT):
                    r += 10
            elif i.key == pygame.K_RIGHT:
                x += 10
                if (i.mod & pygame.KMOD_SHIFT):
                    r += 10
            elif i.key == pygame.K_UP:
                y -= 10
                if (i.mod & pygame.KMOD_SHIFT):
                    r += 10
            elif i.key == pygame.K_DOWN:
                y += 10
                if (i.mod & pygame.KMOD_SHIFT):
                    r += 10
    
    if x > W:
        x = W
    if x < 0:
        x = 0
    if y > H-r:
        y = H-r
    if y < 0:
        y = 0    
    
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, [x, y, r, r], 3)
    pygame.display.update()
    pygame.time.delay(20)     
