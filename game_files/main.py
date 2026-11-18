import pygame
import sys
from constants import *
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    Clock=pygame.time.Clock()
    dt=0
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()


    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers=(updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots,drawable,updatable)
    
    AsteroidField()
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,0)
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running=True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running= False

        updatable.update(dt)
    
        for thing in asteroids:
            if player.collides_with(thing):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(thing):
                    log_event("asteroid_shot")
                    shot.kill()
                    thing.split()

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt=(Clock.tick(60))/1000
        
        
        


if __name__ == "__main__":
    main()

