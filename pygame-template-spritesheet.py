#!/usr/bin/python
#
# -------------------------------------------------------------
# template-spritesheet - template to load a sprite sheet
# 2013-02-24 Javier Cantero <jcantero@escomposlinux.org>
#
# LICENSE:
# Public Domain - Use what/where/how you like and remove this
# -------------------------------------------------------------

import pygame

# general constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 30

class SpriteSheet():
    def __init__(self, spritesheet):
        self.spritesheet = spritesheet

    def rects(self, size, offset, rows=1, cols=1):
        """ Return a list of Rects for each sprite in a grid of
            'rows' x 'cols' of sprites of 'size' size, starting
            at 'offset' point. """

        # check parameters
        sprite_w, sprite_h = size   # 2-tuple
        offset_x, offset_y = offset # 2-tuple
        if cols < 1 or rows < 1: # positive integers
            raise ValueError

        # compare the size of the grid area vs. the spritesheet size
        spritesheet_w, spritesheet_h = self.spritesheet.get_size()
        if cols * sprite_w + offset_x > spritesheet_w:
            raise ValueError
        if rows * sprite_h + offset_y > spritesheet_h:
            raise ValueError

        # calculate the rect of each sprite and populate the list
        rects = []
        for row in range( rows ):
            for col in range( cols ):
                sprite_x = offset_x + (col * sprite_w)
                sprite_y = offset_y + (row * sprite_h)
                sprite_rect = pygame.Rect( sprite_x, sprite_y, sprite_w,
                        sprite_h )
                rects.append( sprite_rect )

        return rects

    def surfaces(self, size, offset, rows=1, cols=1, flags=0):
        """ Return a list of Surfaces for each sprite in a grid of
            'rows' x 'cols' of sprites of 'size' size, starting
            at 'offset' point. The new Surfaces are created
            with the flags passed (if passed). """

        # using rects() to get the Rects of each sprite and
        # then blitting them to new Surfaces

        # the parameters are checked by rects()
        rects = self.rects( size, offset, rows, cols )

        sprites = []
        for rect in rects:
            sprite = pygame.Surface( size, flags )
            sprite.blit( self.spritesheet, (0,0), rect )
            sprites.append( sprite )

        return sprites


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

