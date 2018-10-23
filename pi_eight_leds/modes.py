from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Maximum delay between blinks
MAX_DELAY = 1000  # ms


def all_on(pins):
    GPIO.cleanup()
    try:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)
    except KeyboardInterrupt:
        return
    finally:
        GPIO.cleanup()


def all_off(pins):
    """
    Turns off used pins (but nothing else)
    :param pins: pins to be turned off
    :return: None
    """
    GPIO.cleanup(pins)


def kitt(pins, speed=500, leave_lit=False):
    """
    Lights LEDs from center to the edges like KITT in Knight Rider
    :param leave_lit: leave used LED lit till next iteration
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :param pins: pins to be used, from left to right
    :return: None
    """
    GPIO.cleanup()
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    pin_pairs = [(x, y) for x,y, in zip(pins[:4:-1], pins[4:])]
    while True:
        try:
            for pair in pin_pairs:
                if leave_lit:
                    GPIO.cleanup()
                GPIO.output(pair, GPIO.HIGH)
                sleep((MAX_DELAY-speed) / 1000)
            GPIO.cleanup()
        except KeyboardInterrupt:
            return
        finally:
            GPIO.cleanup()


def left_to_right(pins, speed=500, leave_lit=False):
    """
    Lights LEDs from left edge to right edge
    :param leave_lit: leave used LED lit till next iteration
    :param pins: pins to be used, from left to right
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :return: None
    """
    GPIO.cleanup()
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    while True:
        try:
            for pin in pins:
                if leave_lit:
                    GPIO.cleanup()
                GPIO.output(pin, GPIO.HIGH)
                sleep((MAX_DELAY-speed) / 1000)
        except KeyboardInterrupt:
            return
        finally:
            GPIO.cleanup()


def right_to_left(pins, speed=500, leave_lit=False):
    """
    Lights LEDs from right edge to left edge
    :param leave_lit: leave used LED lit till next iteration
    :param pins: pins to be used, from left to right
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :return: None
    """
    GPIO.cleanup()
    left_to_right(pins[::-1], speed, leave_lit)


def to_center(pins, speed=500, leave_lit=False):
    """
    Lights LEDs from the edges to the center (reverse kitt)
    :param leave_lit: leave used LED lit till next iteration
    :param pins: pins to be used, from left to right
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :return: None
    """
    GPIO.cleanup()
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    swapped_pins = [pins[3], pins[2], pins[1], pins[0], pins[7], pins[6], pins[5], pins[4]]
    kitt(swapped_pins, speed, leave_lit)



