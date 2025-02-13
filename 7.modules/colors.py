

def blue(object):
    """
    Function colors text in blue.
    """
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    ENDCOLOR = '\033[0m'

    colour = BLUE

    return colour + str(object) + ENDCOLOR

def cyan(object):
    """
    Function colors text in cyan.
    """
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    ENDCOLOR = '\033[0m'

    colour = CYAN

    return colour + str(object) + ENDCOLOR





print(blue('blue'))
print(cyan('blue'))