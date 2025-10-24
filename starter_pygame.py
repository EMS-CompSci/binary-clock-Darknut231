import pygame
from starter_functionality import getTimeInBinary
from starter_functionality import drawCircles
import time
import datetime

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Just a test")
color = (255,255,0)
hb = mb = sb = ()
while True:
    screen.fill((0,0,0))
    hb,mb,sb = getTimeInBinary()
    drawCircles(screen,color,hb,mb,sb)
 #   for event in pygame.event.get():
 #       if event.type == pygame.QUIT:
 #           pygame.quit()
    pygame.display.update()