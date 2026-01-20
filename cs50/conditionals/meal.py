def main():
    time=input('whats the time : ')
    t=convert(time)
    if t>=7.0 and t<=8.0:
        print('breakfast time')
    elif t>=12.0 and t<=13.0:
        print('lunch time')
    elif t>=18.0 and t<=19.0:
        print('dinner time')


def convert(time):
    h,m=time.split(':')
    return (float(h)+(float(m)/60))


if __name__ == "__main__":
    main()
