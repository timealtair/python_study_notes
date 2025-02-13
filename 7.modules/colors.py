_BLUE = '\033[94m'
_CYAN = '\033[96m'
_ENDCOLOR = '\033[0m'

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



print(blue('blue'))
print(cyan('blue'))