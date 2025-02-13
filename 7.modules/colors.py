_BLUE = '\033[94m'
_CYAN = '\033[96m'
_ENDCOLOR = '\033[0m'


def blue(object):
    """
    Function colors text in blue.
    """

    colour = _BLUE

    return colour + str(object) + _ENDCOLOR

def cyan(object):
    """
    Function colors text in cyan.
    """

    colour = _CYAN

    return colour + str(object) + _ENDCOLOR



print(blue('blue'))
print(cyan('blue'))