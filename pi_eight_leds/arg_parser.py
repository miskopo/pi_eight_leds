from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("mode",
                    type=str,
                    nargs=1,
                    choices=["help", "allon", 'alloff', 'kitt', 'lefttoright', 'righttoleft', 'tocenter'],
                    help="Desired mode (see README)")
parser.add_argument("--leavelit",
                    help="Leaves LEDs lit within transition",
                    action="store_true",
                    default=False)
parser.add_argument("--speed",
                    help="Speed of blinking, max 1000",
                    nargs=1,
                    type=int,
                    default=[500])
parser.add_argument("--iterations",
                    help="Number of mode iterations (if applicable)",
                    nargs=1,
                    type=int,
                    default=[-1])


def init_args():
    return parser.parse_args()