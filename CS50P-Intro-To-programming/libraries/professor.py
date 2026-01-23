import random


def main():
    score=0
    print("Level: ", end="")
    level = int(input())
    for b in range(0,10):
        i=0
        x=generate_integer(level)
        y=generate_integer(level)
        z=x+y


        while True:
            if i==3:
                print(f'{x} + {y} = {z}')
                break
            try:
                print(f'{x} + {y} = ',end='')
                answer=int(input())
                if answer==z:
                    if i==0:
                        score=score+1
                    break
                else:
                    i+=1
                    print('EEE')
            except ValueError:
                i+=1
                print('EEE')

    print(score)
def get_level():
    while True:
        try:
            level=int(input('Level: '))
            if level>3 or level<=0:
                continue
            else:
                break
        except ValueError:
            continue
    return level
def generate_integer(level):
    if level==1:
        s=random.randint(0,9)
    elif level==2:
        s=random.randint(10,99)
    else:
        s=random.randint(100,999)
    return s
if __name__ == "__main__":
    main()
