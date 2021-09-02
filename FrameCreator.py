import GlobalVariables as gv


def updateFrame():
    gv.WIN.blit(gv.BACKGROUND, (0, 0))

    lives_label = gv.MAIN_FONT.render(f"Level: {gv.LEVEL}", 1, (255,255, 255))
    level_label = gv.MAIN_FONT.render(f"Level: {gv.LEVEL}", 1, (255,255,255))

    gv.WIN.blit(lives_label, (10, 10))
    gv.WIN.blit(level_label, (gv.WIDTH - level_label.get_width() - 10,10))

    gv.PG_LIB.display.update()