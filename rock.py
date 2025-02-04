import pyglet
from config import *

class RockSystem:
    def __init__(self, batch):
        self.batch = batch
        self.rocks = []
        self.cooldown = 0
        self.click_limit = 7
        self.clicks = 0

    def throw_rock(self, start_pos, target_pos):
        if self.clicks < self.click_limit and self.cooldown <= 0:
            dx = target_pos[0] - start_pos[0]
            dy = target_pos[1] - start_pos[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > 0:
                self.rocks.append(Rock(start_pos[0], start_pos[1], 
                                     dx/distance, dy/distance, self.batch))
                self.clicks += 1
                if self.clicks >= self.click_limit:
                    self.cooldown = ROCK_COOLDOWN_MAX

    def update(self, dt):
        self.cooldown = max(0, self.cooldown - dt)
        for rock in self.rocks[:]:
            rock.update(dt)
            if rock.is_off_screen():
                self.rocks.remove(rock)

class Rock:
    def __init__(self, x, y, dx, dy, batch):
        self.shape = pyglet.shapes.Rectangle(x, y, 10, 10, 
                                           color=(165, 42, 42), batch=batch)
        self.dx = dx
        self.dy = dy
        self.speed = 400

    def update(self, dt):
        self.shape.x += self.dx * self.speed * dt
        self.shape.y += self.dy * self.speed * dt

    def is_off_screen(self):
        return (self.shape.x < -10 or self.shape.x > 610 or
                self.shape.y < -10 or self.shape.y > 410)