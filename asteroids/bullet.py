import math

import pygame


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction
        self.life = 30

    def updateBullet(self):
        # Moving
        self.x += BULLET_SPEED * math.cos(self.dir * math.pi / 180)
        self.y += BULLET_SPEED * math.sin(self.dir * math.pi / 180)

        # Drawing
        pygame.draw.circle(gameDisplay, Color.white, (int(self.x), int(self.y)), 3)

        # Wrapping
        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height
        self.life -= 1





class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction
        self.life = 30

    def updateBullet(self):
        # Moving
        self.x += BULLET_SPEED * math.cos(self.dir * math.pi / 180)
        self.y += BULLET_SPEED * math.sin(self.dir * math.pi / 180)

        # Drawing
        pygame.draw.circle(gameDisplay, Color.white, (int(self.x), int(self.y)), 3)

        # Wrapping
        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height
        self.life -= 1









class Bullet(GameObject):
    def __init__(self, x: int, y: int, direction: float,     ):
        self.x = x
        self.y = y
        self.dir = direction
        self.life = 30

    def update(self):
        # Moving
        self.x += BULLET_SPEED * math.cos(self.dir * math.pi / 180)
        self.y += BULLET_SPEED * math.sin(self.dir * math.pi / 180)

        # Drawing
        pygame.draw.circle(gameDisplay, Color.white, (int(self.x), int(self.y)), 3)

        # Wrapping
        if self.x > Display.width:
            self.x = 0
        elif self.x < 0:
            self.x = Display.width
        elif self.y > Display.height:
            self.y = 0
        elif self.y < 0:
            self.y = Display.height
        self.life -= 1

