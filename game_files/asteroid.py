import pygame
from logger import log_event, log_state
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    

    def draw(self,screen):
            pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
            self.position= self.position +(self.velocity*dt)
    def split(self):
          self.kill()
          if self.radius<=ASTEROID_MIN_RADIUS:
                return
          log_event("asteroid_split")
          random_angle=random.uniform(20,50)
          asteroid_1=Asteroid(self.position[0],self.position[1],self.radius/2)
          asteroid_2=Asteroid(self.position[0],self.position[1],self.radius/2)
          asteroid_1.velocity=(pygame.math.Vector2.rotate(self.velocity,random_angle))*1.2
          asteroid_2.velocity=(pygame.math.Vector2.rotate(self.velocity,-random_angle))*1.2
          
      


          
          