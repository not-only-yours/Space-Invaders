import GlobalVariables as gv


def main():
    gv.PG_LIB.display.set_caption("Space Invaders")

    run = True
    clock = gv.PG_LIB.time.Clock()
    while run:
        clock.tick(gv.FPS)

        gv.FrameCreator_LIB.updateFrame()
        if gv.LIVES <= 0 or gv.GOOD_SHIP.health <= 0:
            gv.LOST = True
            gv.LOST_COUNT += 1

        if gv.LOST:
            if gv.LOST_COUNT > gv.FPS * 3:
                run = False

            else:
                continue
        if len(gv.ENEMIES) == 0:
            gv.LEVEL += 1
            gv.WAVE_LENGTH += 5
            for i in range(gv.WAVE_LENGTH):
                enemy = gv.ShipCreator.Enemy(gv.RANDOM_LIB.randrange(50, gv.WIDTH - 100),
                                             gv.RANDOM_LIB.randrange(-1500, -100),
                                             gv.RANDOM_LIB.choice(["red", "blue", "purple"]))
                gv.ENEMIES.append(enemy)
        for event in gv.PG_LIB.event.get():
            if event.type == gv.PG_LIB.QUIT:
                run = False

        keys = gv.PG_LIB.key.get_pressed()
        if keys[gv.PG_LIB.K_a] and gv.GOOD_SHIP.x - gv.PLAYER_VEL > 0:  # left
            gv.GOOD_SHIP.x -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_d] and gv.GOOD_SHIP.x + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEX < gv.WIDTH:  # right
            gv.GOOD_SHIP.x += gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_w] and gv.GOOD_SHIP.y - gv.PLAYER_VEL > 0:  # up
            gv.GOOD_SHIP.y -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_s] and gv.GOOD_SHIP.y + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEY < gv.HEIGHT:  # down
            gv.GOOD_SHIP.y += gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_SPACE]:
            gv.GOOD_SHIP.shoot()
        for enemy in gv.ENEMIES[:]:
            enemy.move(gv.ENEMY_VEL)
            enemy.move_lasers(gv.LASER_VEL, gv.GOOD_SHIP)

            if gv.RANDOM_LIB.randrange(0, 20) == 1:
                enemy.shoot()

            if gv.LaserCreator.collide(enemy, gv.GOOD_SHIP):
                gv.GOOD_SHIP.health -= 10
                gv.ENEMIES.remove(enemy)
                gv.SCORE -= 20

            if enemy.y + gv.BAD_SHIP_SIZEY + 10 > gv.HEIGHT:
                gv.LIVES -= 1
                gv.ENEMIES.remove(enemy)
                gv.SCORE -= 100

        gv.GOOD_SHIP.move_lasers(-gv.LASER_VEL, gv.ENEMIES)

        gv.FrameCreator_LIB.updateFrame()


if __name__ == '__main__':
    title_font = gv.PG_LIB.font.SysFont("comicsans", 70)
    run = True
    main_menu = True
    while run:
        gv.WINDOW.blit(gv.BACKGROUND_PNG, (0, 0))
        title_label = title_font.render("Press any button to begin...", 1, (255, 255, 255))
        score_label = title_font.render("SCORE", 1, (255, 255, 255))

        gv.WINDOW.blit(title_label, (gv.WIDTH / 2 - title_label.get_width() / 2, 100))
        gv.WINDOW.blit(score_label, (gv.WIDTH / 2 - score_label.get_width() / 2, 200))
        if main_menu:
            main_menu = False
            file1 = open('score_table.txt', 'r')
            lines = file1.readlines()
            del lines[3:]
            if lines:
                score = title_font.render(f"{lines}", 1, (255, 255, 255))
            else:
                score = title_font.render("NO SCORE YET!", 1, (255, 255, 255))
        gv.WINDOW.blit(score, (gv.WIDTH / 2 - score.get_width() / 2, 300))
        gv.WINDOW.blit(title_label, (gv.WIDTH / 2 - title_label.get_width() / 2, 100))
        gv.PG_LIB.display.update()
        for event in gv.PG_LIB.event.get():
            if event.type == gv.PG_LIB.QUIT:
                run = False
            if event.type == gv.PG_LIB.KEYDOWN or event.type == gv.PG_LIB.MOUSEBUTTONDOWN:
                main()
    gv.PG_LIB.quit()
