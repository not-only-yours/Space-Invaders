import GlobalVariables as gv


class Ship:
    COOLDOWN = 30

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
        for laser in self.lasers:
            laser.draw(gv.WINDOW)


    def move_lasers(self, vel, obj):
        self.coldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(gv.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = gv.LaserCreator.Laser(self.x + 20,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def coldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter >= 0:
            self.cool_down_counter += 1

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = gv.GOOD_SHIP_PNG
        self.laser_img = gv.GOOD_LASER_PNG
        self.mask = gv.PG_LIB.mask.from_surface(self.ship_img)
        self.max_health = health


    def move_lasers(self, vel, objs):
        self.coldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(gv.HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def healthbar(self, window):
        gv.PG_LIB.draw.rect(window, (255,0,0), (self.x, self.y + gv.GOOD_SHIP_SIZEY + 10, gv.GOOD_SHIP_SIZEX, 10))
        gv.PG_LIB.draw.rect(window, (0, 255, 0), (self.x, self.y + gv.GOOD_SHIP_SIZEY + 10, gv.GOOD_SHIP_SIZEX * (1 - ((self.max_health - self.health)/ self.max_health)), 10))

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)


class Enemy(Ship):
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img = gv.COLOR_MAP[color]
        self.laser_img = gv.BAD_LASER_PNG
        self.mask = gv.PG_LIB.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = gv.LaserCreator.Laser(self.x + 10,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
