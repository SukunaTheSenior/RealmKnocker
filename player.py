import pyglet
from pyglet.window import key
from config import *

class Player:
    def __init__(self, batch):
        self.shape = pyglet.shapes.Rectangle(300, 200, 50, 50, 
                                           color=(255, 255, 0), batch=batch)
        self.speed = PLAYER_SPEED
        self.dash_cooldown = 0
        self.shift_held_time = 0
        self.max_shift_hold = 1.5

    def update(self, dt, keys, mouse_pos, dash_callback):
        # Movement
        if keys[key.W]:
            self.shape.y += self.speed * dt
        if keys[key.S]:
            self.shape.y -= self.speed * dt
        if keys[key.A]:
            self.shape.x -= self.speed * dt
        if keys[key.D]:
            self.shape.x += self.speed * dt

        # Dash handling
        if keys[key.LSHIFT] and self.dash_cooldown <= 0:
            self.shift_held_time += dt
            self.shift_held_time = min(self.shift_held_time, self.max_shift_hold)
        elif self.shift_held_time > 0:
            dash_callback(self.shift_held_time)
            self.shift_held_time = 0
            self.dash_cooldown = DASH_COOLDOWN_MAX

        # Cooldown update
        if self.dash_cooldown > 0:
            self.dash_cooldown -= dt