from propresenter.pb_auto_generated.basicTypes_pb2 import Color


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


def churchtools_blue():
    return Color(red=14.0 / 255.0, green=32 / 255.0, blue=75 / 255.0, alpha=1)


def luhovina():
    return Color(red=40.0 / 255.0, green=200.0 / 255.0, blue=150.0 / 255.0, alpha=1)


def luho_blue():
    return Color(red=0, green=94 / 255.0, blue=168 / 255.0, alpha=1)


def luho_gray():
    return Color(red=170.0 / 255.0, green=178.0 / 255.0, blue=194.0 / 255.0, alpha=1)
