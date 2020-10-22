import pygame

HEIGHT = 600
WIDTH = 800
S = 10

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
R = 50

pygame.display.set_caption("My Pygame Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x = R
y = R

dx, dy = -1, 1
    
while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    surface.fill(BLACK)
    pygame.draw.circle(surface, WHITE, (x, y), R)
    pygame.display.update()
    
    if x < R or x > WIDTH - R:
        dx *= -1
    
    if y < R or y > HEIGHT - R:
        dy *= -1
        
    x += S*dx
    y += S*dy    
    
    pygame.time.Clock().tick(100)