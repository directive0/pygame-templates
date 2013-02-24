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

    def extract(self, size, offset, rows=1, cols=1, flags=None):
        """ Create 'rows'x'cols' individual sprites of 'size' size
            from a sprite sheet starting in 'offset' coordinates.
            The new surfaces of the sprites has set 'flags' flags.
            Return the array of the surfaces."""
        # check params
        sprite_width, sprite_height = size # 2-tuple
        offset_x, offset_y = offset # 2-tuple
        if cols < 1 or rows < 1: # positive integers
            raise ValueError

        # check area to extract is inside the spritesheet
        spritesheet_rect = self.spritesheet.get_rect()
        if sprite_width * cols + offset_x > spritesheet_rect.width:
            raise ValueError
        if sprite_height * rows + offset_y > spritesheet_rect.height:
            raise ValueError

        # copy individual sprites from spritesheet
        sprites = []
        for row in range(0, rows):
            for col in range(0, cols):
                sprite_rect = pygame.Rect( offset_x + (col * sprite_width),
                    offset_y + (row * sprite_height), sprite_width, sprite_height )

                if flags is not None:
                    sprite = pygame.Surface( (sprite_width, sprite_height), flags )
                else:
                    sprite = pygame.Surface( (sprite_width, sprite_height) )
                sprite.blit( self.spritesheet, (0,0), sprite_rect )
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

