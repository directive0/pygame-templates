#!/usr/bin/python
#
# -------------------------------------------------------------
# template - a template to start pygame programs
# 2012-10-01 Javier Cantero <jcantero@escomposlinux.org>
#
# LICENSE:
# Public Domain - Use what/where/how you like and remove this
# -------------------------------------------------------------

import pygame

# general constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 30


class Game():
    def __init__(self):
        pass

    def loop(self, screen):
        clock = pygame.time.Clock()

        while True:
            delta_t = clock.tick( FRAME_RATE )

            # handle input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return # closing the window, end of the game loop

            # render game screen
            screen.fill( (0, 0, 0) ) # black background

            # update display
            pygame.display.update()
            # or pygame.display.flip()

    def quit(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption( 'Example' )
    #pygame.mouse.set_visible( False )

    game = Game()
    game.loop( screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()

