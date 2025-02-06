import pyglet
from pyglet.window import key, mouse
from config import *
from player import Player
from rock import RockSystem
from menu import MenuSystem
from settings_manager import SettingsManager
from enemy import Enemy
class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, 
                        caption="Realm Knocker RGB", resizable=True)
        self.batch = pyglet.graphics.Batch()
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        
        # Systems initialization
        self.settings_manager = SettingsManager(self)
        self.player = Player(self.batch)
        self.rock_system = RockSystem(self.batch)
        self.menu_system = MenuSystem(self, self.settings_manager)
        
        # Game state
        self.mouse_pos = (0, 0)
        self.fps_display = pyglet.window.FPSDisplay(self)
        pyglet.clock.schedule_interval(self.update, 1/120.0)

    def on_draw(self):
        self.clear()
        if self.menu_system.game_state == 1:  # Playing state
            self.batch.draw()
            self.fps_display.draw()
        else:
            self.menu_system.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_pos = (x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.menu_system.game_state != 1:
            self.menu_system.handle_click(x, y)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.menu_system.handle_key_press(symbol)
        elif symbol == key.E and self.menu_system.game_state == 1:
            self.rock_system.throw_rock(
                (self.player.shape.x, self.player.shape.y),
                self.mouse_pos
            )

    def update(self, dt):
        if self.menu_system.game_state == 1:
            self.player.update(dt, self.keys, self.mouse_pos, 
                             self.handle_dash)
            self.rock_system.update(dt)

    def handle_dash(self, duration):
        dx = self.mouse_pos[0] - self.player.shape.x
        dy = self.mouse_pos[1] - self.player.shape.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 0:
            self.player.shape.x += dx / distance * duration * 120
            self.player.shape.y += dy / distance * duration * 120

if __name__ == "__main__":
    window = GameWindow()
    window.set_fullscreen(START_FULLSCREEN)
    pyglet.app.run()
