#!/usr/bin/python
#
# -------------------------------------------------------------
# sprite_viewer - show the sprites in a sprite sheet
# 2013-02-24 Javier Cantero <jcantero@escomposlinux.org>
#
# LICENSE:
# Public Domain - Use what/where/how you like and remove this
# -------------------------------------------------------------

import pygame

# general constants
SCREEN_WIDTH = 640  
SCREEN_HEIGHT = 480
FRAME_RATE = 30

# colors
BLACK = (0, 0, 0)
BLACKGREY = (32, 32, 32)
WHITE = (255, 255, 255)

BACKGROUND = BLACKGREY


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
        spritesheet = SpriteSheet( pygame.image.load( 'iso-64x64-building_2.png' ) )
        self.sprites = spritesheet.surfaces( (64,64), (0,0), 8, 10,
                flags=pygame.SRCALPHA )
        del spritesheet

    def loop(self, screen):
        clock = pygame.time.Clock()
        sprite_pos = 0
        sprites_len = len(self.sprites) - 1
        basicFont = pygame.font.SysFont(None, 48)

        while True:
            delta_t = clock.tick( FRAME_RATE )

            # handle input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return # closing the window, end of the game loop
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return # closing the window, end of the game loop

                # movement keys
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if sprite_pos > 0:
                            sprite_pos -= 1
                    elif event.key == pygame.K_RIGHT:
                        if sprite_pos < sprites_len:
                            sprite_pos += 1

            # render game screen
            screen.fill( BACKGROUND )
            screen.blit( self.sprites[sprite_pos], (SCREEN_WIDTH/2, SCREEN_HEIGHT/2) )
            text = '%d' % (sprite_pos)
            text_sprite =basicFont.render(text, True, WHITE, BACKGROUND )
            screen.blit( text_sprite, (10, 10) )

            # update display
            pygame.display.update()
            # or pygame.display.flip()

    def quit(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption( 'Sprite Viewer' )
    #pygame.mouse.set_visible( False )

    game = Game()
    game.loop( screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()

