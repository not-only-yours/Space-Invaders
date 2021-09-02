import GlobalVariables as gv


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        gv.WINDOW.blit(self.ship_img, (self.x, self.y))


class Player(Ship):
    def __init__(self, x,y,health=100):
        super().__init__(x, y, health)
        self.ship_img = gv.GOOD_SHIP_PNG
        self.laser_img = gv.GOOD_LASER_PNG
        self.mask = gv.PG_LIB.mask.from_surface(self.ship_img)
        self.max_health = health
