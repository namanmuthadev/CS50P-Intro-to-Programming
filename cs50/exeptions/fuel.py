while True:
        try:
            x,y=input('Fraction: ').strip().split('/')
            x=int(x)
            y=int(y)
            z=x/y
            if x>y or x<0 or y<0:
                continue
            break
        except ( ValueError , ZeroDivisionError):
            continue
p=z*100
p=round(p)
if p<=1:
     print('E')
elif p>=99:
     print('F')
else:
     print(f'{p}%')