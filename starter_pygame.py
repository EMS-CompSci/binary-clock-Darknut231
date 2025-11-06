import pygame
from starter_functionality import getTimeInBinary
from starter_functionality import drawCircles
from starter_functionality import oneCircles
import time
import datetime

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Just a test")
color = (255,255,0)
#hb = mb = sb = ()
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
   screen.fill((0,0,0))
   tenhb,hb,tenmb,mb,tensb,sb = getTimeInBinary()
   print(tenhb,hb,tenmb,mb,tensb,sb)
   drawCircles(screen,color,tenhb,tenmb,tensb)
   oneCircles(screen,color,hb,mb,sb)
   pygame.display.update()
   clock.tick(2)
