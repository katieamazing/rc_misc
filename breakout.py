'''Breakout'''
import sys
import sdl2
import sdl2.ext

class Collisions:
    def __init__(self):
        pass

class Movement(sdl2.ext.Applicator):
    def __init__(self, min_x, min_y, max_x, max_y):
        super(Movement, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.sprite
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.min_y, sprite.x)
            sprite.y = max(self.min_y, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.max_x:
                sprite.x = self.max_x - swidth
            if pmaxy > self.max_y:
                sprite.y = self.max_y - sheight

class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0

class Paddle(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite = sprite
        self.sprite.position = x, y
        self.velocity = Velocity()


class Ball(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite = sprite
        self.sprite.position = x, y
        self.velocity = Velocity()

class Bricks:
    def __init__(self, player):
        pass

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(0,0,0))
        super(SoftwareRenderer, self).render(components)

class Player(): #whatever world is??
    def __init__(self, lives, level):
        self.lives = lives
        self.level = level

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window('Breakout', size=(600, 400))
    window.show()

    world = sdl2.ext.World()

    sprite_renderer = SoftwareRenderer(window)
    world.add_system(sprite_renderer)

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    pad_sprite = factory.from_color((sdl2.ext.Color(255,255,255)), size=(80, 20))
    paddle = Paddle(world, pad_sprite, 340, 380)

    ball_sprite = factory.from_color((sdl2.ext.Color(255,255,255)), size=(20,20))
    movement = Movement(0,0,600,400)
    sprite_renderer = SoftwareRenderer(window)

    world.add_system(movement)
    world.add_system(sprite_renderer)

    ball = Ball(world, ball_sprite, 390, 290)
    ball.velocity.vx = -3



    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        world.process()
    return 0

if __name__ == '__main__':
    sys.exit(run())
