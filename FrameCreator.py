import GlobalVariables as gv


def updateFrame():
    gv.WINDOW.blit(gv.BACKGROUND_PNG, (0, 0))

    lives_label = gv.MAIN_FONT.render(f"Level: {gv.LEVEL}", 1, (255, 255, 255))
    level_label = gv.MAIN_FONT.render(f"Level: {gv.LEVEL}", 1, (255, 255, 255))

    gv.WINDOW.blit(lives_label, (10, 10))
    gv.WINDOW.blit(level_label, (gv.WIDTH - level_label.get_width() - 10, 10))

    gv.GOOD_SHIP.draw(gv.WINDOW)
    gv.PG_LIB.display.update()
