try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  "
          "You can achieve this by using 'sudo' to run your script")
    exit(1)
except ImportError:
    print("This program must be run on Raspberry Pi with RPi.GPIO module installed.")
    exit(1)
from .modes import MAX_DELAY, all_on, all_off, kitt
from .arg_parser import init_args


GPIO.setmode(GPIO.BCM)


def help_text(used_pins):
    return """
    Used pins: {}\n
    Maximum delay (speed is calculated as MAX_DELAY-speed): {}\n
    Available modes: {}
    """.format(", ".join(map(str, used_pins)), MAX_DELAY, ", ".join(list(modes.keys())))


# list of used pins, from left led to right
pins = [4, 23, 24, 25, 12, 16, 20, 21]

modes = {
    'allon': all_on,
    'alloff': all_off,
    'kitt': kitt,
    'help': help_text
}

args = init_args()

if __name__ == '__main__':
    modes[args['mode']](pins)