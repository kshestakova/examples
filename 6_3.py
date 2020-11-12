"""
Нарисуйте окно.
Пусть по клику левой кнопкой в окне будут рисоваться красные круги.
По клику правой кнопкой - зеленые прямоугольники. 
А если нажать на колесо мыши (среднюю кнопку), окно должно очищаться. 
"""

import pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

W, H = 800, 600

sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(sc, RED, pos, 10)
            elif i.button == 3:
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(sc, GREEN, [pos[0], pos[1], 20, 10])
            elif i.button == 2:
                sc.fill(WHITE)
        
        pygame.display.update()
        pygame.time.delay(20)     