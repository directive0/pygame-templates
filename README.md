pygame-templates
================

A pygame basic templates repository

pygame-template.py
------------------

The basic pygame template does nothing but opening a 800x600 window with
a black background and handles the Close Window signal.
    
Useful to start a new pygame project.

pygame-template-keyboard.py
---------------------------

The pygame template with a basic keyboard cursor implementation.
It does nothing, but you have examples of use in examples/.

pygame-template-spritesheet.py
------------------------------

The pygame template with a basic class SpriteSheet to manipulate a
sprite sheet as individual sprites. You have an example of use
in examples/.

pygame-template-mouse.py
------------------------

The pygame template with a basic mouse control implementation.
It does nothing.

examples
========


pointer.py
----------

An example of use of pygame-template-keyboard.py that controls a pointer
with cursor keys (you can change them). It needs a pointer.png image in
the directory to work.

pointer2.py
-----------

A more advanced version of pointe.py that check the bounds of the area
in which the cursor can move using a rectangle. You can see the actual
area toggling the space key.

spritesheet\_viewer.py
----------------------

An example of use of the SpriteSheet class to extract individual sprites
from a sprite sheet. Move through the sprites of the loaded sprite sheet
(not included) using right and left cursor keys. The number shown is the
index of the array of sprites.

