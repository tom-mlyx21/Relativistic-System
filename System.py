import pygame
import time
import math

class planet:
    def __init__(self, name, mass, radius, position, velocity, colour):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.colour = colour


class system:
    def __init__(self):
        planets = []
        planets.append(planet('Sun', 1.989e30, 0, (0, 0), (0), (255, 255, 0)))
        planets.append(planet('Mercury', 3.285e23, 1, (1, 0), (58), (140, 131, 129)))
        planets.append(planet('Venus', 4.867e24, 2, (2, 0), (243), (196, 159, 141)))
        planets.append(planet('Earth', 5.972e24, 3, (3, 0), (1), (48, 91, 209)))
        planets.append(planet('Mars', 6.39e23, 4, (4, 0), (1.05), (209, 91, 48)))
        planets.append(planet('Jupiter', 1.898e27, 5, (5, 0), (1/(24/10)), (168, 134, 82)))
        planets.append(planet('Saturn', 5.683e26, 6, (6, 0), (1/(24/10)), (222, 162, 71)))
        planets.append(planet('Uranus', 8.681e25, 7, (7, 0), (1/(24/17)), (132, 225, 227)))
        planets.append(planet('Neptune', 1.024e26, 8, (8, 0), (1/(24/16)), (62, 92, 133)))

    def draw(self):
        for planet in self.planets:
            pygame.draw.circle(screen, planet.colour, planet.position, planet.radius)
            pygame.display.flip()


def circular_orbit(center, planet, time):
    x = center[0] + planet.radius * math.cos(time)
    y = center[1] + planet.radius * math.sin(time)
    return (x, y)


(width, height) = (700, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('System')
screen.fill((0, 0, 30))
pygame.display.flip()

running = True
while running:
    system = system()
    system.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False