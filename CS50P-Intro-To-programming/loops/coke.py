amt=50
coin=[5,10,25]
while amt>0:
    print(f'Amount Due: {amt}')
    coins=int(input('insert coin: '))
    if coins in coin:
        amt-=coins
print(f'Change owed: {abs(amt)}')