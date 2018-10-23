from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("mode",
                    type=str,
                    nargs=1,
                    choices=["allon", 'alloff', 'kitt', 'lefttoright', 'righttoleft', 'tocenter'],
                    help="Desired mode (see README)")


def init_args():
    return parser.parse_args()