from platform import uname

if uname().machine == 'ARMv61':
    import RPi.GPIO as GPIO
else:
    print("This program must be run on Raspberry Pi with RPi.GPIO module installed. Running with fakeRPiGPIO instead.")
    from RPi import GPIO
from .arg_parser import init_args
from .modes import MAX_DELAY, all_on, all_off, kitt, left_to_right, right_to_left, to_center

GPIO.setmode(GPIO.BCM)


def help_text(used_pins):
    print("""
    Used pins: {}\n
    Maximum delay (speed is calculated as MAX_DELAY-speed): {}\n
    Available modes: {}
    """.format(", ".join(map(str, used_pins)), MAX_DELAY, ", ".join(list(modes.keys()))))


# list of used pins, from left led to right
pins = [4, 23, 24, 25, 12, 16, 20, 21]

modes = {
    'allon': all_on,
    'alloff': all_off,
    'kitt': kitt,
    'lefttoright': left_to_right,
    'righttoleft': right_to_left,
    'tocenter': to_center,
    'help': help_text
}


def main():
    args = init_args()
    print("Starting!")
    modes[args.mode[0]](pins, args.speed[0], args.leavelit, args.iterations[0])
    print("Completed!")


if __name__ == '__main__':
    main()