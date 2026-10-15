BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
RED = '\u001b[41m'
RESET = '\u001b[0m'


def p():
    c = '  '
    g = '    '
    for i in range(3):
        line = ''
        for k in range(5):
            if i == 1:
                line += WHITE + c + BLACK + c + WHITE + c
            else:
                line += BLACK + c + WHITE + c + BLACK + c
            line += RESET + g
        print(line)
p()

