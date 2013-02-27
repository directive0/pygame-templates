#!/usr/bin/python
#
# -------------------------------------------------------------
# template-mouse - a template to start pygame programs with
#                  basic mouse management
# 2013-02-26 Javier Cantero <jcantero@escomposlinux.org>
#
# LICENSE:
# Public Domain - Use what/where/how you like and remove this
# -------------------------------------------------------------

import pygame
#from pygame.locals import *

# general constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 30

# mouse movement in the 1/5 margin areas of the screen
MOUSE_HORIZONTAL_AREA = SCREEN_WIDTH / 5
MOUSE_VERTICAL_AREA = SCREEN_HEIGHT / 5

# game constants
HORIZONTAL_LEFT, HORIZONTAL_NOT, HORIZONTAL_RIGHT = ( -1, 0, 1 )
VERTICAL_UP, VERTICAL_NOT, VERTICAL_DOWN = ( -1, 0, 1 )


class Game():
    def __init__(self):
        pass

    def loop(self, screen):
        # main loop variables
        clock = pygame.time.Clock()
        horizontal_dir = HORIZONTAL_NOT
        vertical_dir = VERTICAL_NOT
 
        while True:
            delta_t = clock.tick( FRAME_RATE )

            #
            #   I N P U T
            # --------------------------------------------------------------
    
            for event in pygame.event.get(): # event handling loop
    
                # handle quitting from the program
                if event.type == pygame.QUIT:
                    return # closing the window, end of the game loop
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return # closing the window, end of the game loop

                # mouse events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.MOUSEMOTION:
                    x, y = event.pos  # position of the mouse
                    #relx, rely = event.rel # relative movement of the mouse

                    # handle movement in the margin areas of the screen
                    if 0 <= x <= MOUSE_HORIZONTAL_AREA:
                        horizontal_dir = HORIZONTAL_LEFT
                    elif SCREEN_WIDTH - MOUSE_HORIZONTAL_AREA <= x <= SCREEN_WIDTH:
                        horizontal_dir = HORIZONTAL_RIGHT
                    else:
                        horizontal_dir = HORIZONTAL_NOT
                    if 0 <= y <= MOUSE_VERTICAL_AREA:
                        vertical_dir = VERTICAL_UP
                    elif SCREEN_HEIGHT - MOUSE_VERTICAL_AREA <= y <= SCREEN_HEIGHT:
                        vertical_dir = VERTICAL_DOWN
                    else:
                        vertical_dir = VERTICAL_NOT

            # in window mode the mouse can leave it and we need to stop
            # (in full screen you can remove it)
            if not pygame.mouse.get_focused():
                horizontal_dir = HORIZONTAL_NOT
                vertical_dir = VERTICAL_NOT

            #
            #   U P D A T E
            # --------------------------------------------------------------

            if vertical_dir == VERTICAL_UP:
                pass
            elif vertical_dir == VERTICAL_DOWN:
                pass
            # change if for elif for 4-coordinates only movement
            if horizontal_dir == HORIZONTAL_LEFT:
                pass
            elif horizontal_dir == HORIZONTAL_RIGHT:
                pass

            #
            #   R E N D E R
            # --------------------------------------------------------------
    
            # render game screen
            screen.fill( (0, 0, 0) ) # black background

            # blit the graphic elements to the screen surface


            # update display
            pygame.display.update()

    def quit(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption( 'Mouse' )

    game = Game()
    game.loop( screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()

