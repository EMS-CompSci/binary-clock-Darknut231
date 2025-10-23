import pygame
from starter_functionality import getTimeInBinary
import time
import datetime

pygame.init()

screen = pygame.display.set_mode((400,200))
pygame.display.set_caption("Just a test")
color = (255,255,0)
hb = mb = sb = ()
while True:
    screen.fill((0,0,0))
    hb,mb,sb = getTimeInBinary()
    pygame.draw.circle(screen, color,[30,30],10,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()