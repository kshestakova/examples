# привязываем квадрат к позиции курсора мыши

import pygame
 
WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
 
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)
pygame.display.update()
 
pygame.mouse.set_visible(False)
 
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    sc.fill(WHITE) # если закомментировать эту строку, будем рисовать курсором на экране
 
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(
            sc, BLUE, (pos[0] - 10, pos[1] - 10, 20, 20))
 
    pygame.display.update()
    pygame.time.delay(20)