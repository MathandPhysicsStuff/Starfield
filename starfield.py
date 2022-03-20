import pygame
import sys
import random 
import math
from math import sin, cos, asin, acos, sqrt, pow, fabs

pygame.init()
clock = pygame.time.Clock()

#Varivables
width = 600
height = 600
x_shift = width // 2
y_shift = height // 2
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (100, 100, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Starfield")

def points():
    
    x = random.randint(-width//2, width//2) 
    y = random.randint(-height//2, height//2)
    x2 = x
    y2 = y
    point = [x, y, x2, y2]

    return point


stars = [points() for i in range(50)]

def main(): 

    x_p2 = 0
    y_p2 = 0

    active = True
    while active:

        screen.fill(black)

        for star in stars:

            v1 = (star[0]) / 40  
            v2 = (star[1]) / 40 
            v3 = (star[2]) / 39.9
            v4 = (star[3]) / 39.9 

            star[0] += v1
            star[1] += v2
            star[2] += v3
            star[3] += v4

            x_p1 = star[0] + x_shift  
            y_p1 = star[1] + y_shift  

            x_p2 = star[2] + x_shift 
            y_p2 = star[3] + y_shift 

            size = int(((fabs(star[0]) + fabs(star[1])) / width) * 3 + 1)

            if star[0] > width//2 or star[0] < -width//2:
                star[0] = random.randint(-width//2, width//2)
                star[2] = star[0]
                #size = 0
                v1 = 0
                v2 = 0 
                v3 = 0
                v4 = 0

            if star[1] > height//2 or star[1] < -height//2:
                star[1] = random.randint(-height//2, height//2)
                star[3] = star[1]
                #size = 0
                v1 = 0
                v2 = 0
                v3 = 0
                v4 = 0 

            #pygame.draw.circle(screen, white, (x_p1, y_p1), size) 
            pygame.draw.line(screen, white, (x_p1, y_p1), (x_p2, y_p2), size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


