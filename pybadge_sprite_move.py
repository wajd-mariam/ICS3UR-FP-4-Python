#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: Oct 2019
# This program makes sprites move around

import ugame
import stage

# an image bank of CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# the list of the sprites that will be on the device
sprites = []


def main():
    # this functionm is a scene

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # creating the sprites
    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 75, 56)
    sprites.insert(0, ship)

    # create a stage for the background to show up
    # setting the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # setting the layers to show them in order
    game.layers = sprites + [background]
    # rendering the background and the locations of the sprites
    game.render_block()

    # repeat forever game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)

        if keys & ugame.K_X:
            # print("A")
            pass
        if keys & ugame.K_O:
            # print("B")
            pass
        if keys & ugame.K_START:
            # print("K_START")
            pass
        if keys & ugame.K_SELECT:
            # print("K_SELECT")
            pass
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
            pass
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
            pass
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
            pass
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass

        # update game logic
        # redraw sprites
        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    main()
