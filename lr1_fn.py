import time
RED= "\u001b[41m"
BLUE= "\u001b[44m"
WHITE= "\u001b[47m"
RESET= "\u001b[0m"
BLACK = '\u001b[40m'
PIXEL="  "

def flag():
    hig=10
    len=15
    for i in range(hig):
        print(f"{BLUE}{PIXEL*(len//3)}{WHITE}{PIXEL*(len//3)}{RED}{PIXEL*(len//3)}{RESET}")

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

def animation():
    pixel = ' ' * 8
    height = 6
    colors = [BLUE, WHITE, RED]

    for frame in range(9):
        for i in range(height):
            print(colors[frame % 3] + pixel + colors[(frame + 1) % 3] + pixel + colors[(frame + 2) % 3] + pixel + RESET)#colors[frame % 3] берем нужный элемент 
        print('\x1b[6A', end='')#
        time.sleep(0.5)#
    print('\x1b[6B')#
def fille():
    file=open('sequence.txt')
    a=[]
    b=[]
    for x in file:
        if float(x)>0:
            a.append(x)
        else:
            b.append(x)
    file.close
    print(len(a),len(b))
    print(f"{BLUE}{" " * (len(a)//2)}{RESET}{len(a)/(len(a)+len(b))*100}%")
    print(f"{RED}{" " *(len(b)//2)}{RESET}{len(b)/(len(b)+len(a))*100}%")




flag()
p()
animation()
fille()