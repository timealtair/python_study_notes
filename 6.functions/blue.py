def blue(object, cyan=False):
    """
    Function colors text in blue.
    If 'cyan' True then color will by cyan.
    """
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    ENDCOLOR = '\033[0m'

    if cyan:
        colour = CYAN
    else:
        colour = BLUE

    return colour + str(object) + ENDCOLOR

print('Hello')
print('How ' + blue('are') + blue(' you?', True))
print('Bye')