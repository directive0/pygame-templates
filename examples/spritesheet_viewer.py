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
        spritesheet = SpriteSheet( pygame.image.load( 'iso-64x64-building_2.png' ) )
        self.sprites = spritesheet.extract( (64,64), (0,0), 8, 10,
                flags=pygame.SRCALPHA )

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
            screen.fill( BACKGROUND ) # black background
            screen.blit( self.sprites[sprite_pos], (SCREEN_WIDTH/2,SCREEN_HEIGHT/2) )
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
    pygame.display.set_caption( 'Example' )
    #pygame.mouse.set_visible( False )

    game = Game()
    game.loop( screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()

