from setuptools import setup

setup(
        name='pi_eight_leds',
        version='0.1.0',
        packages=['pi_eight_leds'],
        entry_points={
            'console_scripts': [
                'pi_eight_leds = pi_eight_leds.__main__:main'
                ]
            })