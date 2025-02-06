import pylget

class Enemy(pylget.Entity):
    def __init__(self, x, y, width=50, height=50):
        super().__init__(x, y, width, height)
        self.health = 3
        self.speed = 2
        self.direction = 1  # 1 for right, -1 for left
        self.start_x = x
        self.end_x = x + 200  # Adjust as needed

    def update(self, dt):
        self.move()

    def move(self):
        if self.direction == 1:
            if self.x + self.speed < self.end_x:
                self.x += self.speed
            else:
                self.direction = -1
        else:
            if self.x - self.speed > self.start_x:
                self.x -= self.speed
            else:
                self.direction = 1

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.destroy()