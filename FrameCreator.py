import GlobalVariables as gv


def updateFrame():
    gv.WINDOW.blit(gv.BACKGROUND_PNG, (0, 0))

    lives_label = gv.MAIN_FONT.render(f"Lives: {gv.LIVES}", 1, (255, 255, 255))
    level_label = gv.MAIN_FONT.render(f"Level: {gv.LEVEL}", 1, (255, 255, 255))

    gv.WINDOW.blit(lives_label, (10, 10))
    gv.WINDOW.blit(level_label, (gv.WIDTH - level_label.get_width() - 10, 10))

    for enemy in gv.ENEMIES:
        enemy.draw(gv.WINDOW)

    gv.GOOD_SHIP.draw(gv.WINDOW)

    if gv.LOST:
        lost_label = gv.LOST_FONT.render(f"YOU LOST!", 1, (255, 255, 255))
        gv.WINDOW.blit(lost_label, (gv.WIDTH / 2 - lost_label.get_width() / 2, 350))

    gv.PG_LIB.display.update()



