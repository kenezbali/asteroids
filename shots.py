from circleshape import *
from constants import *
import pygame
class Shot(CircleShape):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        SHOT_RADIUS = 5
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,2)
    def update(self, dt):
        self.position += dt * self.velocity