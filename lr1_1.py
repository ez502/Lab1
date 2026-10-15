RED= "\u001b[41m"
BLUE= "\u001b[44m"
WHITE= "\u001b[47m"
RESET= "\u001b[0m"
PIXEL="  "


def flag():
    hig=10
    len=15
    for i in range(hig):
        print(f"{BLUE}{PIXEL*(len//3)}{WHITE}{PIXEL*(len//3)}{RED}{PIXEL*(len//3)}{RESET}")

