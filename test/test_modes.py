from pi_eight_leds.modes import to_center

pins = [4, 23, 24, 25, 12, 16, 20, 21]


def test_to_center(capsys):
    to_center(pins, iterations=1)
    captured = capsys.readouterr()
    assert captured.out == """cleanup () {}
setup ([4, 23, 24, 25, 12, 16, 20, 21], 'OUT') {'initial': 'LOW'}
cleanup () {}
setup ([25, 24, 23, 4, 21, 20, 16, 12], 'OUT') {'initial': 'LOW'}
cleanup () {}
output ((12, 21), 'HIGH') {}
cleanup () {}
output ((16, 20), 'HIGH') {}
cleanup () {}
output ((20, 16), 'HIGH') {}
cleanup () {}
cleanup () {}
"""
