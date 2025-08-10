from propresenter.pb_auto_generated.basicTypes_pb2 import Color
import random


def blue():
    return Color(red=0, green=0, blue=1, alpha=1)


def red():
    return Color(red=1, green=0, blue=0, alpha=1)


def green():
    return Color(red=0, green=1, blue=0, alpha=1)


def black():
    return Color(red=0, green=0, blue=0, alpha=1)


def white():
    return Color(red=1, green=1, blue=1, alpha=1)


def pink():
    return Color(
        red=1,
        green=0,
        blue=1,
        alpha=1,
    )


def churchtools_blue():
    return Color(red=14.0 / 255.0, green=32 / 255.0, blue=75 / 255.0, alpha=1)


def luhovina():
    return Color(red=40.0 / 255.0, green=200.0 / 255.0, blue=150.0 / 255.0, alpha=1)


def luho_blue():
    return Color(red=0, green=94 / 255.0, blue=168 / 255.0, alpha=1)

def luho_blue_dark_theme():
    return Color(red=50/255.0, green=163 / 255.0, blue=255 / 255.0, alpha=1)


def luho_gray():
    return Color(red=170.0 / 255.0, green=178.0 / 255.0, blue=194.0 / 255.0, alpha=1)


def luho_gold():
    return Color(red=206.0 / 255.0, green=160.0 / 255.0, blue=26.0 / 255.0, alpha=1)

def random_color():
    return Color(red=random.uniform(0,1), green=random.uniform(0,1), blue=random.uniform(0,1), alpha=1)

def transparent():
    return Color(red=0, green=0, blue=0, alpha=0)
