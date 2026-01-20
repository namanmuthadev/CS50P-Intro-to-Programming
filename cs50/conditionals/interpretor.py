x, y, z=input('enter values').split(' ')
x=float(x)
z=float(z)

if y=='+':
    print(f"{(x+z):.1f}")
elif y=='-':
    print(f"{(x-z):.1f}")
elif y=='*':
    print(f"{(x*z):.1f}")
elif y=='/':
    if z==0:
        print('not divisible by zero')
    else:
        print(f"{(x/z):.1f}")
else:
    print('enter the right operator')
