from platform import uname
from time import sleep

if uname().machine == 'ARMv61':
    import RPi.GPIO as GPIO
else:
    from RPi import GPIO

GPIO.setmode(GPIO.BCM)

# Maximum delay between blinks
MAX_DELAY = 1000  # ms


def all_on(pins, speed=500, leave_lit=False, iterations=-1):
    """
    Turns all LEDs on
    :param pins: pins to be turned on
    :param speed: unused
    :param leave_lit: unused
    :param iterations: unused
    :return:
    """
    del speed, leave_lit, iterations
    GPIO.cleanup()
    try:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)
    except KeyboardInterrupt:
        return
    finally:
        GPIO.cleanup()


def all_off(pins, speed=500, leave_lit=False, iterations=-1):
    """
    Turns off used pins (but nothing else)
    :param iterations: unused
    :param leave_lit: unused
    :param speed: unused
    :param pins: pins to be turned off
    :return: None
    """
    del speed, leave_lit, iterations
    GPIO.cleanup(pins)


def kitt(pins, speed=500, leave_lit=False, iterations=-1):
    """
    Lights LEDs from center to the edges like KITT in Knight Rider
    :param leave_lit: leave used LED lit till next iteration
    :param iterations: number of iterations to execute, -1 if infinity
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :param pins: pins to be used, from left to right
    :return: None
    """
    GPIO.cleanup()
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    pin_pairs = [(x, y) for x, y, in zip(pins[:4:-1], pins[4:])]
    while iterations == -1 or iterations > 0:
        try:
            for pair in pin_pairs:
                if not leave_lit:
                    GPIO.cleanup()
                GPIO.output(pair, GPIO.HIGH)
                sleep((MAX_DELAY-speed) / 1000)
            GPIO.cleanup()
            if iterations != -1 and iterations != 0:
                iterations -= 1
        except KeyboardInterrupt:
            return
        finally:
            GPIO.cleanup()


def left_to_right(pins, speed=500, leave_lit=False, iterations=-1):
    """
    Lights LEDs from left edge to right edge
    :param iterations: number of iterations to execute, -1 if infinity
    :param leave_lit: leave used LED lit till next iteration
    :param pins: pins to be used, from left to right
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :return: None
    """
    GPIO.cleanup()
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    while iterations == -1 or iterations > 0:
        try:
            for pin in pins:
                if not leave_lit:
                    GPIO.cleanup()
                GPIO.output(pin, GPIO.HIGH)
                sleep((MAX_DELAY-speed) / 1000)
            if iterations != -1:
                iterations -= 1
        except KeyboardInterrupt:
            return
        finally:
            GPIO.cleanup()


def right_to_left(pins, speed=500, leave_lit=False, iterations=-1):
    """
    Lights LEDs from right edge to left edge
    :param leave_lit: leave used LED lit till next iteration
    :param iterations: number of iterations to execute, -1 if infinity
    :param pins: pins to be used, from left to right
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :return: None
    """
    GPIO.cleanup()
    left_to_right(pins[::-1], speed, leave_lit, iterations)


def to_center(pins, speed=500, leave_lit=False, iterations=-1):
    """
    Lights LEDs from the edges to the center (reverse kitt)
    :param leave_lit: leave used LED lit till next iteration
    :param iterations: number of iterations to execute, -1 if infinity
    :param pins: pins to be used, from left to right
    :param speed: speed of the animation, used as sleep(MAX-DELAY-speed)
    :return: None
    """
    GPIO.cleanup()
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    swapped_pins = [pins[3], pins[2], pins[1], pins[0], pins[7], pins[6], pins[5], pins[4]]
    kitt(swapped_pins, speed, leave_lit, iterations)



