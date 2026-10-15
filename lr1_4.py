RED= "\u001b[41m"
BLUE= "\u001b[44m"
WHITE= "\u001b[47m"
RESET= "\u001b[0m"


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
