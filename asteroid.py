from circleshape import *
from constants import *
import pygame, random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.radius = radius
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,2)
    def update(self, dt):
        self.position += dt * self.velocity
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        velocity_a = self.velocity.rotate(random_angle)
        velocity_b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroida = Asteroid(self.position.x,self.position.y,new_radius)
        asteroidb = Asteroid(self.position.x,self.position.y,new_radius)
        asteroida.velocity = velocity_a * 1.2
        asteroidb.velocity = velocity_b * 1.2 