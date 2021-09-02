import GlobalVariables as gv


def main():
    gv.PG_LIB.display.set_caption("Space Invaders")

    run = True
    clock = gv.PG_LIB.time.Clock()
    while run:
        clock.tick(gv.FPS)
        gv.FrameCreator_LIB.updateFrame()
        for event in gv.PG_LIB.event.get():
            if event.type == gv.PG_LIB.QUIT:
                run = False

        keys = gv.PG_LIB.key.get_pressed()
        if keys[gv.PG_LIB.K_a]and gv.GOOD_SHIP.x - gv.PLAYER_VEL > 0: #left
            gv.GOOD_SHIP.x -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_d] and gv.GOOD_SHIP.x + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEX < gv.WIDTH: #right
            gv.GOOD_SHIP.x += gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_w] and gv.GOOD_SHIP.y - gv.PLAYER_VEL > 0: #up
            gv.GOOD_SHIP.y -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_s] and gv.GOOD_SHIP.y + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEY < gv.HEIGHT: #down
            gv.GOOD_SHIP.y += gv.PLAYER_VEL
main()
