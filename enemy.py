import pyglet
import random
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class Enemy:
    def __init__(self, batch):
        self.size = 20  # Size of the triangle
        self.speed = 100  # Movement speed in pixels per second
        self.x = random.randint(0, WINDOW_WIDTH - self.size)
        self.y = random.randint(0, WINDOW_HEIGHT - self.size)
        self.shape = pyglet.shapes.Triangle(
            self.x, self.y + self.size,  # Bottom-left corner
            self.x + self.size // 2, self.y,  # Top corner
            self.x + self.size, self.y + self.size,  # Bottom-right corner
            color=(255, 0, 0),  # Red color
            batch=batch
        )
        self.is_alive = True

    def move_randomly(self, dt):
        # Randomly move the enemy within the screen bounds
        self.x += (random.choice([-1, 0, 1]) * self.speed * dt)
        self.y += (random.choice([-1, 0, 1]) * self.speed * dt)

        # Keep the enemy within the screen bounds
        self.x = max(0, min(self.x, WINDOW_WIDTH - self.size))
        self.y = max(0, min(self.y, WINDOW_HEIGHT - self.size))

        # Update the triangle's position
        self.shape.x = self.x
        self.shape.y = self.y

    def respawn(self):
        # Respawn the enemy at a random position
        self.x = random.randint(0, WINDOW_WIDTH - self.size)
        self.y = random.randint(0, WINDOW_HEIGHT - self.size)
        self.is_alive = True