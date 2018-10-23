from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Maximum delay between blinks
MAX_DELAY = 1000 # ms


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


def kitt(pins, speed=500):
    """
    Lights LEDs from center to the edges like KITT in Knight Rider
    :param speed:
    :param pins: pins to be used, from left to right
    :return: None
    """
    GPIO.cleanup()
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    pin_pairs = [(x, y) for x,y, in zip(pins[:4], pins[4:])]
    while True:
        try:
            for pair in pin_pairs:
                GPIO.cleanup()
                GPIO.output(pair, GPIO.HIGH)
                sleep((MAX_DELAY-speed) / 1000)
        except KeyboardInterrupt:
            return
        finally:
            GPIO.cleanup()

