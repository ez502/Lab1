import time

BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
RED = '\u001b[41m'
RESET = '\u001b[0m'

def animation():
    pixel = ' ' * 8
    height = 6
    colors = [BLUE, WHITE, RED]

    for frame in range(9):
        for i in range(height):
            print(colors[frame % 3] + pixel + colors[(frame + 1) % 3] + pixel + colors[(frame + 2) % 3] + pixel + RESET)#colors[frame % 3] берем нужный элемент 
        print('\x1b[6A', end='')
        time.sleep(0.5)
    print('\x1b[6B')


animation()