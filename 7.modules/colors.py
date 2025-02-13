_ENDCOLOR = '\033[0m'
_BLUE = '\033[94m'
_CYAN = '\033[96m'
_PINK = '\033[95m'
_GREEN = '\033[92m'
_YELLOW = '\033[93m'
_RED = '\033[91m'


def _color_text(object, color_const):
    return color_const + str(object) + _ENDCOLOR

def blue(object):
    """
    Function colors text in blue.
    """
    return _color_text(object, _BLUE)

def cyan(object):
    """
    Function colors text in cyan.
    """
    return _color_text(object, _CYAN)

def pink(object):
    """
    Function colors text in pink.
    """
    return _color_text(object, _PINK)

def green(object):
    """
    Function colors text in green.
    """
    return _color_text(object, _GREEN)

def yellow(object):
    """
    Function colors text in yellow.
    """
    return _color_text(object, _YELLOW)

def red(object):
    """
    Function colors text in red.
    """
    return _color_text(object, _RED)


if __name__ == '__main__':
    print(blue('blue'))
    print(cyan('cyan'))
    print(pink('pink'))
    print(green('green'))
    print(yellow('yellow'))
    print(red('red'))