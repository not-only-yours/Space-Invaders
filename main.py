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


main()
