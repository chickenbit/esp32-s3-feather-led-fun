# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example repeatedly displays all available animations, at a five second interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.

This example does not work on SAMD21 (M0) boards.
"""
import board
import neopixel
import board
from digitalio import DigitalInOut, Pull, Direction
from adafruit_debouncer import Debouncer
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.customcolorchase import CustomColorChase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import (
    RED,
    YELLOW,
    ORANGE,
    GREEN,
    TEAL,
    CYAN,
    BLUE,
    PURPLE,
    MAGENTA,
    WHITE,
    BLACK,
    GOLD,
    PINK,
    AQUA,
    JADE,
    AMBER,
    OLD_LACE,
)

def init_pixels(pin=board.A0, count=60):
    # Update to match the pin connected to your NeoPixels
    pixel_pin = pin
    # Update to match the number of NeoPixels you have connected
    pixel_num = count

    pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=1.0, auto_write=False)
    return pixels

pixels = init_pixels(board.A0, 60)

halloween_colorcycle = ColorCycle(pixels, speed=0.4, colors=[PURPLE, ORANGE, GREEN])

halloween_color_chase = CustomColorChase(
    pixels, speed=0.1, size=5, spacing=3, colors=[ORANGE, PURPLE, GREEN]
)
halloween_sparkle_pulse = SparklePulse(pixels, speed=0.1, period=3, color=PURPLE)
halloween_chase = Chase(pixels, speed=0.01, size=20, spacing=6, color=PURPLE)
halloween_pulse = Pulse(pixels, speed=0.01, period=30, color=PURPLE)
halloween_comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=40, bounce=True)
purple_comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=40, bounce=True)
orange_comet = Comet(pixels, speed=0.01, color=ORANGE, tail_length=40, bounce=True)
rainbow_comet = RainbowComet(pixels, speed=0.05, tail_length=15, bounce=True)




def setup_lights(pixels):
    # red_chase = Chase(pixels, speed=0.08, size=20, spacing=6, color=RED)
    # green_chase = Chase(pixels, speed=0.1, size=20, spacing=6, color=GREEN)
    # green_pulse = Pulse(pixels, speed=0.01, period=30, color=GREEN)
    # christmas_color_chase = CustomColorChase(
    #     pixels, speed=0.6, size=5, spacing=3, colors=[RED, GREEN]
    # )
    green_comet = Comet(pixels, speed=0.08, color=GREEN, tail_length=40, bounce=True)
    red_comet = Comet(pixels, speed=0.08, color=RED, tail_length=40, bounce=True)
    christmas_animations = AnimationSequence(
        # red_chase,green_chase,
        red_comet,
        green_comet,
        advance_interval=10,
        auto_clear=False,
    )
    return christmas_animations



button_in = DigitalInOut(board.D5)  # defaults to input
button_in.direction = Direction.INPUT
button_in.pull = Pull.UP  # turn on internal pull-up resistor
button = Debouncer(button_in)

print("defined button")

lights_on = True # if reversited, need to deinit
animations = setup_lights(pixels)

while True:
    if lights_on:
        animations.animate()
    # christmas_color_chase.animate()
    button.update()
    if button.fell:
        print("press!")
    if button.rose:
        print("release!")
        if lights_on:
            print("Turning lights off")
            lights_on = False
            pixels.deinit()
        else:
            lights_on = True
            pixels = init_pixels()
            animations = setup_lights(pixels)

            print("Turning lights on")
    # print(f"value: {button.value}")

    # print(f"state: {button.state}")
    # print(f"fell: {button.fell}")
    # print(f"rose: {button.rose}")
